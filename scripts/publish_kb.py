#!/usr/bin/env python3
"""
publish_kb.py — read filtered slice of ~/kb/concepts/ into Astro content collection.

Reads the new 9-macro × 35-meso structure at ~/kb/concepts/ and emits filtered
markdown into ~/projects/sotf-site/src/content/concepts/. The filter strips
private content (granola/memo/email sources, internal-only fields, deal stages)
so the public output is safe.

For each concept:
  • Reads frontmatter + body
  • Strips private fields and private wikilinks
  • Computes 7d / 30d source-count delta from back-refs index
  • Writes filtered markdown to src/content/concepts/{macro}/{meso}/{slug}.md

Runs nightly via cron after KB morning-brief, OR manually before a build.

Safety (added 18 Oct 2026): the 16 Oct run wiped the output dir, then the Mac
restarted 8 minutes in and left 3 of 778 pages on disk. Output is now built in
STAGING and swapped into place only when the run completes AND the new concept
count is at least MIN_KEEP_RATIO of the previous one (the larger of the working
tree and the last commit, so an already-gutted tree can't lower the bar). An
interrupted or short run leaves the live content untouched.

Usage:
    python publish_kb.py             # filter and emit
    python publish_kb.py --dry-run   # report what would change, no write
    python publish_kb.py --allow-shrink   # deliberate large removal; skips the count guard
"""
from __future__ import annotations
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
import yaml

KB = Path.home() / "kb"
KB_CONCEPTS = KB / "concepts"
KB_COMPANIES = KB / "companies"
# Resolve from this file, not a hard-coded path, so a run from a git worktree
# writes into that worktree and never into the main checkout.
SITE = Path(__file__).resolve().parent.parent
OUT = SITE / "src" / "content" / "concepts"
# Members' edition of each concept (the investor-view sections the public page
# strips). Gitignored: upload_members.py syncs it to the private R2 bucket the
# Worker reads from, so this content never enters the public repo or build.
MEMBERS_OUT = SITE / ".members-out"
STAGING = SITE / ".publish-staging"
# Score ledger: last run's scorecards + every change since, so members get a
# history per concept and a "what changed" feed. Lives in the KB (backed up with
# it), never in this public repo. Override with SOTF_MEMBERS_LEDGER.
LEDGER = Path(os.environ.get("SOTF_MEMBERS_LEDGER") or (KB / "scripts" / "sotf_members_ledger.json"))
CHANGES_WINDOW_DAYS = 90
MIN_KEEP_RATIO = 0.90
BACK_REFS = KB / "scripts" / "back_refs.json"

# Base path the site is served from. Matches the `base` in astro.config.mjs.
# Reads from SOTF_BASE env var so the build + nightly cron can swap between
# "/sotf-site" (GitHub Pages subpath preview) and "" (apex once DNS is cut).
# Default is "" since the apex went live (14 Jul 2026, astro.config has no base):
# the old "/sotf-site" default broke every internal link on any manual run.
BASE_PATH = os.environ.get("SOTF_BASE", "").rstrip("/")

# Macros that are public (frameworks + markets stay private — internal lenses)
PUBLIC_MACROS = {
    "compute", "memory", "sensing", "communications", "energy-power",
    "manufacturing", "materials", "photonic-systems", "life-frontier",
    "robotics", "semiconductor-process-flow", "ai-software",
}

# Source kinds that are public-safe
PUBLIC_SOURCE_KINDS = {"substack", "paper", "report", "web", "thesis", "grant", "tto"}

# Source kinds NEVER published (internal/proprietary)
PRIVATE_SOURCE_KINDS = {"granola", "attio", "memo", "email", "note"}

# Frontmatter fields stripped from public output
STRIP_FIELDS = {
    "deal_count", "passed_reason", "decision", "decision_date",
    "memo_present", "stage_rank", "data_source", "data_freshness",
    "sensitivity", "internal_only", "calibration", "attio_id",
    "first_mention_date", "round_size_eur", "target_raise", "valuation_usd",
    "valuation_str", "total_raised_usd", "total_raised_str",
    # Internal-only routing flags
    "domain",       # [cloudberry, sotf, lunar] — internal routing
    "companies_using",  # internal company tracking (separate from public mentions)
    "ideas_referencing", # internal idea-page back-refs
}


def parse_fm(text: str) -> tuple[dict | None, str]:
    """Return (frontmatter_dict, body)."""
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None, text
    return fm, text[m.end():]


def serialise_fm(fm: dict) -> str:
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=10000, default_flow_style=False)


def coerce_str_list(value) -> list[str]:
    """Force a frontmatter list into a list of plain strings.

    A KB bullet that contains an unquoted ``: `` (e.g. a frontier question with a
    colon) is parsed by YAML as a single-key mapping, not a string. Astro's content
    schema then rejects the whole build. Flatten any such mapping back to
    ``"key: value"`` so the field always matches ``z.array(z.string())``.
    """
    if not isinstance(value, list):
        return value
    out = []
    for item in value:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict):
            out.append("; ".join(f"{k}: {v}" for k, v in item.items()))
        else:
            out.append(str(item))
    return out


def load_back_refs() -> dict:
    """Load cross_pollinate back-refs index."""
    if not BACK_REFS.exists():
        return {}
    try:
        return json.loads(BACK_REFS.read_text())
    except Exception:
        return {}


_public_source_index_cache: list[tuple[object, dict]] | None = None


def _public_source_index() -> list[tuple[object, dict]]:
    """Parse every public source page once: [(concepts_mentioned, entry), ...].

    Previously each of ~780 concepts re-read and re-parsed all ~2,000 public
    sources, which made the run take ~25 minutes. Same files, same order, same
    skip rules; only the parsing is shared.
    """
    global _public_source_index_cache
    if _public_source_index_cache is not None:
        return _public_source_index_cache
    out: list[tuple[object, dict]] = []
    for kind in PUBLIC_SOURCE_KINDS:
        d = KB / "sources" / kind
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
                fm, _ = parse_fm(text)
                if not fm:
                    continue
                mentioned = fm.get("concepts_mentioned") or []
                title = fm.get("title") or p.stem
                date_str = str(fm.get("date") or "")
                # Fallback to filename prefix YYYY-MM-DD
                m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", p.stem)
                sort_key = date_str or (m.group(0) if m else "")
                out.append((mentioned, {
                    "slug": p.stem,
                    "title": title.strip(),
                    "date": sort_key,
                    "kind": kind,
                }))
            except Exception:
                continue
    _public_source_index_cache = out
    return out


def public_sources_for_concept(slug: str, limit: int = 8) -> list[dict]:
    """Return recent public sources mentioning this concept.

    Checks each public source's frontmatter concepts_mentioned for `slug`.
    Returns up to `limit` most recent (by date in filename or frontmatter).
    Each entry: {slug, title, date, kind}
    """
    matches = []
    for mentioned, entry in _public_source_index():
        try:
            if slug not in mentioned:
                continue
        except TypeError:
            continue
        matches.append(dict(entry))
    matches.sort(key=lambda x: x["date"], reverse=True)
    return matches[:limit]


def source_is_public(source_ref: str) -> bool:
    """Resolve a wikilink-style source reference to its actual file and check kind.

    source_ref is a slug like '2026-05-08-sotf-interview-omar-durrani-cnuic'.
    Walks ~/kb/sources/ to find the file. Returns True if source_kind is public.
    """
    # Strip wikilink syntax if present
    ref = source_ref.strip("[]").split("|")[0].strip()
    # Try each public kind subdir first
    for kind_dir in PUBLIC_SOURCE_KINDS:
        p = KB / "sources" / kind_dir / f"{ref}.md"
        if p.exists():
            return True
    # If found in a private kind, it's private
    for kind_dir in PRIVATE_SOURCE_KINDS:
        p = KB / "sources" / kind_dir / f"{ref}.md"
        if p.exists():
            return False
    # Not found — conservative: treat as private
    return False


def filter_sources(sources: list) -> list[str]:
    """Filter source array to only public references."""
    out = []
    for s in sources or []:
        s_str = str(s)
        if source_is_public(s_str):
            out.append(s_str)
    return out


def compute_freshness(slug: str, source_list: list[str]) -> dict:
    """Compute source-count delta over last 7d and 30d for a concept."""
    now = datetime.now(timezone.utc)
    cutoff_7d = now - timedelta(days=7)
    cutoff_30d = now - timedelta(days=30)
    sources_7d = 0
    sources_30d = 0
    # Source slugs typically start with YYYY-MM-DD
    for s in source_list:
        ref = s.strip("[]").split("|")[0].strip()
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", ref)
        if not m:
            continue
        try:
            d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), tzinfo=timezone.utc)
        except ValueError:
            continue
        if d >= cutoff_30d:
            sources_30d += 1
        if d >= cutoff_7d:
            sources_7d += 1
    return {"sources_7d": sources_7d, "sources_30d": sources_30d}


def strip_dataview_blocks(body: str) -> str:
    """Remove Obsidian Dataview code blocks — they're meaningless without the Dataview engine.

    Matches ```dataview ... ``` (case-insensitive). Replaces with a placeholder
    comment so future Phase-4 work can render real cross-link panels in their place.
    """
    pattern = re.compile(r"```(?:dataview|dataviewjs)\s*\n.*?\n```", re.DOTALL | re.IGNORECASE)
    return pattern.sub("<!-- dataview block stripped for public site -->", body)


def strip_external_images(body: str) -> str:
    """Drop markdown images whose path escapes the content dir (``../.. /sources/…``).

    The publish pipeline copies no assets, so a KB image reference that points back
    into ~/kb/sources resolves to nothing and hard-fails the Astro build
    (ImageNotFound). Until we copy assets through, strip these references so one
    dangling chart can't red the whole nightly deploy.
    """
    pattern = re.compile(r"!\[[^\]]*\]\(\s*(?:\.\./)+sources/[^)]*\)")
    return pattern.sub("<!-- non-public image stripped for public site -->", body)


_private_pattern_cache: re.Pattern | None = None


def _build_private_pattern() -> re.Pattern:
    """Compile one big regex that matches any reference to a Cloudberry-internal company.

    A company is internal if its KB page has a non-empty `attio_id` (Attio CRM-tracked).
    Public incumbents (Apple, TSMC, Samsung, etc.) have empty attio_id and are safe to mention.

    Conflict resolution: when the same form (slug / canonical / alias) appears under BOTH
    a private and a public company in the KB (e.g. `nilt` and `nil-technology-nilt` both
    canonicalise to "NILT"), the form is treated as PUBLIC — safer than dropping legit
    paragraphs about widely-known companies. This is the right call because the KB has
    duplicate records for some entities and we don't want false-positive deletions.

    Matches: slug form (lowercase, in wikilinks or bare), canonical_name, multi-word aliases.
    Excludes: single-character / very-short aliases that could match English words.
    """
    global _private_pattern_cache
    if _private_pattern_cache is not None:
        return _private_pattern_cache

    private_forms: set[str] = set()
    public_forms: set[str] = set()

    def _collect(fm: dict) -> set[str]:
        forms: set[str] = set()
        slug = fm.get("slug")
        canonical = fm.get("canonical_name") or ""
        aliases = fm.get("aliases") or []
        if slug:
            forms.add(slug)
        if canonical:
            forms.add(canonical)
        for a in aliases:
            if isinstance(a, str) and len(a) >= 4:
                forms.add(a)
        return forms

    if KB_COMPANIES.exists():
        for p in KB_COMPANIES.glob("*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
                m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
                if not m:
                    continue
                fm = yaml.safe_load(m.group(1)) or {}
            except Exception:
                continue
            attio_id = (fm.get("attio_id") or "").strip()
            target = private_forms if attio_id else public_forms
            target |= _collect(fm)

    # Conflict resolution: any form that also appears under a public company → exclude
    truly_private = private_forms - public_forms

    if not truly_private:
        _private_pattern_cache = re.compile(r"(?!x)x")  # match nothing
        return _private_pattern_cache

    # Sort longest-first so multi-word names match before substrings
    escaped = sorted((re.escape(f) for f in truly_private), key=len, reverse=True)
    pattern = r"\b(?:" + "|".join(escaped) + r")\b"
    _private_pattern_cache = re.compile(pattern)
    return _private_pattern_cache


def strip_private_company_paragraphs(body: str) -> str:
    """Drop entire paragraphs that mention Cloudberry-internal companies.

    Mentions can be wikilinks `[[cnuic]]`, canonical names "Cnuic", or aliases "CNUIC".
    Done at publish-time. Underlying KB keeps everything; only the public surface is stripped.
    """
    pattern = _build_private_pattern()
    paragraphs = re.split(r"\n\s*\n", body)
    kept = [p for p in paragraphs if not pattern.search(p)]
    body = "\n\n".join(kept)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def strip_leading_template_noise(body: str) -> str:
    """Strip body-template noise that duplicates layout chrome:

    1. Leading `# Title` H1 — the page layout already renders the title from frontmatter.canonical_name
    2. `*Kind: technology*` italic line — redundant on a tech-concepts site
    3. `*Kind: technology · <rest>*` — strip the prefix, keep <rest> as the summary
    4. `· Attio deal count: \\d+` anywhere — internal Attio reference

    Done at publish-time. Underlying KB keeps the originals.
    """
    # Drop "Attio deal count" anywhere it leaks
    body = re.sub(r"\s*·\s*Attio deal count:\s*\d+", "", body)
    body = re.sub(r"Attio deal count:\s*\d+", "", body)

    # Process the leading lines: skip blanks; strip first H1 if present;
    # strip "*Kind:*" line (or convert to summary line).
    lines = body.split("\n")
    out_lines = []
    state = "leading"
    for line in lines:
        if state == "leading":
            stripped = line.strip()
            if stripped == "":
                # Skip leading blank lines silently
                continue
            # 1. Leading H1: drop it
            if re.match(r"^# [^\n]+$", stripped):
                continue
            # 2. *Kind: X*  →  drop entirely
            m_pure = re.match(r"^\*Kind:\s*[^·*]+\*$", stripped)
            if m_pure:
                continue
            # 3. *Kind: X · Y*  →  keep just *Y*
            m_summary = re.match(r"^\*Kind:\s*[^·]+·\s*(.+?)\*$", stripped)
            if m_summary:
                summary = m_summary.group(1).strip()
                if summary:
                    out_lines.append(f"*{summary}*")
                state = "body"
                continue
            # Anything else marks the start of real body content
            out_lines.append(line)
            state = "body"
        else:
            out_lines.append(line)

    return "\n".join(out_lines)


def strip_cloudberry_content(body: str) -> str:
    """Remove Cloudberry-internal content from a concept body.

    Two-pass strip:
    1. Whole ## sections whose heading starts with "Cloudberry" (e.g. "## Cloudberry relevance",
       "## Cloudberry vantage", "## Cloudberry view") — removed heading + content up to the
       next ## heading or end of file.
    2. Any remaining paragraph (separated by blank lines) that mentions "Cloudberry" — dropped
       in full.

    Done at publish-time so the underlying KB keeps the Cloudberry framing for internal use.
    """
    # Pass 1: section-level strip
    body = re.sub(
        r"^##+\s+Cloudberry[^\n]*\n.*?(?=^##+\s|\Z)",
        "",
        body,
        flags=re.MULTILINE | re.DOTALL,
    )
    # Pass 2: paragraph-level strip (any paragraph that mentions Cloudberry)
    paragraphs = re.split(r"\n\s*\n", body)
    paragraphs = [p for p in paragraphs if "cloudberry" not in p.lower()]
    body = "\n\n".join(paragraphs)
    # Tidy any triple-blank-lines created by removals
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


_public_slug_paths_cache: dict[str, str] | None = None


def _public_slug_paths() -> dict[str, str]:
    """Build slug → "macro/meso/slug" path map for every public concept.

    Used by the wikilink resolver to turn `[[maskless-lithography]]` into
    `[Maskless Lithography](/manufacturing/lithography/maskless-lithography/)`.
    """
    global _public_slug_paths_cache
    if _public_slug_paths_cache is not None:
        return _public_slug_paths_cache
    out: dict[str, str] = {}
    for macro in PUBLIC_MACROS:
        macro_dir = KB_CONCEPTS / macro
        if not macro_dir.exists():
            continue
        for f in macro_dir.rglob("*.md"):
            if f.name.startswith("_"):
                continue
            rel = f.relative_to(KB_CONCEPTS)
            parts = rel.with_suffix("").parts
            if len(parts) == 3:
                out[f.stem] = "/".join(parts)
    _public_slug_paths_cache = out
    return out


_canonical_name_cache: dict[str, str] | None = None


def _canonical_names() -> dict[str, str]:
    """Build slug → canonical_name map by reading frontmatter of every public concept."""
    global _canonical_name_cache
    if _canonical_name_cache is not None:
        return _canonical_name_cache
    out: dict[str, str] = {}
    for macro in PUBLIC_MACROS:
        macro_dir = KB_CONCEPTS / macro
        if not macro_dir.exists():
            continue
        for f in macro_dir.rglob("*.md"):
            if f.name.startswith("_"):
                continue
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
                fm, _ = parse_fm(text)
                if fm:
                    out[f.stem] = fm.get("canonical_name") or f.stem
            except Exception:
                continue
    _canonical_name_cache = out
    return out



_source_meta_cache: dict | None = None


def _source_meta() -> dict:
    """slug -> (title, url) for PUBLIC source pages, so an inline citation can
    become a real reference instead of a de-slugged prose fragment."""
    global _source_meta_cache
    if _source_meta_cache is not None:
        return _source_meta_cache
    out = {}
    for kind in PUBLIC_SOURCE_KINDS:
        d = KB / "sources" / kind
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            try:
                fm, body = parse_fm(f.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                continue
            if not fm:
                continue
            m = re.match(r"^(\d{4}-\d{2}-\d{2})", f.stem)
            out[f.stem] = {
                "title": str(fm.get("title") or f.stem).strip(),
                "url": str(fm.get("url") or "").strip(),
                "date": str(fm.get("date") or (m.group(1) if m else ""))[:10],
                "kind": kind,
                "blurb": _blurb_from_fm(fm, body),
            }
    _source_meta_cache = out
    return out


def strip_private_wikilinks(body: str) -> str:
    """Resolve wikilinks:
       - Public concept slug → markdown link `[Canonical Name](/macro/meso/slug/)`
       - Everything else → plain bold text (private companies, ideas, people, etc.)
    """
    slug_paths = _public_slug_paths()
    canonical = _canonical_names()

    def repl(m):
        inner = m.group(1)
        # Handle [[slug|display]] form
        if "|" in inner:
            slug, display = inner.split("|", 1)
            slug = slug.strip()
            display = display.strip()
        else:
            slug = inner.strip()
            display = ""

        if slug in slug_paths:
            label = display or canonical.get(slug) or slug.replace("-", " ").title()
            return f"[{label}]({BASE_PATH}/{slug_paths[slug]}/)"
        # Private date-prefixed SOURCE slug: a bold de-slugged filename mid-sentence
        # reads as debris ("**2026 07 23 Basert Advancing…**"), so render plain text
        # with the date prefix dropped and no emphasis.
        m_date = re.match(r"^\d{4}-\d{2}-\d{2}-(.+)$", slug)
        if m_date and not display:
            # A source citation. Rendering it as de-slugged prose produced
            # unreadable run-ons ("...the post silicon semiconductor era a
            # review of physics synth"), so public sources become a superscript
            # reference link and everything else is dropped outright.
            sm = _source_meta().get(slug)
            title, url = (sm["title"], sm["url"]) if sm else ("", "")
            if url.startswith("http"):
                safe = title.replace('"', "'")[:120]
                return (f'<sup class="ref"><a href="{url}" title="{safe}" '
                        f'rel="noopener">ref</a></sup>')
            return ""
        # Other private entities (companies, ideas, people) — plain bold label.
        label = display or slug.replace("-", " ").title()
        return f"**{label}**"

    body = re.sub(r"\[\[([^\]]+)\]\]", repl, body)
    # A dropped citation (source with no URL) leaves an orphan space before the
    # punctuation it preceded: "...the thermal ceiling ." Tidy those up.
    body = re.sub(r"[ \t]+([.,;:!?\)])", r"\1", body)
    body = re.sub(r"\(\s+", "(", body)
    body = re.sub(r"[ \t]{2,}", " ", body)
    # Malformed half-wikilinks ("[[slug-]" with a dropped bracket — LLM-synthesised
    # bodies occasionally produce these) survive the pattern above and render as
    # literal [[ debris. Collapse them to plain de-dated text.
    body = re.sub(
        r"\[\[(?:\d{4}-\d{2}-\d{2}-)?([^\]\n]{1,90})\]?",
        lambda m: m.group(1).replace("-", " ").rstrip(),
        body,
    )
    return body


def wikilinks_to_plain(value: str) -> str:
    """For frontmatter strings rendered as raw text (frontier questions):
    collapse any wikilink to its display name — no links, no bold."""
    canonical = _canonical_names()

    def repl(m):
        inner = m.group(1)
        if "|" in inner:
            _, display = inner.split("|", 1)
            return display.strip()
        slug = inner.strip()
        return canonical.get(slug) or slug.replace("-", " ")

    value = re.sub(r"\[\[([^\]]+)\]\]", repl, value)
    # malformed half-wikilinks (dropped bracket) — same cleanup as body
    value = re.sub(
        r"\[\[(?:\d{4}-\d{2}-\d{2}-)?([^\]\n]{1,90})\]?",
        lambda m: m.group(1).replace("-", " ").rstrip(),
        value,
    )
    return value


def strip_internal_annotations(body: str) -> str:
    """KB housekeeping lines that read as debris on the public page:
    merge/backfill provenance headings and stub-creation notes."""
    out = []
    for line in body.split("\n"):
        s = line.strip().strip("*_# ").rstrip(")").strip()
        if s.startswith("Merged from root duplicate"):
            continue
        if s.startswith("Concept stub created"):
            continue
        out.append(line)
    return "\n".join(out)


def filter_concept(fm: dict, body: str, slug: str) -> tuple[dict, str]:
    """Apply publish filter to a concept's frontmatter + body."""
    # Strip private fields
    out = {k: v for k, v in fm.items() if k not in STRIP_FIELDS}

    # Guard string-array fields against YAML mis-parsing an unquoted ": " bullet
    # as a mapping — Astro's schema rejects the whole build otherwise.
    for field in ("frontier", "aliases", "tags", "parent_concepts",
                  "related_concepts", "descendants"):
        if field in out:
            out[field] = coerce_str_list(out[field])

    # Frontier questions render as raw text on the page: drop empty items
    # (the KB's `frontier: ['']` stubs were emitting empty bullets on 292 pages)
    # and collapse wikilinks to plain display names.
    if "frontier" in out:
        out["frontier"] = [
            wikilinks_to_plain(q).strip()
            for q in out["frontier"]
            if isinstance(q, str) and q.strip()
        ]

    # Filter sources to public-only
    if "sources" in out:
        out["sources"] = filter_sources(out["sources"])

    # Compute freshness (uses pre-filter source list — captures all citations including private)
    freshness = compute_freshness(slug, fm.get("sources") or [])
    out["sources_7d"] = freshness["sources_7d"]
    out["sources_30d"] = freshness["sources_30d"]

    # Build recent-mentions list (public sources only, last ~8)
    out["recent_mentions"] = public_sources_for_concept(slug, limit=8)

    # Build the neighborhood for the per-page radial graph.
    # Just the related-concept slugs that are also public; layout happens client-side.
    slug_paths = _public_slug_paths()
    canon = _canonical_names()
    neighbors = []
    for rel in (fm.get("related_concepts") or []):
        if not isinstance(rel, str):
            continue
        if rel in slug_paths:
            neighbors.append({
                "slug": rel,
                "name": canon.get(rel, rel.replace("-", " ").title()),
                "path": f"{BASE_PATH}/{slug_paths[rel]}/",
                "macro": slug_paths[rel].split("/")[0],
            })
    out["neighbors"] = neighbors[:20]  # cap for the radial

    # Strip noise + Cloudberry + private-company paragraphs + leading template lines + private wikilinks
    return out, public_body(body)


# Sections that are the members' edition: the reasoning and the calls. The public
# page keeps what a technology is, how it works and who is in it; members get why
# it scores the way it does, the prediction, and what would change the view.
# Matched against the heading text, case-insensitive, at any ## depth.
MEMBER_SECTIONS = re.compile(
    r"^(?:prediction|predictions|forecast|verdict|"
    r"overrated or underrated|over-?rated|under-?rated|"
    r"viability|drivers|novelty|diffusion|impact|timing|"
    r"what would change (?:my|the) (?:mind|view)|bull case|bear case|"
    r"investment view|investor view|the call|our view|my view)\b",
    re.IGNORECASE,
)

# The fund is never named in either edition. Both strip it; this is the belt to
# strip_cloudberry_content's braces, applied last so nothing re-introduces it.
FUND_WORDS = re.compile(r"cloudberry", re.IGNORECASE)


def scrub_fund_mentions(body: str) -> str:
    """Drop every paragraph (and heading) that names the fund."""
    paragraphs = re.split(r"\n\s*\n", body)
    kept = [p for p in paragraphs if not FUND_WORDS.search(p)]
    return re.sub(r"\n{3,}", "\n\n", "\n\n".join(kept))


def split_sections(body: str) -> list[tuple[int, str, str]]:
    """[(level, heading, text)] — level 0 is the preamble before the first heading.

    A section runs to the next heading of the same or a higher level, so a ###
    inside a ## section stays with its parent.
    """
    lines = body.split("\n")
    out: list[tuple[int, str, list[str]]] = [(0, "", [])]
    for line in lines:
        m = re.match(r"^(##+)\s+(.+?)\s*$", line)
        if m:
            out.append((len(m.group(1)), m.group(2), [line]))
        else:
            out[-1][2].append(line)
    return [(lvl, h, "\n".join(ls)) for lvl, h, ls in out]


def strip_member_sections(body: str) -> str:
    """Public edition: remove the members' sections and their sub-sections."""
    kept: list[str] = []
    skipping_level = 0
    for level, heading, text in split_sections(body):
        if skipping_level and level > skipping_level:
            continue                       # sub-section of a removed section
        skipping_level = 0
        if level and MEMBER_SECTIONS.match(heading):
            skipping_level = level
            continue
        kept.append(text)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip("\n") + "\n"


def member_body(body: str) -> str:
    """The members' edition: the whole note minus everything confidential.

    Stripped for everyone: fund framing (the product stands on its own), Attio-
    tracked companies (deal flow), private source kinds, deal fields, Dataview
    debris. What members get that the public page does not is decided by
    MEMBER_SECTIONS, applied in public_body().
    """
    body = strip_internal_annotations(body)
    new_body = strip_dataview_blocks(body)
    new_body = strip_external_images(new_body)
    new_body = strip_cloudberry_content(new_body)
    new_body = strip_private_company_paragraphs(new_body)
    new_body = strip_leading_template_noise(new_body)
    new_body = strip_private_wikilinks(new_body)
    return scrub_fund_mentions(new_body)


def public_body(body: str) -> str:
    """The public page: the members' edition minus the reasoning sections."""
    return strip_member_sections(member_body(body))


def _headings(body: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^##+\s+([^\n]+)$", body, re.MULTILINE)]


def first_sentence(body: str, limit: int = 170) -> str:
    """One plain sentence for a link blurb: first real paragraph, markdown stripped."""
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p.startswith(("#", "|", "```", "![", "<!--", "- ", "* ")):
            continue
        p = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", p)
        p = re.sub(r"\[\[([^\]]+)\]\]", r"\1", p)
        p = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", p)
        p = re.sub(r"[*_`>#]", "", p)
        p = re.sub(r"\s+", " ", p).strip()
        m = re.match(r"^(.+?[.!?])(\s|$)", p)
        s = m.group(1) if m and len(m.group(1)) >= 40 else p
        if len(s) > limit:
            s = s[: limit - 1].rsplit(" ", 1)[0] + "…"
        return s
    return ""


def _blurb_from_fm(fm: dict, body: str) -> str:
    """A source page's one-liner: the first of several likely frontmatter fields, else its body."""
    for key in ("summary", "tldr", "one_liner", "takeaway", "key_takeaway", "description", "abstract"):
        v = fm.get(key)
        if isinstance(v, str) and v.strip():
            return first_sentence(v.strip())
    return first_sentence(body)


def member_sources(source_refs: list) -> list[dict]:
    """The full public reading list for a concept: every public source, linked, with a blurb."""
    meta = _source_meta()
    out = []
    for s in source_refs or []:
        ref = str(s).strip("[]").split("|")[0].strip()
        m = meta.get(ref)
        if not m:
            continue                        # private kind or missing: never listed
        out.append({"slug": ref, **m})
    out.sort(key=lambda x: x.get("date", ""), reverse=True)
    return out


def member_essays(slug: str) -> list[dict]:
    """The author's own newsletter pieces that discuss this concept, linked."""
    meta = _source_meta()
    out = []
    for mentioned, entry in _public_source_index():
        if entry["kind"] != "substack":
            continue
        try:
            if slug not in mentioned:
                continue
        except TypeError:
            continue
        m = meta.get(entry["slug"], {})
        if not m.get("url"):
            continue
        out.append({"slug": entry["slug"], **m})
    out.sort(key=lambda x: x.get("date", ""), reverse=True)
    return out


_public_companies_cache: dict[str, dict] | None = None


def _public_companies() -> dict[str, dict]:
    """slug -> safe company card for companies WITHOUT an Attio id.

    Attio-tracked companies are pipeline and never leave the KB. Public companies
    and well-known startups are fair to list. Field names are read defensively:
    the company template has varied, and a missing field is simply omitted.
    """
    global _public_companies_cache
    if _public_companies_cache is not None:
        return _public_companies_cache
    out: dict[str, dict] = {}
    if KB_COMPANIES.exists():
        for p in KB_COMPANIES.glob("*.md"):
            try:
                fm, body = parse_fm(p.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                continue
            if not fm or (fm.get("attio_id") or "").strip():
                continue
            card = {"slug": p.stem, "name": fm.get("canonical_name") or fm.get("name") or p.stem}
            for out_key, keys in (
                ("website", ("website", "url", "homepage")),
                ("hq", ("hq", "location", "country")),
                ("founded", ("founded", "founded_year", "year_founded")),
                ("stage", ("stage", "company_stage", "status")),
                ("blurb", ("one_liner", "summary", "description", "tldr")),
            ):
                for k in keys:
                    v = fm.get(k)
                    if isinstance(v, (str, int)) and str(v).strip():
                        card[out_key] = str(v).strip()
                        break
            if "blurb" not in card:
                b = first_sentence(scrub_fund_mentions(body))
                if b:
                    card["blurb"] = b
            if "blurb" in card and FUND_WORDS.search(card["blurb"]):
                del card["blurb"]
            out[p.stem] = card
    _public_companies_cache = out
    return out


def member_companies(company_refs: list) -> list[dict]:
    cards = _public_companies()
    out = []
    for c in company_refs or []:
        ref = str(c).strip("[]").split("|")[0].strip()
        if ref in cards:
            out.append(cards[ref])
    out.sort(key=lambda x: x["name"].lower())
    return out


def _norm(body: str) -> str:
    return re.sub(r"\s+", " ", body).strip()


def _iso(v) -> str:
    """Frontmatter dates arrive as str or datetime.date; JSON wants a string."""
    return "" if v is None else str(v)[:10]


def emit_concept(p: Path, dry_run: bool = False, out_root: Path = OUT,
                 members_root: Path | None = None) -> dict:
    """Read a KB concept, apply filter, emit to public site content dir.

    When the members' edition carries content the public page does not, the
    public frontmatter gets `members: true` (the page shows the teaser) and the
    full members' note is written as JSON under `members_root`.

    Returns a row describing the emission for the summary.
    """
    rel = p.relative_to(KB_CONCEPTS)
    parts = rel.parts
    if len(parts) < 3:
        return {"slug": p.stem, "status": "skipped — flat path", "macro": parts[0] if parts else "?"}
    macro, meso = parts[0], parts[1]
    if macro not in PUBLIC_MACROS:
        return {"slug": p.stem, "status": f"skipped — private macro {macro}", "macro": macro}

    text = p.read_text(encoding="utf-8", errors="ignore")
    fm, body = parse_fm(text)
    if fm is None:
        return {"slug": p.stem, "status": "skipped — no frontmatter", "macro": macro}

    out_fm, out_body = filter_concept(fm, body, p.stem)
    out_path = out_root / macro / meso / f"{p.stem}.md"

    m_body = member_body(body)
    has_members = _norm(m_body) != _norm(out_body)
    public_heads = set(_headings(out_body))
    # Top-level members' sections only, for the teaser ("Prediction · Impact (4/5)").
    extra_sections = [h for lvl, h, _ in split_sections(m_body)
                      if lvl == 2 and h not in public_heads]
    if has_members:
        out_fm["members"] = True
        out_fm["members_sections"] = extra_sections   # named in the public teaser

    sc = out_fm.get("scorecard") or {}
    scores = {k: (sc.get(k) if isinstance(sc.get(k), (int, float)) else None)
              for k in ("viability", "drivers", "novelty", "diffusion", "impact")}
    words = len(m_body.split())
    if any(v is not None for v in scores.values()):
        status = "draft" if out_fm.get("scorecard_status") == "draft" else "scored"
    elif words < 60 or "Stub leader page" in m_body:
        status = "stub"
    else:
        status = "unscored"
    member_entry = {
        "slug": p.stem,
        "name": out_fm.get("canonical_name") or p.stem,
        "macro": macro,
        "meso": meso,
        "path": f"{macro}/{meso}/{p.stem}",
        "last_updated": _iso(out_fm.get("last_updated")),
        "summary": first_sentence(out_body),          # the sentence under every link to it
        "extra_sections": extra_sections,
        "members": has_members,
        "status": status,
        "scores": scores,
        "verdict": sc.get("verdict") or "",
        "timing": sc.get("timing_band") or "",
        "words": words,
        "sources_7d": out_fm.get("sources_7d", 0),
        "sources_30d": out_fm.get("sources_30d", 0),
    }

    if dry_run:
        return {"slug": p.stem, "status": "would emit", "macro": macro, "meso": meso,
                "out": str((OUT / macro / meso / f"{p.stem}.md").relative_to(SITE)),
                "members": has_members, "member_entry": member_entry}

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(f"---\n{serialise_fm(out_fm)}---\n{out_body}", encoding="utf-8")

    if has_members and members_root is not None:
        m_path = members_root / macro / meso / f"{p.stem}.json"
        m_path.parent.mkdir(parents=True, exist_ok=True)
        m_path.write_text(json.dumps({
            **member_entry,
            "scorecard": out_fm.get("scorecard"),
            "scorecard_status": out_fm.get("scorecard_status"),
            "body_md": m_body,
            # Reading list: every public source, linked, one sentence each.
            "sources": member_sources(fm.get("sources") or []),
            "essays": member_essays(p.stem),
            # Who is building it — public companies and well-known startups only.
            "companies": member_companies(fm.get("companies_using") or []),
            "recent_mentions": out_fm.get("recent_mentions", []),
        }, ensure_ascii=False), encoding="utf-8")

    return {"slug": p.stem, "status": "emitted", "macro": macro, "meso": meso,
            "sources_30d": out_fm.get("sources_30d", 0),
            "members": has_members, "member_entry": member_entry,
            "recent_mentions": out_fm.get("recent_mentions", [])}


def emit_atlas_data(dry_run: bool = False, atlas_path: Path | None = None) -> dict:
    """Walk all public concepts, build nodes+edges for the full atlas view.

    Output JSON shape:
      { nodes: [{slug, name, macro, path, deg}], edges: [{a, b}] }
    `deg` is the degree (number of public neighbours) — used for node sizing.
    """
    slug_paths = _public_slug_paths()
    canon = _canonical_names()
    nodes_by_slug: dict[str, dict] = {}
    edges_set: set[tuple[str, str]] = set()

    for slug, path in slug_paths.items():
        f = KB_CONCEPTS / f"{path}.md"
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
            fm, _ = parse_fm(text)
        except Exception:
            continue
        if not fm:
            continue
        macro = path.split("/")[0]
        nodes_by_slug[slug] = {
            "slug": slug,
            "name": canon.get(slug, slug),
            "macro": macro,
            "path": f"{BASE_PATH}/{path}/",
            "deg": 0,
        }
        for rel in fm.get("related_concepts") or []:
            if not isinstance(rel, str):
                continue
            if rel in slug_paths:
                a, b = sorted([slug, rel])
                edges_set.add((a, b))

    # Compute degree
    for a, b in edges_set:
        if a in nodes_by_slug:
            nodes_by_slug[a]["deg"] += 1
        if b in nodes_by_slug:
            nodes_by_slug[b]["deg"] += 1

    out = {
        "nodes": sorted(nodes_by_slug.values(), key=lambda x: x["slug"]),
        "edges": [{"a": a, "b": b} for a, b in sorted(edges_set)],
    }

    if not dry_run:
        atlas_path = atlas_path or SITE / "src" / "data" / "atlas.json"
        atlas_path.parent.mkdir(parents=True, exist_ok=True)
        atlas_path.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")

    return out


def update_ledger(entries: list[dict], today: str) -> tuple[dict, list[dict]]:
    """Diff today's scorecards against the ledger; return (ledger, today's events).

    The first run only records a snapshot (no 778 "new concept" events). After
    that every score move, verdict or timing change, first scoring and new
    concept becomes an event with the date it was seen.
    """
    ledger: dict = {"snapshots": {}, "events": [], "bootstrapped": None}
    if LEDGER.exists():
        try:
            ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"WARN: ledger unreadable ({e}); starting a fresh one", file=sys.stderr)
    snaps = ledger.setdefault("snapshots", {})
    first_run = not snaps
    events: list[dict] = []

    def ev(e: dict, kind: str, field: str = "", old=None, new=None) -> dict:
        return {"date": today, "slug": e["slug"], "name": e["name"], "path": e["path"],
                "summary": e.get("summary", ""), "members": bool(e.get("members")),
                "kind": kind, "field": field, "old": old, "new": new}

    for e in entries:
        prev = snaps.get(e["slug"])
        if prev is None:
            if not first_run:
                events.append(ev(e, "new"))
        else:
            for dim, new in e["scores"].items():
                old = (prev.get("scores") or {}).get(dim)
                if old != new and new is not None:
                    events.append(ev(e, "score", dim, old, new))
            if e["verdict"] and prev.get("verdict") != e["verdict"]:
                events.append(ev(e, "verdict", "verdict", prev.get("verdict") or None, e["verdict"]))
            if e["timing"] and prev.get("timing") != e["timing"]:
                events.append(ev(e, "timing", "timing", prev.get("timing") or None, e["timing"]))
            if e["status"] != prev.get("status") and e["status"] in ("scored", "draft"):
                events.append(ev(e, "status", "status", prev.get("status"), e["status"]))
        snaps[e["slug"]] = {
            "name": e["name"], "path": e["path"], "scores": e["scores"],
            "verdict": e["verdict"], "timing": e["timing"], "status": e["status"],
            "first_seen": (prev or {}).get("first_seen") or today,
        }

    if first_run:
        ledger["bootstrapped"] = today
    ledger["events"] = (ledger.get("events") or []) + events
    ledger["updated"] = today
    return ledger, events


def build_changes(ledger: dict, entries: list[dict], today: str) -> dict:
    """changes.json: the last CHANGES_WINDOW_DAYS of events plus this week's most-cited concepts."""
    cutoff = (datetime.fromisoformat(today) - timedelta(days=CHANGES_WINDOW_DAYS)).date().isoformat()
    week = (datetime.fromisoformat(today) - timedelta(days=7)).date().isoformat()
    events = [e for e in ledger.get("events", []) if e.get("date", "") >= cutoff]
    events.sort(key=lambda e: (e["date"], e["name"].lower()), reverse=True)

    meta = _source_meta()
    active = []
    for e in sorted(entries, key=lambda x: (-x.get("sources_7d", 0), x["name"].lower())):
        if e.get("sources_7d", 0) <= 0:
            break
        mentions = []
        for m in e.get("recent_mentions", []):
            if m.get("date", "") < week:
                continue
            sm = meta.get(m["slug"], {})
            mentions.append({"title": m["title"], "date": m["date"], "kind": m["kind"],
                             "url": sm.get("url", ""), "blurb": sm.get("blurb", "")})
        active.append({"slug": e["slug"], "name": e["name"], "path": e["path"],
                       "summary": e.get("summary", ""), "members": bool(e.get("members")),
                       "sources_7d": e["sources_7d"], "mentions": mentions[:6]})
        if len(active) >= 15:
            break
    return {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "bootstrapped": ledger.get("bootstrapped"), "events": events, "active": active}


def previous_count(live: Path) -> int:
    """Pages in `live` before this run: the larger of the working tree and HEAD.

    Using HEAD too means a tree already gutted by an interrupted run (16 Oct:
    3 files left) cannot lower the bar the next run is measured against.
    """
    on_disk = sum(1 for _ in live.rglob("*.md")) if live.exists() else 0
    try:
        res = subprocess.run(
            ["git", "-C", str(SITE), "ls-tree", "-r", "--name-only", "HEAD",
             "--", str(live.relative_to(SITE))],
            capture_output=True, text=True, check=True,
        )
        committed = sum(1 for line in res.stdout.splitlines() if line.endswith(".md"))
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"WARN: could not read committed page count from git ({e}); "
              f"using working tree count {on_disk}", file=sys.stderr)
        committed = 0
    return max(on_disk, committed)


def swap_into_place(staged: Path, live: Path) -> None:
    """Replace `live` with `staged` using renames on the same filesystem."""
    old = staged.parent / f"{live.name}.old"
    if old.exists():
        shutil.rmtree(old)
    live.parent.mkdir(parents=True, exist_ok=True)
    if live.exists():
        live.rename(old)
    staged.rename(live)
    if old.exists():
        shutil.rmtree(old)


def main():
    dry_run = "--dry-run" in sys.argv
    allow_shrink = "--allow-shrink" in sys.argv

    # Build into a fresh staging dir; the live content dir is not touched until
    # the run has finished and passed the count guard. A leftover staging dir
    # is debris from an interrupted run and is safe to discard.
    staged_concepts = STAGING / "concepts"
    staged_members = STAGING / "members"
    staged_atlas = STAGING / "atlas.json"
    if not dry_run:
        if STAGING.exists():
            shutil.rmtree(STAGING)
        staged_concepts.mkdir(parents=True)
        staged_members.mkdir(parents=True)

    rows = []
    for p in sorted(KB_CONCEPTS.rglob("*.md")):
        if p.name.startswith("_"):
            continue
        rows.append(emit_concept(p, dry_run=dry_run, out_root=staged_concepts,
                                 members_root=staged_members))

    emitted = sum(1 for r in rows if r["status"] == "emitted" or r["status"] == "would emit")
    member_rows = [r for r in rows if r.get("members")]
    entries = sorted((r["member_entry"] for r in rows if "member_entry" in r),
                     key=lambda e: (e["macro"], e["meso"], e["name"].lower()))
    today = datetime.now(timezone.utc).date().isoformat()

    # Members' index — every public concept with its scores and status, so the
    # screener and coverage map see the whole corpus; `members` marks the ones
    # with an edition of their own. recent_mentions are needed for the changes
    # feed only; keep index.json lean.
    if not dry_run:
        (staged_members / "index.json").write_text(json.dumps({
            "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "count": len(member_rows),
            "total": len(entries),
            "concepts": entries,
        }, ensure_ascii=False), encoding="utf-8")
    skipped_private = sum(1 for r in rows if "private" in r.get("status", ""))
    skipped_other = sum(1 for r in rows if "skipped" in r.get("status", "") and "private" not in r["status"])

    # Atlas data — corpus-wide graph for /atlas/
    atlas = emit_atlas_data(dry_run=dry_run, atlas_path=staged_atlas)

    if not dry_run:
        previous = previous_count(OUT)
        floor = int(previous * MIN_KEEP_RATIO)
        print(f"count guard: {emitted} emitted vs {previous} before (floor {floor})")
        if emitted == 0 or (emitted < floor and not allow_shrink):
            print(f"ABORT: {emitted} concepts is below {MIN_KEEP_RATIO:.0%} of the previous "
                  f"{previous}. Live content left untouched; staged output kept in "
                  f"{STAGING} for inspection. Re-run with --allow-shrink if the drop is deliberate.",
                  file=sys.stderr)
            sys.exit(2)

        # Guard passed: this run counts. Record scores, emit the changes feed,
        # and give every members' concept its own history.
        for r in rows:
            if "member_entry" in r:
                r["member_entry"]["recent_mentions"] = r.get("recent_mentions", [])
        ledger, new_events = update_ledger(entries, today)
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(json.dumps(ledger, ensure_ascii=False), encoding="utf-8")
        changes = build_changes(ledger, entries, today)
        (staged_members / "changes.json").write_text(json.dumps(changes, ensure_ascii=False), encoding="utf-8")
        by_slug: dict[str, list[dict]] = {}
        for e in ledger.get("events", []):
            by_slug.setdefault(e["slug"], []).append(e)
        for r in member_rows:
            m_path = staged_members / r["macro"] / r["meso"] / f"{r['slug']}.json"
            if m_path.exists():
                data = json.loads(m_path.read_text(encoding="utf-8"))
                data["history"] = sorted(by_slug.get(r["slug"], []), key=lambda e: e["date"], reverse=True)
                m_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        print(f"ledger: {len(new_events)} change events today"
              f"{' (bootstrap run — snapshot only)' if ledger.get('bootstrapped') == today else ''}; "
              f"{len(changes['active'])} concepts active this week")

        swap_into_place(staged_concepts, OUT)
        swap_into_place(staged_members, MEMBERS_OUT)
        atlas_live = SITE / "src" / "data" / "atlas.json"
        atlas_live.parent.mkdir(parents=True, exist_ok=True)
        os.replace(staged_atlas, atlas_live)
        shutil.rmtree(STAGING)

    print(f"publish_kb.py summary ({'DRY RUN' if dry_run else 'APPLY'}):")
    print(f"  • {emitted} concepts emitted")
    print(f"  • {len(member_rows)} with a members' edition → {MEMBERS_OUT.relative_to(SITE)}/")
    print(f"  • {skipped_private} skipped (private macro — frameworks/markets)")
    print(f"  • {skipped_other} skipped (other)")
    print(f"  • atlas: {len(atlas['nodes'])} nodes, {len(atlas['edges'])} edges")

    # Distribution by macro
    from collections import Counter
    by_macro = Counter(r.get("macro") for r in rows if r["status"] in ("emitted", "would emit"))
    print()
    print("By macro:")
    for macro in sorted(PUBLIC_MACROS):
        if macro in by_macro:
            print(f"  {macro:<22} {by_macro[macro]}")


if __name__ == "__main__":
    main()

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

Usage:
    python publish_kb.py             # filter and emit
    python publish_kb.py --dry-run   # report what would change, no write
"""
from __future__ import annotations
import json
import os
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
import yaml

KB = Path.home() / "kb"
KB_CONCEPTS = KB / "concepts"
KB_COMPANIES = KB / "companies"
SITE = Path.home() / "projects" / "sotf-site"
OUT = SITE / "src" / "content" / "concepts"
BACK_REFS = KB / "scripts" / "back_refs.json"

# Base path the site is served from. Matches the `base` in astro.config.mjs.
# Reads from SOTF_BASE env var so the build + nightly cron can swap between
# "/sotf-site" (GitHub Pages subpath preview) and "" (apex once DNS is cut).
BASE_PATH = os.environ.get("SOTF_BASE", "/sotf-site").rstrip("/")

# Macros that are public (frameworks + markets stay private — internal lenses)
PUBLIC_MACROS = {
    "compute", "memory", "sensing", "communications", "energy-power",
    "manufacturing", "materials", "photonic-systems", "life-frontier",
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


def load_back_refs() -> dict:
    """Load cross_pollinate back-refs index."""
    if not BACK_REFS.exists():
        return {}
    try:
        return json.loads(BACK_REFS.read_text())
    except Exception:
        return {}


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
        # Private — render display or de-slugged name as plain bold
        label = display or slug.replace("-", " ").title()
        return f"**{label}**"

    return re.sub(r"\[\[([^\]]+)\]\]", repl, body)


def filter_concept(fm: dict, body: str, slug: str) -> tuple[dict, str]:
    """Apply publish filter to a concept's frontmatter + body."""
    # Strip private fields
    out = {k: v for k, v in fm.items() if k not in STRIP_FIELDS}

    # Filter sources to public-only
    if "sources" in out:
        out["sources"] = filter_sources(out["sources"])

    # Compute freshness (uses pre-filter source list — captures all citations including private)
    freshness = compute_freshness(slug, fm.get("sources", []))
    out["sources_7d"] = freshness["sources_7d"]
    out["sources_30d"] = freshness["sources_30d"]

    # Strip noise + Cloudberry + private-company paragraphs + leading template lines + private wikilinks
    new_body = strip_dataview_blocks(body)
    new_body = strip_cloudberry_content(new_body)
    new_body = strip_private_company_paragraphs(new_body)
    new_body = strip_leading_template_noise(new_body)
    new_body = strip_private_wikilinks(new_body)

    return out, new_body


def emit_concept(p: Path, dry_run: bool = False) -> dict:
    """Read a KB concept, apply filter, emit to public site content dir.

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
    out_path = OUT / macro / meso / f"{p.stem}.md"

    if dry_run:
        return {"slug": p.stem, "status": "would emit", "macro": macro, "meso": meso, "out": str(out_path.relative_to(SITE))}

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(f"---\n{serialise_fm(out_fm)}---\n{out_body}", encoding="utf-8")
    return {"slug": p.stem, "status": "emitted", "macro": macro, "meso": meso, "sources_30d": out_fm.get("sources_30d", 0)}


def main():
    dry_run = "--dry-run" in sys.argv

    # Wipe + recreate output dir for clean slate (no stale files)
    if not dry_run:
        if OUT.exists():
            shutil.rmtree(OUT)
        OUT.mkdir(parents=True)

    rows = []
    for p in sorted(KB_CONCEPTS.rglob("*.md")):
        if p.name.startswith("_"):
            continue
        rows.append(emit_concept(p, dry_run=dry_run))

    emitted = sum(1 for r in rows if r["status"] == "emitted" or r["status"] == "would emit")
    skipped_private = sum(1 for r in rows if "private" in r.get("status", ""))
    skipped_other = sum(1 for r in rows if "skipped" in r.get("status", "") and "private" not in r["status"])

    print(f"publish_kb.py summary ({'DRY RUN' if dry_run else 'APPLY'}):")
    print(f"  • {emitted} concepts emitted")
    print(f"  • {skipped_private} skipped (private macro — frameworks/markets)")
    print(f"  • {skipped_other} skipped (other)")

    # Distribution by macro
    from collections import Counter
    by_macro = Counter(r.get("macro") for r in rows if r["status"] in ("emitted", "would emit"))
    print()
    print("By macro:")
    for macro in ["compute", "memory", "sensing", "communications", "energy-power",
                  "manufacturing", "materials", "photonic-systems", "life-frontier"]:
        if macro in by_macro:
            print(f"  {macro:<22} {by_macro[macro]}")


if __name__ == "__main__":
    main()

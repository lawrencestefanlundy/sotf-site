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
SITE = Path.home() / "projects" / "sotf-site"
OUT = SITE / "src" / "content" / "concepts"
BACK_REFS = KB / "scripts" / "back_refs.json"

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


def strip_private_wikilinks(body: str) -> str:
    """Replace wikilinks to private slugs with plain text.

    Public slugs (concepts in the new public macros, tours, writing) stay as
    wikilinks; everything else (companies, ideas, people, private sources) becomes
    plain bold text.
    """
    # Build public-slug allowlist: every concept in a public macro
    public_slugs = set()
    for macro in PUBLIC_MACROS:
        macro_dir = KB_CONCEPTS / macro
        if not macro_dir.exists():
            continue
        for f in macro_dir.rglob("*.md"):
            public_slugs.add(f.stem)

    def repl(m):
        inner = m.group(1)
        # Handle [[slug|display]] form
        if "|" in inner:
            slug, display = inner.split("|", 1)
            slug = slug.strip()
            display = display.strip()
        else:
            slug = inner.strip()
            display = slug.replace("-", " ").title()
        if slug in public_slugs:
            return m.group(0)  # leave wikilink as-is
        # Private: render display name as plain bold
        return f"**{display}**"

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

    # Strip Dataview blocks (useless on public site) + private wikilinks
    new_body = strip_dataview_blocks(body)
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

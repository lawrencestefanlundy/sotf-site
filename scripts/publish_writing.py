#!/usr/bin/env python3
"""
publish_writing.py — emit the Substack archive index into the site.

Two sources, merged:
  1. ~/kb/sources/substack/*.md — carry a VERIFIED canonical `url` in
     frontmatter. Authoritative, but incomplete (they thin out after early 2026).
  2. ~/icloud/.../Substack/posts-md/*.md — the complete backfilled archive
     (99 posts), but its filenames use DESCRIPTIVE slugs that diverge from
     Substack's canonical slugs for ~14 posts, so a URL derived from the
     filename can 404.

For (2) the candidate URL is therefore HTTP-verified before it is published,
with an alias map for the known divergences. Results are cached in
scripts/.writing_url_cache.json so the nightly run doesn't re-check ~100 URLs;
delete the cache to force a full re-verify.

Emits src/content/writing/<slug>.md — frontmatter only (title, date, url).
Bodies are NOT copied: the canonical read is on Substack, and duplicating the
essays here would compete with them in search.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
import publish_kb as pk  # noqa: E402

KB_SUBSTACK = Path.home() / "kb" / "sources" / "substack"
ICLOUD_ARCHIVE = (Path.home() / "Library/Mobile Documents/com~apple~CloudDocs"
                  / "Work/State of the Future/Substack/posts-md")
OUT = Path(__file__).resolve().parent.parent / "src" / "content" / "writing"
CACHE = Path(__file__).parent / ".writing_url_cache.json"
BASE_URL = "https://stateofthefuture.substack.com/p/"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Local descriptive filename slug -> canonical Substack slug.
# Source: ~/reference/work/stateofthefuture/substack.md § "Slug aliasing".
ALIASES = {
    "friday-four-issue-1-agents-automation-fractile-olix": "four-things-friday",
    "friday-four-issue-2-security-vs-productivity": "four-things-friday-575",
    "friday-four-issue-3-the-panic-stage": "four-things-what-do-these-people",
    "friday-four-issue-4-wake-up-and-stay-sexy": "state-of-the-future-friday-four",
    "friday-four-issue-5-i-am-become-the-orchestrator": "state-of-the-future-friday-four-be4",
    "friday-four-issue-6-the-new-sovereigns-are-plugging-in": "state-of-the-future-friday-four-03a",
    "friday-four-issue-7-compute-goes-vertical": "state-of-the-future-friday-four-d68",
    "friday-four-issue-8-two-asset-classes-in-a-trenchcoat": "state-of-the-future-friday-four-251",
    "friday-four-issue-9-ai-now-behind-closed-doors": "state-of-the-future-friday-four-551",
    "friday-four-issue-10-half-term-man": "state-of-the-future-friday-four-67c",
    "friday-four-issue-11-everywhere-except-in-the-statistics": "state-of-the-future-friday-four-002",
    "friday-four-issue-12-anthropic-is-cheap-at-010-peg-r": "state-of-the-future-friday-four-7b7",
    "how-to-invest-in-ai-sovereignty": "how-to-invest-in-ai-sovereignty-sovereign",
    "pragmatic-semiconductor-interview": "fungible-compute-mortal-computing",
}

MASTHEAD = re.compile(r"^state of the future", re.I)


def load_cache() -> dict:
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text())
        except Exception:
            return {}
    return {}


def verify(url: str, cache: dict, session: requests.Session) -> bool:
    if url in cache:
        return bool(cache[url])
    ok = False
    try:
        r = session.get(url, headers={"User-Agent": UA}, timeout=20,
                        allow_redirects=True, stream=True)
        ok = r.status_code == 200
        r.close()
    except requests.RequestException:
        ok = False
    cache[url] = ok
    time.sleep(0.4)  # be polite to Substack
    return ok


def title_from_archive(body: str, slug: str) -> str:
    """Archive posts put the piece title in the first '## ' heading; the '# '
    line is usually the masthead ('State of the Future: Friday Three')."""
    h2 = [m.group(1).strip() for m in re.finditer(r"(?m)^##\s+(.+)$", body)]
    for h in h2:
        if h and not MASTHEAD.match(h):
            return h
    h1 = [m.group(1).strip() for m in re.finditer(r"(?m)^#\s+(.+)$", body)]
    for h in h1:
        h = re.sub(r"^[^\w]*", "", h).strip()  # drop leading emoji
        if h and not MASTHEAD.match(h):
            return h
    return slug.replace("-", " ").capitalize()


def main() -> None:
    force = "--reverify" in sys.argv
    cache = {} if force else load_cache()
    session = requests.Session()
    posts: dict[str, dict] = {}

    # 1. KB sources — good TITLES, but their `url` is NOT trustworthy: 69 of 71
    # point at https://stateofthefuture.io/p/... , the Substack custom domain
    # that was planned and never cut over, so those links are dead. Only the
    # slug is reused; the URL is rebuilt on the real Substack host and verified
    # like every other link.
    kb_titles: dict[str, tuple[str, str]] = {}
    for p in sorted(KB_SUBSTACK.glob("*.md")):
        fm, _ = pk.parse_fm(p.read_text(encoding="utf-8", errors="ignore"))
        if not fm:
            continue
        url = (fm.get("url") or "").strip()
        title = (fm.get("title") or "").strip()
        date = str(fm.get("date") or "")[:10]
        if "/p/" not in url or not title or not date:
            continue  # e.g. one entry points at a Google Doc, not a post
        kb_titles[url.rstrip("/").rsplit("/", 1)[-1]] = (title, date)

    kb_count = 0
    for slug, (title, date) in kb_titles.items():
        url = BASE_URL + slug
        if not verify(url, cache, session):
            continue
        posts[slug] = {"title": title, "published_date": date, "external_url": url}
        kb_count += 1

    # 2. Full archive — derive + verify.
    checked = added = failed = 0
    if ICLOUD_ARCHIVE.exists():
        for p in sorted(ICLOUD_ARCHIVE.glob("*.md")):
            m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", p.name)
            if not m:
                continue
            date, local_slug = m.group(1), m.group(2)
            slug = ALIASES.get(local_slug, local_slug)
            url = BASE_URL + slug
            if slug in posts:
                # Already have it from the KB, but the KB `date:` is the SOURCE
                # date (when the piece was drafted/recorded) and can precede
                # publication. The archive filename carries Substack's true
                # publish date, so that wins for an archive index.
                posts[slug]["published_date"] = date
                continue
            checked += 1
            if not verify(url, cache, session):
                failed += 1
                continue
            body = p.read_text(encoding="utf-8", errors="ignore")
            posts[slug] = {
                "title": title_from_archive(body, local_slug),
                "published_date": date,
                "external_url": url,
            }
            added += 1

    CACHE.write_text(json.dumps(cache, indent=0, sort_keys=True))

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for slug, data in posts.items():
        name = f"{data['published_date']}-{slug}.md"
        (OUT / name).write_text(f"---\n{pk.serialise_fm(data)}---\n", encoding="utf-8")

    print(f"writing publish: {len(posts)} posts "
          f"({kb_count} verified from KB titles, {added} added from archive, "
          f"{failed} archive URLs unverified and skipped of {checked} checked)")


if __name__ == "__main__":
    main()

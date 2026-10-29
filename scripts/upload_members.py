#!/usr/bin/env python3
"""
upload_members.py — sync the members' edition (.members-out/) to the private R2 bucket.

publish_kb.py writes one JSON per paywalled concept plus index.json into
.members-out/ (gitignored — this repo is public). The Worker serving
/members/… reads those objects straight from R2, so a sync here is the
members' deploy: no rebuild, live on the next request.

Credentials come from the environment (set in ~/.config/kb/env, which
nightly_publish.sh sources):

    R2_ACCOUNT_ID          Cloudflare account id
    R2_ACCESS_KEY_ID       R2 API token (Object Read & Write on the bucket)
    R2_SECRET_ACCESS_KEY
    R2_BUCKET              defaults to "sotf-members"

Needs boto3 in the kb venv:  pip install boto3

Usage:
    python upload_members.py             # upload changed/new objects, delete stale ones
    python upload_members.py --dry-run   # report only
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
SRC = SITE / ".members-out"
BUCKET = os.environ.get("R2_BUCKET", "sotf-members")
# Never wipe the bucket because a broken run produced an empty or tiny tree.
MIN_OBJECTS = 10


def client():
    try:
        import boto3  # noqa: WPS433 — optional dependency, only needed here
        from botocore.config import Config
    except ImportError:
        sys.exit("upload_members.py: boto3 missing — run `pip install boto3` in the kb venv")
    account = os.environ.get("R2_ACCOUNT_ID")
    key = os.environ.get("R2_ACCESS_KEY_ID")
    secret = os.environ.get("R2_SECRET_ACCESS_KEY")
    if not (account and key and secret):
        sys.exit("upload_members.py: R2_ACCOUNT_ID / R2_ACCESS_KEY_ID / R2_SECRET_ACCESS_KEY not set")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account}.r2.cloudflarestorage.com",
        aws_access_key_id=key,
        aws_secret_access_key=secret,
        region_name="auto",
        config=Config(signature_version="s3v4", retries={"max_attempts": 4}),
    )


def local_objects() -> dict[str, Path]:
    if not SRC.exists():
        sys.exit(f"upload_members.py: {SRC} does not exist — run publish_kb.py first")
    return {str(p.relative_to(SRC)).replace(os.sep, "/"): p for p in SRC.rglob("*.json")}


def remote_objects(s3) -> dict[str, str]:
    """key -> ETag (an MD5 for single-part uploads, which is all we do)."""
    out: dict[str, str] = {}
    token = None
    while True:
        kwargs = {"Bucket": BUCKET, "MaxKeys": 1000}
        if token:
            kwargs["ContinuationToken"] = token
        resp = s3.list_objects_v2(**kwargs)
        for obj in resp.get("Contents", []):
            out[obj["Key"]] = obj.get("ETag", "").strip('"')
        if not resp.get("IsTruncated"):
            return out
        token = resp.get("NextContinuationToken")


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    local = local_objects()
    if len(local) < MIN_OBJECTS:
        sys.exit(f"upload_members.py: only {len(local)} objects in {SRC}; refusing to sync "
                 f"(floor {MIN_OBJECTS}) — looks like a broken publish run")
    if "index.json" not in local:
        sys.exit("upload_members.py: index.json missing from .members-out — refusing to sync")

    s3 = client()
    remote = remote_objects(s3)

    to_upload = []
    for key, path in local.items():
        md5 = hashlib.md5(path.read_bytes()).hexdigest()
        if remote.get(key) != md5:
            to_upload.append((key, path))
    to_delete = [k for k in remote if k not in local]

    print(f"upload_members.py: {len(local)} local, {len(remote)} remote → "
          f"{len(to_upload)} to upload, {len(to_delete)} to delete"
          f"{' (DRY RUN)' if dry_run else ''}")
    if dry_run:
        for k, _ in to_upload[:20]:
            print(f"  ↑ {k}")
        for k in to_delete[:20]:
            print(f"  ✕ {k}")
        return

    def put(item):
        key, path = item
        s3.put_object(Bucket=BUCKET, Key=key, Body=path.read_bytes(),
                      ContentType="application/json; charset=utf-8",
                      CacheControl="private, no-store")
        return key

    # Upload concepts first, index.json last, so the index never points at a
    # concept the bucket does not hold yet.
    concepts = [i for i in to_upload if i[0] != "index.json"]
    with ThreadPoolExecutor(max_workers=16) as pool:
        list(pool.map(put, concepts))
    for item in to_upload:
        if item[0] == "index.json":
            put(item)

    for i in range(0, len(to_delete), 1000):
        chunk = to_delete[i:i + 1000]
        s3.delete_objects(Bucket=BUCKET, Delete={"Objects": [{"Key": k} for k in chunk], "Quiet": True})

    summary = json.loads((SRC / "index.json").read_text(encoding="utf-8"))
    print(f"upload_members.py: synced {summary.get('count', '?')} members' concepts to r2://{BUCKET}")


if __name__ == "__main__":
    main()

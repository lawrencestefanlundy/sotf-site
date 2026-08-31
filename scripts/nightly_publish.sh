#!/usr/bin/env bash
# Nightly KB → site publish.
#
# Runs daily at 07:30 (after KB morning-brief at 06:30) via launchd plist
# com.lawrence.sotf-site.publish. Steps:
#   1. Source ~/.config/kb/env (PATH, ANTHROPIC_API_KEY etc.)
#   2. Activate the kb scripts venv (provides PyYAML etc.)
#   3. Run publish_kb.py — walks ~/kb/concepts/, filters, emits filtered markdown
#      to ~/projects/sotf-site/src/content/concepts/
#   4. Commit + push the snapshot to github.com/lawrencelundy/sotf-site
#   5. GitHub Action picks up the push, rebuilds, deploys to GitHub Pages
#
# Logs to ~/projects/sotf-site/logs/nightly-publish.log

set -euo pipefail

# Site is served at the apex domain (stateofthefuture.io), so internal links
# resolve from root — publish with an empty base path, not the /sotf-site preview.
export SOTF_BASE=""

SITE_DIR="$HOME/projects/sotf-site"
LOG_DIR="$SITE_DIR/logs"
LOG_FILE="$LOG_DIR/nightly-publish.log"
mkdir -p "$LOG_DIR"

# shellcheck disable=SC1090
. "$HOME/.config/kb/env" 2>/dev/null || true

# Activate the kb venv (provides yaml, etc. for publish_kb.py)
# shellcheck disable=SC1091
. "$HOME/kb/scripts/.venv/bin/activate"

stamp=$(date '+%Y-%m-%d %H:%M:%S %Z')
echo "" >> "$LOG_FILE"
echo "=== $stamp — nightly publish ===" >> "$LOG_FILE"

# Step 1: emit filtered KB snapshot into the Astro content collection.
python3 "$SITE_DIR/scripts/publish_kb.py" >> "$LOG_FILE" 2>&1

# Step 1a: Substack archive index (URL-verified, cached).
python3 "$SITE_DIR/scripts/publish_writing.py" >> "$LOG_FILE" 2>&1

# Step 2: stage + commit (only if there are real changes; git commit
#   --allow-empty=NO will exit 1 if nothing to commit — we treat that as success).
cd "$SITE_DIR"

# Push with retry: launchd at 07:30 sometimes runs before DNS/network is up
# ("Could not resolve host: github.com" — 10 failures, 19-28 Aug 2026, which left
# the live site 11 days stale). 3 attempts, 60s apart; a final failure is loud.
push_with_retry() {
  local attempt
  for attempt in 1 2 3; do
    if git push -q >> "$LOG_FILE" 2>&1; then
      return 0
    fi
    echo "push attempt $attempt failed; retrying in 60s" >> "$LOG_FILE"
    sleep 60
  done
  echo "PUSH FAILED after 3 attempts — site NOT deployed; commits remain local" >> "$LOG_FILE"
  return 1
}

git add src/content/concepts src/content/writing >> "$LOG_FILE" 2>&1

if git diff --cached --quiet; then
  # Even with no new content, catch up any commits stranded by earlier push failures.
  if [ -n "$(git log --oneline @{u}..HEAD 2>/dev/null)" ]; then
    echo "No new changes, but unpushed commits found — pushing backlog." >> "$LOG_FILE"
    push_with_retry
  else
    echo "No changes since last publish — skipping commit + push." >> "$LOG_FILE"
  fi
  exit 0
fi

today=$(date '+%Y-%m-%d')
git commit -q -m "Nightly KB publish — $today" >> "$LOG_FILE" 2>&1
push_with_retry
echo "Pushed snapshot. GitHub Action will rebuild + redeploy." >> "$LOG_FILE"

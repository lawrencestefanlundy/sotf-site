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

# Step 2: stage + commit (only if there are real changes; git commit
#   --allow-empty=NO will exit 1 if nothing to commit — we treat that as success).
cd "$SITE_DIR"
git add src/content/concepts >> "$LOG_FILE" 2>&1

if git diff --cached --quiet; then
  echo "No changes since last publish — skipping commit + push." >> "$LOG_FILE"
  exit 0
fi

today=$(date '+%Y-%m-%d')
git commit -q -m "Nightly KB publish — $today" >> "$LOG_FILE" 2>&1
git push -q >> "$LOG_FILE" 2>&1
echo "Pushed snapshot. GitHub Action will rebuild + redeploy." >> "$LOG_FILE"

#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "==> Pulling latest digest from GitHub Actions..."
git pull origin main

echo "==> Publishing draft to Substack..."
uv run python -m outwire.main --publish --no-email --reuse-last

echo ""
echo "Done. Review your draft at https://outwire.substack.com/publish"
echo "Hit publish when ready."

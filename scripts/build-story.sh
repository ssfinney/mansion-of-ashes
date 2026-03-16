#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TWEEGO_BIN="$ROOT_DIR/.tools/tweego/tweego"
STORY_FILE="$ROOT_DIR/story/mansion-of-ashes.tw"
OUTPUT_FILE="$ROOT_DIR/build/mansion-of-ashes.html"

if [ ! -x "$TWEEGO_BIN" ]; then
  echo "Missing Tweego at $TWEEGO_BIN" >&2
  echo "Install the local toolchain before building." >&2
  exit 1
fi

"$TWEEGO_BIN" -f sugarcube-2 -o "$OUTPUT_FILE" "$STORY_FILE"
echo "Built $OUTPUT_FILE"

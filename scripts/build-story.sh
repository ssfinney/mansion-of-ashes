#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TWEEGO_BIN="$ROOT_DIR/.tools/tweego/tweego"
STORY_FORMATS_ROOT="$ROOT_DIR/.storyformats"
STORY_FORMAT_DIR="$STORY_FORMATS_ROOT/sugarcube-2"
STORY_FORMAT_FILE="$STORY_FORMAT_DIR/format.js"
STORY_FILE="$ROOT_DIR/story/mansion-of-ashes.tw"
OUTPUT_FILE="$ROOT_DIR/build/mansion-of-ashes.html"

if [ ! -x "$TWEEGO_BIN" ]; then
  echo "Missing Tweego at $TWEEGO_BIN" >&2
  echo "Install the local toolchain before building." >&2
  exit 1
fi

if [ ! -d "$STORY_FORMAT_DIR" ]; then
  echo "Missing SugarCube story format at $STORY_FORMAT_DIR" >&2
  echo "Install SugarCube into .storyformats/sugarcube-2 before building." >&2
  exit 1
fi

if [ ! -f "$STORY_FORMAT_FILE" ]; then
  echo "Incomplete SugarCube install: missing $STORY_FORMAT_FILE" >&2
  echo "Reinstall the SugarCube format bundle into .storyformats/sugarcube-2." >&2
  exit 1
fi

TWEEGO_PATH="$STORY_FORMATS_ROOT" "$TWEEGO_BIN" -f sugarcube-2 -o "$OUTPUT_FILE" "$STORY_FILE"
echo "Built $OUTPUT_FILE"

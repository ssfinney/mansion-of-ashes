# Browser Validation Notes (2026-04-05)

## Baseline Findings Before Fixes

- Replay from all three endings used `[[Play again->Title]]`, which returns to `Title` without a hard story restart; this risks stale state in-session.
- Existing HUD and prose styling were atmospheric and readable on desktop defaults, but small-screen density and link touch spacing needed targeted polish.
- No obvious narrative-flow issues were introduced by the current compact reconvergent structure.

## Post-Change Verification Checklist

- Build succeeds with `bash scripts/build-story.sh`.
- Replay from endings now uses `Engine.restart()` and starts from clean state.
- Mobile-oriented media queries applied for ~768px and ~360–390px ranges to improve text comfort, link spacing, and HUD wrapping.

## Screenshot Smoke Coverage (Playwright)

- Visual baselines now live in `tests/screenshots/baseline/`.
- Screenshot diffs and failure artifacts are written to `tests/screenshots/failures/`.
- Covered states:
  - `title.desktop` at `1280x800`
  - `title.mobile` at `390x844`
  - `hud.desktop` after one choice click from title
  - `hud.mobile` after one choice click from title
  - `ending.desktop` fallback capture at two clicks from title (Hallway), since no stable ending passage is reachable in three clicks or fewer

## Local Visual Validation Commands

1. Build export: `bash scripts/build-story.sh`
2. Start local server: `python -m http.server 8000 --bind 127.0.0.1`
3. Create or refresh baselines: `pytest -q tests/test_visual_smoke.py --browser chromium --update-snapshots`
4. Diff against baseline: `pytest -q tests/test_visual_smoke.py --browser chromium`

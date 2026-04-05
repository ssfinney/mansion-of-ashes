# Browser Validation Notes (2026-04-05)

## Baseline Findings Before Fixes

- Replay from all three endings used `[[Play again->Title]]`, which returns to `Title` without a hard story restart; this risks stale state in-session.
- Existing HUD and prose styling were atmospheric and readable on desktop defaults, but small-screen density and link touch spacing needed targeted polish.
- No obvious narrative-flow issues were introduced by the current compact reconvergent structure.

## Post-Change Verification Checklist

- Build succeeds with `bash scripts/build-story.sh`.
- Replay from endings now uses `Engine.restart()` and starts from clean state.
- Mobile-oriented media queries applied for ~768px and ~360–390px ranges to improve text comfort, link spacing, and HUD wrapping.

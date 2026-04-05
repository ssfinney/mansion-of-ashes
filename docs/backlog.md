# Backlog

## Done

- ~~Export a browser-ready HTML build into `build/`~~ — Tweego toolchain documented in `scripts/export-notes.md`; Twine 2 import path documented as alternative
- ~~Expand the conservatory sequence with one more optional clue and a stronger visual set piece~~ — birdcage examine zone added with diary-aware text; dawn-phase sky in glass ceiling
- ~~Introduce a weather layer that shifts room descriptions as dawn approaches~~ — dawn progression via `$endingScore` in Hallway and Conservatory
- ~~Add more object examination passages that enrich theme without adding major branches~~ — caretaker presence traces in Bedroom, Kitchen, Fuse Box, Main Exit; kitchen direction cue in Hallway

## Prioritized Improvements

- Add a second, earlier interaction beat with the caretaker — a muffled sound, a shape at a window — to deepen ambiguity before the exit
- Tighten wording through playtesting to keep average completion time inside 20 to 30 minutes
- Add a hint-safe fail state or reset affordance for players who reach the basement too early without matches (current handling is functional but bare)
- Prepare a scene-by-scene prose revision queue for Claude collaboration

## Content Expansion Ideas (5 passage slots remain)

- Add a locked servant passage with material that complicates the family's public history
- Add one alternate route to the fuse box that trades safety for speed
- Create a post-ending codex or epilogue unlocked by clue completeness (`$endingScore >= 5`)

## Playtesting Checklist

- Confirm the central puzzle can be solved without guesswork
- Confirm players understand the silver key opens the conservatory
- Check whether the ledger clue is strong enough to direct the portrait interaction
- Check whether the service-door clue reads as meaningful rather than ornamental
- Verify that endings feel earned rather than abrupt
- Check trust-choice wording so the caretaker remains ambiguous, not sinister or saintly
- Verify dawn sky progression feels organic, not mechanical
- Verify birdcage examine text lands correctly with and without the diary page
- Verify every loop back to `Hallway` remains readable and not repetitive


## Claude Next-Step Review (2026-04-05)

### 1) Second-playthrough hint in `Title`

**Recommendation:** do next, but keep the hint subtle and optional.

- **Why:** returning players currently restart with no acknowledgement of prior completion. A lightweight hint can improve replay discovery without flattening mystery tone.
- **Implementation note:** this needs cross-run persistence. `[[Play again->Title]]` does not reset story state or re-run `StoryInit`; use `Engine.restart()` for an in-session hard reset, and use SugarCube metadata (`memorize()`/`recall()`) to persist a completion flag across full restarts or refreshes.
- **Scope guard:** one short line and one optional link in `Title`; avoid explicit solution text.
- **Risk:** over-directive copy could reduce pacing and undermine discovery.

### 2) Ambient sound via HTML audio (rain, house-settling)

**Recommendation:** treat as a controlled polish task after mobile readability.

- **Why:** atmosphere gain is real, but browser autoplay policies and mobile power/network behavior can make audio brittle.
- **Implementation note:** default audio should be off until user interaction. Add an explicit toggle and persistent preference state.
- **Scope guard:** one looping rain bed + one sparse settling layer is enough; avoid continuous jump-scare stingers.
- **Risk:** if not optional, audio can hurt accessibility and first-load reliability.

### 3) Fourth optional conservatory clue (birdcage atmosphere beat)

**Recommendation:** good fit for current design philosophy; implement soon.

- **Why:** deepens interpretation without expanding hard branches, and naturally reinforces the conservatory reveal.
- **Implementation note:** keep this clue interpretive rather than confirmatory. It should suggest memory, neglect, and ritualized care without proving a supernatural event.
- **Scope guard:** one interaction in `Conservatory` that reconverges immediately to hallway loop.
- **State/doc impact:** add one boolean only if referenced later; if purely atmospheric and single-use, avoid extra state.

### 4) Mobile CSS pass

**Recommendation:** highest priority polish pass before audio.

- **Why:** current typography and spacing target desktop rhythm; small screens need deliberate scaling for readability and tap comfort.
- **Implementation note:** add focused media queries in `StoryStyles` for body text, HUD density, and link spacing; test common viewport widths.
- **Scope guard:** keep visual identity unchanged; prioritize legibility and interaction reliability.

## Bugs And Technical Debt To Address During Next Steps

- `$endingScore` now functions as pacing/atmosphere state for dawn progression; keep docs explicit that ending routing depends on clue-state booleans (`_fullTruth`) rather than score thresholds.
- Any second-playthrough hint feature should treat two concerns separately: (1) in-session restart behavior (`Engine.restart()`), and (2) cross-session persistence via metadata (`memorize()`/`recall()`).

## Suggested Implementation Order

1. Mobile CSS pass (high player impact, low continuity risk)
2. Birdcage optional clue (content value, low system risk)
3. Second-playthrough hint (small UX gain, requires persistence decision)
4. Ambient audio (highest technical/accessibility surface area)

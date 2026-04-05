# Backlog

## Done

- ~~Export a browser-ready HTML build into `build/`~~ — Tweego toolchain documented in `scripts/export-notes.md`; Twine 2 import path documented as alternative
- ~~Expand the conservatory sequence with one more optional clue and a stronger visual set piece~~ — birdcage examine zone added with diary-aware text; dawn-phase sky in glass ceiling
- ~~Introduce a weather layer that shifts room descriptions as dawn approaches~~ — dawn progression via `$endingScore` in Hallway and Conservatory
- ~~Add more object examination passages that enrich theme without adding major branches~~ — caretaker presence traces in Bedroom, Kitchen, Fuse Box, Main Exit; kitchen direction cue in Hallway
- ~~Add a second, earlier interaction beat with the caretaker~~ — Vale glimpsed through the conservatory's collapsed window moving across the grounds
- ~~Add a hint-safe fail state or reset affordance for early basement access~~ — improved evocative fail text; dark descent option (no matches + has fuse + read ledger)
- ~~Add a locked servant passage with material that complicates the family's public history~~ — `Servant's Quarters` passage, power-gated, with third-party letter establishing Vale as Elise's de facto guardian; alternative 4th clue for Bitter Truth
- ~~Add one alternate route to the fuse box that trades safety for speed~~ — dark descent via `$descendedDark`; skip kitchen if you have fuse + ledger knowledge
- ~~Create a post-ending codex/epilogue unlocked by clue completeness~~ — `Epilogue` passage linked from all endings when `$unlockedEpilogue`; neutral assembled account of the night of the fire
- ~~Tighten wording~~ — Study opening paragraph compressed; Ending: Escape closing line revised

## Remaining Ideas (3 passage slots)

- Add a fourth confrontation choice with Vale ("Ask what he's been tending") that yields a distinct flavor of Escape — curious rather than resigned
- Post-game replay hint on the Title screen after first completion
- Consider a brief Bedroom examination (the nameplate on the door) that hints the player woke in Elise's room

## Playtesting Checklist

- Confirm the central puzzle can be solved without guesswork
- Confirm the dark descent route works: Conservatory (fuse) → Basement (no matches, has fuse + ledger) → dark descent → power restored
- Confirm Servant's Quarters appears in Hallway only when `$powerOn`; letter reads correctly; `$readServantLog` gates Bitter Truth as alternative to `$heardLockedDoor`
- Confirm Epilogue link appears in all three endings when `$unlockedEpilogue` is true (set at confrontation, before choice)
- Confirm Epilogue does NOT appear when `_fullTruth` was false at confrontation
- Confirm players understand the silver key opens the conservatory
- Check whether the ledger clue is strong enough to direct the portrait interaction
- Verify that endings feel earned rather than abrupt
- Verify dawn sky progression feels organic, not mechanical
- Verify birdcage examine text lands correctly with and without the diary page
- Verify Vale glimpse in Conservatory lands as recognition rather than alarm

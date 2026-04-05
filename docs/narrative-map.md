# Narrative Map

## Passage List

- Title
- Credits: Audio
- StoryInit
- Bedroom
- Hallway
- Kitchen
- Study Door
- Study
- Basement Stairs
- Fuse Box
- Conservatory
- Caretaker Encounter
- Main Exit
- Ending: Escape
- Ending: Bitter Truth
- Ending: House of Lies

Technical passage (non-narrative): `PassageHeader` handles centralized audio routing when enabled.

## Flow Overview

`Title -> Bedroom -> Hallway`

From `Title`, the player can optionally open `Credits: Audio` and return to `Title` before starting.

From `Hallway`, the player can circulate through:

- `Kitchen` to secure matches
- `Kitchen` to discover an optional service-door clue that sharpens the ending context
- `Study Door -> Study` to read the ledger and recover the diary page
- `Basement Stairs -> Fuse Box` to learn a fuse is missing and later restore power
- portrait interaction in `Hallway` to claim the silver key after reading the ledger
- `Conservatory` once the silver key is obtained
- `Main Exit` once power is restored

`Main Exit` routes to `Caretaker Encounter`, which resolves to one of three endings.

## Reconvergence Notes

- Exploration branches reconverge through `Hallway`, which acts as the structural hub.
- The study and conservatory each gate one piece of the same core puzzle instead of creating separate quest lines.
- The diary-page and service-door clues do not create new branches; they enrich the confrontation and ending evaluation.
- Endings diverge late, keeping the playable prototype compact while making earlier choices matter.

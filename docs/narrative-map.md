# Narrative Map

## Passage List

- Title
- StoryInit
- Bedroom
- Hallway
- Hallway-Portrait
- Kitchen
- Study Door
- Study
- Basement Stairs
- Fuse Box
- Servant's Quarters
- Conservatory
- Main Exit
- Caretaker Encounter
- Ending: Escape
- Ending: Bitter Truth
- Ending: House of Lies
- Epilogue

**Total: 22 passages (3 slots remaining)**

## Flow Overview

`Title -> Bedroom -> Hallway`

From `Hallway`, the player can circulate through:

- `Kitchen` to secure matches; optional service-door clue (pantry)
- `Study Door -> Study` to read the ledger and recover the diary page
- `Basement Stairs -> Fuse Box` to learn a fuse is missing and later restore power; dark descent available if player has fuse + ledger read and no matches
- portrait interaction in `Hallway` to claim the silver key after reading the ledger
- `Conservatory` once the silver key is obtained
- `Servant's Quarters` once power is restored — optional; contains alternative 4th clue for Bitter Truth
- `Main Exit` once power is restored

`Main Exit` routes to `Caretaker Encounter`, which resolves to one of three endings. All three endings offer a link to `Epilogue` when `$unlockedEpilogue` is true.

## Reconvergence Notes

- Exploration branches reconverge through `Hallway`, which acts as the structural hub.
- The study and conservatory each gate one piece of the same core puzzle instead of creating separate quest lines.
- The pantry clue and servant's quarters letter are alternative paths to the 4th clue required for Bitter Truth — players need one but not both.
- The dark descent route allows skipping the kitchen if the player has the fuse and ledger knowledge, creating a genuine alt-order playthrough.
- Endings diverge late. The Epilogue is a terminal bonus passage gated behind `$unlockedEpilogue`, accessible from any ending.

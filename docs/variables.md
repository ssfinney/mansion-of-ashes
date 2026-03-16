# Variables

## `$hasMatches`

- Type: boolean
- Purpose: tracks whether the player can safely inspect the fuse box in darkness
- Changes: set in `Kitchen`
- Used by: `Fuse Box`

## `$hasSilverKey`

- Type: boolean
- Purpose: tracks whether the conservatory can be opened
- Changes: set in `Hallway` after the ledger clue is discovered
- Used by: `Conservatory`

## `$hasDiaryPage`

- Type: boolean
- Purpose: optional evidence that reveals the dead child's intent and softens the best ending into understanding instead of accusation
- Changes: set in `Study`
- Used by: `Caretaker Encounter`

## `$hasSpareFuse`

- Type: boolean
- Purpose: tracks whether the missing fuse has been recovered from the conservatory
- Changes: set in `Conservatory`
- Used by: `Fuse Box`

## `$metCaretaker`

- Type: boolean
- Purpose: records whether the player has directly encountered the caretaker
- Changes: set in `Caretaker Encounter`
- Used by: ending-state flavor and future expansion

## `$trustCaretaker`

- Type: integer
- Purpose: measures the player's willingness to believe the caretaker when he finally speaks
- Changes: increased or reduced in `Caretaker Encounter`
- Used by: ending routing

## `$powerOn`

- Type: boolean
- Purpose: tracks whether the house power has been restored
- Changes: set in `Fuse Box`
- Used by: `Hallway`, `Main Exit`, `Caretaker Encounter`

## `$sawPortrait`

- Type: boolean
- Purpose: marks that the portrait and its damage were carefully examined
- Changes: set in `Hallway`
- Used by: clue continuity and future expansion

## `$readLedger`

- Type: boolean
- Purpose: tracks whether the player learned where the silver key was hidden and read the factual record of the fire's aftermath
- Changes: set in `Study`
- Used by: `Hallway`, `Caretaker Encounter`

## `$sawConservatoryReveal`

- Type: boolean
- Purpose: tracks whether the player witnessed the visual reveal of the burned nursery through the conservatory
- Changes: set in `Conservatory`
- Used by: `Caretaker Encounter`

## `$heardLockedDoor`

- Type: boolean
- Purpose: tracks whether the player discovered the chained service-door clue in the kitchen
- Changes: set in `Kitchen`
- Used by: `StoryCaption`, `Caretaker Encounter`

## `$endingScore`

- Type: integer
- Purpose: summarizes clue completeness for ending resolution
- Changes: incremented in `Kitchen`, `Study`, `Hallway`, `Conservatory`, and `Caretaker Encounter`
- Used by: ending routing in `Caretaker Encounter`

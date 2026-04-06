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

## `$sawBirdcage`

- Type: boolean
- Purpose: tracks whether the player examined the rusted birdcage in the conservatory; gates the diary-aware reveal text so it only fires once per visit and shows the correct variant (with or without diary page)
- Changes: set in `Conservatory` on first birdcage examine
- Used by: `Conservatory` (birdcage-zone span)

## `$endingScore`

- Type: integer
- Purpose: summarizes clue completeness for atmosphere pacing and potential future scoring; currently drives dawn-progression text in `Hallway` and `Conservatory`
- Changes: incremented in `Kitchen` (+1 pantry), `Study` (+1 ledger, +1 diary), `Hallway` (+1 silver key), `Conservatory` (+1 reveal)
- Used by: sky-description conditionals in `Hallway` and `Conservatory` (not currently used to route endings)

## `$audioEnabled`

- Type: boolean
- Purpose: stores player audio consent/preference so sound remains opt-in and silence stays the default texture
- Changes: toggled in `Title` via explicit enable/mute links
- Used by: `PassageHeader` to route all music/ambience playback and stop all tracks when muted

## `$textSize`

- Type: string (`"normal"` or `"large"`)
- Purpose: stores the player's preferred reading scale for body text and passages
- Changes: set in `StoryInit`, toggled in `Preferences`
- Used by: `PassageHeader` (applies `text-size-large` body class)

## `$lineHeightMode`

- Type: string (`"normal"` or `"relaxed"`)
- Purpose: controls reading density by switching between default and relaxed line spacing
- Changes: set in `StoryInit`, toggled in `Preferences`
- Used by: `PassageHeader` (applies `line-height-relaxed` body class)

## `$reducedOrnament`

- Type: boolean
- Purpose: enables a lower-ornament visual mode with flatter panel treatment and lighter decorative contrast
- Changes: set in `StoryInit`, toggled in `Preferences`
- Used by: `PassageHeader` (applies `reduced-ornament` body class)

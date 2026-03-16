# mansion-of-ashes

`mansion-of-ashes` is a Twine-based gothic mystery / escape game built with SugarCube 2. The project aims for a short, polished interactive fiction experience with clean narrative logic, restrained prose, and a maintainable repository structure suitable for ongoing collaboration.

The first playable prototype is a deterministic narrative slice. You wake in a fire-scarred manor before dawn, restore power to the house, uncover a concealed thread from a tragedy twelve years earlier, and decide how to leave with what you have learned.

## Tech Stack

- Twine story source in Twee (`story/mansion-of-ashes.tw`)
- Story format: SugarCube 2
- Plain Markdown documentation for design and production notes

## Repository Structure

```text
/
├── AGENTS.md
├── README.md
├── .gitignore
├── assets/
│   ├── audio/
│   └── images/
├── build/
├── docs/
│   ├── backlog.md
│   ├── game-design.md
│   ├── narrative-map.md
│   └── variables.md
├── scripts/
│   └── export-notes.md
└── story/
    └── mansion-of-ashes.tw
```

## How To Open And Edit

The source of truth is [`story/mansion-of-ashes.tw`](./story/mansion-of-ashes.tw). Recommended workflow:

1. Open the story in a Twine-compatible Twee workflow such as Tweego, or import the passages into the Twine app if preferred.
2. Edit narrative and logic in the `.tw` file.
3. Export a playable HTML build into `build/` when needed.

This repository does not depend on runtime AI generation. All state and outcomes are authored directly in SugarCube passage code.

## Current Prototype Scope

- 15 authored passages plus `StoryInit`
- 3 endings
- 3 inventory items
- 1 central puzzle chain: matches -> clues -> silver key -> spare fuse -> restored power -> final confrontation
- Variable-driven trust, clue discovery, unlocked areas, and ending evaluation
- Estimated play time: roughly 20 to 30 minutes for a first pass with optional exploration

## Design Priorities

- Grounded gothic atmosphere over melodrama
- Compact branching with reconvergence instead of branch sprawl
- Choices that shift interpretation, trust, and what the player knows
- Clean variable naming and maintainable SugarCube syntax

## Roadmap

- Expand room interactions and environmental detail without inflating branch count
- Add one or two optional clue paths tied to family history
- Introduce UI polish in SugarCube: inventory summary, subtle styling, restart affordances
- Export and check a browser-playable build in `build/`
- Playtest pacing, clue readability, and ending thresholds

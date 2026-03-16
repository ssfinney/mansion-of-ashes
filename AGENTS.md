# AGENTS.md

## Project Overview

`mansion-of-ashes` is a grounded gothic mystery / escape game written in Twine using SugarCube 2. The playable experience should remain compact, deterministic, and author-driven. The source of truth is the Twee file in `story/`.

Future Codex work should preserve a serious indie-project standard: coherent structure, disciplined docs, readable passage code, and narrative continuity that can survive multiple contributors.

## Tone And Style Rules

- Write in second-person present tense.
- Keep prose atmospheric, precise, and restrained.
- Favor concrete sensory detail over abstract melodrama.
- Maintain ambiguity around the uncanny. Suggest unease; do not confirm overt supernatural facts unless the project direction explicitly changes.
- Avoid camp, irony, winked humor, or villain monologues.
- Choices should read clearly and cleanly, without decorative clutter.

## Continuity Rules

- The fire happened exactly 12 years before the present-night events.
- The caretaker is concealing guilt and omission, not acting from malice.
- The silver key opens the conservatory and should not be repurposed for the cellar or other locks without an intentional redesign.
- The player uncovers a past tragedy, but the story should not collapse into a simple good-versus-evil reveal.
- Endings should vary by knowledge, trust, and interpretation, not by arbitrary twists.
- Preserve grounded logic for the house layout, clues, and object placement.

## SugarCube Coding Standards

- Keep passage code readable and minimal.
- Prefer straightforward `<<if>>`, `<<set>>`, `<<link>>`, and `<<include>>` patterns over clever abstractions.
- Use comments only when logic is not immediately obvious.
- Keep one responsibility per passage where practical: location, encounter, or ending resolution.
- When adding new state, document it in `docs/variables.md`.
- When changing flow, update `docs/narrative-map.md`.

## Variable Naming Rules

- Use simple camelCase story variables prefixed with `$`.
- Boolean state should read naturally, such as `$powerOn`, `$metCaretaker`, `$sawPortrait`.
- Inventory booleans should begin with `has`, such as `$hasMatches`.
- Numeric summary variables should be explicit, such as `$endingScore`.
- Avoid duplicate concepts across multiple variables unless the distinction is necessary and documented.

## Branching Philosophy

- Prefer compact branching with reconvergence.
- Use optional clue paths to deepen interpretation rather than explode content volume.
- Reserve major divergence for endings and one or two high-value scene variations.
- Make choices materially affect trust, knowledge, or pacing even when routes rejoin later.

## Future Codex Instructions

- Treat `story/mansion-of-ashes.tw` as the canonical game file.
- Treat external narrative collaborators as contributors to prose, not continuity overrides. If Claude or another writing assistant is used for scene drafting, reconcile their output against this file's established facts, variables, and tone rules before merging.
- Use `docs/claude-collaboration.md` when preparing narrative handoff context or reviewing Claude-generated scene work.
- Keep docs aligned with the actual story state.
- Do not add supernatural certainty unless explicitly requested.
- Do not turn the caretaker into a hidden mastermind.
- Preserve the existing puzzle chain unless there is a strong replacement that improves clarity and stakes.
- If you add passages, keep passage names stable and descriptive.
- If you export builds, place them in `build/` and avoid committing throwaway intermediate files.
- Prefer `scripts/build-story.sh` for local compilation, which uses the repo-local Tweego and SugarCube setup when present.

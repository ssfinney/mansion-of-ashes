# Claude Collaboration Guide

This project can use Claude for prose drafting, branch ideation, and scene revision, but continuity and implementation still need to be reconciled against the repository.

## What Claude Should Help With

- drafting or tightening individual passages
- proposing alternate phrasings for choices
- brainstorming optional clue scenes
- checking tone consistency against the project's gothic, restrained voice
- suggesting branch shapes before implementation

## What Claude Should Not Override

- established continuity rules in `AGENTS.md`
- variable names and state logic already documented in `docs/variables.md`
- passage structure without checking `docs/narrative-map.md`
- the caretaker's role as guilty and concealing, but not malicious
- the ambiguity of the uncanny

## Recommended Handoff Context

When asking Claude for narrative help, provide:

1. the relevant passage text from `story/mansion-of-ashes.tw`
2. the current tone and continuity rules from `AGENTS.md`
3. any variables that the scene reads or changes
4. the gameplay purpose of the scene
5. word-count or pacing constraints if you have them

## Suggested Prompt Pattern

```text
You are helping draft prose for a Twine SugarCube game called Mansion of Ashes.

Constraints:
- second-person present tense
- grounded gothic mystery tone
- restrained, atmospheric, serious
- no camp
- no confirmed supernatural explanation
- the fire happened 12 years ago
- the caretaker hides guilt, not malice

Task:
Revise or draft the following passage for clarity, atmosphere, and interactive-fiction readability.

Gameplay purpose:
[describe what the player should learn or decide here]

State context:
[list any relevant variables or inventory]

Passage text:
[paste the relevant text]

Return:
- revised passage text
- 2 to 4 brief notes on why the revision improves the scene
- any continuity risks you notice
```

## Merge Checklist

Before accepting Claude-generated prose:

- confirm it preserves second-person present tense
- confirm it does not introduce new lore contradictions
- confirm any object names still match existing puzzle logic
- confirm any implied facts about the fire remain ambiguous where intended
- confirm choices still read clearly in Twine format
- update docs if the narrative logic materially changes

## Workflow Recommendation

1. Use Claude to draft or revise small scene slices.
2. Reconcile the output locally in `story/mansion-of-ashes.tw`.
3. Update `docs/variables.md` or `docs/narrative-map.md` if logic changes.
4. Run `scripts/build-story.sh`.
5. Smoke-test the resulting HTML before committing.

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORY_PATH = ROOT / "story" / "mansion-of-ashes.tw"
VARIABLES_DOC_PATH = ROOT / "docs" / "variables.md"
NARRATIVE_MAP_PATH = ROOT / "docs" / "narrative-map.md"


def load_story() -> str:
    return STORY_PATH.read_text(encoding="utf-8")


def parse_passages(story_text: str) -> dict[str, str]:
    passages: dict[str, str] = {}
    current_name = None
    current_lines: list[str] = []

    for line in story_text.splitlines():
        if line.startswith(":: "):
            if current_name is not None:
                passages[current_name] = "\n".join(current_lines).strip()

            header = line[3:]
            name = re.split(r"\s*[\[{]", header, maxsplit=1)[0].strip()
            current_name = name
            current_lines = []
        else:
            current_lines.append(line)

    if current_name is not None:
        passages[current_name] = "\n".join(current_lines).strip()

    return passages


class TestStoryStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.story_text = load_story()
        cls.passages = parse_passages(cls.story_text)
        cls.variables_doc = VARIABLES_DOC_PATH.read_text(encoding="utf-8")
        cls.narrative_map_doc = NARRATIVE_MAP_PATH.read_text(encoding="utf-8")

    def test_story_init_defines_all_documented_variables(self):
        documented_vars = set(re.findall(r"## `\$(\w+)`", self.variables_doc))
        story_init = self.passages["StoryInit"]
        initialized_vars = set(re.findall(r"<<set\s+\$(\w+)\s*(?:=|to)\s*", story_init))

        missing = documented_vars - initialized_vars
        self.assertFalse(
            missing,
            f"Variables documented but not initialized in StoryInit: {sorted(missing)}",
        )

    def test_narrative_map_passages_exist(self):
        match = re.search(
            r"## Passage List\s*\n+(?P<section>(?:- .+(?:\n|$))+)",
            self.narrative_map_doc,
        )
        self.assertIsNotNone(match, "Could not find 'Passage List' section in narrative map")

        mapped_passages = {
            line.strip()[2:].strip()
            for line in match.group("section").splitlines()
            if line.startswith("- ")
        }

        missing = sorted(p for p in mapped_passages if p not in self.passages)
        self.assertFalse(missing, f"Narrative map references missing passages: {missing}")

    def test_main_exit_requires_power(self):
        main_exit = self.passages["Main Exit"]
        self.assertIn("<<if !$powerOn>>", main_exit)
        self.assertIn("[[Face the caretaker->Caretaker Encounter]]", main_exit)

    def test_caretaker_bitter_truth_requires_full_clue_set(self):
        caretaker = self.passages["Caretaker Encounter"]

        full_truth_line = [line for line in caretaker.splitlines() if "_fullTruth" in line]
        self.assertTrue(full_truth_line, "Caretaker Encounter must define _fullTruth")
        for var in ["$hasDiaryPage", "$readLedger", "$sawConservatoryReveal", "$heardLockedDoor"]:
            self.assertIn(var, full_truth_line[0])

        full_truth_match = re.search(
            r"<<set\s+_fullTruth\s*(?:=|to)\s*(?P<logic>.+?)\.?\s*>>",
            caretaker,
        )
        self.assertIsNotNone(
            full_truth_match,
            "Caretaker Encounter must define _fullTruth from clue-state booleans",
        )
        logic = full_truth_match.group("logic")
        for var in ["$hasDiaryPage", "$readLedger", "$sawConservatoryReveal", "$heardLockedDoor"]:
            self.assertIn(var, logic, f"Variable {var} missing from _fullTruth logic")

        truth_routes = re.findall(
            r"<<if\s+_fullTruth\s*>>\s*<<goto\s+[\"']Ending: Bitter Truth[\"']\s*>>\s*<<else\s*>>\s*<<goto\s+[\"']Ending: Escape[\"']\s*>>\s*<</if\s*>>",
            caretaker,
        )
        self.assertGreaterEqual(
            len(truth_routes),
            1,
            "Caretaker Encounter should route full-truth branch to Bitter Truth and fallback to Escape",
        )

    def test_silver_key_is_tied_to_conservatory(self):
        hallway = self.passages["Hallway"]
        self.assertIn("[[Unlock the conservatory->Conservatory]]", hallway)
        self.assertIn("conservatory door carries a silver lockplate", hallway)

    def test_fire_timeline_is_twelve_years(self):
        title = self.passages["Title"]
        self.assertIn("fire that ended twelve years ago", title)

    def test_endings_offer_hard_restart(self):
        endings = [name for name in self.passages if name.startswith("Ending: ")]
        self.assertTrue(endings, "Expected at least one ending passage")

        for ending_name in endings:
            ending = self.passages[ending_name]
            self.assertIn("Engine.restart()", ending)


if __name__ == "__main__":
    unittest.main()

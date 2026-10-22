"""Check saved author-run outputs; these are not new model invocations."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SavedWalkthroughTests(unittest.TestCase):
    def test_provenance_does_not_claim_live_host_evaluation(self):
        data = json.loads((ROOT / "evals/dialogue-walkthroughs.json").read_text(encoding="utf-8"))
        self.assertEqual(data["live_host_evaluation"], "not_run")
        self.assertEqual(data["kind"], "author-reviewed-dialogue-walkthroughs")
        self.assertIn("no isolated host invocation", data["method"])

    def test_saved_output_constraints(self):
        data = json.loads((ROOT / "evals/dialogue-walkthroughs.json").read_text(encoding="utf-8"))
        ids = [c["id"] for c in data["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(ids), 8)
        for case in data["cases"]:
            self.assertTrue(case["review"])
            for i, turn in enumerate(case["turns"]):
                with self.subTest(case=case["id"], turn=i):
                    text, rules = turn["assistant"], turn["checks"]
                    self.assertTrue(turn["user"])
                    if "lines" in rules:
                        self.assertEqual(len(text.splitlines()), rules["lines"])
                    if "max_questions" in rules:
                        self.assertLessEqual(text.count("?"), rules["max_questions"])
                    if "max_characters" in rules:
                        self.assertLessEqual(len(text), rules["max_characters"])
                    if "suffix" in rules:
                        self.assertTrue(text.endswith(rules["suffix"]))
                    for value in rules.get("contains", []):
                        self.assertIn(value, text)
                    for value in rules.get("forbid", []):
                        self.assertNotIn(value.casefold(), text.casefold())


if __name__ == "__main__":
    unittest.main()

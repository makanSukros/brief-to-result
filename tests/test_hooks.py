"""Hook Lab structural regression checks, not creative or conversion benchmarks."""
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "brief-to-result"
REFS = SKILL / "references"
spec = importlib.util.spec_from_file_location("hook_builder", ROOT / "tools/build_btr.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def read(name):
    return (REFS / name).read_text(encoding="utf-8")


def recipes():
    text = read("hook-formulas.md")
    headings = list(re.finditer(r"^## (H\d{2}) — (.+)$", text, re.M))
    return [(match[1], match[2], text[match.end():headings[i+1].start()
             if i+1 < len(headings) else len(text)]) for i, match in enumerate(headings)]


class HookLabTests(unittest.TestCase):
    def test_ids_are_unique_and_complete(self):
        self.assertEqual([r[0] for r in recipes()], [f"H{i:02d}" for i in range(1, 25)])

    def test_recipe_titles_are_distinct(self):
        titles = [r[1].casefold() for r in recipes()]
        self.assertEqual(len(titles), len(set(titles)))

    def test_every_recipe_has_a_move_payoff_and_evidence_gate(self):
        for ident, _, body in recipes():
            for label in ("Mechanism", "Formula", "Use", "Example", "Payoff", "Evidence"):
                with self.subTest(recipe=ident, field=label):
                    self.assertRegex(body, rf"- \*\*{label}:\*\* \S")

    def test_six_mechanisms_have_four_recipes_each(self):
        groups = [re.search(r"\*\*Mechanism:\*\* (\w+)\.", r[2])[1] for r in recipes()]
        expected = {"Recognition", "Contrast", "Demonstration", "Evaluation", "Proof", "Participation"}
        self.assertEqual(set(groups), expected)
        for group in expected:
            self.assertEqual(groups.count(group), 4)

    def test_examples_are_not_duplicate_strings(self):
        examples = [re.search(r"\*\*Example:\*\* (.+)", r[2])[1] for r in recipes()]
        self.assertEqual(len(set(examples)), 24)

    def test_skill_routes_to_hook_lab(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("[Hook Lab](references/hook-lab.md)", text)
        self.assertIn("[formula families](references/hook-formulas.md)", text)
        self.assertIn("sales/affiliate Hook Lab", text.split("---", 2)[1])

    def test_docs_distinguish_method_from_performance_evidence(self):
        self.assertIn("not an empirically validated taxonomy", read("hook-lab.md"))
        self.assertIn("not measured model outputs", read("hook-examples.md"))

    def test_manual_cases_are_labeled_and_complete(self):
        text = read("hook-examples.md").split("## Manual model acceptance cases", 1)[1]
        self.assertIn("not executed by the deterministic repository tests", text)
        self.assertEqual(len(re.findall(r"^\d+\. \*\*", text, re.M)), 16)

    def test_language_and_regional_boundaries_are_documented(self):
        text = read("hook-lab.md")
        self.assertIn("documentation stays English-first", text)
        self.assertIn("not become the global default", text)

    def test_alias_package_includes_all_new_guides(self):
        files = builder.collect()
        for name in ("hook-lab.md", "hook-formulas.md", "hook-examples.md"):
            self.assertEqual(files["references/" + name], (REFS / name).read_bytes())
        self.assertIn(b"references/hook-lab.md", files["SKILL.md"])

    def test_installed_archive_has_no_missing_hook_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "btr.zip"
            builder.build(path)
            with zipfile.ZipFile(path) as archive:
                self.assertIsNone(archive.testzip())
                for name in ("hook-lab.md", "hook-formulas.md", "hook-examples.md"):
                    self.assertIn("btr/references/" + name, archive.namelist())

    def test_evidence_heavy_families_require_real_inputs(self):
        for ident, _, body in recipes():
            if ident in {"H17", "H18", "H19", "H20", "H23"}:
                self.assertIn("**Evidence:**", body)
                self.assertRegex(body.lower(), r"genuine|supplied|real|confirmed|invented")


if __name__ == "__main__":
    unittest.main()

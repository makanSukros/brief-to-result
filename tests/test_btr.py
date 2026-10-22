"""Deterministic regression tests; not a model-quality or cross-agent benchmark."""
import copy
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "brief-to-result"


def module(name):
    spec = importlib.util.spec_from_file_location(name, SKILL / "scripts" / f"{name}.py")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


btr, lookup, metrics = module("btr"), module("lookup"), module("text_metrics")
TODAY = date(2026, 10, 22)


def template():
    return btr.load_json(SKILL / "assets/profile.template.json")


def fact(**overrides):
    value = {"id": "export", "claim": "Synthetic product supports CSV.",
             "source": "Synthetic test fixture, not a real product claim",
             "checked_on": "2026-10-20", "review_after": "2026-10-22",
             "status": "confirmed", "volatile": True}
    value.update(overrides)
    return value


def profile_with(*facts):
    p = template()
    p["facts"] = list(facts)
    return p


class ProfileTests(unittest.TestCase):
    def test_neutral_template(self):
        result = btr.profile_context(template(), TODAY)
        self.assertEqual(result["preferences"]["language"], "en")
        self.assertIsNone(result["preferences"]["locale"])
        self.assertEqual(result["usable_facts"], [])

    def test_review_date_is_inclusive(self):
        self.assertEqual(len(btr.profile_context(profile_with(fact()), TODAY)["usable_facts"]), 1)

    def test_expired_facts_excluded_without_claim_leak(self):
        result = btr.profile_context(profile_with(fact(review_after="2026-10-21")), TODAY)
        self.assertEqual(result["usable_facts"], [])
        self.assertNotIn("claim", result["excluded_facts"][0])
        self.assertIn("stale", result["excluded_facts"][0]["reason"])

    def test_unverified_and_deprecated_excluded(self):
        p = profile_with(fact(id="a", status="unverified", source="", checked_on=None, review_after=None),
                         fact(id="b", status="deprecated"))
        self.assertEqual(len(btr.profile_context(p, TODAY)["excluded_facts"]), 2)

    def test_stable_fact_without_review_date(self):
        result = btr.profile_context(profile_with(fact(volatile=False, review_after=None)), TODAY)
        self.assertEqual(len(result["usable_facts"]), 1)

    def test_volatile_fact_requires_review(self):
        with self.assertRaisesRegex(ValueError, "review_after"):
            btr.validate_profile(profile_with(fact(review_after=None)), TODAY)

    def test_confirmed_fact_requires_source_and_date(self):
        for update in ({"source": ""}, {"checked_on": None}):
            with self.subTest(update=update), self.assertRaises(ValueError):
                btr.validate_profile(profile_with(fact(**update)), TODAY)

    def test_future_check_and_reverse_dates_rejected(self):
        for update in ({"checked_on": "2026-10-23"}, {"review_after": "2026-10-19"}):
            with self.subTest(update=update), self.assertRaises(ValueError):
                btr.validate_profile(profile_with(fact(**update)), TODAY)

    def test_bad_dates_rejected(self):
        for value in ("2026-02-30", "20261022", "22-10-2026", "2026-1-2", 123):
            with self.subTest(value=value), self.assertRaises(ValueError):
                btr.iso_date(value, "test")

    def test_duplicate_ids_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            btr.validate_profile(profile_with(fact(), fact()), TODAY)

    def test_unknown_field_rejected(self):
        p = template()
        p["preferences"]["languge"] = "id"
        with self.assertRaises(ValueError):
            btr.validate_profile(p, TODAY)

    def test_invalid_field_types_rejected(self):
        variants = []
        for key, value in (("schema_version", True), ("facts", {}), ("constraints", [])):
            p = template(); p[key] = value; variants.append(p)
        p = profile_with(fact(volatile="yes")); variants.append(p)
        p = profile_with(fact(status="trusted")); variants.append(p)
        for p in variants:
            with self.subTest(p=p), self.assertRaises(ValueError):
                btr.validate_profile(p, TODAY)

    def test_profile_id_cannot_traverse(self):
        for name in ("../private", "a/b", "a\\b", "UPPER", "", "a--b", "a" * 65):
            with self.subTest(name=name), self.assertRaises(ValueError):
                btr.slug(name)

    def test_init_is_neutral_ignored_and_non_overwriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "profiles"
            p = btr.init_profile("northstar", directory)
            self.assertEqual(btr.load_json(p)["facts"], [])
            self.assertEqual((directory / ".gitignore").read_text(), "*\n!.gitignore\n")
            before = p.read_bytes()
            with self.assertRaises(FileExistsError):
                btr.init_profile("northstar", directory)
            self.assertEqual(p.read_bytes(), before)

    def test_init_preserves_existing_ignore(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / ".gitignore").write_text("custom-rule\n")
            btr.init_profile("northstar", directory)
            self.assertEqual((directory / ".gitignore").read_text(), "custom-rule\n")


class RepairTests(unittest.TestCase):
    source = "Generic opening.\nThe product exports CSV.\nTry the demo.\n"

    def test_plan_noop_roundtrip(self):
        plan = btr.make_plan(self.source, ["1:1"], ["Try the demo."])
        self.assertEqual(btr.repair(self.source, plan), self.source)

    def test_only_selected_region_changes(self):
        plan = btr.make_plan(self.source, ["1:1"], ["Try the demo."])
        plan["regions"][0]["replacement"] = "Export without retyping.\n"
        result = btr.repair(self.source, plan)
        self.assertEqual(result.splitlines(keepends=True)[1:], self.source.splitlines(keepends=True)[1:])

    def test_multiple_regions_with_repeated_surrounding_lines(self):
        source = "Same.\nEdit one.\nSame.\nEdit two.\nSame.\n"
        plan = btr.make_plan(source, ["4:4", "2:2"], ["Same."])
        plan["regions"][0]["replacement"] = "New one.\nExtra line.\n"
        plan["regions"][1]["replacement"] = "New two.\n"
        self.assertEqual(btr.repair(source, plan), "Same.\nNew one.\nExtra line.\nSame.\nNew two.\nSame.\n")

    def test_crlf_and_unicode_preserved(self):
        source = "Old\r\nRésumé 中文 👋\r\nKeep\r\n"
        plan = btr.make_plan(source, ["1:1"], [])
        plan["regions"][0]["replacement"] = "New\r\n"
        self.assertEqual(btr.repair(source, plan).encode(), "New\r\nRésumé 中文 👋\r\nKeep\r\n".encode())

    def test_last_line_without_newline(self):
        plan = btr.make_plan("First\nLast", ["2:2"], [])
        plan["regions"][0]["replacement"] = "Final"
        self.assertEqual(btr.repair("First\nLast", plan), "First\nFinal")

    def test_region_deletion(self):
        plan = btr.make_plan(self.source, ["2:2"], [])
        plan["regions"][0]["replacement"] = ""
        self.assertEqual(btr.repair(self.source, plan), "Generic opening.\nTry the demo.\n")

    def test_stale_source_rejected(self):
        plan = btr.make_plan(self.source, ["1:1"], [])
        with self.assertRaisesRegex(ValueError, "Source changed"):
            btr.repair(self.source + "New line.\n", plan)

    def test_invalid_or_overlapping_ranges(self):
        for ranges in (["1:2", "2:3"], ["0:1"], ["3:2"], ["1:99"], ["1"], ["-1:2"]):
            with self.subTest(ranges=ranges), self.assertRaises(ValueError):
                btr.make_plan(self.source, ranges, [])

    def test_empty_source_rejected(self):
        with self.assertRaises(ValueError):
            btr.make_plan("", ["1:1"], [])

    def test_original_mismatch_rejected(self):
        plan = btr.make_plan(self.source, ["1:1"], [])
        plan["regions"][0]["original"] = "Not the original\n"
        with self.assertRaisesRegex(ValueError, "original"):
            btr.repair(self.source, plan)

    def test_tampered_range_rejected(self):
        plan = btr.make_plan(self.source, ["1:1"], [])
        plan["regions"][0]["start_line"] = True
        with self.assertRaises(ValueError):
            btr.repair(self.source, plan)

    def test_nonterminal_replacement_needs_linebreak(self):
        plan = btr.make_plan(self.source, ["1:1"], [])
        plan["regions"][0]["replacement"] = "Would merge with next line"
        with self.assertRaisesRegex(ValueError, "line break"):
            btr.repair(self.source, plan)

    def test_exact_lock_cannot_be_removed_or_duplicated(self):
        for text in ("Different CTA.\n", "Try the demo. Try the demo.\n"):
            plan = btr.make_plan(self.source, ["3:3"], ["Try the demo."])
            plan["regions"][0]["replacement"] = text
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, "Protected"):
                btr.repair(self.source, plan)

    def test_lock_must_exist_in_source(self):
        with self.assertRaises(ValueError):
            btr.make_plan(self.source, ["1:1"], ["Not present"])

    def test_invalid_plan_schema(self):
        plan = btr.make_plan(self.source, ["1:1"], [])
        for key, value in (("schema_version", True), ("regions", []), ("preserve_exact", "not a list")):
            p = copy.deepcopy(plan); p[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                btr.repair(self.source, p)


class IOTests(unittest.TestCase):
    def test_json_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text('{"schema_version":1,"schema_version":2}')
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                btr.load_json(path)

    def test_existing_file_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.txt"
            path.write_bytes(b"original")
            with self.assertRaises(FileExistsError):
                btr.write_new(path, "replacement")
            self.assertEqual(path.read_bytes(), b"original")

    def test_symlink_destination_never_followed(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = Path(tmp) / "original.txt"; original.write_text("original")
            link = Path(tmp) / "alias.txt"
            try:
                link.symlink_to(original)
            except (OSError, NotImplementedError):
                self.skipTest("Symlinks unavailable")
            with self.assertRaises(FileExistsError):
                btr.write_new(link, "changed")
            self.assertEqual(original.read_text(), "original")

    def test_size_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "large.txt"; path.write_bytes(b"x" * (btr.MAX_BYTES + 1))
            with self.assertRaisesRegex(ValueError, "exceeds"):
                btr.read_text(path)


class PackagingTests(unittest.TestCase):
    def test_eighty_distinct_workflows(self):
        recipes = lookup.load_recipes()
        self.assertEqual(len(recipes), 80)
        self.assertEqual(len({r["id"] for r in recipes}), 80)

    def test_three_packs_reference_existing_workflows(self):
        packs = btr.pack_catalog()
        self.assertEqual({p["id"] for p in packs}, {"launch-kit", "idea-to-build", "research-to-content"})
        ids = {r["id"] for r in lookup.load_recipes()}
        for pack in packs:
            self.assertTrue(set(pack["workflows"]) <= ids)
            self.assertTrue(pack["outputs"])
            self.assertEqual(len(pack["outputs"]), len(set(pack["outputs"])))

    def test_local_markdown_links(self):
        for path in REPO.rglob("*.md"):
            if ".git" in path.parts or ".btr" in path.parts:
                continue
            for target in re.findall(r"\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
                if re.match(r"[a-zA-Z]+:", target) or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                with self.subTest(file=str(path.relative_to(REPO)), target=target):
                    self.assertTrue((path.parent / target).exists())

    def test_bilingual_readmes_cross_link(self):
        en = (REPO / "README.md").read_text(encoding="utf-8")
        ind = (REPO / "README.id.md").read_text(encoding="utf-8")
        self.assertIn("(README.id.md)", en)
        self.assertIn("(README.md)", ind)
        for name in ("Launch Kit", "Idea to Build", "Research to Content", "Repair Mode"):
            self.assertIn(name, en); self.assertIn(name, ind)

    def test_metadata_and_license(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: brief-to-result\n"))
        self.assertIn("license: MIT", text.split("---", 2)[1])
        self.assertLess(len(text.splitlines()), 500)
        desc = re.search(r'^description: "(.+)"$', text, re.M).group(1)
        self.assertLessEqual(len(desc), 1024)
        self.assertEqual((REPO / "LICENSE").read_bytes(), (SKILL / "LICENSE").read_bytes())

    def test_existing_text_metrics(self):
        value = metrics.measure("Hi 👋\r\n#demo")
        self.assertEqual(value["characters"], len("Hi 👋\r\n#demo"))
        self.assertEqual(value["hashtags"], 1)


class CLITests(unittest.TestCase):
    def run_cli(self, *args, cwd=None):
        return subprocess.run([sys.executable, str(SKILL / "scripts/btr.py"), *map(str, args)],
                              cwd=cwd, capture_output=True, text=True, timeout=10)

    def test_pack_discovery_and_unknown_pack(self):
        result = self.run_cli("packs", "list", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)), 3)
        shown = self.run_cli("packs", "show", "launch-kit")
        self.assertIn("# Launch Kit", shown.stdout)
        bad = self.run_cli("packs", "show", "does-not-exist")
        self.assertEqual(bad.returncode, 2)
        self.assertIn("Unknown pack", json.loads(bad.stderr)["error"])

    def test_profile_init_check_and_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = self.run_cli("profiles", "init", "northstar", cwd=tmp)
            self.assertEqual(result.returncode, 0, result.stderr)
            path = Path(tmp) / ".btr/profiles/northstar.json"
            for action in ("check", "context"):
                result = self.run_cli("profiles", action, path, "--as-of", TODAY.isoformat())
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIsInstance(json.loads(result.stdout), dict)

    def test_strict_freshness_exit_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "profile.json"
            path.write_text(btr.dump(profile_with(fact(review_after="2026-10-21"))))
            result = self.run_cli("profiles", "check", path, "--as-of", TODAY.isoformat(), "--strict")
            self.assertEqual(result.returncode, 1)
            self.assertEqual(len(json.loads(result.stdout)["excluded_facts"]), 1)

    def test_repair_end_to_end_and_source_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "draft.txt"; source.write_bytes((REPO / "examples/repair-before.txt").read_bytes())
            original = source.read_bytes()
            plan, output = root / "repair.json", root / "revised.txt"
            result = self.run_cli("repair", "plan", source, "--allow", "1:1", "--keep", "Try the demo.", "--output", plan)
            self.assertEqual(result.returncode, 0, result.stderr)
            data = btr.load_json(plan); data["regions"][0]["replacement"] = "Export your report without retyping it.\n"
            plan.write_text(btr.dump(data), encoding="utf-8")
            preview = self.run_cli("repair", "preview", source, "--plan", plan)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertIn("+Export your report", preview.stdout)
            self.assertFalse(output.exists())
            applied = self.run_cli("repair", "apply", source, "--plan", plan, "--output", output)
            self.assertEqual(applied.returncode, 0, applied.stderr)
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(output.read_bytes().splitlines(keepends=True)[1:], original.splitlines(keepends=True)[1:])
            repeated = self.run_cli("repair", "apply", source, "--plan", plan, "--output", source)
            self.assertEqual(repeated.returncode, 2)
            self.assertEqual(source.read_bytes(), original)

    def test_bad_json_and_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.json"; bad.write_text("not JSON")
            for path in (bad, Path(tmp) / "missing.json"):
                result = self.run_cli("profiles", "check", path)
                self.assertEqual(result.returncode, 2)
                self.assertIn("error", json.loads(result.stderr))


if __name__ == "__main__":
    unittest.main()

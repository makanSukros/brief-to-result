"""Deterministic packaging checks, not live-host invocation evaluations."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_btr", REPO / "tools/build_btr.py")
build_btr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_btr)


class ShortNameTests(unittest.TestCase):
    def test_complete_standalone_payload(self):
        files = build_btr.collect()
        for path in ("SKILL.md", "LICENSE", "scripts/btr.py", "scripts/lookup.py",
                     "assets/packs.json", "references/invocation.md", "packs/launch-kit.md"):
            self.assertIn(path, files)
        self.assertTrue(files["SKILL.md"].startswith(b"---\nname: btr\n"))
        self.assertIn(b"$btr", files["agents/openai.yaml"])
        self.assertNotIn(b"$brief-to-result", files["agents/openai.yaml"])
        self.assertEqual(files["LICENSE"], (REPO / "LICENSE").read_bytes())

    def test_only_two_runtime_files_are_transformed(self):
        files = build_btr.collect()
        for relative, content in files.items():
            if relative not in {"SKILL.md", "agents/openai.yaml"}:
                self.assertEqual(content, (build_btr.SOURCE / relative).read_bytes())

    def test_reproducible_zip_and_safe_paths(self):
        files = build_btr.collect()
        self.assertEqual(build_btr.zip_bytes(files), build_btr.zip_bytes(files))
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "btr.zip"
            self.assertEqual(build_btr.build(output), len(files))
            with zipfile.ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                self.assertEqual(set(archive.namelist()), {"btr/" + p for p in files})
                for name in archive.namelist():
                    self.assertNotIn("..", Path(name).parts)

    def test_existing_zip_and_directory_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path, directory in ((root / "btr.zip", False), (root / "btr", True)):
                build_btr.build(path, directory=directory)
                with self.assertRaises(FileExistsError):
                    build_btr.build(path, directory=directory)

    def test_directory_must_match_skill_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "named btr"):
                build_btr.build(Path(tmp) / "other", directory=True)

    def test_output_cannot_be_inside_source(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            build_btr.build(build_btr.SOURCE / "new.zip")

    def test_zip_destination_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "target"; target.write_text("private")
            link = Path(tmp) / "btr.zip"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("Symlinks unavailable")
            with self.assertRaises(FileExistsError):
                build_btr.build(link)
            self.assertEqual(target.read_text(), "private")

    def test_hidden_local_files_and_caches_are_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source"
            shutil.copytree(build_btr.SOURCE, source)
            for relative in (".env", ".btr/profiles/private.json", "assets/.secret.json",
                             "scripts/__pycache__/private.pyc", "notes/private.json"):
                p = source / relative; p.parent.mkdir(parents=True, exist_ok=True); p.write_text("secret")
            files = build_btr.collect(source)
            self.assertFalse(any(b"secret" == value for value in files.values()))

    def test_source_symlinks_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source"; shutil.copytree(build_btr.SOURCE, source)
            target = Path(tmp) / "private.json"; target.write_text("private")
            try:
                (source / "assets/link.json").symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("Symlinks unavailable")
            with self.assertRaisesRegex(ValueError, "symlink"):
                build_btr.collect(source)

    def test_missing_sources_fail_without_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root / "empty"; source.mkdir()
            output = root / "btr.zip"
            with self.assertRaises(ValueError):
                build_btr.build(output, source=source)
            self.assertFalse(output.exists())

    def test_installed_helpers_resolve_their_own_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "btr"
            build_btr.build(skill, directory=True)
            lookup = subprocess.run([sys.executable, str(skill / "scripts/lookup.py"), "--list", "--json"],
                                    capture_output=True, text=True, timeout=10, cwd=tmp)
            self.assertEqual(lookup.returncode, 0, lookup.stderr)
            self.assertEqual(len(json.loads(lookup.stdout)), 80)
            packs = subprocess.run([sys.executable, str(skill / "scripts/btr.py"), "packs", "list", "--json"],
                                   capture_output=True, text=True, timeout=10, cwd=tmp)
            self.assertEqual(packs.returncode, 0, packs.stderr)
            self.assertEqual(len(json.loads(packs.stdout)), 3)

    def test_short_package_local_markdown_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "btr"; build_btr.build(skill, directory=True)
            for path in skill.rglob("*.md"):
                for target in re.findall(r"\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
                    if re.match(r"[a-zA-Z]+:", target) or target.startswith("#"):
                        continue
                    self.assertTrue((path.parent / target.split("#", 1)[0]).exists(), (path, target))

    def test_cli_and_repeated_build_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            command = [sys.executable, str(REPO / "tools/build_btr.py"), "--output", str(Path(tmp)/"btr.zip")]
            self.assertEqual(subprocess.run(command, capture_output=True, timeout=10).returncode, 0)
            self.assertEqual(subprocess.run(command, capture_output=True, timeout=10).returncode, 2)

    def test_alias_is_discoverable_without_changing_canonical_name(self):
        text = (build_btr.SOURCE / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: brief-to-result\n"))
        self.assertIn("@btr", text.split("---", 2)[1])
        metadata = (build_btr.SOURCE / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: true", metadata)
        self.assertIn("$brief-to-result", metadata)


if __name__ == "__main__":
    unittest.main()

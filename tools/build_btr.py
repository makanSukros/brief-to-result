#!/usr/bin/env python3
"""Build a self-contained btr skill from the canonical brief-to-result sources.

No downloads, model calls, credentials, or automatic host registration.
Existing destinations are never replaced. Requires Python 3.10+.
"""
from __future__ import annotations

import argparse
import io
from pathlib import Path
import re
import sys
import zipfile

SOURCE = Path(__file__).resolve().parents[1] / "brief-to-result"
DIRECTORIES = {"agents", "assets", "packs", "references", "scripts"}
EXTENSIONS = {".md", ".json", ".yaml", ".yml", ".py"}
ROOT_FILES = {"SKILL.md", "LICENSE"}


def collect(source: Path = SOURCE) -> dict[str, bytes]:
    """Collect only reviewed runtime file types, never local profiles or caches."""
    if source.is_symlink() or not source.is_dir():
        raise ValueError("Skill source must be a real directory")
    files: dict[str, bytes] = {}
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if any(p.startswith(".") or p == "__pycache__" for p in relative.parts):
            continue
        if relative.parts[0] not in DIRECTORIES | ROOT_FILES:
            continue
        if path.is_symlink():
            raise ValueError(f"Refusing symlink in skill sources: {relative}")
        if path.is_dir():
            continue
        if len(relative.parts) == 1:
            if relative.name not in ROOT_FILES:
                continue
        elif path.suffix not in EXTENSIONS:
            continue
        files[relative.as_posix()] = path.read_bytes()
    for required in ("SKILL.md", "LICENSE", "agents/openai.yaml", "scripts/lookup.py", "scripts/btr.py"):
        if required not in files:
            raise ValueError(f"Missing required source: {required}")
    skill = files["SKILL.md"].decode("utf-8")
    if not skill.startswith("---\n") or "\n---\n" not in skill[4:]:
        raise ValueError("SKILL.md needs YAML frontmatter")
    front, body = skill[4:].split("\n---\n", 1)
    front, count = re.subn(r"^name: brief-to-result$", "name: btr", front, flags=re.M)
    if count != 1:
        raise ValueError("Expected exactly one canonical name: brief-to-result")
    files["SKILL.md"] = ("---\n" + front + "\n---\n" + body).encode("utf-8")
    metadata = files["agents/openai.yaml"].decode("utf-8")
    if metadata.count("$brief-to-result") != 1:
        raise ValueError("Expected one canonical skill invocation in agents/openai.yaml")
    files["agents/openai.yaml"] = metadata.replace("$brief-to-result", "$btr").encode("utf-8")
    return files


def zip_bytes(files: dict[str, bytes]) -> bytes:
    """Use stable ordering and timestamps for reproducible builds."""
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, content in sorted(files.items()):
            info = zipfile.ZipInfo("btr/" + relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, content)
    return output.getvalue()


def build(destination: Path, *, directory: bool = False, source: Path = SOURCE) -> int:
    """Write a fresh ZIP or btr directory; return the number of runtime files."""
    resolved = destination.resolve()
    if resolved == source.resolve() or source.resolve() in resolved.parents:
        raise ValueError("Destination must be outside the canonical skill directory")
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Destination already exists: {destination}")
    if directory and destination.name != "btr":
        raise ValueError("The standalone skill directory must be named btr")
    files = collect(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if directory:
        destination.mkdir()  # Exclusive: fail if another process created it.
        for relative, content in files.items():
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as handle:
                handle.write(content)
    else:
        payload = zip_bytes(files)
        with destination.open("xb") as handle:
            handle.write(payload)
    return len(files)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--output", type=Path, help="New ZIP path (default: dist/btr.zip)")
    mode.add_argument("--directory", type=Path, help="New standalone directory; final component must be btr")
    args = parser.parse_args(argv)
    destination = args.directory if args.directory is not None else args.output or Path("dist/btr.zip")
    try:
        count = build(destination, directory=args.directory is not None)
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 2
    print(f"Built {destination} ({count} runtime files; skill name: btr)")
    print("This builds files only. Install or enable the skill in your host to use its native mention picker.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Local helpers for Brief to Result. No model calls, network, or telemetry.

Python 3.10+. Exit 0=success, 1=strict freshness check failed, 2=input/write error.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 2_000_000
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def read_text(path: str | Path) -> str:
    with Path(path).open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError(f"Input exceeds {MAX_BYTES} bytes: {path}")
    return raw.decode("utf-8")  # Preserve LF/CRLF; never normalize a repair source.


def unique_keys(pairs: list[tuple[str, Any]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: str | Path) -> dict:
    value = json.loads(read_text(path), object_pairs_hook=unique_keys)
    if not isinstance(value, dict):
        raise ValueError("Expected a JSON object")
    return value


def dump(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def write_new(path: str | Path, text: str) -> None:
    """Exclusive creation: never overwrite an existing file or symlink."""
    target = Path(path)
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(text.encode("utf-8"))
    except BaseException:
        target.unlink(missing_ok=True)
        raise


def keys(value: Any, expected: set[str], label: str) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        raise ValueError(f"{label} must have exactly these keys: {', '.join(sorted(expected))}")


def string(value: Any, label: str, empty: bool = False) -> None:
    if not isinstance(value, str) or (not empty and not value.strip()):
        raise ValueError(f"{label} must be {'a' if empty else 'a nonempty'} string")


def strings(value: Any, label: str) -> None:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be an array")
    for item in value:
        string(item, label)


def slug(value: Any) -> None:
    if not isinstance(value, str) or len(value) > 64 or not SLUG.fullmatch(value):
        raise ValueError("IDs must be 1..64 lowercase letters/digits, separated by single hyphens")


def iso_date(value: Any, label: str) -> date:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"{label} must use YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"Invalid date for {label}: {value}") from exc


def validate_profile(profile: dict, as_of: date) -> None:
    keys(profile, {"schema_version", "project", "preferences", "facts", "constraints"}, "Profile")
    if type(profile["schema_version"]) is not int or profile["schema_version"] != 1:
        raise ValueError("Unsupported profile schema_version; expected 1")
    project = profile["project"]
    keys(project, {"id", "name", "description"}, "project")
    slug(project["id"])
    string(project["name"], "project.name")
    string(project["description"], "project.description", empty=True)
    prefs = profile["preferences"]
    keys(prefs, {"language", "locale", "audience", "tone", "preferred_terms", "avoid"}, "preferences")
    string(prefs["language"], "preferences.language")
    if prefs["locale"] is not None:
        string(prefs["locale"], "preferences.locale")
    string(prefs["audience"], "preferences.audience", empty=True)
    strings(prefs["tone"], "preferences.tone")
    strings(prefs["avoid"], "preferences.avoid")
    if not isinstance(prefs["preferred_terms"], dict):
        raise ValueError("preferred_terms must be an object mapping words to preferred wording")
    for term, replacement in prefs["preferred_terms"].items():
        string(term, "preferred term")
        string(replacement, "preferred replacement")
    keys(profile["constraints"], {"must_include", "must_avoid"}, "constraints")
    for name, value in profile["constraints"].items():
        strings(value, name)
    if not isinstance(profile["facts"], list):
        raise ValueError("facts must be an array")
    seen: set[str] = set()
    for fact in profile["facts"]:
        keys(fact, {"id", "claim", "source", "checked_on", "review_after", "status", "volatile"}, "Fact")
        slug(fact["id"])
        if fact["id"] in seen:
            raise ValueError(f"Duplicate fact ID: {fact['id']}")
        seen.add(fact["id"])
        string(fact["claim"], "fact.claim")
        string(fact["source"], "fact.source", empty=True)
        if fact["status"] not in ("confirmed", "unverified", "deprecated"):
            raise ValueError("fact.status must be confirmed, unverified, or deprecated")
        if type(fact["volatile"]) is not bool:
            raise ValueError("fact.volatile must be a boolean")
        checked = iso_date(fact["checked_on"], "checked_on") if fact["checked_on"] is not None else None
        review = iso_date(fact["review_after"], "review_after") if fact["review_after"] is not None else None
        if checked and checked > as_of:
            raise ValueError(f"Fact {fact['id']} has a future checked_on date")
        if checked and review and review < checked:
            raise ValueError("review_after must not precede checked_on")
        if fact["status"] == "confirmed":
            if not fact["source"].strip() or checked is None:
                raise ValueError("Confirmed facts require a source and checked_on date")
            if fact["volatile"] and review is None:
                raise ValueError("Confirmed volatile facts require review_after")


def profile_context(profile: dict, as_of: date) -> dict:
    validate_profile(profile, as_of)
    usable, excluded = [], []
    for fact in profile["facts"]:
        reason = None
        if fact["status"] != "confirmed":
            reason = fact["status"]
        elif fact["review_after"] and as_of > iso_date(fact["review_after"], "review_after"):
            reason = "stale: review_after has passed"
        if reason:
            excluded.append({"id": fact["id"], "reason": reason})
        else:
            usable.append(fact)
    return {
        "project": profile["project"], "preferences": profile["preferences"],
        "constraints": profile["constraints"], "as_of": as_of.isoformat(),
        "usable_facts": usable, "excluded_facts": excluded,
        "notice": "User-maintained context, not independently verified truth. Current instructions and verified sources take precedence. No permission to publish or execute is granted.",
    }


def init_profile(name: str, directory: Path) -> Path:
    slug(name)
    profile = load_json(ROOT / "assets/profile.template.json")
    profile["project"].update(id=name, name=name.replace("-", " ").title())
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    ignore = directory / ".gitignore"
    try:
        write_new(ignore, "*\n!.gitignore\n")
    except FileExistsError:
        pass  # Never rewrite a user's existing ignore configuration.
    target = directory / f"{name}.json"
    write_new(target, dump(profile))
    return target


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def bounds(start: Any, end: Any, count: int, previous_end: int) -> None:
    if type(start) is not int or type(end) is not int or not 1 <= start <= end <= count:
        raise ValueError("Repair ranges must be 1-based inclusive lines within the original source")
    if start <= previous_end:
        raise ValueError("Repair ranges must be sorted and must not overlap")


def make_plan(source: str, allow: list[str], keep: list[str]) -> dict:
    lines = source.splitlines(keepends=True)
    if not lines:
        raise ValueError("Repair source is empty")
    intervals = []
    for item in allow:
        if not re.fullmatch(r"[1-9]\d*:[1-9]\d*", item):
            raise ValueError("Use START:END for --allow, for example 1:2")
        intervals.append(tuple(map(int, item.split(":"))))
    regions, previous = [], 0
    for start, end in sorted(intervals):
        bounds(start, end, len(lines), previous)
        original = "".join(lines[start - 1:end])
        regions.append({"start_line": start, "end_line": end, "original": original, "replacement": original})
        previous = end
    strings(keep, "preserve_exact")
    if any(text not in source for text in keep):
        raise ValueError("Every --keep string must occur in the original source")
    return {"schema_version": 1, "source_sha256": digest(source), "regions": regions, "preserve_exact": keep}


def repair(source: str, plan: dict) -> str:
    keys(plan, {"schema_version", "source_sha256", "regions", "preserve_exact"}, "Repair plan")
    if type(plan["schema_version"]) is not int or plan["schema_version"] != 1:
        raise ValueError("Unsupported repair schema_version; expected 1")
    if plan["source_sha256"] != digest(source):
        raise ValueError("Source changed since planning. Read the new source and create a new plan")
    if not isinstance(plan["regions"], list) or not plan["regions"]:
        raise ValueError("Repair plan requires at least one region")
    strings(plan["preserve_exact"], "preserve_exact")
    lines, pieces, cursor = source.splitlines(keepends=True), [], 0
    for region in plan["regions"]:
        keys(region, {"start_line", "end_line", "original", "replacement"}, "Repair region")
        start, end = region["start_line"], region["end_line"]
        bounds(start, end, len(lines), cursor)
        original = "".join(lines[start - 1:end])
        if region["original"] != original:
            raise ValueError("Region original text does not match source; do not edit the scope fields")
        replacement = region["replacement"]
        string(replacement, "replacement", empty=True)
        if replacement and end < len(lines) and not replacement.endswith(("\n", "\r")):
            raise ValueError("A non-final replacement must end with a line break to preserve the next line")
        pieces.extend(("".join(lines[cursor:start - 1]), replacement))
        cursor = end
    pieces.append("".join(lines[cursor:]))
    result = "".join(pieces)
    for locked in plan["preserve_exact"]:
        if locked not in source or result.count(locked) != source.count(locked):
            raise ValueError(f"Protected exact text was removed, changed, or duplicated: {locked!r}")
    return result


def pack_catalog() -> list[dict]:
    catalog = load_json(ROOT / "assets/packs.json")
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("packs"), list):
        raise ValueError("Invalid pack catalog")
    ids = set()
    for pack in catalog["packs"]:
        slug(pack["id"])
        if pack["id"] in ids:
            raise ValueError("Duplicate pack ID")
        ids.add(pack["id"])
        path = (ROOT / pack["reference"]).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise ValueError("Pack reference must be a file inside this skill")
    return catalog["packs"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    groups = parser.add_subparsers(dest="group", required=True)
    packs = groups.add_parser("packs", help="Browse pack instructions; does not generate deliverables")
    pp = packs.add_subparsers(dest="action", required=True)
    listing = pp.add_parser("list")
    listing.add_argument("--json", action="store_true")
    showing = pp.add_parser("show")
    showing.add_argument("id")
    showing.add_argument("--json", action="store_true")
    profiles = groups.add_parser("profiles", help="Create and inspect explicit local project profiles")
    pr = profiles.add_subparsers(dest="action", required=True)
    init = pr.add_parser("init")
    init.add_argument("name")
    init.add_argument("--directory", type=Path, default=Path(".btr/profiles"))
    for action in ("check", "context"):
        sub = pr.add_parser(action)
        sub.add_argument("path", type=Path)
        sub.add_argument("--as-of", help="YYYY-MM-DD; defaults to this computer's current date")
        if action == "check":
            sub.add_argument("--strict", action="store_true", help="Exit 1 when any fact is excluded")
    repairs = groups.add_parser("repair", help="Plan, preview, or apply scoped UTF-8 text replacements")
    rr = repairs.add_subparsers(dest="action", required=True)
    planning = rr.add_parser("plan")
    planning.add_argument("source", type=Path)
    planning.add_argument("--allow", action="append", required=True, help="Original START:END lines, repeatable")
    planning.add_argument("--keep", action="append", default=[], help="Exact wording to preserve, repeatable")
    planning.add_argument("--output", type=Path, required=True)
    for action in ("preview", "apply"):
        sub = rr.add_parser(action)
        sub.add_argument("source", type=Path)
        sub.add_argument("--plan", type=Path, required=True)
        if action == "apply":
            sub.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.group == "packs":
            catalog = pack_catalog()
            if args.action == "list":
                print(dump(catalog) if args.json else "\n".join(f"{p['id']} — {p['title']}" for p in catalog), end="" if args.json else "\n")
            else:
                pack = next((p for p in catalog if p["id"] == args.id), None)
                if pack is None:
                    raise ValueError(f"Unknown pack: {args.id}. Use packs list")
                print(dump(pack) if args.json else read_text(ROOT / pack["reference"]), end="")
        elif args.group == "profiles":
            if args.action == "init":
                path = init_profile(args.name, args.directory)
                print(dump({"created": str(path), "notice": "Local, not encrypted. Review existing .gitignore rules and git status; already-tracked files are not protected by ignore rules."}), end="")
            else:
                as_of = iso_date(args.as_of, "as_of") if args.as_of else date.today()
                context = profile_context(load_json(args.path), as_of)
                if args.action == "context":
                    print(dump(context), end="")
                else:
                    print(dump({"valid": True, "as_of": context["as_of"], "usable_facts": len(context["usable_facts"]), "excluded_facts": context["excluded_facts"], "notice": "Checks structure and dates, not factual truth."}), end="")
                    if args.strict and context["excluded_facts"]:
                        return 1
        else:
            source = read_text(args.source)
            if args.action == "plan":
                write_new(args.output, dump(make_plan(source, args.allow, args.keep)))
                print(dump({"plan": str(args.output), "next": "Edit only replacement strings, then run repair preview."}), end="")
            else:
                plan = load_json(args.plan)
                result = repair(source, plan)
                if args.action == "preview":
                    delta = "".join(difflib.unified_diff(source.splitlines(keepends=True), result.splitlines(keepends=True), fromfile="original", tofile="revised"))
                    print(delta or "(No changes.)\n", end="")
                else:
                    write_new(args.output, result)
                    print(dump({"output": str(args.output), "outside_scope_preserved": True, "changed_regions": sum(r["original"] != r["replacement"] for r in plan["regions"]), "source_sha256": digest(source), "result_sha256": digest(result), "notice": "Text boundaries and exact locks checked; meaning and factual accuracy still require review."}), end="")
        return 0
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print(dump({"error": str(exc)}), file=sys.stderr, end="")
        return 2


if __name__ == "__main__":
    sys.exit(main())

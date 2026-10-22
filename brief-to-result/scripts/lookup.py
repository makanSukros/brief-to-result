#!/usr/bin/env python3
"""List or retrieve focused Brief to Result workflows using only local files."""
import argparse
import json
import re
import sys
from pathlib import Path


FILES = {
    "W": "writing.md", "U": "understanding.md", "I": "ideation.md", "M": "sales.md",
    "C": "content.md", "P": "product.md", "T": "technical.md", "O": "operations.md",
}
HEADER = re.compile(r"^## ([WUIMCPTO]\d{2})\s+[—–-]\s+(.+)$", re.MULTILINE)


def load_recipes():
    reference_dir = Path(__file__).resolve().parent.parent / "references"
    recipes = []
    for prefix, filename in FILES.items():
        path = reference_dir / filename
        document = path.read_text(encoding="utf-8")
        headings = list(HEADER.finditer(document))
        for index, match in enumerate(headings):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(document)
            body = document[match.start():end].strip()
            if not match[1].startswith(prefix):
                raise ValueError(f"Unexpected recipe prefix in {filename}: {match[1]}")
            recipes.append({"id": match[1], "title": match[2],
                            "file": "references/" + filename, "body": body})
    ids = [recipe["id"] for recipe in recipes]
    expected = {f"{prefix}{n:02d}" for prefix in FILES for n in range(1, 11)}
    if len(ids) != len(set(ids)) or set(ids) != expected:
        raise ValueError("Recipe catalog must contain each of the 80 documented IDs exactly once")
    return recipes


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--list", action="store_true")
    mode.add_argument("--id", dest="recipe_id")
    mode.add_argument("--query")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= 80:
        parser.error("--limit must be 1..80")
    try:
        recipes = load_recipes()
        if args.recipe_id:
            recipe_id = args.recipe_id.upper()
            matches = [r for r in recipes if r["id"] == recipe_id]
            if not matches:
                parser.error(f"unknown recipe ID: {args.recipe_id}")
            output = matches[0]
            print(json.dumps(output, ensure_ascii=False, indent=2) if args.json else output["body"])
            return 0
        if args.query is not None:
            tokens = re.findall(r"\w+", args.query.casefold(), flags=re.UNICODE)
            if not tokens:
                parser.error("--query must contain a word")
            scored = []
            for recipe in recipes:
                title = recipe["title"].casefold()
                body = recipe["body"].casefold()
                trigger = next((line.casefold() for line in recipe["body"].splitlines()
                                if line.casefold().startswith("- **trigger:**")), "")
                score = sum(6 * int(t in title) + 3 * int(t in trigger) + int(t in body)
                            for t in tokens)
                if score:
                    scored.append((score, recipe))
            scored.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
            recipes = [r for _, r in scored[:args.limit]]
        rows = [{k: r[k] for k in ("id", "title", "file")} for r in recipes]
        if args.json:
            print(json.dumps(rows, ensure_ascii=False, indent=2))
        elif rows:
            print("\n".join(f"{r['id']} — {r['title']} ({r['file']})" for r in rows))
        else:
            print("No keyword matches. Use --list and choose by the requested outcome.")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Catalog error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
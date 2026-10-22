#!/usr/bin/env python3
"""Measure copy without network access. Exit 0=pass, 1=limit failed, 2=input error."""
import argparse
import json
import math
import re
import sys
from pathlib import Path


def nonnegative(value):
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be nonnegative")
    return number


def percent(value):
    number = float(value)
    if not math.isfinite(number) or not 0 <= number <= 100:
        raise argparse.ArgumentTypeError("must be between 0 and 100")
    return number


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be finite and positive")
    return number


def read_exact(path):
    with Path(path).open("r", encoding="utf-8", newline="") as stream:
        return stream.read()


def measure(text):
    tags = re.findall(r"(?<![\w#])#[\w]+", text, flags=re.UNICODE)
    words = re.findall(r"\S+", text)
    return {
        "characters": len(text),
        "utf8_bytes": len(text.encode("utf-8")),
        "words": len(words),
        "lines": len(text.splitlines()) if text else 0,
        "hashtags": len(tags),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", help="UTF-8 draft; whitespace is not stripped")
    source.add_argument("--stdin", action="store_true")
    parser.add_argument("--max-chars", type=nonnegative)
    parser.add_argument("--max-words", type=nonnegative)
    parser.add_argument("--max-hashtags", type=nonnegative)
    parser.add_argument("--reference", help="UTF-8 original for reduction measurement")
    parser.add_argument("--reduction-percent", type=percent)
    parser.add_argument("--tolerance", type=percent, default=5,
                        help="percentage-point tolerance around target reduction")
    parser.add_argument("--reduction-unit", choices=["characters", "words"], default="characters")
    parser.add_argument("--words-per-minute", type=positive, default=140)
    args = parser.parse_args(argv)
    if args.reduction_percent is not None and not args.reference:
        parser.error("--reduction-percent requires --reference")
    try:
        text = read_exact(args.file) if args.file else sys.stdin.read()
        metrics = measure(text)
        checks = []
        for name, limit in [("characters", args.max_chars), ("words", args.max_words),
                            ("hashtags", args.max_hashtags)]:
            if limit is not None:
                checks.append({"check": "max_" + name, "actual": metrics[name],
                               "limit": limit, "pass": metrics[name] <= limit})
        result = {
            "metrics": metrics,
            "counting": "Unicode code points; spaces, line endings and URLs included; not platform-weighted",
            "word_counting": "Whitespace-delimited tokens; approximate for speech and languages without word spaces",
            "estimated_speech_seconds": round(metrics["words"] / args.words_per_minute * 60, 2),
            "words_per_minute_assumption": args.words_per_minute,
        }
        if args.reference:
            reference_metrics = measure(read_exact(args.reference))
            unit = args.reduction_unit
            original = reference_metrics[unit]
            if original == 0:
                parser.error("reference must contain at least one counted unit")
            reduction = (1 - metrics[unit] / original) * 100
            result["reduction"] = {"unit": unit, "original": original,
                                   "draft": metrics[unit], "percent": round(reduction, 2)}
            if args.reduction_percent is not None:
                checks.append({"check": "target_reduction", "actual": round(reduction, 2),
                               "target": args.reduction_percent, "tolerance_points": args.tolerance,
                               "pass": abs(reduction - args.reduction_percent) <= args.tolerance + 1e-9})
        result["checks"] = checks
        result["pass"] = all(item["pass"] for item in checks)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["pass"] else 1
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
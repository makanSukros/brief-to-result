#!/usr/bin/env python3
"""Inspect a structured dialogue state. No model, network, persistence, or permissions.

The host supplies semantic IDs and interpretations; this module does not understand
raw messages, verify facts, or detect paraphrases. Requires Python 3.10+.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import sys

MODES = {"auto", "guided", "draft"}
KINDS = {"blocker", "conflict", "claim", "leverage", "preference"}
STATUSES = {"answered", "unknown", "deferred"}
FIELDS = {"mode", "task_known", "complete", "partial_available", "rounds_without_output",
          "asked", "inspected", "decisions", "gaps"}
MAX_BYTES = 262144


def _text(value, field, *, empty=True):
    if not isinstance(value, str) or (not empty and not value.strip()):
        raise ValueError(f"{field} must be {'nonempty ' if not empty else ''}text")
    return value


def normalize(raw: dict) -> dict:
    """Validate without silently accepting misspelled fields or mutating input."""
    if not isinstance(raw, dict) or set(raw) - FIELDS:
        raise ValueError("State must be an object with documented fields only")
    state = {"mode": "auto", "task_known": True, "complete": False,
             "partial_available": False, "rounds_without_output": 0,
             "asked": [], "inspected": [], "decisions": {}, "gaps": []}
    state.update(copy.deepcopy(raw))
    if not isinstance(state["mode"], str) or state["mode"] not in MODES:
        raise ValueError("mode must be auto, guided, or draft")
    for key in ("task_known", "complete", "partial_available"):
        if type(state[key]) is not bool:
            raise ValueError(f"{key} must be boolean")
    rounds = state["rounds_without_output"]
    if type(rounds) is not int or rounds < 0:
        raise ValueError("rounds_without_output must be a nonnegative integer")
    for key in ("asked", "inspected"):
        items = state[key]
        if not isinstance(items, list):
            raise ValueError(f"{key} must be a list")
        for item in items:
            _text(item, key, empty=False)
        if len(items) != len(set(items)):
            raise ValueError(f"{key} contains duplicate IDs")
    if not isinstance(state["decisions"], dict):
        raise ValueError("decisions must be an object")
    for key, item in state["decisions"].items():
        _text(key, "decision ID", empty=False)
        if not isinstance(item, dict) or set(item) != {"status", "value"}:
            raise ValueError("Each decision needs status and value")
        if not isinstance(item["status"], str) or item["status"] not in STATUSES:
            raise ValueError("Invalid decision status")
        _text(item["value"], "decision value", empty=item["status"] != "answered")
    if not isinstance(state["gaps"], list):
        raise ValueError("gaps must be a list")
    ids = set()
    for gap in state["gaps"]:
        if not isinstance(gap, dict) or set(gap) != {"id", "kind", "question", "changes", "fallback", "lookup"}:
            raise ValueError("Each gap needs id, kind, question, changes, fallback, lookup")
        ident = _text(gap["id"], "gap ID", empty=False)
        if ident in ids or ident == "__task__":
            raise ValueError("Duplicate or reserved gap ID")
        ids.add(ident)
        if not isinstance(gap["kind"], str) or gap["kind"] not in KINDS:
            raise ValueError("Invalid gap kind")
        for field in ("question", "changes", "fallback"):
            _text(gap[field], field)
        if type(gap["lookup"]) is not bool:
            raise ValueError("lookup must be boolean")
    return state


def next_action(raw: dict) -> dict:
    """Return one next-step recommendation, never an executable external action."""
    s = normalize(raw)
    pending = [g for g in s["gaps"]
               if s["decisions"].get(g["id"], {}).get("status") != "answered"]
    if not s["task_known"]:
        pending.insert(0, {"id": "__task__", "kind": "blocker",
                          "question": "What would you like help with?", "changes": "Identifies the task.",
                          "fallback": "", "lookup": False})
    hard = [g for g in pending if g["kind"] in {"blocker", "conflict", "claim"} and not g["fallback"].strip()]
    fallbacks = [{"id": g["id"], "text": g["fallback"]} for g in pending if g["fallback"].strip()]

    def result(action, reason, gap=None):
        return {"action": action, "reason": reason,
                "gap_id": gap["id"] if gap else None,
                "question": gap["question"] if gap and action == "ask" else None,
                "blocked_ids": [g["id"] for g in hard], "fallbacks": fallbacks}

    if s["complete"] and not hard:
        return result("done", "The requested outcome is complete; do not add an automatic follow-up.")
    priority = {"blocker": 0, "conflict": 1, "claim": 2, "leverage": 3, "preference": 4}
    pending.sort(key=lambda g: priority[g["kind"]])
    hard.sort(key=lambda g: priority[g["kind"]])
    # Read an identified source first; do not repeatedly inspect a failed source.
    for gap in pending:
        if (gap["lookup"] and gap["id"] not in s["inspected"] and gap["kind"] != "preference"
                and (gap["changes"].strip() or gap in hard)):
            return result("inspect", "Inspect the identified authorized source before asking.", gap)
    for gap in hard:
        can_ask = (s["mode"] != "draft" and gap["id"] not in s["asked"]
                   and gap["id"] not in s["decisions"] and gap["question"].strip())
        if can_ask:
            return result("ask", "Resolve the required input or material conflict; complete independent work.", gap)
    if hard:
        action = "partial" if s["partial_available"] else "blocked"
        return result(action, "Do not repeat a declined/answered-unknown question or invent essential input.", hard[0])
    challenge = next((g for g in pending if g["kind"] in {"conflict", "claim"}), None)
    if challenge:
        return result("challenge_and_draft", "Use the supported alternative and identify the consequential assumption.", challenge)
    if s["mode"] != "draft" and s["rounds_without_output"] < 2:
        for gap in pending:
            if (gap["kind"] == "leverage" and gap["changes"].strip() and gap["question"].strip()
                    and gap["id"] not in s["asked"] and gap["id"] not in s["decisions"]):
                return result("ask", "This answer changes the next deliverable, not just a cosmetic preference.", gap)
    if pending:
        return result("draft", "Use a reversible first pass; omit unsupported claims and respect known decisions.")
    return result("do", "The brief is sufficient; deliver without unnecessary questions.")


def record_question(raw: dict, ident: str) -> dict:
    """Record only the question selected by the policy; preserve caller state."""
    s = normalize(raw)
    choice = next_action(s)
    if choice["action"] != "ask" or choice["gap_id"] != ident:
        raise ValueError("This question is not the current recommended question")
    s["asked"].append(ident)
    s["rounds_without_output"] += 1
    return s


def record_answer(raw: dict, ident: str, value: str = "", *, status="answered") -> dict:
    """Record a volunteered answer or correction, not a verified fact or permission."""
    s = normalize(raw)
    if ident != "__task__" and ident not in {g["id"] for g in s["gaps"]}:
        raise ValueError("Unknown decision ID")
    s["decisions"][ident] = {"status": status, "value": value}
    if ident == "__task__" and status == "answered":
        s["task_known"] = True
    s["complete"] = False
    return normalize(s)


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        with args.state.open("rb") as handle:
            data = handle.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError("State exceeds 256 KiB")
        state = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicate_keys)
        print(json.dumps(next_action(state), ensure_ascii=False, indent=2))
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        print(f"Dialogue state error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Repair Mode

Revise the requested part while preserving what is already correct. Trigger on targeted feedback such as "only fix the opening", "keep the facts and CTA", or "repair this section". A request to *write a repair prompt* stays in Create a prompt mode.

## Agent contract

1. Identify the exact current artifact. Read it, or use the actual visible prior draft. Do not invent missing text or assume a file's contents from its name.
2. Build a bounded repair contract: goal, editable regions, locked wording/facts, structure/language constraints, and observable success criteria. For a small edit, do this internally. If there are several plausible targets, ask one focused question rather than modifying the wrong artifact.
3. Convert vague feedback to a concrete intervention: "too robotic" means reduce generic framing and use natural wording; "stronger hook" means lead with a supported benefit or tension, not inflate claims; "shorter" means remove repetition without dropping material conditions.
4. Make the smallest sufficient change. Preserve unrelated paragraphs, links, facts, conditions, negation, audience, and commitments. Outside-scope problems may be noted, not silently rewritten. If a locked inaccurate claim or scope restriction makes the goal impossible, explain the conflict and request a scope/priority decision.
5. Review the requested improvement and invariants. Allow one bounded corrective pass for a failed check; if still blocked, report the exact conflict instead of looping indefinitely or broadening scope.
6. Return the revised target, or the full artifact when requested. For substantial work, add a concise change summary and checks actually run. Do not append a full audit to a one-line edit.

For a pack, repair only the selected deliverable. If a corrected fact affects other deliverables, identify the consistency impact; update those only when the authorized scope includes them. Do not let a project profile rewrite the rest of an existing artifact.

## Optional deterministic text helper

Use the helper for UTF-8 plain-text/Markdown artifacts with clear line boundaries. It does not generate wording, assess truth, edit DOCX/PDF files, or understand code semantics. Use appropriate specialist tools for those formats. Without Python, compare original and revised text directly and do not claim byte-exact enforcement.

```bash
python3 <skill-dir>/scripts/btr.py repair plan draft.txt   --allow 1:2 --keep "Try the demo." --output repair.json
# Edit only each region's replacement string in repair.json.
python3 <skill-dir>/scripts/btr.py repair preview draft.txt --plan repair.json
python3 <skill-dir>/scripts/btr.py repair apply draft.txt   --plan repair.json --output revised.txt
```

Select line ranges from the actual file, not this illustrative example. `--allow START:END` is 1-based, inclusive, and repeatable for disjoint regions. Line numbering follows Python `splitlines`; LF and CRLF are preserved outside selected regions. Select smaller lines/regions when part of a paragraph must remain unchanged.

The plan contains a source SHA-256, original text, and replacement text. Only replacements should be edited; changing scope requires a newly authorized plan. A plan is a reviewable contract, not a security boundary against someone deliberately changing its scope.

`preview` emits a unified diff and writes nothing. `apply` creates a **new** output, refuses any existing file/symlink, rejects stale source hashes, checks sorted non-overlapping ranges and source excerpts, preserves unselected source spans, and enforces occurrence counts for `--keep` strings. It never overwrites the source. A non-final nonempty replacement needs a trailing line break; an empty replacement deletes only the selected range.

Exact locks protect wording, not every aspect of meaning. A lock can still be moved within an editable region; negation, implication, and other semantic constraints require human/agent review. The helper cannot certify that a claim is true or that a hook is effective. Check code-point/word limits with `text_metrics.py` as appropriate.

Keep private source/plan/output files under the project's ignored `.btr/` directory or another approved local location. Plans include original excerpts; treat them with the same confidentiality as the source. Do not publish them automatically.

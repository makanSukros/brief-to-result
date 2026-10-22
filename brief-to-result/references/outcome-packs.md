# Outcome Packs: shared execution contract

A pack is an agent-run workflow for a complete outcome, not a command that calls a model. The local CLI only lists or displays pack instructions. Use a named pack or a clearly requested bundle; do not turn a small task into a pack without reason.

## Run protocol

1. Read the selected pack, supplied source material, and only the explicitly selected project profile. Resolve output language and user constraints first.
2. Establish one shared evidence ledger: claim, source/location, date when relevant, and status (supported, assumption, unknown, stale, or conflict). A profile's `confirmed` label is user-maintained, not independent verification. Do not copy facts from example files into real work.
3. Resolve material contradictions before using a claim. Recheck stale facts when suitable tools are available. Otherwise exclude them from final copy and list the gap. Never fill absent prices, dates, metrics, URLs, testimonials, or capabilities.
4. Choose the smallest set of workflow stages needed for the output contract. Load those references on demand. Defaults are overridable: one requested post means one post, not the whole default bundle.
5. Draft every requested deliverable from the same ledger. Keep names, availability, terms, and calls to action consistent across outputs. Reuse facts, not identical wording everywhere.
6. Review deliverables individually and together. Count explicit limits with the text helper, check material claims against the ledger, and record unperformed checks honestly. A source-access failure is not evidence of a claim.
7. Return clearly separated, copy-ready deliverables. Put assumptions and gaps outside publishable copy. For a file request, create and verify real files with available tools; headings in chat are not files. List each requested deliverable as completed, blocked, or intentionally omitted by the user's scope. Never label a partially blocked pack fully complete.

Keep the ledger compact and expose evidence only where useful. Research outputs need citations; marketing copy may keep verification notes separately, unless inline attribution is required. Do not claim verification simply because all deliverables agree with one another.

## Scope and permissions

Prepare does not mean publish. A pack grants no permission to send emails, deploy code, purchase, or upload private data. Respect existing authorization without asking for it again. Use specialist skills for actual code, design, documents, and media. Do not attempt to implement a feature merely because the pack is named Idea to Build.

## Missing inputs

If the source itself is missing, ask for that source rather than inventing it. When only one output is blocked, complete the unaffected outputs and explain the exact dependency. Never replace missing substantive content with an unlabeled placeholder in a supposedly ready-to-use result.

## Selection

| ID | Outcome | Load |
| --- | --- | --- |
| `launch-kit` | Consistent product-launch drafts | [Launch Kit](../packs/launch-kit.md) |
| `idea-to-build` | An implementation-ready feature handoff | [Idea to Build](../packs/idea-to-build.md) |
| `research-to-content` | Source-grounded content | [Research to Content](../packs/research-to-content.md) |

Use `python3 <skill-dir>/scripts/btr.py packs list` or `packs show launch-kit` to discover instructions without loading all packs.

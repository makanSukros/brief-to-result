# Idea to Build

**ID:** `idea-to-build`

**Outcome:** A feature handoff that a developer or coding agent can implement and test.

Use when a user requests Idea to Build or a bundle of requirements, flows, criteria, and tasks. It produces a specification, not deployed software. Apply the [shared pack contract](../references/outcome-packs.md).

## Inputs

Required: the feature idea and intended user problem. Use existing repository/docs, target platform, users, permissions, constraints, and the selected profile when available. Inspect referenced existing artifacts before making claims about their architecture. If unavailable, label integration details as proposals.

## Method

1. Use P01 to define the user, problem, desired outcome, non-goals, and a success signal that can actually be measured. Distinguish requirements from preferences.
2. Use P05 for the happy path, empty/loading/error states, cancellation, retries, and recovery. Map role and data-ownership boundaries when applicable.
3. Use P10 to bound the first usable release. Include operational dependencies; do not replace a reliable release with a screenshot-only demo.
4. Assign stable requirement IDs (R01...) and use P09 for testable criteria (AC01...). Every critical requirement must have acceptance evidence, including denial/failure cases.
5. Use T01 and O04 for interface/data contracts and dependency-ordered implementation tasks (TASK01...). Link each task to requirement and acceptance IDs. Do not prescribe a framework or vendor without context.
6. Audit traceability, permissions, failure handling, compatibility, and unresolved decisions. Never mark a requirement implemented or a test passed without actual execution evidence.

## Default output contract

| Deliverable | Required content |
| --- | --- |
| `brief` | Problem, audience, scope/non-goals, requirements with IDs, constraints, and success signals |
| `user-flow` | Main flow, alternate/error states, data ownership, and authorization boundaries |
| `acceptance-criteria` | Given/When/Then or equally testable conditions mapped to requirement IDs |
| `implementation-tasks` | Ordered tasks, dependencies, affected components when known, completion evidence, and acceptance IDs |
| `open-decisions` | Assumptions, unresolved choices, options/tradeoffs, and which tasks each decision blocks |

For security or data operations, specify server-side authorization, cross-tenant denial cases, validation, and recovery where relevant. These are design requirements, not evidence of an existing implementation. Use applicable specialist skills when implementation is separately authorized.

## Example invocation

```text
Use Brief to Result: Idea to Build.
We need saved report views shared within a workspace.
Use the attached current permissions model. Include cross-workspace
access denial, empty states, and acceptance criteria. Do not code yet.
```

**Done means:** critical requirements map to testable criteria and ordered tasks; assumptions are explicit; the handoff is usable without pretending unresolved dependencies are settled.

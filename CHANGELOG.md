# Changelog

## 0.4.0 — 2026-10-22

- Add a cross-workflow adaptive dialogue contract: consequential questions, proactive blindspot checks, source inspection, answer reuse, corrections, unknown/deferred decisions, and explicit stop conditions.
- Replace the blockers-only clarification rule with a consequence-based decision: ask only when the answer changes correctness or direction enough to justify interrupting the work.
- Respect guided conversations and no-questions requests without inventing essential facts; show tangible progress after two optional question rounds by default.
- Add an optional, standard-library structured dialogue policy helper. It makes no model/network calls, interprets no raw conversation, writes no files, and grants no permissions.
- Add policy transition, error-path, installed-package, and saved-output regression tests. Retain a regression for mandatory-input prioritization found during testing.
- Add eight author-reviewed dialogue walkthroughs with 13 saved responses, explicit provenance, and a separate live-host evaluation procedure. These are not independent model benchmarks.
- Update English and Indonesian READMEs with interaction examples while retaining ten role categories and three copyable requests per category.
- Preserve 80 workflows, 24 Hook Lab formulas, three packs, opt-in profiles, scoped repair, short-name packaging, and MIT licensing.

## 0.3.0 — 2026-10-22

- Add an agent-run sales and affiliate Hook Lab with 24 formula families across six persuasive mechanisms.
- Route ordinary hook requests through product facts, recognizable situations, distinct angles, proof-aware claims, and concrete payoffs rather than copied hook templates.
- Separate creative strategy from conversational, humorous, premium, and regional voice; retain English-first instructions and requested output languages.
- Include original fictional English/Indonesian examples, a light regional example, a connected video concept, and 16 manual model acceptance cases.
- Add structural regression tests and include all Hook Lab guides in standalone btr builds. Local tests are not creative-quality or conversion benchmarks.
- Preserve the 80 core workflows, three Outcome Packs, Project Profiles, scoped Repair Mode, existing short-name installation, and MIT license.

## 0.2.1 — 2026-10-22

- Add @btr task-invocation guidance, contextual routing, and one-question handling when a task is missing.
- Add a reproducible, standalone short-name `btr` package builder; preserve canonical `brief-to-result` installations.
- Expose BTR in interface metadata and allow description-based matching for deliberate text mentions.
- Document native ChatGPT @ selection versus Codex CLI/IDE $ selection without claiming automatic installation.
- Add English and Indonesian quick-start examples and packaging regression tests.

## 0.2.0 — 2026-10-22

- Add three agent-run Outcome Packs: Launch Kit, Idea to Build, Research to Content.
- Add optional local Project Profiles with explicit selection, preference precedence, provenance fields, and freshness filtering.
- Add scoped Repair Mode plus source-hash checks, exact wording locks, preview, and new-file-only application for UTF-8 text.
- Add a standard-library Python CLI for pack discovery, profile handling, and deterministic text repair.
- Add automated regression tests and fictional manual acceptance examples.
- Add an Indonesian README alongside the English default README.
- Preserve the 80 existing workflows and MIT licensing.

This version number describes the source update; it does not imply a published GitHub Release or cross-agent certification.

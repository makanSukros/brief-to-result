# Technical work and troubleshooting

Use evidence from available artifacts, repository instructions, and applicable specialist skills. Implement when requested and authorized rather than stopping at a plan. State access and verification limits precisely. Follow an explicit output language or specified audience language. Preserve the source language when editing unless translation is requested. Default new content to English when there is no language signal; do not infer locale, currency, date conventions, or timezone. User constraints override suggested counts.

## Contents

- T01 — Turn a request into implementation specifications
- T02 — Diagnose errors from evidence
- T03 — Make the smallest effective fix
- T04 — Review code changes
- T05 — Refactor while preserving behavior
- T06 — Test meaningful risks
- T07 — Improve performance through measurement
- T08 — Design an API integration
- T09 — Recover code with explicit fidelity limits
- T10 — Prepare a release and recovery plan

## T01 — Turn a request into implementation specifications

- **Trigger:** “Build this feature,” “Turn this idea into coding tasks,” or an implementation request with unclear behavioral boundaries.
- **Input:** Require the desired outcome. If a repository is available, read its instructions and inspect related flows; do not invent files or technologies.
- **Method:** Identify current behavior, required changes, affected components, data contracts, failure cases, and verification. Follow existing project patterns. Surface decisions that materially affect implementation.
- **Output:** Concise specifications or a direct implementation, according to the request, with acceptance criteria and dependency notes. Distinguish planned work from completed changes.
- **Check:** Trace requirements to concrete changes. Avoid major architecture changes, migrations, or dependencies without a clear need.
- **Example:** “Add a task-status filter using existing components, and define its URL behavior and empty state.”

## T02 — Diagnose errors from evidence

- **Trigger:** “Why is this failing?” or a problem report containing an error message, screenshot, log, or reproduction steps.
- **Input:** Require an observable symptom. Reuse version, environment, recent-action, and log information; request one decisive missing detail if needed.
- **Method:** Separate symptoms, observed facts, and causal hypotheses. Order checks by safety and their ability to distinguish hypotheses. Examine recent changes and boundaries between the application, network, and external services.
- **Output:** An explanation with an appropriate confidence level, ordered diagnostic steps, and the next action for each possible result. Use accessible instructions for nontechnical users.
- **Check:** Do not assert a root cause from a generic symptom. Request redacted evidence instead of passwords, secrets, or sensitive logs.
- **Example:** “Explain this upload error to a beginner and identify the most informative first check.”

## T03 — Make the smallest effective fix

- **Trigger:** “Fix this bug” or a diagnosis with enough evidence to change the implementation.
- **Input:** Require the symptom and access to relevant code or configuration. Respect repository instructions, reproduction steps, and existing local changes.
- **Method:** Reproduce when possible, trace the cause, and change the smallest area that removes it. Preserve unrelated contracts. Run verification proportionate to the fix's risks.
- **Output:** Reviewable code changes, the cause, resulting behavior, and actual verification evidence. If access is blocked, provide a concrete patch or instructions without claiming they were applied.
- **Check:** Keep unrelated rewrites out of the fix. Distinguish checks that passed, failed, or were not run, and preserve the user's existing work.
- **Example:** “Fix the subtotal not updating after a quantity edit, then verify price changes and zero quantity.”

## T04 — Review code changes

- **Trigger:** “Review this pull request,” “Check this diff,” or a request to find problems in specific changes.
- **Input:** Require an accessible diff or change set. Use the change objective, related contracts, project instructions, and available tests.
- **Method:** Trace effects on correctness, compatibility, data access, failure handling, and regression risk. Inspect surrounding code before drawing conclusions. Prioritize issues with a concrete failure scenario.
- **Output:** Findings ordered by impact, relevant locations, failure scenarios, and repair suggestions. If no strong findings emerge, say so and describe the review's limits.
- **Check:** Do not present style preferences as bugs. A partial diff review cannot establish whole-system safety; qualify uncertain findings.
- **Example:** “Review this cache change for cross-user data leakage, invalidation behavior, and compatibility with existing callers.”

## T05 — Refactor while preserving behavior

- **Trigger:** “Clean up this code,” “Split this large component,” or a maintainability improvement intended to preserve functionality.
- **Input:** Require the target code and reason for refactoring. Inspect public contracts, dependencies, and existing tests before defining scope.
- **Method:** State the behavior that must remain, identify the main source of complexity, and make incremental changes. Improve naming, responsibility boundaries, and duplication where they help maintenance. Verify risky paths afterward.
- **Output:** A bounded refactor, a summary of the new structure, available evidence of preserved behavior, and any explicitly agreed behavior changes.
- **Check:** Shorter code is not automatically clearer. Avoid hidden contract or dependency changes; do not claim complete equivalence without sufficient evidence.
- **Example:** “Split this order-processing function while preserving validation order and error-response formats.”

## T06 — Test meaningful risks

- **Trigger:** “What should we test?” “Verify this change,” or work with a concrete regression risk.
- **Input:** Require the changed behavior or implementation. Use existing tests, failure patterns, contracts, and impact to choose scope.
- **Method:** Identify major risks and select checks that would fail for a plausible incorrect implementation. Use the most efficient test level. Include boundary inputs, failure paths, or component interactions when relevant.
- **Output:** A focused test plan or executed checks, as requested, with real results, remaining risks, and reasons for the selected coverage.
- **Check:** Avoid tests that merely mirror implementation logic. Broaden testing only for unresolved risks or project requirements; passing tests does not guarantee every case is safe.
- **Example:** “Run the most important checks for payment retries, especially whether one transaction can be processed twice.”

## T07 — Improve performance through measurement

- **Trigger:** “The application is slow,” “Optimize this,” or a suspected speed or resource bottleneck.
- **Input:** Require the performance symptom and affected operation. Use available workload, data size, environment, and metrics; never invent a baseline.
- **Method:** Choose the user-relevant metric, measure a representative baseline, and separate computation, network, storage, and rendering time. Prioritize measured bottlenecks. Compare results under equivalent conditions after changes.
- **Output:** Bottleneck findings, targeted changes or experiments, before-and-after results when available, and effects on cost, memory, or complexity.
- **Check:** Do not promise percentage improvements without measurements. Distinguish synthetic benchmarks from production experience and preserve correctness while optimizing.
- **Example:** “Measure why this contact list becomes slow with large datasets, then optimize the most consequential bottleneck.”

## T08 — Design an API integration

- **Trigger:** “Integrate this service,” “Connect this API,” or a request to define interactions between systems.
- **Input:** Require the integration objective and target service. Use current official documentation, local contracts, environments, and available access.
- **Method:** Map authentication, requests, responses, data transformations, rate limits, timeouts, retries, idempotency, and relevant webhooks. Define failure handling and recovery. Separate configuration, secrets, and information safe to log.
- **Output:** Contract design or implementation, as requested, a list of required configuration names without secret values, and a verification and outage-handling plan.
- **Check:** Do not invent endpoints, service capabilities, or connection results. Use applicable provider skills and follow session authorization for environment changes.
- **Example:** “Design payment integration covering duplicate webhooks, pending states, and reconciliation of delayed payments.”

## T09 — Recover code with explicit fidelity limits

- **Trigger:** “Recover my code,” “Reconstruct this build,” or a request to reproduce an application from available artifacts.
- **Input:** Require accessible artifacts and the recovery scope. Use available code, assets, recordings, and authorized access without bypassing controls.
- **Method:** Inventory observable components and separate frontend, backend, configuration, and dependencies. Recover what can be substantiated; label reconstruction based on observation and unavailable components. Compare representative scenarios.
- **Output:** Recovered code or a recovery map, as requested, including component origins, verified functions, approximations, and requirements for closing gaps.
- **Check:** Do not claim an engine or interface is completely identical when only partial artifacts are visible. Observed behavior does not establish internal implementation details.
- **Example:** “Recover this application from its build files and identify identical, reconstructed, and unverified parts.”

## T10 — Prepare a release and recovery plan

- **Trigger:** “Is this ready to deploy?” “Prepare a release,” or a deployment with environmental dependencies.
- **Input:** Require the changes and target environment. Reuse project procedures, session authorization, configuration, dependencies, and timing constraints.
- **Method:** Check critical journeys, data compatibility, configuration, release steps, observability, and rollback options. Define failure signals and recovery actions. Complete authorized preparations before any final decision that actually requires approval.
- **Output:** An evidence-backed readiness status or blockers, release sequence, recovery plan, and deployment results only if execution occurred and was confirmed.
- **Check:** A successful build does not prove application health. Inspect deployment results before claiming success; keep production changes within session authorization.
- **Example:** “Prepare the import-feature release, check critical paths, and define rollback conditions if errors increase.”
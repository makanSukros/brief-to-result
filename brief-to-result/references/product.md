# Product and UX

Choose the recipe that matches the requested outcome. Respect the user's scope, audience, and constraints; suggested counts are defaults. Follow an explicit output language or specified audience language. Preserve the source language when editing unless translation is requested. Default new content to English when there is no language signal; do not infer locale, currency, date conventions, or timezone. Distinguish proposals, prototypes, implementations, and verified behavior.

## Contents

- P01 — Turn a feature idea into an actionable brief
- P02 — Write a PRD ready for implementation
- P03 — Audit a clearly bounded interface
- P04 — Design navigation around shared data
- P05 — Map user flows and interaction states
- P06 — Prioritize a roadmap with explicit reasons
- P07 — Guide onboarding toward the first useful result
- P08 — Define roles and access boundaries
- P09 — Write verifiable acceptance criteria
- P10 — Define a release scope that can operate reliably

## P01 — Turn a feature idea into an actionable brief

- **Trigger:** “Develop this feature,” or an idea describing a solution without explaining its purpose.
- **Input:** Require an initial idea or problem. Reuse available audience, product, and timing context instead of asking for it again.
- **Method:** Identify the user's job, current obstacle, and intended behavior change. Define the main flow, scope, exclusions, dependencies, and one observable success measure. Label unverified needs as hypotheses.
- **Output:** A concise brief covering the problem, audience, proposed solution, flow, boundaries, and next decision. Include alternatives only when they affect the implementation choice.
- **Check:** Connect each capability to a real problem. Do not generalize one customer's request into a proven market requirement.
- **Example:** “Turn task reminders into a feature brief for small teams, including the main flow and first-release boundaries.”

## P02 — Write a PRD ready for implementation

- **Trigger:** “Write a complete PRD,” “Prepare specifications for a coding agent,” or a feature that spans several modules.
- **Input:** Require a product or feature objective. Reuse existing materials and identify current capabilities, integrations, and unresolved decisions.
- **Method:** Translate the objective into roles, user journeys, business rules, data states, system interactions, nonfunctional requirements, dependencies, and acceptance criteria. Separate mandatory requirements, design choices, and blocking questions.
- **Output:** A structured document with scope, behavioral specifications, failure scenarios, implementation stages, verification, and open decisions. Assign requirement identifiers for traceability.
- **Check:** Resolve contradictions between modules and unsupported integration assumptions. A complete document does not mean the application has been built or is production-ready.
- **Example:** “Write a booking-page PRD covering rescheduling, failed payments, and verifiable acceptance criteria.”

## P03 — Audit a clearly bounded interface

- **Trigger:** “Redesign this section,” “Why does this screen feel confusing?” or a request to improve a specific screenshot or component.
- **Input:** Require an inspectable area or artifact. Use the page objective and target device when known; state observation limits if the image is unavailable.
- **Method:** Examine information hierarchy, action clarity, density, readability, consistency, accessibility, and interaction states. Rank findings by their effect on the user's task. Preserve the requested boundaries.
- **Output:** Three to five high-impact issues, concrete changes, and a design or implementation matching the request and tools.
- **Check:** Separate visible evidence from inferred behavior. Do not call a mockup interactive before implementing interactions; inspect the visual result when producing an interface.
- **Example:** “Improve this statistics card while preserving the navigation, panel width, and brand identity.”

## P04 — Design navigation around shared data

- **Trigger:** “Where should this menu live?” or confusion about data used by several modules.
- **Input:** Require the shared entities and consuming modules. Reuse known roles, access patterns, current navigation, and technical constraints.
- **Method:** Separate the authoritative data source, management location, and contextual entry points. Map tasks from each module. Compare arrangements by discoverability, consistency, context switching, and migration impact.
- **Output:** An information-architecture recommendation, navigation map, contextual link or picker behavior, and rules for cross-module changes. Include a representative user journey.
- **Check:** Multiple entry points must not silently create separate copies of the same data. Explain access rules and the consequences of editing or deleting shared entities.
- **Example:** “Design access to contacts and lists from messaging and email while keeping one consistent source of data.”

## P05 — Map user flows and interaction states

- **Trigger:** “Create a user flow,” “Find gaps in this journey,” or a feature described only through its successful path.
- **Input:** Require the user's job and starting point. Reuse available device, role, prerequisite, and service-limit information.
- **Method:** Map the main path to completion. Add relevant empty, loading, success, failure, access-denied, session-expired, cancellation, and recovery states. Specify the information and actions available in each state.
- **Output:** A concise flow with meaningful branches and a state table covering triggers, presentation, actions, and transitions. Use a diagram when branching is easier to understand visually.
- **Check:** Avoid unexplained dead ends. Ensure retrying, returning, or canceling does not silently duplicate transactions or discard the user's work.
- **Example:** “Map contact import from upload to completion, including duplicate records, invalid rows, and cancellation.”

## P06 — Prioritize a roadmap with explicit reasons

- **Trigger:** “Which feature comes first?” “Build a roadmap,” or a backlog that exceeds team capacity.
- **Input:** Require candidate work and a primary objective. Use available capacity, deadlines, demand evidence, and dependencies; label estimates.
- **Method:** Select relevant criteria such as user impact, business value, evidence confidence, cost, and dependencies. Avoid false numerical precision. Prioritize prerequisites and blocking risks even when they are less visible.
- **Output:** A reasoned order, now–next–later groups, conditions that would change priorities, and validation steps for weakly supported candidates.
- **Check:** Align criteria with the stated objective. Do not invent a schedule without capacity evidence; use relative sequencing when timing estimates are unavailable.
- **Example:** “Prioritize these ten features to reduce the number of new users who leave before completing their first project.”

## P07 — Guide onboarding toward the first useful result

- **Trigger:** “Onboarding is too complicated,” “Users sign up and disappear,” or a request to design a new-user experience.
- **Input:** Require the first task that delivers meaningful value. Use the current flow, mandatory steps, user types, and available behavior data.
- **Method:** Define the first useful result, map obstacles to it, and defer unnecessary steps. Design contextual guidance, starter examples, progress states, and recovery when users stop midway.
- **Output:** An onboarding flow, primary-action copy, rules for showing help, and proposed stage-level measurement. Separate evidence-backed changes from design hypotheses.
- **Check:** Avoid requesting information or integrations before they help. Experienced users should be able to skip optional guidance without losing essential functionality.
- **Example:** “Design onboarding so a new team creates one shared task before completing optional profile details.”

## P08 — Define roles and access boundaries

- **Trigger:** “Design permissions,” “Who can access what?” or a feature involving organizations, teams, and data ownership.
- **Input:** Require roles, resources, and primary actions. Flag unclear ownership or organizational boundaries.
- **Method:** Map relevant view, create, edit, delete, invite, export, and permission-management actions. Define data scope, exceptions, inheritance, and membership-change behavior. Start with the minimum access each role needs.
- **Output:** A role–action–scope matrix, enforcement rules, denial scenarios, and verification cases across organizations and roles.
- **Check:** Hiding a button is not sufficient access control. Distinguish a proposed policy from inspected implementation. Address residual access after removal, shared links, and whether exported copies remain outside system control.
- **Example:** “Define owner, administrator, and member permissions for projects, files, data exports, and invitations.”

## P09 — Write verifiable acceptance criteria

- **Trigger:** “When is this feature done?” “Write acceptance criteria,” or requirements that rely on subjective language.
- **Input:** Require the intended behavior. Reuse agreed business rules, example data, and nonfunctional constraints.
- **Method:** Translate each requirement into an initial condition, action, and observable outcome. Include relevant input boundaries, significant failures, and access rules. Separate functional checks from performance targets or visual-quality requirements.
- **Output:** Identified criteria with example scenarios, verification methods, and links to source requirements. Mark thresholds that still require a decision.
- **Check:** Each criterion should support a pass-or-fail judgment without guessing the author's intent. Never present a proposed target as an already achieved test result.
- **Example:** “Write acceptance criteria for task reminders, including deadline changes and duplicate notification delivery.”

## P10 — Define a release scope that can operate reliably

- **Trigger:** “Build a proper first release,” “Avoid a throwaway MVP,” or a launch constrained by team capacity.
- **Input:** Require the essential launch outcome. Use available capacity, risks, target users, and existing commitments.
- **Method:** Choose a complete, valuable user journey. Reduce feature breadth or variation while retaining relevant essentials such as access control, error recovery, support, and observability. Explain how later capabilities can be added.
- **Output:** Release scope, deferred work, launch prerequisites, readiness criteria, and subsequent development stages. Identify dependencies that could delay release.
- **Check:** Do not leave the core journey ending at a placeholder. A readiness checklist defines requirements; it does not prove the checks have passed.
- **Example:** “Define a first course-platform release that completes the purchase, enrollment, and learning journey for individual instructors.”
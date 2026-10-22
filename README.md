# Brief to Result

**Less prompting. More finished work.**

[English](README.md) | [Bahasa Indonesia](README.id.md) · [MIT License](LICENSE)

**Brief to Result helps your AI agent turn everyday requests into useful results:** a message ready to review and send, meeting notes organized into actions, a difficult topic explained clearly, or a rough idea turned into a practical plan.

Describe what you need in natural language and provide the relevant text, notes, or files. The skill guides a compatible agent to choose an approach, follow your constraints, and check the result. You do not need to memorize workflow IDs or write a long prompt for every task.

## Just mention @btr

After installing the **btr** package, select the skill and talk normally:

```text
Please help me with this @btr.
```

```text
@btr make this email friendly but firm.
```

```text
Turn these meeting notes into clear next steps @btr.
```

The mention can go at the beginning, middle, or end of your task. BTR uses the relevant conversation and material you provide, then chooses a workflow. No workflow numbers, pack names, or technical commands are required for everyday use. Without a task or relevant context, it asks one short question instead of guessing. Ask `@btr menu` only when you want a small menu of options.

**In ChatGPT with Skills support:** type `@`, search for **BTR — Brief to Result**, and select the installed skill. **In Codex CLI/IDE:** use `$btr`. A plain-text marker alone does not install the skill or guarantee a native menu selection. Use the [short-name installation](#installation) below; existing long-name installations remain supported. See the [invocation guide](brief-to-result/references/invocation.md) for setup and limitations.

## What is Brief to Result?

It is a **reusable set of instructions, examples, and optional local tools for an AI agent**. Think of it as a work guide your agent can follow, rather than a separate chatbot or a new AI model.

The skill brings together **80 focused workflows, three Outcome Packs, optional Project Profiles, and scoped Repair Mode**. You can use it for a small everyday task or a larger project, without running the entire catalog.

You still need a compatible host agent and its model access. Reading files, browsing sources, generating artifacts, and other actions depend on the tools and permissions available to that agent. The skill does not add those capabilities by itself. After installation, ordinary writing and planning requests do not require coding; Python helpers are optional.

> Executes the requested work by default. Ask it to improve an email and it should return the improved email—not instructions for improving it. It writes a prompt only when you ask for one. Preparing content never implies permission to send or publish it.

## Purpose and practical benefits

**The goal is to reduce the effort between “I need help with this” and a result you can actually use.** It is designed to make your requests easier to act on while preserving the facts, meaning, and boundaries you supply.

| Everyday friction | How the skill helps |
| --- | --- |
| You know what you need, but not how to phrase a detailed prompt. | Starts from your request and available context; asks a focused question only when essential information is missing. |
| The answer is generic, too long, or in the wrong format. | Uses your audience, tone, length, language, and format requirements to shape the deliverable. |
| You keep explaining the same project or brand. | Lets you explicitly select a local Project Profile with reusable preferences and sourced facts. |
| You need several related outputs, but their facts drift apart. | Outcome Packs use shared source facts for a coordinated set of drafts. |
| You ask for one change and receive a completely different document. | Repair Mode defines what may change and what must stay; an optional text helper checks exact edit boundaries. |
| Missing details turn into invented dates, prices, or promises. | Instructs the agent to distinguish supplied facts, assumptions, and unknowns rather than fill gaps with unsupported claims. |

These are working methods, not a guarantee of perfect answers or measured time savings. Review important facts and commitments before using the result.

## Who is it for?

Anyone using a compatible AI agent for day-to-day work or learning: professionals handling messages and meetings, students studying from notes, creators preparing content, freelancers and small-business owners communicating with customers, and product or development teams turning ideas into tasks. You do not have to be a developer to use the writing, learning, or planning workflows.

## Everyday use cases

After installation, mention **@btr**, describe the task, and attach or paste the relevant material. The examples below show requests you can adapt and the kind of result to ask for; they are not benchmark results.

| Situation | Example request | Useful result |
| --- | --- | --- |
| You want to decline an invitation politely. | “@btr help me decline this invitation warmly. Keep it short and do not invent an excuse.” | A respectful reply that does not add a false reason or a new commitment. |
| You need to follow up on unfinished work. | “@btr make this follow-up friendly but clear. Keep the deadline already in my draft.” | A ready-to-review message with the request and existing deadline intact. |
| Your meeting notes are messy. | “@btr turn these notes into decisions, tasks, owners, and deadlines. Mark anything we did not agree on.” | An action summary that separates confirmed assignments from open questions. |
| A topic in your study notes is confusing. | “@btr explain this topic for a beginner, give one concrete example, and write three practice questions.” | An explanation and a small exercise based on the supplied material. |
| You have too much to do this week. | “@btr here are my tasks, deadlines, and six available hours. Recommend three priorities and what to defer.” | A proposed plan grounded in your stated capacity, without changing your calendar. |
| A long document is hard to act on. | “@btr summarize this document: what changed, what I need to do, and what remains unclear.” | Key points and next steps, with missing information clearly identified. |
| A customer is unhappy. | “@btr draft a calm reply using this complaint and our support policy. Do not promise refunds or delivery dates that are not confirmed.” | An empathetic draft with a supported next step. |
| One product update needs several announcements. | “@btr turn these release notes into one customer email and two social posts. Use the same product facts.” | Coordinated drafts adapted to each channel. |
| You have a feature idea but no clear handoff. | “@btr turn this idea into a brief, user flow, acceptance criteria, and implementation tasks. Do not code yet.” | A structured handoff with unresolved decisions called out. |
| Most of a draft works, but the opening does not. | “@btr rewrite only the opening. Keep the rest of the text and the call to action unchanged.” | A targeted revision instead of an unnecessary full rewrite. |

Simple tasks do not need a full Outcome Pack or a Project Profile. Start with the smallest result that solves your problem; add structure when the work needs it.

### What does a finished result look like?

The examples below are fictional illustrations of the intended output, not recorded model evaluations.

<details>
<summary><strong>Example 1: turn a rough message into a polite follow-up</strong></summary>

**Your draft:**

> hi Sam any news about the draft you said you'd send yesterday? i need it today

**Your request:**

> @btr make this friendly and professional. Keep it short and preserve the existing deadline.

**Illustrative result:**

> Hi Sam, just following up on the draft you planned to send yesterday. I need it today—could you share an update? Thanks!

The result keeps the actual request and timing without adding a meeting, an excuse, or a new promise.

</details>

<details>
<summary><strong>Example 2: turn scattered meeting notes into an action summary</strong></summary>

**Your notes:**

> Alex drafts the proposal. Morgan reviews it. Budget still undecided. No due dates agreed.

**Your request:**

> @btr extract tasks, owners, deadlines, and open decisions. Do not fill in missing information.

**Illustrative result:**

| Task | Owner | Deadline |
| --- | --- | --- |
| Draft the proposal | Alex | Not agreed |
| Review the proposal | Morgan | Not agreed |

**Open decision:** the budget has not been decided.

The output makes the notes actionable without inventing a budget or due dates.

</details>

## Start with a real task

Once the skill is installed, ask your agent:

```text
@btr Launch Kit.
Turn these release notes into one customer email and two social posts.
Use only supplied facts. Prepare drafts; do not publish.
```

```text
@btr use the project profile .btr/profiles/northstar.json.
Turn this feature idea into requirements, user flows, acceptance criteria,
and dependency-ordered tasks. Flag unresolved decisions. Do not code yet.
```

```text
@btr Repair Mode.
Only rewrite the opening paragraph. Keep every product fact, the remaining
paragraphs, and the CTA unchanged. Return the full revised draft.
```

These examples use the installed short-name package. Use `$btr` in Codex CLI/IDE; long-name installations still use `$brief-to-result`. Host compatibility is not implied by documentation examples.

## What's included

| Feature | What you get | Guide |
| --- | --- | --- |
| **Outcome Packs** | A coordinated bundle with shared facts and explicit completion checks | [Pack protocol](brief-to-result/references/outcome-packs.md) |
| **Project Profiles** | Local, opt-in project defaults plus sourced and dated fact records | [Profile guide](brief-to-result/references/project-profiles.md) |
| **Repair Mode** | Targeted changes with protected wording and preserved surrounding text | [Repair guide](brief-to-result/references/repair-mode.md) |
| **80 workflows** | Writing, explanation, strategy, sales, content, product, engineering, and operations | [Skill entry point](brief-to-result/SKILL.md) |

### Three Outcome Packs

| Pack | Default deliverables |
| --- | --- |
| [Launch Kit](brief-to-result/packs/launch-kit.md) | Message, email, social posts, FAQ, launch checklist, evidence/open items |
| [Idea to Build](brief-to-result/packs/idea-to-build.md) | Brief, user flow, acceptance criteria, implementation tasks, open decisions |
| [Research to Content](brief-to-result/packs/research-to-content.md) | Source map, summary, angles, draft, verification notes |

Your requested scope overrides the defaults. A single email does not become a campaign. Unavailable sources, unknown prices, and blocked outputs are surfaced rather than invented. Packs are executed by your host agent, not by the Python helper.

### Project Profiles without hidden memory

Select a profile explicitly; it does not load across unrelated projects or save preferences automatically. Current task instructions override profile defaults. Existing text keeps its language unless you request translation; new content defaults to English when no other language is established.

Profile preferences and product facts are separate. Changeable facts need provenance and review dates. The helper excludes stale, unverified, or deprecated records; a `confirmed` label is user-maintained and **not independent fact verification**. Profiles remain local to the selected directory, but the host model can see any profile you ask it to read. Do not store credentials or private customer records.

### Repairs that stay in scope

Repair Mode identifies the target, editable parts, protected facts/wording, and success criteria before revising. The optional text helper checks the source hash, preserves unselected spans, previews a diff, and writes to a **new file only**. It rejects overlapping/out-of-range edits, stale plans, and changes to exact wording locks. Meaning, factual accuracy, and style still need review.

## Installation

### Short name: btr (recommended)

The canonical sources remain in `brief-to-result/`; the builder produces a **complete, standalone `btr` skill**, not a wrapper that needs a second skill installed. It changes the skill name and native default prompt while keeping all runtime resources and the MIT license together.

```bash
git clone https://github.com/makanSukros/brief-to-result.git
cd brief-to-result
python3 tools/build_btr.py --output dist/btr.zip
```

For ChatGPT accounts with skill upload, import `dist/btr.zip` through **Plugins → Skills → Create → Upload from your computer**, then review and install it. Once enabled, type `@` and select **BTR — Brief to Result**. Availability and installation are controlled by your host; publishing on GitHub does not install it in your account.

For a first local installation in an agent that supports `~/.agents/skills/`, build directly to a new directory:

```bash
python3 tools/build_btr.py --directory "$HOME/.agents/skills/btr"
```

The builder refuses existing destinations and does not overwrite an installed version. Review/back up an older installation before replacing it. Use your client's documented directory if different. In Codex CLI/IDE, select `$btr` or browse `/skills`. Prefer one active installation to avoid duplicate entries.

### Existing long-name installation

`brief-to-result/` and `$brief-to-result` remain supported. Copying that original directory installs the long name, not a native skill named `btr`. Do not merely rename its folder: the directory and frontmatter name must match. Use the builder for the short name. Natural-language `@btr` matching in a long-name installation depends on the host discovering and applying the skill description; it is not a universal menu alias.

Keep project profiles outside the installed skill directory. Markdown instructions can be followed without Python. Building the short-name package and using `btr.py` requires **Python 3.10+**, only the standard library, and no network/model calls. You still need a compatible agent and its own model access; this is not a standalone chatbot or background automation service.

See the [invocation guide](brief-to-result/references/invocation.md) for official host documentation and manual acceptance cases.

## Local helpers

Run these examples from the cloned repository root. For an installed copy, substitute its actual path for `brief-to-result/`.

### Discover a pack

```bash
python3 brief-to-result/scripts/btr.py packs list
python3 brief-to-result/scripts/btr.py packs show launch-kit
```

These commands show instructions, not generated deliverables. `--json` returns machine-readable pack metadata.

### Create a project profile

```bash
python3 brief-to-result/scripts/btr.py profiles init northstar
# Edit .btr/profiles/northstar.json with your actual preferences and supported facts.
python3 brief-to-result/scripts/btr.py profiles check .btr/profiles/northstar.json
python3 brief-to-result/scripts/btr.py profiles context .btr/profiles/northstar.json
```

Initialization refuses to overwrite a profile and creates a local ignore file if absent. Files are not encrypted; ignore rules do not protect already-tracked files. Review `git status` before committing. Add `--as-of YYYY-MM-DD` for reproducible date checks or `--strict` to `profiles check` to fail when any fact is excluded. See the [template](brief-to-result/assets/profile.template.json) and [full schema rules](brief-to-result/references/project-profiles.md).

### Preview and apply a scoped repair

The supplied Northstar example is fictional. Create a plan for its first line:

```bash
mkdir -p .btr
python3 brief-to-result/scripts/btr.py repair plan examples/repair-before.txt \
  --allow 1:1 --keep "Try the demo." --output .btr/repair.json
```

Edit only the `replacement` string in `.btr/repair.json`, keeping its trailing `\n`. For example: `Export your report without retyping it.\n`. Then:

```bash
python3 brief-to-result/scripts/btr.py repair preview examples/repair-before.txt --plan .btr/repair.json
python3 brief-to-result/scripts/btr.py repair apply examples/repair-before.txt \
  --plan .btr/repair.json --output .btr/revised.txt
```

Repeat `--allow START:END` for disjoint original line ranges and `--keep` for additional exact wording locks. Preview writes nothing; apply refuses existing destinations. UTF-8 text only, not binary document editing. Plans contain original excerpts, so handle them as confidentially as the source. Scope fields are a reviewable contract, not a security sandbox.

### Existing workflow and text tools

```bash
python3 brief-to-result/scripts/lookup.py --list
python3 brief-to-result/scripts/lookup.py --id W03
python3 brief-to-result/scripts/lookup.py --query "caption"
python3 brief-to-result/scripts/text_metrics.py --help
```

| Category | IDs | Examples |
| --- | --- | --- |
| Writing | W01–W10 | Rewrite, shorten, preserve voice, reply |
| Understanding | U01–U10 | Explain, synthesize, compare, teach |
| Ideation | I01–I10 | Validate, position, prioritize, find blind spots |
| Sales | M01–M10 | Offers, landing pages, objections |
| Content | C01–C10 | Posts, scripts, carousels |
| Product | P01–P10 | PRDs, flows, permissions, criteria |
| Technical | T01–T10 | Debug, review, integrate, release |
| Operations | O01–O10 | SOPs, decisions, support, updates |

Each workflow contains a trigger, input, method, output, checks, and example. English documentation does not imply US-only conventions, currency, or audience.

## Tests and limits

```bash
python3 -m unittest discover -s tests -v
```

Automated tests cover standalone short-name packaging, local helpers, error paths, freshness rules, text boundaries, catalog integrity, and local documentation links. [Manual acceptance examples](examples/README.md) cover the three packs, language precedence, and targeted revisions. These examples are not published model benchmark results. Passing local tests does not establish equivalent behavior across all agents, factual truth, or improved sales/content performance.

Helper exit codes: `0` success, `1` excluded facts under a strict profile check, `2` invalid input or write failure. The existing `text_metrics.py` uses `1` for a failed length check. Source changes since a repair plan was created require a new plan; the original is never overwritten.

## License and changes

[MIT](LICENSE), copyright (c) 2026 makanSukros. A [license copy](brief-to-result/LICENSE) travels with standalone skill installations. See [CHANGELOG.md](CHANGELOG.md) for source-version changes.

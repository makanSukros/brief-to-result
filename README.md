# Brief to Result

**Less prompting. More finished work.**

[English](README.md) | [Bahasa Indonesia](README.id.md) · [MIT License](LICENSE)

An English-first, globally adaptable agent skill: **80 focused workflows, three Outcome Packs, optional Project Profiles, and scoped Repair Mode**. Ask for an outcome, reuse the context you choose, and improve only what needs changing.

> Executes the requested work by default. It writes a prompt only when you ask for one. Preparing content never implies permission to publish it.

## Start with a real task

Once the skill is installed, ask your agent:

```text
Use Brief to Result: Launch Kit.
Turn these release notes into one customer email and two social posts.
Use only supplied facts. Prepare drafts; do not publish.
```

```text
Use Brief to Result with the project profile .btr/profiles/northstar.json.
Turn this feature idea into requirements, user flows, acceptance criteria,
and dependency-ordered tasks. Flag unresolved decisions. Do not code yet.
```

```text
Use Brief to Result: Repair Mode.
Only rewrite the opening paragraph. Keep every product fact, the remaining
paragraphs, and the CTA unchanged. Return the full revised draft.
```

In clients that support it, you can invoke `$brief-to-result`. Invocation and installation conventions vary by agent; this repository does not certify every client.

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

Clone the repository and copy the **entire** inner `brief-to-result/` directory into your agent's supported skill directory. Do not copy `SKILL.md` alone.

```bash
git clone https://github.com/makanSukros/brief-to-result.git
cd brief-to-result
```

For a first installation in an agent that supports `~/.agents/skills/`:

```bash
mkdir -p ~/.agents/skills
cp -R brief-to-result ~/.agents/skills/
```

Use your client's documented directory if different. If already installed, review/back up the existing skill before replacing it; do not blindly merge old and new versions. Keep project profiles outside the installed skill directory so replacing the skill does not replace your project data.

The Markdown workflows can be followed without Python. The new `btr.py` helper requires **Python 3.10+**, uses only the standard library, and makes no network/model calls. You still need a compatible host agent and its own model access; this is not a standalone chatbot or background automation service.

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

Automated tests cover local helpers, error paths, freshness rules, text boundaries, catalog integrity, and local documentation links. [Manual acceptance examples](examples/README.md) cover the three packs, language precedence, and targeted revisions. These examples are not published model benchmark results. Passing local tests does not establish equivalent behavior across all agents, factual truth, or improved sales/content performance.

Helper exit codes: `0` success, `1` excluded facts under a strict profile check, `2` invalid input or write failure. The existing `text_metrics.py` uses `1` for a failed length check. Source changes since a repair plan was created require a new plan; the original is never overwritten.

## License and changes

[MIT](LICENSE), copyright (c) 2026 makanSukros. A [license copy](brief-to-result/LICENSE) travels with standalone skill installations. See [CHANGELOG.md](CHANGELOG.md) for source-version changes.

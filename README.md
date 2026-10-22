# Brief to Result

**Less prompting. More finished work.**

[English](README.md) | [Bahasa Indonesia](README.id.md) · [MIT License](LICENSE)

**Turn an everyday request into something useful:** product-specific affiliate hooks, sales copy, customer replies, content drafts, meeting actions, learning exercises, or a feature brief your team can work from.

BTR is a reusable skill for a compatible AI agent, not a separate chatbot or a new model. It combines **80 workflows, Hook Lab with 24 creative formulas, three Outcome Packs, optional Project Profiles, Repair Mode, and adaptive dialogue**. Describe your task normally. You do not need to learn feature names or workflow IDs.

[How to use it](#quick-start) · [Interactive conversations](#dialogue) · [Examples by role](#use-cases) · [Features](#features) · [Installation](#installation) · [Tests](#tests)

## Purpose and benefits

The goal is to reduce the work between **“help me with this”** and a usable result. BTR guides the agent to understand the relevant context, ask about consequential gaps, preserve facts and constraints, and deliver the work rather than a longer prompt. It can reuse an explicitly selected project profile, coordinate related drafts, and revise only the part you want changed.

It does not add browsing, file access, image generation, persistent memory, or publishing permissions. Those depend on the host. Important facts and commitments still need review; these methods do not guarantee perfect answers, virality, sales, or measured time savings.

<a id="quick-start"></a>
## Just mention @btr

After installing and selecting the skill in a compatible host:

```text
@btr write 12 affiliate hooks for this product. Make the angles genuinely different.
```

```text
Help me reply to this customer calmly and clearly @btr.
```

```text
@btr only improve the opening. Keep the rest exactly as it is.
```

Paste or attach the relevant material. BTR should use context already available rather than ask you to repeat it. With no identifiable task, it asks a short question. Use `@btr menu` only when you want a menu.

**A mention is not an installer.** Native skill selection belongs to the host application. Dollar-prefixed clients use `$btr`; existing long-name installations use `$brief-to-result`. See the [invocation guide](brief-to-result/references/invocation.md). Preparing a draft does not authorize sending or publishing it.

<a id="dialogue"></a>
## Interactive when it helps, direct when it does not

BTR now treats conversation as part of the work, not a mandatory questionnaire. It checks whether a missing answer would actually change the output before interrupting you.

| Situation | Intended behavior |
| --- | --- |
| The task and material are clear. | Deliver immediately. |
| An attachment or earlier answer contains the missing information. | Read or reuse it before asking. |
| A decision changes the approach. | Ask one focused question and explain the consequence when helpful. |
| A request depends on an unsupported claim. | Flag the assumption and use a truthful alternative where possible. |
| You say “I don't know.” | Offer a reversible recommendation or two concrete directions. |
| You correct an earlier answer. | Use the correction without restarting the intake. |
| You say “just draft, no more questions.” | Stop optional questions; do not invent essential facts. |
| Enough context is available. | Stop interviewing and produce the work. |

**Example: adapting a product-video concept.** This is an illustration, not an independent model benchmark.

> **You:** Help me plan a cable-clip video around the visual material I can use. I haven't described the assets yet.
>
> **BTR:** Do you have actual demo footage, or only product photos? That changes whether the opening can promise a visible test.
>
> **You:** Only photos.
>
> **BTR:** Use a photo-led opening, not a fake test. On-screen line: “Where did the cable go this time?” Follow with the product photo and its actual cable-holding function.

For a simple text-only hook request with the product function already known, BTR should **skip the footage question** and write the hooks. A useful question is not a compulsory field.

You can say `@btr help me think this through`, `@btr challenge the assumptions`, or `@btr just draft with what we know`. These are natural requests, not new commands. Guided conversations should produce a tangible draft or synthesis after two question rounds by default, unless you explicitly want a longer interview. A missing source can still block an honest answer. See the [adaptive dialogue contract](brief-to-result/references/adaptive-dialogue.md) and [test evidence and limits](evals/README.md).

<a id="use-cases"></a>
## Find examples for your work

Choose a category and copy a request. Supply the material it refers to; follow-ups use the context already in the conversation. These categories are not modes you must configure.

| You are… | Start here | Typical output |
| --- | --- | --- |
| An affiliate creator | [Affiliates](#affiliates) | Hooks, demo concepts, opening revisions |
| A seller or small-business owner | [Sellers](#sellers) | Product copy, objection replies, launch drafts |
| A creator or social media manager | [Creators](#creators) | Posts, carousels, repurposed content |
| A marketer or copywriter | [Marketing](#marketing) | Angles, landing-page copy, A/B plans |
| A freelancer or agency | [Freelancers](#freelancers) | Proposals, scope replies, revisions |
| A support or admin professional | [Support](#support) | Replies, FAQs, escalation notes |
| A professional or team lead | [Teams](#teams) | Meeting actions, priorities, SOPs |
| A student or educator | [Learning](#learning) | Explanations, exercises, lesson plans |
| A founder, product manager, or developer | [Product](#product) | Validation, requirements, debugging |
| Someone handling personal tasks | [Everyday life](#everyday) | Messages, plans, comparisons |

<a id="affiliates"></a>
### Examples for affiliate creators

**Use it for:** product-specific selling angles, hooks, video concepts, and targeted revisions. **Useful input:** the real product function, audience, available visuals, current offer, and your actual experience when relevant. You do not need every detail to start.

```text
@btr write 12 affiliate hooks for a desk cable clip that holds a cable end
at the edge of a desk. Target people working at desks. Use conversational
English and a little humor. Different everyday situations, not synonyms.
No invented price, popularity, or personal review. Hooks only.
```

```text
@btr choose three promising hooks from that batch. For each, write the
opening, first shot, product demo, and one CTA. Aim for about 20 seconds;
timing is an estimate until read aloud. I may earn an affiliate commission,
so include a clear disclosure in the script.
```

```text
@btr these openings still sound generic. Rewrite only the hooks using
more specific daily moments. Keep the product facts, body, and CTA.
Do not turn them into fake testimonials.
```

**Intended result:** distinct reasons to notice the product and a payoff that matches the hook. For a fictional cable-clip example, “This little gadget will change your life” might become **“The desk looks great. Finding the charging cable still involves crawling.”** The next shot must show the real problem and product function.

[Hook Lab](brief-to-result/references/hook-lab.md) uses [24 formulas](brief-to-result/references/hook-formulas.md), not a list of famous lines with the product name replaced. [Examples](brief-to-result/references/hook-examples.md) are illustrations, not conversion evidence.

<a id="sellers"></a>
### Examples for sellers and small businesses

**Use it for:** explaining benefits, handling objections, and consistent launch messages. **Useful input:** product details, actual price and conditions, target buyer, or a customer message.

```text
@btr rewrite this product description for first-time buyers. Explain which
real problem each feature helps with. Preserve specifications, price,
and limitations. Return the description, not writing advice.
```

```text
@btr draft a short, friendly reply to this customer who says it is too
expensive. Use the benefits and terms I supplied. Do not invent a discount
or pressure them to buy.
```

```text
@btr use these confirmed release notes and offer terms to prepare one
customer email, two social posts, and five FAQ answers. Keep all product
facts consistent. Draft only; do not publish.
```

**Intended result:** buyer-oriented copy grounded in the same product facts. A missing policy must not become an invented promise.

<a id="creators"></a>
### Examples for creators and social media managers

**Use it for:** finding an angle and adapting content while preserving your voice. **Useful input:** an article, transcript, draft, notes, or examples of your writing.

```text
@btr turn this article into two short English posts for X. Open with the
most interesting supported point. Keep my conversational voice and the
source's important caveats. Deliver what the hook promises.
```

```text
@btr turn these notes into a six-slide carousel for beginners. Give each
slide one idea, short on-slide copy, and a visual direction. Make the
opening specific, not “Everything you need to know.”
```

```text
@btr use this transcript for one LinkedIn post, one Instagram caption,
and one short-video outline. Keep the facts but change the angle and
structure for each channel. Drafts only, not a posting schedule.
```

**Intended result:** channel-appropriate drafts. A visual direction is not a generated image or a rendered video.

<a id="marketing"></a>
### Examples for marketing and copywriting

**Use it for:** ad angles, clear positioning, and testable creative hypotheses. **Useful input:** audience, offer, product evidence, landing page, and campaign constraints.

```text
@btr develop five ad angles for this offer and audience. Each should address
a different problem, objection, or buying motivation. Give each one a
headline and opening sentence. No unsupported superlatives.
```

```text
@btr rewrite only this landing page's hero section. Make clear who it is
for, what it helps them do, and the next step. Preserve the actual offer
and claims. Give one recommended version.
```

```text
@btr plan an A/B test for these openings. Keep audience, offer, body,
and CTA comparable. Explain the hypothesis, what to measure, and what
the test cannot tell us. Do not predict a winning CTR.
```

**Intended result:** different concepts with a rationale to test, not fabricated performance scores.

<a id="freelancers"></a>
### Examples for freelancers and agencies

**Use it for:** workable scope and professional client communication. **Useful input:** brief, agreed deliverables, fees, timeline, and revision terms.

```text
@btr turn this client brief into a concise proposal: objective,
deliverables, exclusions, dependencies, and open questions. Use only
fees and timelines actually agreed. Mark unresolved details.
```

```text
@btr help me reply to this extra request warmly but firmly. Explain what
is outside the attached scope and what needs agreement before proceeding.
Do not promise free work or invent a fee.
```

```text
@btr apply the client's feedback only to the headline and closing paragraph.
Keep the approved body, product facts, and deliverables unchanged.
Return the revision and a short change summary.
```

**Intended result:** a clearer proposal, reply, or scoped revision. Drafting does not send or accept an agreement.

<a id="support"></a>
### Examples for customer support and admin

**Use it for:** empathetic replies, FAQs, and internal handoffs. **Useful input:** anonymized messages, approved policies, incident facts, and support notes.

```text
@btr draft a calm reply using this complaint and our support policy.
Acknowledge the issue and give the next supported step. Ask only for
necessary information. Do not invent a refund or resolution time.
```

```text
@btr group these anonymized customer questions into an FAQ. Answer using
our supplied documentation. Flag anything it does not answer rather than
filling in policy gaps.
```

```text
@btr turn this thread into an internal handoff: reported problem, evidence,
steps already tried, customer impact, and missing information.
Separate confirmed facts from suspected causes.
```

**Intended result:** reviewable replies and useful internal notes. Remove unnecessary private data; nothing is sent automatically.

<a id="teams"></a>
### Examples for work and team management

**Use it for:** meeting actions, realistic priorities, and repeatable procedures. **Useful input:** notes, deadlines, capacity, and process descriptions.

```text
@btr turn these meeting notes into decisions, tasks, owners, and deadlines.
Mark missing owners or dates as not agreed. Keep open questions separate.
Do not assign commitments absent from the notes.
```

```text
@btr here are my tasks and deadlines. I have six hours this week.
Recommend three priorities, what to defer, and the main tradeoff.
Label estimated effort. Do not change my calendar.
```

```text
@btr turn this process into an SOP for a new team member: when to start,
inputs, steps, exceptions, escalation, and completion criteria.
Flag missing policy decisions.
```

**Intended result:** clear next actions without inventing decisions for other people.

<a id="learning"></a>
### Examples for students and educators

**Use it for:** understanding, practice, and focused teaching plans. **Useful input:** notes, excerpts, learning objectives, level, or your attempted answer.

```text
@btr explain this part of my notes for a beginner. Start with the main idea,
give one concrete example, and address the likely misconception.
Keep the technical details accurate.
```

```text
@btr create five practice questions from these notes, from easy to harder.
Give the questions first and wait for my answers before explaining them.
Label anything outside the notes as extra material.
```

```text
@btr use this material for a 30-minute lesson at the stated learner level.
Include an objective, explanation, activity, and understanding check.
Treat the timing as a plan, not a measured duration.
```

**Intended result:** explanations and learning materials, not invented quotations or sources. An interactive quiz can wait for your answer intentionally.

<a id="product"></a>
### Examples for founders, product teams, and developers

**Use it for:** validating assumptions, specifying behavior, and debugging from evidence. **Useful input:** problem, audience, feature notes, current flows, code, logs, or reproduction steps.

```text
@btr challenge this product idea. Find the three riskiest assumptions,
what evidence would support or reject each, and a small experiment to
run first. Do not treat demand as proven.
```

```text
@btr turn this feature idea into a brief, user flow, acceptance criteria,
edge cases, and dependency-ordered implementation tasks.
Flag unresolved decisions. Do not start coding yet.
```

```text
@btr inspect this error, relevant code, and reproduction steps. Separate
observations from hypotheses. Recommend the smallest useful check and,
when supported, a focused fix and a way to test it.
```

**Intended result:** a validation plan, buildable handoff, or evidence-led diagnosis. A proposed fix is not a tested fix.

<a id="everyday"></a>
### Examples for everyday life

**Use it for:** clear messages and practical plans. **Useful input:** the message, available time, constraints, or options you are comparing.

```text
@btr help me decline this invitation warmly. Keep it short.
Do not invent an excuse or commit me to another date.
```

```text
@btr organize these household tasks into a practical weekend plan.
Use the time and constraints I supplied. Mark estimates and do not
assume someone else agreed to help.
```

```text
@btr compare these options using my priorities. Recommend one,
explain the tradeoff, and say what missing fact could change the choice.
Do not fill unknown prices or specifications with guesses.
```

**Intended result:** a message or plan you can review and use. Small requests do not need a full pack or profile.

<a id="features"></a>
## What's included

| Feature | Purpose | Guide |
| --- | --- | --- |
| Adaptive dialogue | Consequential questions, blindspot checks, answer reuse, and stop conditions | [Dialogue](brief-to-result/references/adaptive-dialogue.md) |
| Hook Lab | Product-specific sales and affiliate openings using 24 creative formulas | [Hook Lab](brief-to-result/references/hook-lab.md) |
| Outcome Packs | Related deliverables using shared source facts | [Packs](brief-to-result/references/outcome-packs.md) |
| Project Profiles | Explicitly selected local preferences and sourced, dated facts | [Profiles](brief-to-result/references/project-profiles.md) |
| Repair Mode | Targeted revision with protected surrounding text | [Repairs](brief-to-result/references/repair-mode.md) |
| 80 workflows | Writing, understanding, ideas, sales, content, product, technical work, operations | [SKILL.md](brief-to-result/SKILL.md) |

The three packs are [Launch Kit](brief-to-result/packs/launch-kit.md), [Idea to Build](brief-to-result/packs/idea-to-build.md), and [Research to Content](brief-to-result/packs/research-to-content.md). Your requested scope overrides their defaults. One email does not become a campaign; a blocked part does not justify inventing its contents.

Profiles are opt-in and local, not hidden cross-chat memory. A `confirmed` label is user-maintained, not independent verification. Stale, unverified, or deprecated facts must not fill gaps in publishable copy. Files are not encrypted and a selected profile is visible to the host model. Never store credentials or private customer records.

Repair Mode distinguishes a proposed change from a completed edit. Its optional UTF-8 text helper checks source hashes and exact wording locks, previews a diff, and writes only to a new file. It does not verify truth or edit binary documents.

English remains the documentation base. Outputs follow requested language and context; existing text retains its language unless translation is requested. English does not imply US currency, locale, or audience.

<a id="installation"></a>
## Installation

The canonical sources are in `brief-to-result/`. The builder creates a complete standalone skill named `btr`, including runtime resources and the MIT license.

```bash
git clone https://github.com/makanSukros/brief-to-result.git
cd brief-to-result
python3 tools/build_btr.py --output dist/btr.zip
```

Import that ZIP through your host's supported skill-upload flow, review it, and enable it. Native `@` or `$` selection depends on the host; GitHub publication does not install it in your account. See [host-specific guidance](brief-to-result/references/invocation.md).

For a first installation in a client supporting `~/.agents/skills/`:

```bash
python3 tools/build_btr.py --directory "$HOME/.agents/skills/btr"
```

The builder refuses existing destinations. Review/back up an older installation before replacing it, keep profiles outside the skill directory, and prefer one active installation. Existing long-name installations remain supported. Do not merely rename the original folder: the directory and frontmatter name must match.

Markdown instructions work without Python. Building the package and using the new helpers requires **Python 3.10+**, only the standard library, and no network or model calls. You still need a compatible host and its own model access. This is not a standalone chatbot or a background service.

<a id="local-tools"></a>
## Optional local tools

Everyday users can ask normally. Run these commands only when useful, from the repository root; substitute your installed path where appropriate.

<details>
<summary><strong>Browse packs and workflows</strong></summary>

```bash
python3 brief-to-result/scripts/btr.py packs list
python3 brief-to-result/scripts/btr.py packs show launch-kit
python3 brief-to-result/scripts/lookup.py --list
python3 brief-to-result/scripts/lookup.py --id W03
python3 brief-to-result/scripts/lookup.py --query "caption"
python3 brief-to-result/scripts/text_metrics.py --help
```

These commands display instructions or measure text, not model-generated deliverables. The 80 workflow IDs remain W01-W10, U01-U10, I01-I10, M01-M10, C01-C10, P01-P10, T01-T10, and O01-O10. The 24 H-series formulas are additional creative recipes, not extra general workflows.

</details>

<details>
<summary><strong>Create and inspect a project profile</strong></summary>

```bash
python3 brief-to-result/scripts/btr.py profiles init northstar
# Edit .btr/profiles/northstar.json with real preferences and supported facts.
python3 brief-to-result/scripts/btr.py profiles check .btr/profiles/northstar.json
python3 brief-to-result/scripts/btr.py profiles context .btr/profiles/northstar.json
```

Initialization refuses overwrite and creates an ignore file if absent. Ignore rules do not protect already-tracked files; review `git status`. Use `--as-of YYYY-MM-DD` for reproducible freshness checks or `--strict` to fail when a fact is excluded. See the [template](brief-to-result/assets/profile.template.json) and [schema](brief-to-result/references/project-profiles.md).

</details>

<details>
<summary><strong>Preview a scoped text repair</strong></summary>

The Northstar example is fictional.

```bash
mkdir -p .btr
python3 brief-to-result/scripts/btr.py repair plan examples/repair-before.txt \
  --allow 1:1 --keep "Try the demo." --output .btr/repair.json
```

Edit only the plan's `replacement` string, retaining its trailing `\n`, for example `Export your report without retyping it.\n`. Then:

```bash
python3 brief-to-result/scripts/btr.py repair preview examples/repair-before.txt --plan .btr/repair.json
python3 brief-to-result/scripts/btr.py repair apply examples/repair-before.txt \
  --plan .btr/repair.json --output .btr/revised.txt
```

Preview writes nothing; apply refuses existing destinations. Repeat `--allow START:END` for disjoint original line ranges and `--keep` for exact wording locks. Plans contain source excerpts: handle them with the source's confidentiality. This is a reviewable scope contract, not a security sandbox.

</details>

<details>
<summary><strong>Inspect a dialogue decision</strong></summary>

```bash
python3 brief-to-result/scripts/dialogue_policy.py --state path/to/approved-local-state.json
```

This optional helper reads explicit structured state and recommends a next action. It does not understand raw conversation, detect blindspots, verify facts, call a model, write files, or grant permissions. Ordinary users do not need to create JSON. See the [state contract](brief-to-result/references/adaptive-dialogue.md).

</details>

<a id="tests"></a>
## Tests and honest limits

```bash
python3 -m unittest discover -s tests -v
```

Tests cover helper behavior, error cases, policy transitions, no-repeat questions, unknown answers, corrections, packaging, catalog integrity, and local links. [Eight saved dialogue walkthroughs](evals/dialogue-walkthroughs.json) include author-generated responses and mechanical checks. They are **author self-review, not isolated host runs or independent model benchmarks**. See the [evaluation record](evals/README.md) for the exact distinction and live-host test procedure.

Passing these checks does not prove equal behavior across agents, semantic accuracy, conversion lift, or genuine persistent memory. Model-level interpretation still matters. Helper exit codes: `0` success, `1` strict profile exclusions or a failed text-length check, `2` invalid input or write failure.

## License and changes

[MIT](LICENSE), copyright (c) 2026 makanSukros. A [license copy](brief-to-result/LICENSE) travels with standalone installations. See [CHANGELOG.md](CHANGELOG.md). Version numbers describe source changes, not necessarily a published GitHub Release or host certification.

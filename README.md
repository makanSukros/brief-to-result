# Brief to Result

**Turn short requests into clear, accurate, usable work.**

Brief to Result is an **English-first, globally adaptable agent skill** that routes short or underspecified requests through **80 practical workflows** across writing, understanding, ideation, sales, content, product/UX, engineering, and operations.

> **Execute by default.** When someone asks you to "improve this", deliver the improved result—not a longer prompt. Create a prompt only when requested.

## What it does

- Turns a brief request into a useful result without unnecessary clarification.
- Selects one primary workflow and optional supporting workflow.
- Preserves source facts, author intent, qualifications, and constraints.
- Produces distinct creative options instead of superficial rewordings.
- Checks length limits and distinguishes assumptions from verified claims.
- Separates proposed work from implementation, testing, and publication.
- Uses English as its documentation and new-content default while respecting other requested languages and locales.

## 80 workflows

| Area | IDs | Common jobs |
| --- | --- | --- |
| Writing & editing | W01–W10 | Rewrite, shorten, preserve voice, reply |
| Understanding | U01–U10 | Explain, synthesize, compare, teach |
| Ideation & strategy | I01–I10 | Generate ideas, validate, prioritize, find blind spots |
| Sales & persuasion | M01–M10 | Landing pages, offers, objection handling |
| Content & storytelling | C01–C10 | Social posts, video scripts, carousels |
| Product & UX | P01–P10 | PRDs, user flows, navigation, acceptance criteria |
| Technical work | T01–T10 | Debugging, code review, integrations, release readiness |
| Operations & decisions | O01–O10 | SOPs, prioritization, support, updates |

Each workflow has a **trigger, input, method, output, quality checks, and example**.

## Installation

The complete skill is in [`brief-to-result/`](brief-to-result/), with its entry point at [`brief-to-result/SKILL.md`](brief-to-result/SKILL.md).

Copy the **entire** `brief-to-result/` folder into your AI agent's supported skills directory and follow that agent's instructions for activating local skills. Do not copy `SKILL.md` alone—the supporting reference files matter.

For agents that support local discovery under `~/.agents/skills/`:

```bash
git clone https://github.com/makanSukros/brief-to-result.git
mkdir -p ~/.agents/skills
cp -R brief-to-result/brief-to-result ~/.agents/skills/
```

The example is only for compatible agents. Other clients have different skill directories and invocation conventions.

## Example requests

```text
Use Brief to Result to improve this message for an international audience.
Preserve its meaning and give me one ready-to-send version.
```

```text
Use Brief to Result to generate 10 genuinely different onboarding ideas
for a B2B product. Recommend the top three with clear tradeoffs.
```

```text
Use Brief to Result to turn this feature brief into acceptance criteria,
edge cases, and a reasonable release scope.
```

```text
Use Brief to Result to create a reusable prompt for converting technical
release notes into concise social content. Do not write the posts yet.
```

## Working modes

- **Execute** (default): produce the requested deliverable.
- **Create a prompt**: return a reusable template when explicitly requested.
- **Audit**: inspect weaknesses, evidence, and actionable improvements.
- **Menu**: show relevant workflows when asked.

## Included tools

```bash
python3 brief-to-result/scripts/lookup.py --list
python3 brief-to-result/scripts/lookup.py --query "caption"
python3 brief-to-result/scripts/lookup.py --id W03
python3 brief-to-result/scripts/text_metrics.py --help
```

These helper scripts use the Python standard library.

## Project layout

```text
brief-to-result/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── writing.md
│   ├── understanding.md
│   ├── ideation.md
│   ├── sales.md
│   ├── content.md
│   ├── product.md
│   ├── technical.md
│   ├── operations.md
│   ├── combinations.md
│   └── preferences.md
└── scripts/
    ├── lookup.py
    └── text_metrics.py
```

## Language and safety

English is the base language for documentation and newly created content, **not** an assumption about a user's country. Preserve the language of existing text unless the user asks to translate it. Never invent facts, prices, testimonials, sources, implementation status, or verification results. Always follow the host agent's permissions and safety boundaries.

## License

**No open-source license has been selected yet.** Publishing source code publicly does not itself grant permission to copy, modify, or redistribute it. The repository owner can add a LICENSE file after selecting the intended terms.

# Useful Workflow Combinations

Choose combinations by the requested deliverable. Apply supporting checks internally and show only the result and explanation the user needs.

| Request | Workflows | Expected result |
| --- | --- | --- |
| "Shorten this caption to 300 characters without weakening it" | C01 + W03 | One caption within the explicit limit, preserving facts and the call to action |
| "Turn this article into a short social thread" | C02 + U04 | Separate posts in the requested language and length, with supported claims |
| "Make this offer more convincing" | M01 + M03 | Copy that addresses the main objection using available evidence |
| "Challenge this product idea and find what I missed" | I10 + P01 | Prioritized risks and assumptions, followed by an actionable feature direction |
| "Review how shared contacts and lists fit across messaging and email" | P04 + P05 | Information architecture, shared data ownership, entry and return paths, and relevant states |
| "Explain this bug to a nontechnical customer" | O08 + T02 | A clear response grounded in observed symptoms, safe next checks, and only necessary evidence requests |
| "Turn these release notes into a community announcement" | O09 + W07 | Copy-ready changes, user impact, availability limits, and next actions |
| "Create a motion ad from this concept" | C08 + M01 | A focused concept and script, followed by media production with available tools when requested |

## Constraints that are easy to miss

- "Three versions" means different approaches, not synonym substitutions. If the user asks for one version, return one.
- "50% shorter" targets roughly half the source length, not half its facts. Measure the relevant unit and flag conflicts with required content.
- "Beginner-friendly" requires concrete examples and explained terms while preserving technical accuracy.
- "Ready for a coding agent" requires clear behavior, data contracts, acceptance criteria, dependencies, and open decisions. It does not establish that implementation already exists.
- "Create the image or preview" requires a real artifact. Use suitable tools and report actual generation or rendering blockers.
- "Give me more" requires useful differences in concepts or mechanisms. Do not split one idea into several titles to fill a quota.
- "Global audience" requires checking locale assumptions as well as language. English copy alone does not justify assuming a country, currency, time zone, or cultural reference.
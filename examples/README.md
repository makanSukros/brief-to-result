# Worked examples and manual acceptance checks

All Northstar product details here are fictional. Do not reuse them as facts about a real product. These are reproducible prompts and expected behavior, **not measured model benchmark results**.

## Launch Kit

Input:

```text
Use Brief to Result: Launch Kit.
Fictional example: Northstar now exports reports as CSV, on desktop only.
Existing customers can use it from Reports > Export. No date or price is supplied.
Write one email and two short social posts. Keep the desktop-only qualifier.
```

Expected: one email and two distinct posts, consistent CSV/desktop availability, and a CTA to Reports > Export. No invented pricing, URL, release date, or quantified time saving. The explicit output count overrides the full default pack.

## Idea to Build

Input:

```text
Use Brief to Result: Idea to Build.
We need saved report views shared within one workspace. Only workspace members
may read shared views; only the creator may edit them. Do not choose a stack.
```

Expected: requirements with IDs, flow/error states, cross-workspace denial criteria, dependency-ordered tasks with matching requirement/acceptance IDs, and open decisions such as deletion/ownership transfer. No claim that implementation or tests already exist.

## Research to Content

Input:

```text
Use Brief to Result: Research to Content.
Source A (provided synthetic survey): 20 of 50 respondents preferred CSV.
Source B (provided synthetic interviews): 3 participants requested PDF.
Suggest three angles and draft one neutral post. Do not generalize to all users.
```

Expected: distinguish the survey sample from interviews; do not combine the denominators or infer market-wide preference. Attribute to the supplied synthetic sources, not fabricated URLs. One draft and three angles.

## Project Profile precedence and freshness

Create a profile with language `en`, then explicitly ask for a new announcement in Indonesian. Expected: Indonesian. Edit an existing Spanish draft without requesting translation. Expected: Spanish, not the profile default. Add an expired confirmed fact and an unverified price. Expected: both excluded from publishable copy, without claiming the helper verified other claims.

## Repair Mode

Use [repair-before.txt](repair-before.txt). Replace only line 1 with `Export your report without retyping it.`, retaining the line break. Keep the final two lines byte-for-byte. The CTA is `Try the demo.`. This example's benefit is fictional, not a real product claim.

Create a plan, edit only `replacement`, preview it, and apply to a new output file. Changing the source after planning must fail. Asking to preserve all wording while also making it half as long should surface a conflict, not a false claim of success.

## Testing boundaries

Run `python3 -m unittest discover -s tests -v` from the repository root for deterministic helper, catalog, and packaging checks. Run these manual cases in each target agent separately. Passing Python tests does not prove equivalent behavior across agents or better model output.

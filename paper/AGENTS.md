# AGENTS.md

## Scope
This directory contains the LaTeX manuscript, paper-specific assets, and template/sample workflow artifacts used to bootstrap manuscript drafting.

## Primary goals
- Improve the manuscript for clarity, accuracy, and submission readiness.
- Keep all empirical claims aligned with repository evidence.
- Preserve LaTeX correctness and conference template integrity.

## Evidence sources
When editing the manuscript, use the following as the main sources of truth:
- `../runs/` for experiment outputs and logs
- `../outputs/` for generated artifacts and result summaries
- `../docs/PROJECT_PLAN.md` for project intent and study boundaries
- `../docs/research_context.md` for research framing
- `../docs/current_status.md` for current repository state

If evidence for a claim is missing or ambiguous, insert a TODO or suggest a conservative rewrite instead of guessing.

## Writing policy
- Never invent metrics, baselines, ablations, datasets, citations, or conclusions.
- Preserve citation keys, labels, references, and LaTeX commands unless explicitly asked to change them.
- Preserve the conference style files and overall manuscript structure unless a structural change is requested.
- Prefer precise, conservative scientific writing over promotional language.
- Keep claims proportional to the available evidence.

## Style adaptation
When revising English prose, consult the sample prior-paper style template if available.
Recommended location:
- `style/prior_paper_style.md`

Use that file only for:
- tone
- phrasing preferences
- paragraph rhythm
- level of claim conservativeness

Do not copy text, citations, technical claims, or structure from prior papers or template artifacts.

## Terminology preference
If the manuscript has project-specific terminology preferences, keep them in a separate project-local glossary or terminology note.

When revising prose:
- prefer the terminology defined by the manuscript glossary or project context
- preserve original terminology inside paper titles, dataset names, and cited claims when needed
- keep terminology consistent within a paragraph and section
- avoid awkward replacements that would make a sentence less precise or alter an official name or proper noun

## Skill routing for manuscript work
For paper tasks, prefer the most specific relevant skill instead of generic writing behavior.

Use these defaults under `../.agents/skills/`:
- For literature review planning, synthesis, and citation-aware structure: prefer `citation-management`, `scientific-critical-thinking`, and `scientific-writing`.
- For evidence checking of manuscript claims: prefer `claim-auditor`.
- For rewriting prose to match the project’s established voice: prefer `prior-style-adapter`.
- For draft result tables and placeholder result sections before final metrics exist: prefer `results-scaffold`.
- For reviewer-style critique of clarity, weaknesses, and framing: prefer `peer-review`.

When multiple skills are relevant, use them in this order:
1. claim correctness and scope
2. structure and reasoning
3. style adaptation
4. citation cleanup

Do not invoke unrelated skills by default.
Repository evidence and manuscript-specific rules in this file take priority over generic skill behavior.

## Literature review workflow
For Related Work, literature surveys, citation discovery, and paper grouping tasks, prefer using the installed `literature-review` skill before drafting prose.

Expected workflow for literature-review tasks:
1. search for relevant papers beyond the current `.bib` when needed,
2. identify the most relevant papers for the specific subsection or paragraph goal,
3. group them by theme, method family, dataset setting, or failure mode,
4. propose where each citation belongs,
5. only then draft outline or prose.

Do not restrict literature-review tasks to citations already present in the manuscript or bibliography unless explicitly asked.

When external search is used:
- prioritize peer-reviewed or highly credible sources,
- prefer papers directly relevant to the project scope,
- avoid padding the section with weakly related citations,
- clearly distinguish repository citations from newly identified references.

For Related Work drafting, prefer this skill order:
1. `literature-review` for discovery and grouping
2. `scientific-critical-thinking` for gap analysis and positioning
3. `citation-management` for citation hygiene and consistency
4. `scientific-writing` or `prior-style-adapter` for final prose drafting

If writing prose for Related Work, do not begin drafting until the literature groups and citation plan are established.

## Working style
- Before major edits, briefly explain the plan.
- Prefer small, reviewable edits.
- Report which manuscript files changed.
- Flag unsupported or weakly supported claims explicitly.
- For literature-review and related-work tasks, do not assume the current bibliography is complete; search for missing but relevant papers when needed.

## Build
Use the local LaTeX workflow for validation:
- `latexmk -pdf paper.tex`

If the main file changes, detect and use the correct manuscript entry file.

## Boundaries
- Do not edit code, training, or evaluation logic outside `paper/` unless explicitly asked.
- Do not change reported results unless the corresponding evidence exists in the repository.
- Do not broaden the paper’s scope implicitly.

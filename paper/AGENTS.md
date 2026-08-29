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

## Canonical manuscript workflow

Route durable manuscript orchestration to `../.agents/guidance/manuscript-writing.md`.

- Use writing slices rather than section-only drafting.
- Stage semantic or scientific-risk changes in `paper/draft/`; risk, not edit size, controls staging.
- Treat ambiguous classification as fail-closed and handle it as a normal writing slice.
- Keep candidate and resolved drafts provisional; do not automatically copy or merge them into the main manuscript.
- Resolve the protected integration target through `../docs/project_profile.md` → `main_manuscript_path`.
  A valid configured project-relative path is the target; `UNASSIGNED` or a missing/invalid value is
  unresolved, while `NOT_APPLICABLE` means protected integration does not apply under normal project
  configuration. An explicit current human instruction may provide a task-scoped target without changing
  the permanent profile.
- A configured manuscript path is not write permission; the normal role and human-authorization
  integration gate remains required.
- `research_lead` determines scientific readiness; `human_researcher` authorizes integration; `integration_agent` performs the separate protected integration.
- When used, `independent_reviewer` remains strictly read-only.
- Candidate writer(s) are bounded prose executors, not scientific authorities; one final prose owner normally produces the resolved slice.
- For substantive semantic drafting, read `../docs/agent/agent_role_profile.md`; project-local `candidate_writers_required`, `candidate_independence_required`, and `candidate_cross_visibility_before_comparison` control candidate production.
- Template projects may initialize with two candidate slots, but project-local configuration controls the actual count. Do not silently reduce the configured count; an explicit `human_researcher` slice override may temporarily do so, while all candidates remain provisional prose executors and one final prose owner resolves the slice.
- Evidence and citation checks remain mandatory.
- Revalidate changeable evidence before integrating a previously accepted slice.

## Style adaptation
When revising English prose, consult the sample prior-paper style template if available.
Recommended location:
- `style/prior_paper_style.md`

Use that file only for:
- tone
- phrasing preferences
- paragraph rhythm
- stylistic expression of evidence-calibrated hedging already authorized by the scientific brief

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
- For optional bounded naturalness refinement after scientific and style resolution: use `academic-humanizer`.
- For optional read-only inspection of invisible Unicode or text-transfer artifacts: use `watermark-hygiene`.
- For draft result tables and placeholder result sections before final metrics exist: prefer `results-scaffold`.
- For reviewer-style critique of clarity, weaknesses, and framing: prefer `peer-review`.

When multiple skills are relevant, use them in this order:
1. claim correctness and scope
2. structure and reasoning
3. style adaptation
4. optional academic naturalness refinement
5. citation cleanup

For material prose transformations, preserve the pre-transformation text and route the post-transformation slice through differential claim/evidence validation. `watermark-hygiene` remains optional inspection outside this prose-refinement chain.

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

Use the local LaTeX workflow for validation only after resolving the manuscript entry target through
`../docs/project_profile.md` → `main_manuscript_path` or an explicit current human task-scoped target.

If build inspection suggests that the configured entry file is stale or incorrect, treat that as a
configuration inconsistency. Do not silently replace the protected target by auto-detecting another
manuscript file. Resolve the target explicitly before protected integration or authoritative manuscript
validation.

## Boundaries
- Do not edit code, training, or evaluation logic outside `paper/` unless explicitly asked.
- Do not change reported results unless the corresponding evidence exists in the repository.
- Do not broaden the paper’s scope implicitly.

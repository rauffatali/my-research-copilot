# Artifact Naming Conventions

This note defines the default naming pattern for workflow artifacts in the skeleton.

## Core rules

- Use lowercase `snake_case`.
- Prefer short, descriptive names over vague names.
- Keep one concern per file.
- Use stable names for canonical templates.
- Use suffixes for variants instead of overwriting meaning.
- Avoid spaces, CamelCase, and random abbreviations.

## Common suffixes

- `_draft` for in-progress text
- `_final` for the approved version
- `_frozen` for a locked phase artifact
- `_review` for review output
- `_notes` for supporting reasoning
- `_v2`, `_v3` for successive revisions when history matters

## Directory patterns

### `docs/agent/`

Use canonical phase templates for the main workflow artifacts:

- `research_direction.md`
- `brainstorming_brief.md`
- `hypotheses.md`
- `novelty_risk_matrix.md`
- `project_plan.md`
- `implementation_notes.md`
- `result_interpretation.md`
- `claim_ledger.md`

When there are multiple rounds or variants, add a suffix that makes the difference obvious, such as `research_direction_draft.md` or `claim_ledger_round_2.md`.

Workflow guidance files such as the canonical example workflow live under
`.agents/skills/workflow-manager/references/`, not in `docs/agent/`.

### `paper/agent/`

Use the same naming style for manuscript-support artifacts:

- `claim_support.md`
- `section_notes.md`
- `style_notes.md`
- `review_method.md`
- `review_context.md`
- `review_domain.md`
- `review_hybrid.md`
- `review_meta.md`
- `revision_plan.md`
- `response_to_reviewers_draft.md`
- `claim_audit.md`
- `review_context.md`
- `review_notes.md`

Use round or version suffixes when the artifact is iterative.

### `sources/`

Use source-specific names that identify what was saved and where it came from.

Good examples:

- `arxiv_topic_summary.md`
- `benchmark_name_notes.md`
- `dataset_name_page.md`
- `paper_title_metadata.md`

If a source is revised, keep the source identity in the name and add a version or date suffix.

### `runs/` and `outputs/`

Use run IDs or experiment slugs in the directory or file name.

Good examples:

- `runs/2026-05-24_baseline/`
- `outputs/ablation_attention_dropout/`
- `outputs/results_seed_01.md`

Prefer a stable run identifier over a generic label like `latest` or `test`.

## Avoid

- `notes.md`
- `temp.md`
- `final.md`
- `new.md`
- `stuff.md`
- `misc.md`

If a file name does not explain its role, rename it before treating it as durable workflow memory.

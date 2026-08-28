# Figure Support

This file records the evidence, intent, references, specification, style plan, and critique history for manuscript figures.

Use it for methodology diagrams, architecture figures, workflow schematics, technical graphical abstracts, and other evidence-sensitive scientific visuals.

For any figure that supports a research claim, record the relevant claim IDs, durable evidence sources, verification, and scope and limitations. This file records the figure's support package; final claim status remains in `docs/agent/claim_ledger.md`, and post-aggregation figure safety is reviewed in `docs/agent/figure_review.md`.

## Suggested fields

- `figure_id`
- `target_file`
- `source_context`
- `communicative_intent`
- `figure_type`
- `evidence_sources`
- `claim_ids`
- `verification`
- `scope_and_limitations`
- `reference_examples`
- `diagram_spec_path_or_summary`
- `style_plan`
- `generation_method`
- `candidate_paths`
- `critic_notes`
- `final_decision`
- `status`

## Suggested statuses

- `brief`
- `specified`
- `candidate_generated`
- `needs_revision`
- `approved`
- `superseded`

## Figure workflow

1. Define the figure brief from manuscript text, method notes, outputs, or explicit user instruction.
2. Retrieve or list relevant reference examples and explain why they are useful.
3. Write a diagram specification before generation.
4. Write a style plan for palette, typography, arrows, layout, and density.
5. Generate one or more candidates using the safest appropriate method.
6. Critique candidates for faithfulness, conciseness, readability, aesthetics, and caption alignment.
7. Iterate only when the critique identifies a concrete fix.
8. Record the final decision and the remaining uncertainty.

## Suggested table

| Figure ID | Type | Evidence sources | Claim IDs | Verification | Scope And Limitations | Candidate | Critic status | Final decision |
|---|---|---|---|---|---|---|---|---|
| fig_01 |  |  |  |  |  |  |  |  |

## Usage notes

- Treat source context and communicative intent as required inputs for non-trivial scientific figures.
- Link each claim ID to the durable evidence that the figure visualizes or summarizes.
- State how the source outputs, calculations, diagram specification, and caption were verified.
- Record what the figure supports and what it does not establish.
- For plots, prefer code-generated figures from real `runs/` or `outputs/` data.
- For raster rendering of technical diagrams, lock the diagram specification first.
- Do not use generated visual polish to hide unsupported scientific content.

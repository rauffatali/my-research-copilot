# Figure Review

This file records Phase 3 figure checks after outputs have been aggregated.

Use it to keep plotting quality, caption alignment, and visual evidence review separate from the main result interpretation.

## Suggested fields

- `figure_id`
- `source_outputs`
- `figure_path`
- `caption`
- `what_the_figure_shows`
- `alignment_issue`
- `visual_issue`
- `recommended_fix`
- `status`

## Suggested statuses

- `draft`
- `checked`
- `needs_fix`
- `superseded`

## Figure and Table Evidence Rule

Every figure or table used for a research claim must link to:

- source run(s);
- output file(s);
- result card(s);
- claim ID(s), if the figure supports a claim.

A figure or table should be marked unsafe if:

- it cannot be traced to runs or outputs;
- the metric calculation is unclear;
- the baseline comparison is invalid or unknown;
- the axis/label/caption overstates the evidence;
- cherry-picked examples are presented as representative;
- uncertainty or seed variance is hidden when it matters.

Use `docs/agent/result_cards/` and `docs/agent/result_to_claim_map.md` to decide what the figure or table is allowed to claim.

## Suggested table

| Figure/Table ID | Source outputs | Result card | Claim IDs | Status | Required fix |
|---|---|---|---|---|---|
| FIG-001 | | RES-001 | CL-001 | safe / needs_fix / unsafe | |

## Usage notes

- Use this after result aggregation and before manuscript drafting.
- Keep figure captions and figure content synchronized.
- Record duplicated panels, missing labels, misleading axes, or unclear legends.
- Link to the underlying outputs and plot files instead of copying the full analysis here.

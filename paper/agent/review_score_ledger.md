# Review Score Ledger

This file records structured review scoring for Phase 5.

Use it to keep reviewer judgments comparable across rounds and across reviewer roles.

## Suggested fields

- `round`
- `reviewer_role`
- `paper_section_or_claim`
- `soundness_score`
- `presentation_score`
- `contribution_score`
- `overall_score`
- `confidence`
- `accept_or_reject`
- `main_strengths`
- `main_weaknesses`
- `must_fix`
- `optional`

## Suggested scale

- Use the same score scale for every reviewer role.
- Keep the scale explicit in the review files or in the review prompt.
- Record whether the score is from a single review or a meta-review.

## Suggested table

| Round | Role | Soundness | Presentation | Contribution | Overall | Decision | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | Method Reviewer |  |  |  |  |  |  |

## Usage notes

- Pair scores with short rationale rather than raw numbers alone.
- Keep the per-role reviewer files and the meta-review consistent with this ledger.
- Use the ledger to summarize acceptance likelihood, not to replace the qualitative review.

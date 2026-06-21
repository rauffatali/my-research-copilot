# Claim Ledger

## Claim Support Status Values

Use the same support-status vocabulary as the claim-auditor skill.

Allowed values:

- `supported`
- `partially_supported`
- `preliminary`
- `hypothesis`
- `needs_citation`
- `wrong_citation`
- `unsupported`
- `contradicted`
- `out_of_scope`
- `needs_manual_check`

## Status Meanings

| Status | Meaning |
|---|---|
| `supported` | Durable evidence directly supports the claim. |
| `partially_supported` | Some evidence supports the claim, but scope, strength, or wording must be narrowed. |
| `preliminary` | Early evidence exists, but it is not strong enough for a final manuscript claim. |
| `hypothesis` | The claim is a proposed idea or expectation, not yet evidence-backed. |
| `needs_citation` | The claim may be true, but requires source support. |
| `wrong_citation` | The attached citation does not support the claim or supports a different claim. |
| `unsupported` | No adequate evidence currently supports the claim. |
| `contradicted` | Available evidence conflicts with the claim. |
| `out_of_scope` | The claim is beyond what the project studies or can responsibly assert. |
| `needs_manual_check` | The claim requires human or domain-expert verification. |

## Claim Ledger Rule

Do not invent new support-status labels.

Do not use vague labels such as:

- `ok`
- `valid`
- `maybe`
- `good`
- `weak`
- `done`
- `verified`
- `unclear`

Map them to the allowed support-status values instead.

A claim can be marked `supported` only when the supporting result cards, citations, source artifacts, or other durable evidence are listed.

A claim should be marked `preliminary`, `partially_supported`, `needs_citation`, or `needs_manual_check` when evidence exists but is incomplete, indirect, or not yet audited.

## Canonical Claim Status Rule

`docs/agent/claim_ledger.md` is the source of truth for final claim support status.

All claim-related artifacts must use the same support-status vocabulary:

- `supported`
- `partially_supported`
- `preliminary`
- `hypothesis`
- `needs_citation`
- `wrong_citation`
- `unsupported`
- `contradicted`
- `out_of_scope`
- `needs_manual_check`

Do not invent local support labels.

Keep support statuses separate from decisions, next actions, and rewrite instructions.

## Relationship to Result Evidence

Claims should be updated from interpreted evidence, not from raw metrics alone.

Preferred evidence chain:

`docs/agent/result_cards/` -> `docs/agent/result_to_claim_map.md` -> `docs/agent/claim_ledger.md`

A claim can be marked `supported` only when the supporting result cards, citations, or other durable evidence are listed.

Do not mark a claim as supported only because a run completed.

## Ledger Status

* Status: `draft`
* Allowed values: `draft`, `frozen`, `superseded`
* Project claims recorded: `no`
* Claim count: 0

## Claim Table

No project-specific claims have been recorded yet.

| Claim ID | Claim | Claim Type | Location | Evidence | Support Status | Missing Evidence | Risk | Decision | Allowed Wording |
| -------- | ----- | ---------- | -------- | -------- | -------------- | ---------------- | ---- | -------- | --------------- |

## Decision Values

Use decision values separately from support-status values.

Suggested decision values:

* `use`
* `narrow`
* `rewrite`
* `move_to_limitation`
* `remove`
* `needs_more_evidence`
* `needs_manual_check`
* `defer`

## Notes

* This ledger is initialized as a template/default artifact.
* Do not add placeholder claims.
* Add real claims only after they appear in a research artifact, result interpretation, manuscript draft, review finding, or source-backed claim discussion.

## Next Step

* Add the first real claim when Phase 3 result interpretation, Phase 4 writing, or Phase 5 review produces a claim that needs tracking.


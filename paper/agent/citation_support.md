# Citation Support

This file tracks citation justification for Phase 4 drafting.

Use it to keep each important claim, the citation(s) attached to it, and the reason for including them together in one reviewable place.

This is a citation-level evidence record, not the source of truth for final claim support. The final claim status remains in `docs/agent/claim_ledger.md`, while this file records whether a cited source supports the exact claim and within what scope.

## Suggested fields

- `claim_id`
- `claim_text`
- `section`
- `citation_key_or_source`
- `source_artifact_and_location`
- `evidence_state`
- `what_the_citation_supports`
- `support_strength`
- `verification`
- `scope_and_limitations`
- `replacement_or_note`
- `status`

## Suggested statuses

- `draft`
- `checked`
- `needs_better_support`
- `superseded`

These statuses describe the citation record only. They are not claim support statuses; use the canonical vocabulary in `docs/agent/claim_ledger.md` for the final claim decision.

## Evidence State

Optionally record `Evidence State` for manuscript claimability using the canonical `evidence_state` vocabulary from `.agents/workflow/policies/evidence_and_claim_policy.md`. Use `citation_pending` while required source/reference or source-to-claim verification remains incomplete. Use `evidence_ready` only when the relevant source has been verified sufficiently for downstream claim evaluation. A citation record marked `checked` still does not automatically mean the claim is `supported`; `claim-auditor` evaluates the exact relationship.

## Suggested table

| Claim ID | Section | Citation | Source artifact / location | Evidence State | Supports | Verification | Scope And Limitations | Strength | Status |
|---|---|---|---|---|---|---|---|---|---|
| c01 |  |  |  |  |  |  |  |  |  |

## Usage notes

- Record the reason a citation belongs in the manuscript, not just the bibliographic metadata.
- Identify the durable source artifact and the relevant page, section, table, or figure.
- State how the source was checked against the exact claim.
- Record what the source supports and what it does not establish.
- Separate background citations from direct evidence citations when possible.
- Flag claims that need a stronger source or a narrower wording.
- Use this alongside `claim_support.md` and `section_notes.md` while drafting.

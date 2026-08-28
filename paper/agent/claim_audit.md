# Claim Audit

## Support Status Vocabulary

Use the same support-status values as `docs/agent/claim_ledger.md` and the claim-auditor skill:

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

Review comments may explain nuance, but the final status must use one of these labels.

## Claim Audit Table

No manuscript claims have been audited yet.

| Claim ID | Manuscript Location | Claim | Evidence References | Citation | Verification | Support Status | Scope And Limitations | Required Fix | Closure Status | Closure Verification |
|---|---|---|---|---|---|---|---|---|---|---|

For every audited claim:

- `Evidence References` must identify the durable result, source, citation, or project artifact supporting the claim.
- `Citation` must state whether the citation exists, is correctly attached, and actually supports the claim.
- `Verification` must explain how the claim was checked against its evidence.
- `Scope And Limitations` must state what the evidence supports and what it does not establish.
- `Required Fix` must remain separate from support status and may contain actions such as `rewrite`, `narrow`, `add_caveat`, or `remove`.
- `Closure Status` must use the shared revision-closure vocabulary and show whether the required fix is open, in progress, verified, accepted as risk, or deferred.
- `Closure Verification` must state how a verified fix was checked, or why an accepted risk or deferral is justified.

## Closure Status Values

Use one of these revision-closure statuses:

- `open`
- `in_progress`
- `verified`
- `accepted_risk`
- `deferred`

These are revision workflow statuses, not claim support statuses. Keep the final claim support status in the `Support Status` column and in `docs/agent/claim_ledger.md`.

## Next Step
- [State the next step.]

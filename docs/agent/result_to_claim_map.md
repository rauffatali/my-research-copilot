# Result-to-Claim Map

## Purpose

This file maps interpreted result evidence to research and manuscript claims.

It is the bridge between Phase 3 result consolidation and Phase 4 writing.

A manuscript claim should not be drafted as a strong claim unless it appears here or in `docs/agent/claim_ledger.md` with adequate support.

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

Do not introduce local variants.

## Status

- draft
- Allowed values: draft, frozen, superseded

## Claim Support Table

No project-specific claim mappings have been recorded yet.

| Claim ID | Claim | Claim type | Supporting result cards | Supporting citations | Support status | Allowed wording | Not allowed wording |
|---|---|---|---|---|---|---|---|

## Claim Types

Use these when relevant:

- novelty
- performance
- robustness
- generalization
- efficiency
- ablation
- mechanism
- baseline
- dataset
- qualitative
- limitation
- failure_mode
- implementation
- reproducibility

## Support Status Values

Use the same vocabulary as `docs/agent/claim_ledger.md` and the claim auditor:

- supported
- partially_supported
- preliminary
- hypothesis
- needs_citation
- wrong_citation
- unsupported
- contradicted
- out_of_scope
- needs_manual_check

---

## Claim Mapping Entry Template

### CL-001: [Short Claim Name]

#### Claim

[Write the claim.]

#### Claim Type

[Choose from claim types.]

#### Supporting Result Cards

- `docs/agent/result_cards/RES-001_...md`
- `docs/agent/result_cards/RES-002_...md`

#### Supporting Citations

- `sources/...`

#### Support Status

- supported / partially_supported / preliminary / hypothesis / needs_citation / wrong_citation / unsupported / contradicted / out_of_scope / needs_manual_check

#### Allowed Wording

[Conservative wording that the evidence supports.]

Example:

- “In our evaluation setting, the method improves X over the reproduced baseline.”

#### Not Allowed Wording

[Overclaims not supported by evidence.]

Example:

- “The method is generally robust.”
- “The method achieves state-of-the-art performance.”
- “The method solves the failure mode.”

#### Missing Evidence

[What evidence is still needed?]

#### Required Manuscript Caveat

[What limitation or caveat must appear if this claim is used?]

#### Decision

Choose one:

- use_as_main_claim
- use_as_limited_claim
- move_to_limitation
- mark_preliminary
- remove
- needs_more_evidence

#### Next Step

[Concrete next action.]
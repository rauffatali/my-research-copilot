# Result-to-Claim Map

## Purpose

This file maps interpreted result evidence to research and manuscript claims.

It is the bridge between Phase 3 result consolidation and Phase 4 writing.

A manuscript claim should not be drafted as a strong claim unless it appears here or in `docs/agent/claim_ledger.md` with adequate support.

Each mapping entry must connect a claim to interpreted, durable evidence. Raw metrics, completed runs, or the existence of a citation do not establish claim support by themselves.

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

## Evidence State(s)

Record one or more relevant dependency states using the canonical `evidence_state` vocabulary in `.agents/workflow/policies/evidence_and_claim_policy.md`. `Evidence State(s)` describe evidence lifecycle/readiness; `Support Status` remains the separate final judgment for the exact claim wording.

For result-based evidence:

- a planned experiment -> `experiment_planned`;
- a raw or unconsolidated result -> `result_pending`;
- result evidence that has completed the applicable Phase 3 interpretation, verification, scope/limitations, mapping, and evidence-review path -> `evidence_ready`.

A completed run does not automatically mean `evidence_ready`.

## Status

- draft
- Allowed values: draft, frozen, superseded

## Claim Support Table

No project-specific claim mappings have been recorded yet.

| Claim ID | Claim | Claim Type | Evidence References | Evidence State(s) | Verification | Support Status | Scope And Limitations | Allowed Wording | Not Allowed Wording | Missing Evidence | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|

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

### Claim ID

Use `CL-001`, `CL-002`, etc. only when adding a real project claim.

### Short Claim Name

[Short name.]

#### Claim

[Write the claim.]

#### Claim Type

[Choose from claim types.]

#### Evidence References

List every durable artifact that supports or constrains the claim.

Examples:

- `docs/agent/result_cards/RES-001_...md`
- `sources/paper_cards/...`
- `sources/...`
- `runs/...`
- `outputs/...`

#### Evidence State(s)

[One or more canonical evidence states for the claim's dependencies. Do not use this field as the support verdict.]

#### Verification

[Explain how the evidence was checked. Include the relevant source section, metric, table, comparison, rerun, calculation, or audit.]

#### Support Status

- supported / partially_supported / preliminary / hypothesis / needs_citation / wrong_citation / unsupported / contradicted / out_of_scope / needs_manual_check

#### Scope And Limitations

[State where the evidence supports the claim and what it does not establish.]

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

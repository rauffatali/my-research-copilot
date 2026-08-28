# Novelty Risk Matrix

## Status
- draft
- Allowed values: draft, frozen, superseded

## Comparator Ledger
Every plausible closest-prior-work or reviewer-alternative comparator must have a decision before Phase 1 can freeze.

Each comparator row must identify durable evidence, explain how that evidence was verified, and state the scope or limitation of the comparison.

Allowed decisions: `include`, `probe_planned`, `probe_completed`, `excluded_with_evidence`, `deferred_with_reason`, `unresolved`.

| Comparator | Evidence References | Verification | Decision | Rationale or Probe Result | Scope And Limitations |
|---|---|---|---|---|---|
| [comparator name] | [paper card or durable source artifact] | [source section, comparison, or probe check performed] | [include / probe_planned / probe_completed / excluded_with_evidence / deferred_with_reason / unresolved] | [reasoning, probe setup, or probe result] | [what the comparison does and does not establish] |

Do not freeze Phase 1 while any row is `unresolved`. `excluded_with_evidence` requires a specific, cited reason, not "out of scope" or "no time" alone.

Evidence status and comparator decisions are separate:

- evidence references and verification describe the support for the comparison;
- the decision records what the project should do with the comparator;
- do not use claim support-status labels such as `supported` or `unsupported` as comparator decisions.

## Notes
- [Write additional novelty notes not captured in the ledger.]

## Next Step
- [State the next step.]

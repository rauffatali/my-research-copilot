# Evidence and claim policy

Never present unsupported research claims as fact.

## Chain of Evidence

For every material claim that may persist in a decision, result, or manuscript artifact, maintain this chain:

- `claim_id` — stable identifier used across related artifacts;
- `claim` — concise statement of what is being asserted;
- `evidence_refs` — one or more durable artifact references;
- `verification` — how the evidence was checked;
- `support_status` — one canonical claim support status;
- `scope_and_limitations` — where the claim does and does not apply.

Evidence references must identify durable project artifacts:

- literature claims -> `sources/paper_cards/`, verified citation records, and relevant page or section;
- method or configuration claims -> repository path, configuration, implementation symbol, or approved project artifact;
- experimental claims -> run, log, metric, table, or output under `runs/` or `outputs/`;
- derived claims -> input artifacts plus the script, calculation, or transformation that produced the result.

Chain completeness means that every material claim has an evidence reference or is explicitly recorded as a hypothesis or unresolved statement. Chain correctness means that the referenced evidence supports the exact claim, scope, and strength being asserted; the existence of an artifact or citation alone is not sufficient.

Chat-only statements, raw lookup output, and unrecorded tool output are not durable evidence.

Reuse the existing claim-related artifacts instead of creating a separate Chain-of-Evidence file. `docs/agent/claim_ledger.md` remains the source of truth for final support status; `docs/agent/result_to_claim_map.md` and `paper/agent/claim_audit.md` provide phase-specific links and audits.

## Canonical Claim Support Status

`support_status` answers how strongly the current evidence supports the exact claim wording. Keep the existing canonical vocabulary unchanged:

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

`docs/agent/claim_ledger.md` remains the source of truth for this final claim-support verdict. Do not put lifecycle or dependency-readiness labels in this list.

## Evidence State / Claimability Discipline

`evidence_state` is a separate dependency/readiness axis. It answers:

```text
What lifecycle or readiness condition is the relevant evidence dependency in?
```

It does not answer whether the exact claim is supported. The reusable evidence-state vocabulary is exactly:

- `evidence_ready`
- `implementation_defined`
- `implementation_pending`
- `experiment_planned`
- `result_pending`
- `citation_pending`
- `placeholder_only`

### Evidence-state meanings

- `evidence_ready` — the relevant durable evidence exists and has passed the applicable workflow-level readiness or verification step sufficiently to be evaluated for claim support. It means ready for audit, not `supported`; `claim-auditor` must still evaluate the exact claim.
- `implementation_defined` — the relevant method, configuration, implementation behavior, or engineering fact is established by durable implementation or configuration artifacts. It may support factual implementation descriptions within the verified scope, but does not establish performance, robustness, generalization, improvement, causal mechanism, or experimental outcome without separate result evidence.
- `implementation_pending` — the implementation detail exists only as a plan, intended design, TODO, unresolved change, or not-yet-validated implementation. It must not be described as already implemented; planned or pending wording may be used when appropriate.
- `experiment_planned` — an experiment has been proposed, approved, or planned, but no consolidated result evidence exists. Expected outcomes are not findings.
- `result_pending` — execution may have begun or outputs may exist, but the relevant result has not completed the required interpretation, verification, consolidation, or evidence-review path. Raw metrics or a completed run may still be `result_pending`.
- `citation_pending` — a literature-dependent statement lacks a sufficiently verified source and/or source-to-claim relationship. Metadata validity alone does not clear this state; source/reference reality and the support relationship must be checked.
- `placeholder_only` — an intentionally structural or provisional artifact has no evidence value by itself. Empty result tables, TODO metric cells, planned figures, result-section shells, placeholder captions, and draft visualization slots use this state until actual evidence replaces them.

An artifact may record one or more `Evidence State(s)` when a claim has multiple dependencies. For example, method wording may depend on `implementation_defined`, a performance clause on `result_pending`, and a comparison-to-prior-work clause on `citation_pending`. The final claim record still has one canonical `support_status` for the exact claim wording.

### Orthogonality invariant

```text
evidence_state
    = lifecycle/readiness condition of an evidence dependency

support_status
    = strength of support for the exact claim
```

Valid combinations include:

```text
implementation_defined + supported
result_pending + preliminary
evidence_ready + contradicted
citation_pending + needs_citation
```

There is no one-to-one mapping between the two vocabularies. `evidence_ready` does not imply `supported`, and `supported` does not make a mutable dependency permanently current.

### Evidence-state transitions

Use only these transition rules:

- `implementation_pending` -> `implementation_defined` only after the relevant implementation or configuration exists and passes the validation needed for the factual description.
- `experiment_planned` -> `result_pending` when execution or result production begins or outputs exist while consolidation is incomplete.
- `result_pending` -> `evidence_ready` only after the applicable Phase 3 result card, interpretation, verification, scope/limitations, result-to-claim mapping, and required evidence review are complete.
- `citation_pending` -> `evidence_ready` only after the required source/reference and source-to-claim relationship checks are complete; metadata verification alone is insufficient.
- `placeholder_only` -> a relevant real evidence state only after actual durable evidence replaces the placeholder. It must never transition directly to `supported` because `supported` is not an evidence state.

### No silent promotion

A tool, model response, completed command, successful run, generated table, or file existence must not silently promote `implementation_pending`, `experiment_planned`, `result_pending`, `citation_pending`, or `placeholder_only` to `evidence_ready`. Promotion requires:

```text
durable artifact + applicable verification + workflow-specific review
```

Chat-only statements cannot advance an evidence state. An `independent_reviewer` may report that a state appears stale or incorrect, but cannot write the state change because that role is strictly read-only.

### No duplicate evidence-state ledger

Do not create a global evidence-state ledger. Record each state in the artifact closest to its dependency and summarize it in existing support artifacts when needed:

- implementation state -> implementation or configuration artifacts and implementation notes;
- experiment/run state -> experiment plan and run registry;
- result readiness -> result cards and result-to-claim map;
- citation readiness -> source and citation-support artifacts;
- final claim support -> claim ledger;
- manuscript dependency summary -> existing paper support and audit artifacts.

### Revalidation

For mutable dependencies, recheck applicable evidence states when the scientific brief is resolved, before writing-slice acceptance, and immediately before protected integration. If a dependency changes, the earlier wording and support verdict require revalidation rather than silent reuse.

## Experimental claims

Do not claim experimental outcomes unless supported by artifacts in:

- `runs/`
- `outputs/`
- documented result files
- tracked experiment summaries

When discussing results, identify the supporting artifact.

## Literature and novelty claims

Do not claim novelty unless supported by project literature artifacts, citation records, or an explicit gap analysis.

If evidence is missing, mark the statement using the shared claim support-status vocabulary when applicable:

- `unsupported`
- `needs_citation`
- `hypothesis`
- `preliminary`
- `needs_manual_check`

Use `requires_validation` only as a next action or decision note, not as a claim support status.

## Paper claims

Do not edit `paper/` during code-only tasks unless explicitly asked.

When editing paper text, keep claims traceable to at least one of:

- cited literature,
- experiment result,
- documented limitation,
- documented hypothesis,
- project-approved assumption.

Avoid polished academic prose that hides uncertainty.

## Mathematical and theoretical claims

Mathematical hallucination is more dangerous than most other claim failures because confident notation and formal-sounding language are persuasive even when wrong.

Use exactly one label from this canonical vocabulary for every mathematical or theoretical claim:

- `proven` — a specific theorem or result, in a specific cited paper or standard reference, that directly applies here.
- `established_result` — a widely known mathematical fact that does not need a novel citation but should still be named precisely.
- `heuristic_analogy` — structurally inspired by a real mathematical object, but not proven to transfer to this exact setting.
- `empirically_motivated` — the technique works in practice; the mathematical framing is a plausible explanation, not a guarantee.
- `unverified_conjecture` — a new derivation or claim, not yet independently checked.

Do not invent a sixth label. Do not upgrade a label without new evidence.

Do not name a theorem, bound, or named mathematical property without a citation or a fully shown derivation. Do not claim a technique is "principled" or "theoretically motivated" in manuscript-facing text unless the rigor label and source are attached.

Use `theoretical-lens` when proposing a mathematical framing for a research contribution, and `claim-auditor` when checking whether manuscript prose asserting a mathematical property matches its rigor label and source.

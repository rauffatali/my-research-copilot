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
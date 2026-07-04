# Evidence and claim policy

Never present unsupported research claims as fact.

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
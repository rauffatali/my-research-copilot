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
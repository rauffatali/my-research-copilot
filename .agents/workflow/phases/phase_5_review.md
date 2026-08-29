# Phase 5 Contract: Formal Broader Manuscript Review / Red-Team

Phase 5 performs formal broader manuscript-scale or coherent-manuscript-unit review from a skeptical external-reviewer perspective. It is distinct from the embedded writing-slice review inside Phase 4.

## Canonical manuscript workflow

Follow `.agents/guidance/manuscript-writing.md` for the detailed relationship between slice-local readiness review, protected integration, and broader formal review.

```text
Phase 4 embedded review
= writing-slice local
= pre-integration/readiness review
= remains phase_4_active

Phase 5 formal review
= broader integrated manuscript or coherent-unit review
= normally later/post-integration
= skeptical external-reviewer perspective
```

Every material reviewer finding must be traceable to a manuscript section or claim, durable evidence or an explicitly recorded evidence gap, and a closure record. Use `paper/agent/claim_audit.md` for claim-support and status changes and `paper/agent/revision_plan.md` for revision actions; do not leave finding rationale or closure only in chat.

## Input

- A broader integrated manuscript or coherent manuscript-unit review target in `paper/` (required for Phase 5).
- Stable claims and evidence artifacts from Phase 3 and Phase 4.
- Relevant source artifacts in `sources/`.
- Early red-team artifacts in `docs/agent/`, including `pre_mortem.md`, `experiment_red_team.md`, `evidence_review.md`, and `red_team_issue_ledger.md` when available.
- Any manuscript-support notes in `paper/agent/`.

Ordinary writing-slice review is not a Phase 5 entry condition. It remains `phase_4_active` even when it uses an independent reviewer.

## Actions

1. Read the broader review target, current claim/support context, and early red-team artifacts before reviewing, especially unresolved or accepted-risk issues in `docs/agent/red_team_issue_ledger.md`.
2. Prepare `paper/agent/review_context.md` with a compact manuscript summary, claim map, baseline context, question engine, and reviewer questions.
3. Use distinct optional review lenses for methodology, novelty/related work, evidence/claim support, presentation/clarity, and meta-review. For each material finding, record the affected section or claim, evidence references or an explicit missing-evidence record, concern, severity, required action, and closure state in writable review artifacts.
4. Use `scientific-critical-thinking`, `claim-auditor`, `research-lookup`, or `citation-management` when the review requires their respective checks.
5. Keep `independent_reviewer` strictly read-only. Writable roles may record adjudicated review artifacts, but no reviewer role may silently revise manuscript prose.
6. Do not repeat the ordinary candidate-writing production loop in Phase 5. Route required prose revision back to Phase 4.
7. Update `paper/agent/claim_audit.md`, `paper/agent/revision_plan.md`, and `docs/agent/claim_ledger.md` only as permitted by the applicable role and workflow policies.
8. Update `docs/current_status.md` with the review round, main objections, claim-status changes, accepted fixes, remaining risks, and next decision.

## Optional review lenses

Method, Domain, Hybrid, and Meta are optional critique perspectives, not canonical agent roles and not mandatory assignments. They may be exercised by appropriate assigned agents according to the role policy. They must not be confused with the `independent_reviewer` permission role.

## Relevant Skills

Use the smallest relevant set:

- `peer-review`
- `scientific-critical-thinking`
- `claim-auditor`
- `research-lookup` when missing external context must be checked
- `citation-management` when references need verification or repair

## Outputs

Expected artifacts may include:

- `paper/agent/review_context.md`
- `paper/agent/review_method.md`
- `paper/agent/review_domain.md`
- `paper/agent/review_hybrid.md`
- `paper/agent/review_meta.md`
- `paper/agent/revision_plan.md`
- `paper/agent/response_to_reviewers_draft.md`
- `paper/agent/review_score_ledger.md`
- `paper/agent/responsible_use_disclosure.md`
- `paper/agent/claim_audit.md`
- `paper/agent/review_notes.md`

Each reviewer file should keep all rounds in one place, with new rounds appended as new sections such as `## Round 1`, `## Round 2`, and so on.

## Boundary and rollback

Phase 5 is broader and formal; it is not the ordinary review loop for every writing slice. If formal review requires prose revision, return to Phase 4. If it exposes an incomplete or weak evidence package, return to Phase 3. If it invalidates the research direction, return to Phase 1. Do not silently revise the manuscript during review.

## Exit condition

Phase 5 is complete only when:

- reviewer concerns are organized into actionable buckets;
- material findings link concerns to claims or sections and durable evidence, or explicitly record missing evidence;
- required fixes are separated from optional improvements;
- claim support is rechecked using the shared support-status vocabulary;
- early red-team issues are reconciled with the revision plan, limitations, or claim audit;
- review-driven claim-status changes and closure verification are recorded in the appropriate writable artifacts; and
- the next action is clear: revise through Phase 4, return to Phase 3 or Phase 1, resubmit, hold, or archive.

Do not treat formal review as a purely stylistic pass. It is a scientific and evidentiary stress test, and it does not reproduce candidate-writing production.

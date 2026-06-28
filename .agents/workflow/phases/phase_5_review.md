# Phase 5 Contract: Multi-Agent Review / Red-Team

Phase 5 turns a mature manuscript draft into a structured review-and-revision cycle.

## Input

- Mature manuscript draft in `paper/`.
- Stable claims and evidence artifacts from Phase 3 and Phase 4.
- Relevant source artifacts in `sources/`.
- Early red-team artifacts in `docs/agent/`, including `pre_mortem.md`, `experiment_red_team.md`, `evidence_review.md`, and `red_team_issue_ledger.md` when available.
- Any manuscript-support notes in `paper/agent/`.

## Actions

1. Read the manuscript draft and the current claim/support context before reviewing.
2. Review early red-team artifacts before starting manuscript-stage critique, especially unresolved or accepted-risk issues in `docs/agent/red_team_issue_ledger.md`.
3. Prepare a review context bundle in `paper/agent/review_context.md` with a compact paper summary, claim map, baseline context, a question engine, and the reviewer questions that should drive critique.
4. Run reviewer-style critique with distinct roles rather than duplicate criticism.
5. Use `peer-review` in multi-reviewer panel mode to simulate reviewer viewpoints such as methodology, novelty/related work, evidence/claim support, and presentation/clarity, followed by a meta-review.
6. Use `scientific-critical-thinking` to pressure-test the weakest assumptions, the missing baseline, the leakage risk, and alternative explanations.
7. Use `claim-auditor` to verify that the manuscript claims remain supported after drafting and style adaptation.
8. When auditing manuscript claims, assign one of the shared support-status labels:
   * `supported`
   * `partially_supported`
   * `preliminary`
   * `hypothesis`
   * `needs_citation`
   * `wrong_citation`
   * `unsupported`
   * `contradicted`
   * `out_of_scope`
   * `needs_manual_check`
9. Update `paper/agent/claim_audit.md` with manuscript-facing claim audit findings.
10. Update `docs/agent/claim_ledger.md` if the review changes final claim support status.
11. Keep review decisions separate from support statuses. For example, `unsupported` is a support status, while `remove`, `rewrite`, `narrow`, `add_caveat`, or `run_ablation` are review decisions or next actions.
12. Use `research-lookup` when a reviewer question requires missing prior work, baseline context, source-reading, or citation support.
13. Use `citation-management` when reviewer feedback exposes citation or metadata issues.
14. Write revision-oriented artifacts in `paper/agent/` rather than silently revising the paper.
15. Update `docs/current_status.md` with the review round, main objections, claim-status changes, accepted fixes, and remaining risks.

## Reviewer roles

Run separate reviewer passes so the feedback remains distinct and auditable.

- Reviewer Agent 1: Method Reviewer
- Reviewer Agent 2: Domain / Novelty Reviewer
- Reviewer Agent 3: Hybrid / Evidence Reviewer
- Reviewer Agent 4: Meta-Reviewer / Area Chair

Each reviewer role should use the same underlying `peer-review` skill, but with a different critique focus and output artifact. The meta-reviewer synthesizes the panel into one decision-oriented summary.

## Required skills

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

## Exit condition

Phase 5 is complete only when:

- reviewer concerns are organized into actionable buckets;
- required fixes are separated from optional improvements;
- claim support is rechecked after review using the shared support-status vocabulary;
- manuscript-stage review reconciles open or accepted-risk early red-team issues with the revision plan, limitations, or claim audit;
- any review-driven claim-status changes are reflected in `paper/agent/claim_audit.md` and, when final support status changes, in `docs/agent/claim_ledger.md`;
- the next action is clear: revise, resubmit, hold, or return to an earlier phase;
- `docs/current_status.md` reflects the review outcome and next decision.

Do not treat review as a purely stylistic pass. It is a scientific and evidentiary stress test.
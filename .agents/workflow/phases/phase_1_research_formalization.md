# Phase 1 Contract: Brainstorming / Research Formalization

Phase 1 turns a broad research idea into a debated, evidence-backed, user-approved research package.

Phase 1 is intentionally interactive. Do not treat brainstorming as a one-pass artifact-writing task.

## Input

- A broad human idea, problem statement, or research intent.
- Any existing project context in `docs/`.
- Any previously saved external evidence in `sources/`.

## Actions

1. Clarify the starting intent only enough to begin evidence lookup.
2. Initialize or update `docs/research_context.md` with the high-level project snapshot (problem domain, project type, data/domain context, objectives, high-level approach, constraints) as soon as the framing is stable enough to state briefly. If the file does not exist yet, initialize it from `.agents/templates/RESEARCH_CONTEXT.template.md`. Keep it high-level: detailed debate belongs in `docs/agent/brainstorming_brief.md`, and the approved decision belongs in `docs/agent/research_direction.md`.
3. Read relevant saved source artifacts from `sources/` before new lookup work.
4. Use `research-lookup` to gather candidate prior work, baselines, datasets, benchmarks, and technical references.
5. For novelty, closest-prior-work, baseline, dataset, benchmark, evaluation, or positioning decisions, track important sources in `sources/reading_queue.md`, promote high-priority sources into `sources/paper_cards/`, and summarize direction-relevant comparisons in `sources/literature_matrix.md`.
6. For every plausible closest-prior-work or reviewer-alternative comparator surfaced during lookup or critique, add or update a row in `docs/agent/novelty_risk_matrix.md`'s comparator ledger with a decision of `include`, `probe_planned`, `probe_completed`, `excluded_with_evidence`, or `deferred_with_reason`. Do not leave a comparator row `unresolved` when freezing the direction, and do not accept "out of scope" or "no time" alone as an `excluded_with_evidence` reason.
7. If a source substantially weakens or complicates the proposed direction, update `docs/agent/research_direction.md`, `docs/agent/novelty_risk_matrix.md`, or `docs/agent/idea_archive.md`.
8. Present a compact evidence briefing to the user: what was found, why it matters, what seems promising, what seems risky, and what remains unclear. For each material literature, novelty, baseline, dataset, evaluation, or direction claim, include its durable evidence reference, verification note, support status when applicable, and scope or limitation.
9. Ask targeted clarifying questions before formalizing the direction, covering contribution type (architectural novelty, adaptation/combination for a domain, systematic comparative study, dataset/benchmark, or theoretical/engineering-systems contribution), scope, baseline/reference point, metric or evaluation signal, dataset/evaluation assumptions, risk, and implementation feasibility.
10. Record each debate round in `docs/agent/brainstorming_brief.md`, including the claim or decision under discussion, durable evidence references, verification performed, questions asked, user responses, current interpretation, and unresolved uncertainty.
11. Repeat lookup, synthesis, critique, and user questioning until the idea is rejected, deferred, or strong enough to formalize.
12. Use `literature-review`, `claim-auditor`, and `scientific-critical-thinking` as needed to synthesize closest prior work, test claimability, and pressure-test novelty, leakage risk, evaluation decisiveness, failure modes, and contribution strength. When invoking `scientific-critical-thinking` at the point of freezing the direction, require a decision per comparator-ledger row rather than a general risk narrative.
13. Use `citation-management` only when reference metadata or BibTeX hygiene needs verification for candidate sources.
14. For high novelty risk, unclear baseline, fragile assumptions, or uncertain evaluation, run an early pre-mortem in `docs/agent/pre_mortem.md`, record concrete follow-up issues in `docs/agent/red_team_issue_ledger.md`, and do not freeze the direction until the decision is `proceed`, `proceed_with_caveats`, or the user explicitly accepts the recorded risk.
15. If the idea is weak, refine it or recommend stopping; if it is promising, propose a final research package and ask the user to approve, revise, or reject it. When the direction is approved, sync the final framing back into `docs/research_context.md` so it reflects the approved package.

### Project context template

The canonical research-context template is `.agents/templates/RESEARCH_CONTEXT.template.md`.

For a real project, agents must use `docs/research_context.md` as the active high-level project snapshot. If it is missing or still template-like, initialize it from `.agents/templates/RESEARCH_CONTEXT.template.md` early in Phase 1.

`docs/research_context.md` is a stable, high-level snapshot, not a decision log or task tracker. It complements, and must stay consistent with, but does not replace:

- `docs/agent/research_direction.md`, which holds the debated, evidence-backed, user-approved decision record;
- `docs/PROJECT_PLAN.md`, which holds the workstream and task breakdown.

Update `docs/research_context.md` only when the high-level framing itself changes, not on every debate round or planning decision.

### Probe experiments

Phase 1 may include small, cheap, decision-oriented pilot runs when they resolve a specific comparator-ledger row or a direction-shaping uncertainty — for example, a quick baseline comparison, or a zero-shot check of a foundation-model comparator. These probes are lighter than Phase 2 experiments: they do not require `docs/agent/experiment_plan.md` or `docs/agent/run_registry.md`, but their setup, result, and decision impact must be recorded in `docs/agent/brainstorming_brief.md` and reflected in the relevant `docs/agent/novelty_risk_matrix.md` row.

Do not let a probe experiment silently become the claim-grade evidence for a manuscript result; Phase 3 still owns claim-grade result interpretation once the direction moves to full experimentation.

## Interaction rule

Do not directly patch a final `research_direction.md` from the user's initial idea alone.

Phase 1 may write draft brainstorming notes while the discussion is active, but it must not freeze the research direction or move to Phase 2 until:

- relevant evidence has been gathered or existing evidence has been reviewed;
- the evidence briefing has been shown to the user;
- the user has answered the main clarifying questions or explicitly deferred them;
- unresolved assumptions are recorded;
- the final direction has been presented for user approval;
- the user has approved proceeding, or the decision is recorded as revise, defer, or stop.

## Relevant Skills

Use the smallest relevant set:

- `research-lookup` for external discovery.
- `literature-review` when selected sources need synthesis.
- `claim-auditor` when proposed direction, novelty framing, or early wording needs claimability checking.
- `scientific-critical-thinking` when novelty, leakage risk, evaluation decisiveness, failure modes, or contribution strength need pressure testing.
- `theoretical-lens` when a failure mode or design choice may have a load-bearing mathematical framing worth adopting as part of the contribution; use sparingly, not on every idea.
- `citation-management` only when references are being stabilized.

## Outputs

Phase 1 durable artifacts include:

- `docs/research_context.md` — high-level project snapshot; lives in `docs/`, not `docs/agent/`.

Phase 1 durable artifacts in `docs/agent/`, including as needed:

- `docs/agent/research_direction.md`
- `docs/agent/brainstorming_brief.md`
- `docs/agent/idea_archive.md`
- `docs/agent/hypotheses.md`
- `docs/agent/novelty_risk_matrix.md`

Update `docs/current_status.md` with the active Phase 1 artifact paths, unresolved questions or blockers, and next recommended step.

## Exit condition

Phase 1 is complete only when the idea has:

- closest-prior-work and novelty-sensitive decisions are backed by paper cards or saved source artifacts;
- material direction, novelty, baseline, dataset, and evaluation claims have durable evidence references, or are explicitly marked as hypotheses or unresolved;
- evidence references identify the relevant source artifact and page, section, metric, comparison, or other verification location when available;
- major source candidates are tracked in `sources/reading_queue.md`;
- literature comparisons that affect the direction are summarized in `sources/literature_matrix.md`;
- at least one evidence-backed debate round;
- user responses incorporated into the final direction;
- a concrete failure mode;
- a baseline or reference point;
- a comparator ledger in `docs/agent/novelty_risk_matrix.md` with no `unresolved` rows for identified closest-prior-work or reviewer-alternative comparators;
- an explicit contribution type recorded in `docs/agent/research_direction.md`;
- a metric or evaluation signal;
- an ablation or isolation plan;
- an identified risk or tradeoff;
- high-risk directions have a pre-mortem or an explicit reason why pre-mortem was deferred;
- unresolved pre-mortem risks are recorded in `docs/agent/red_team_issue_ledger.md` or in the research direction artifact;
- a publication-worthiness assessment or explicit reason to stop/defer;
- a clear decision to proceed, revise, or stop;
- `docs/research_context.md` reflects the approved high-level framing.

Do not move to implementation without a frozen Phase 1 artifact package.

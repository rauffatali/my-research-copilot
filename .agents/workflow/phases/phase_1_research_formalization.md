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
6. If a source substantially weakens or complicates the proposed direction, update `docs/agent/research_direction.md`, `docs/agent/novelty_risk_matrix.md`, or `docs/agent/idea_archive.md`.
7. Present a compact evidence briefing to the user: what was found, why it matters, what seems promising, what seems risky, and what remains unclear.
8. Ask targeted clarifying questions before formalizing the direction, covering contribution, scope, baseline/reference point, metric or evaluation signal, dataset/evaluation assumptions, risk, and implementation feasibility.
9. Record each debate round in `docs/agent/brainstorming_brief.md`, including evidence found, questions asked, user responses, current interpretation, and unresolved uncertainty.
10. Repeat lookup, synthesis, critique, and user questioning until the idea is rejected, deferred, or strong enough to formalize.
11. Use `literature-review`, `claim-auditor`, and `scientific-critical-thinking` as needed to synthesize closest prior work, test claimability, and pressure-test novelty, leakage risk, evaluation decisiveness, failure modes, and contribution strength.
12. Use `citation-management` only when reference metadata or BibTeX hygiene needs verification for candidate sources.
13. For high novelty risk, unclear baseline, fragile assumptions, or uncertain evaluation, run an early pre-mortem in `docs/agent/pre_mortem.md`, record concrete follow-up issues in `docs/agent/red_team_issue_ledger.md`, and do not freeze the direction until the decision is `proceed`, `proceed_with_caveats`, or the user explicitly accepts the recorded risk.
14. If the idea is weak, refine it or recommend stopping; if it is promising, propose a final research package and ask the user to approve, revise, or reject it. When the direction is approved, sync the final framing back into `docs/research_context.md` so it reflects the approved package.

### Project context template

The canonical research-context template is `.agents/templates/RESEARCH_CONTEXT.template.md`.

For a real project, agents must use `docs/research_context.md` as the active high-level project snapshot. If it is missing or still template-like, initialize it from `.agents/templates/RESEARCH_CONTEXT.template.md` early in Phase 1.

`docs/research_context.md` is a stable, high-level snapshot, not a decision log or task tracker. It complements, and must stay consistent with, but does not replace:

- `docs/agent/research_direction.md`, which holds the debated, evidence-backed, user-approved decision record;
- `docs/PROJECT_PLAN.md`, which holds the workstream and task breakdown.

Update `docs/research_context.md` only when the high-level framing itself changes, not on every debate round or planning decision.

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
- major source candidates are tracked in `sources/reading_queue.md`;
- literature comparisons that affect the direction are summarized in `sources/literature_matrix.md`;
- at least one evidence-backed debate round;
- user responses incorporated into the final direction;
- a concrete failure mode;
- a baseline or reference point;
- a metric or evaluation signal;
- an ablation or isolation plan;
- an identified risk or tradeoff;
- high-risk directions have a pre-mortem or an explicit reason why pre-mortem was deferred;
- unresolved pre-mortem risks are recorded in `docs/agent/red_team_issue_ledger.md` or in the research direction artifact;
- a publication-worthiness assessment or explicit reason to stop/defer;
- a clear decision to proceed, revise, or stop;
- `docs/research_context.md` reflects the approved high-level framing.

Do not move to implementation without a frozen Phase 1 artifact package.

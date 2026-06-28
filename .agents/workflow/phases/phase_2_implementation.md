# Phase 2 Contract: Implementation / Experimentation

Phase 2 turns an approved research direction into controlled implementation and experiment artifacts.

## Input

- Frozen Phase 1 artifacts in `docs/agent/`.
- Relevant source artifacts in `sources/`.
- Any existing codebase, configs, tests, and data layout.

## Actions

1. Read `docs/agent/research_direction.md` before implementation or experimentation. If it is missing, template-like, or not stable enough to guide work, route back to Phase 1 or enter `backfill_required`.
2. Read and update `docs/PROJECT_PLAN.md` as the canonical active project plan. If it is missing or still template-like, initialize it from `.agents/templates/PROJECT_PLAN.template.md` before Phase 2 work.
3. When experiment design depends on prior work, inspect relevant paper cards, `sources/literature_matrix.md`, and `sources/baseline_candidates.md`; if literature suggests a missing baseline, benchmark, dataset, metric, or ablation, update `docs/agent/experiment_queue.md`, `docs/agent/ablation_matrix.md`, or promote decisions into `docs/agent/baseline_ledger.md`.
4. Before research-changing implementation, data changes, training, evaluation, or experiment execution, check relevant gates in `docs/research_gates.md`, especially Gates 3-6, and keep work aligned with the frozen direction, failure mode, baseline/control, metric, and validation plan.
5. For implementation-only work, use `docs/agent/implementation_notes.md` for reasoning, engineering decisions, debugging notes, changed files, validation, outputs, blockers, and next step.
6. For experiment selection, check `docs/agent/experiment_queue.md` before serious experiments and use it when priority is unclear, multiple candidate experiments exist, compute is limited, or the next run should be chosen by decision value. If an experiment is not approved, add or update it in the queue instead of running it.
7. Promote a queue item to `docs/agent/experiment_plan.md` only when it has a linked hypothesis or direction, decision target, baseline/control, experimental change, target metric or failure mode, minimal viable version, stop condition, and expected outcomes.
8. Before running an expensive, claim-critical, or direction-changing experiment, red-team the plan in `docs/agent/experiment_red_team.md`; record concrete follow-up issues in `docs/agent/red_team_issue_ledger.md`, and do not run red-flagged experiments until the decision is `approve_to_run`, `run_minimal_version_first`, or the user explicitly accepts the recorded risk.
9. During experiment execution, record actual runs in `docs/agent/run_registry.md`, save configs/logs/metrics/checkpoints/predictions/plots under durable `runs/` and `outputs/` paths, and update `docs/agent/experiment_journal.md`.
10. When relevant, update supporting validity artifacts: `docs/agent/baseline_ledger.md`, `docs/agent/ablation_matrix.md`, `docs/agent/dataset_card.md`, and `docs/agent/leakage_audit.md`.
11. Run narrow validation before expensive or full-scale execution: tests, smoke checks, config validation, data-loader checks, metric dry runs, or small synthetic/subset runs.
12. Record failed, cancelled, unstable, or inconclusive implementation and experiment attempts instead of hiding them.
13. If implementation reveals a flawed research direction, hypothesis, baseline, metric, or evaluation plan, pause Phase 2 and route back to Phase 1 or `backfill_required`.
14. If experiment outputs are ready for interpretation, route to Phase 3 rather than turning raw metrics directly into claims.
15. Update `docs/current_status.md` when the active implementation task, experiment state, artifact set, blocker, or next step changes.

### Project plan template

The canonical project-plan template is `.agents/templates/PROJECT_PLAN.template.md`.

For a real project, agents must use `docs/PROJECT_PLAN.md` as the active project plan. If `docs/PROJECT_PLAN.md` is missing or still contains template placeholders, the agent should initialize or complete it from `.agents/templates/PROJECT_PLAN.template.md` before Phase 2 work.

## Required Skills And Policies

- Use `scientific-critical-thinking` when implementation or experiment choices need methodological critique.
- Load `.agents/workflow/policies/engineering_policy.md` for material code, config, script, data, training, evaluation, packaging, notebook, or reproducibility changes.
- Load `.agents/workflow/policies/research_policy.md` for research-design, architecture, method, dataset, training, evaluation, or claim-sensitive changes.

## Outputs

Phase 2 outputs are project-dependent, but serious work should leave a durable artifact chain.

Implementation-only work may update:

- `docs/PROJECT_PLAN.md`
- `docs/agent/implementation_notes.md`
- `src/`
- `scripts/`
- `tests/`
- `configs/`

Experiment work may update:

- `docs/agent/experiment_queue.md` for proposed, deferred, cancelled, superseded, or promoted experiments.
- `docs/agent/experiment_plan.md` for approved runnable experiments.
- `docs/agent/run_registry.md` and `docs/agent/experiment_journal.md` for executed runs.
- `runs/<experiment_or_run_id>/` and `outputs/experiments/<experiment_or_run_id>/` for durable configs, logs, metrics, checkpoints, predictions, plots, and summaries.
- `docs/agent/baseline_ledger.md`, `docs/agent/ablation_matrix.md`, `docs/agent/dataset_card.md`, and `docs/agent/leakage_audit.md` when comparison, mechanism, dataset, or leakage validity matters.

Do not treat a queued experiment as approved, an approved experiment as completed, or a completed run as interpreted evidence until Phase 3 consolidates it.

## Exit condition

Phase 2 is complete only when:

- the approved implementation or experiment plan is done;
- `docs/PROJECT_PLAN.md` captures workstreams, tasks, dependencies, validation, risks, and exit criteria;
- validation has been run or explicitly deferred with a reason;
- experiment choices are recorded in `docs/agent/experiment_queue.md` when choice, priority, compute, or approval matters;
- serious executed experiments have a linked queue item or bypass reason, linked experiment plan, run registry entry, saved config, saved output path, and recorded next decision;
- baseline, ablation, dataset, and leakage validity artifacts are updated when comparison, mechanism, or evaluation claims depend on them;
- expensive, claim-critical, or direction-changing experiments have an experiment red-team record or a recorded deferral reason;
- unresolved experiment critique issues are recorded in `docs/agent/red_team_issue_ledger.md`;
- the implementation has not silently changed the contribution target;
- `docs/current_status.md` reflects the current implementation state and next step.

Do not redefine the research direction during implementation. If the idea changes materially, return to Phase 1.
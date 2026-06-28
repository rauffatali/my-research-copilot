# Phase 2 Contract: Implementation / Experimentation

Phase 2 turns an approved research direction into controlled implementation and experiment artifacts.

## Input

- Frozen Phase 1 artifacts in `docs/agent/`.
- Relevant source artifacts in `sources/`.
- Any existing codebase, configs, tests, and data layout.

## Actions

1. Read `docs/agent/research_direction.md` before starting implementation or experimentation. If the research direction is missing, still a template, or not frozen enough to guide implementation, route back to Phase 1 or enter `backfill_required`.
2. When experiment design depends on prior work, inspect relevant paper cards and `sources/literature_matrix.md` before finalizing `docs/agent/experiment_plan.md`.
3. Use `sources/baseline_candidates.md` to track baselines suggested by prior work before promoting them to `docs/agent/baseline_ledger.md`.
4. If literature suggests a missing baseline, benchmark, dataset, metric, or ablation, update `docs/agent/experiment_queue.md` or `docs/agent/ablation_matrix.md`.
5. Read and update `docs/PROJECT_PLAN.md` as the canonical project plan with explicit objective, scope, workstreams, task breakdown, dependencies, validation per task, risks/blockers, and exit criteria. If it is missing or still a template, initialize it from the project-plan template before Phase 2 work.
6. Use `docs/agent/implementation_notes.md` for implementation reasoning, engineering decisions, design tradeoffs, debugging notes, and non-experiment implementation context.
7. Use `docs/agent/experiment_queue.md` before `docs/agent/experiment_plan.md` when experiment priority is unclear, multiple candidate experiments exist, compute is limited, or the next experiment should be selected by expected decision value.
8. Promote a queue item to `docs/agent/experiment_plan.md` only when it has:
   * a linked hypothesis or research direction;
   * a decision it will enable;
   * a baseline or control;
   * an experimental change;
   * a target metric or failure mode;
   * a minimal viable version;
   * a stop condition;
   * expected outcomes if the hypothesis is true or false.
9. Before implementing a research change, check `docs/research_gates.md`, especially:
   * Gate 3: Research Change Gate;
   * Gate 4: Implementation Gate;
   * Gate 5: Dataset and Leakage Gate;
   * Gate 6: Experiment Decision Gate.
10. Keep implementation aligned with the frozen research direction, target failure mode, baseline/control, metric, and validation plan.
11. Before running a serious experiment, check `docs/agent/experiment_queue.md` to see whether the experiment is already proposed, deferred, cancelled, or superseded.
12. If the experiment is not yet approved, add or update it in `docs/agent/experiment_queue.md` rather than running it immediately.
13. Once an experiment is selected, create or update `docs/agent/experiment_plan.md`.
14. Before running an expensive, claim-critical, or direction-changing experiment, red-team the plan in `docs/agent/experiment_red_team.md`.
15. Record concrete experiment critique issues in `docs/agent/red_team_issue_ledger.md` when they require follow-up.
16. Do not run a red-flagged experiment until the decision is `approve_to_run`, `run_minimal_version_first`, or the user explicitly accepts the recorded risk.
17. During execution, record actual runs in `docs/agent/run_registry.md`.
18. Save experiment configs, logs, metrics, checkpoints, predictions, plots, and summaries under durable `runs/` and `outputs/` paths.
19. Update `docs/agent/experiment_journal.md` as the chronological index of what happened, what failed, what changed, and what decision was made.
20. When comparisons, ablations, datasets, or leakage risks matter, update the corresponding supporting artifact:
* `docs/agent/baseline_ledger.md` for baseline/control validity;
* `docs/agent/ablation_matrix.md` for component or mechanism isolation;
* `docs/agent/dataset_card.md` for dataset, split, preprocessing, and evaluation assumptions;
* `docs/agent/leakage_audit.md` for leakage and evaluation trustworthiness.
21. Run tests, sanity checks, smoke tests, small-subset runs, or minimal viable experiments before expensive or full-scale execution.
22. Record failed, cancelled, unstable, or inconclusive implementation/experiment attempts instead of hiding them.
23. If implementation reveals that the research direction, hypothesis, baseline, metric, or evaluation plan is flawed, pause Phase 2 and route back to Phase 1 or `backfill_required`.
24. If experiment outputs are ready for interpretation, route to Phase 3 rather than turning raw metrics directly into claims.
25. Update `docs/current_status.md` when the active implementation task, experiment state, artifact set, blocker, or next step changes.

### Project plan template

The canonical project-plan template is `.agents/templates/PROJECT_PLAN.template.md`.

For a real project, agents must use `docs/PROJECT_PLAN.md` as the active project plan. If `docs/PROJECT_PLAN.md` is missing or still contains template placeholders, the agent should initialize or complete it from `.agents/templates/PROJECT_PLAN.template.md` before Phase 2 work.

## Required skills and guidances

- `scientific-critical-thinking`
- `ai-ml-research-dev` when ML research/development practice applies
- `cv-dev` when computer vision engineering practice applies
- `cv-researcher` when research design, baselines, ablations, or evaluation apply
- `python-dev` when Python implementation, packaging, or testing apply

## Outputs

Phase 2 artifacts are project-dependent, but serious implementation and experimentation work should leave a durable artifact chain.

For implementation-only tasks, expected artifacts may include:

- `docs/agent/implementation_notes.md`
- `docs/PROJECT_PLAN.md`
- `src/`
- `scripts/`
- `tests/`
- `configs/`

For experiment selection and prioritization, use:

- `docs/agent/experiment_queue.md`

Use `docs/agent/experiment_queue.md` before `docs/agent/experiment_plan.md` when experiment priority is unclear, multiple candidate experiments exist, compute is limited, or the next experiment should be selected by expected decision value.

For approved experiment execution, use:

- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- `runs/<experiment_or_run_id>/`
- `outputs/experiments/<experiment_or_run_id>/`

When relevant, also update:

- `docs/agent/baseline_ledger.md`
- `docs/agent/ablation_matrix.md`
- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`

Do not treat a queued experiment as approved.
Do not treat an approved experiment as completed.
Do not treat a completed run as interpreted evidence until Phase 3 consolidates it.

## Exit condition

Phase 2 is complete only when:

- the approved plan has been implemented;
- the project plan captures workstreams, tasks, subtasks, dependencies, validation, risks, and exit criteria rather than a flat to-do list;
- validation has been run or explicitly deferred with a reason;
- candidate experiments are recorded, prioritized, deferred, cancelled, or promoted in `docs/agent/experiment_queue.md` when experiment choice matters;
- every serious executed experiment has a linked queue item or an explicit reason for bypassing the queue;
- every approved experiment has a linked experiment plan, run registry entry, saved config, saved output path, and recorded next decision;
- literature-suggested baselines that matter for experiment validity are either promoted to `docs/agent/baseline_ledger.md`, deferred with a reason, or rejected with a reason;
- comparisons are backed by `docs/agent/baseline_ledger.md` when baseline claims are likely;
- ablations are backed by `docs/agent/ablation_matrix.md` when mechanism or component claims are likely;
- dataset and leakage assumptions are backed by `docs/agent/dataset_card.md` and `docs/agent/leakage_audit.md` when evaluation validity depends on them;
- expensive, claim-critical, or direction-changing experiments have an experiment red-team record or an explicit reason why red-team was deferred;
- unresolved experiment critique issues are recorded in `docs/agent/red_team_issue_ledger.md`;
- the implementation has not silently changed the contribution target;
- `docs/current_status.md` reflects the current implementation state and next step.

Do not redefine the research direction during implementation. If the idea changes materially, return to Phase 1.
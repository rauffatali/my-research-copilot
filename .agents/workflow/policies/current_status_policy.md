# Current Status Protocol

## Purpose

`docs/current_status.md` is the shared live state pointer for the research workflow.

It should answer:

- What phase is active?
- What substep is active?
- What durable artifacts matter right now?
- What blocker or open question affects the next action?
- What should the agent do next?

It should not be used as:

- a long research notebook;
- a manuscript draft;
- an experiment log;
- a literature review;
- a source dump;
- a changelog of the scaffold itself.

`docs/current_status.md` should stay short, current, and operational.

This protocol defines how `docs/current_status.md` should be updated, when it is stale, and how agents should recover from stale or template-default status.

---

## Relationship to Other Workflow Files

Use these files together:

- `docs/current_status.md` — short live state pointer.
- `.agents/workflow/policies/current_status_policy.md` — rules for updating the live state pointer.
- `docs/workflow_state_machine.md` — canonical phase and transition model.
- `docs/research_gates.md` — gates that decide whether work can proceed.
- `docs/agent/` — durable research workflow artifacts.
- `paper/agent/` — manuscript, review, and revision-support artifacts.
- `sources/` — external evidence and literature artifacts.

Do not duplicate full artifact content inside `docs/current_status.md`.

Instead, link to the durable artifact path.

---

## Required Structure of `docs/current_status.md`

Every `docs/current_status.md` update should use this structure:

- Metadata
- Phase
- Latest Action
- Active Artifacts
- Blockers
- Open Questions
- Next Step
- Notes, optional

Recommended shape:

    # Current Status

    ## Metadata
    - Status type:
    - Project initialized:
    - Last updated:
    - State source: `docs/workflow_state_machine.md`
    - Status protocol: `.agents/workflow/policies/current_status_policy.md`

    ## Phase
    - Current phase:
    - Current substep:

    ## Latest Action
    - ...

    ## Active Artifacts
    - ...

    ## Blockers
    - ...

    ## Open Questions
    - ...

    ## Next Step
    - ...

    ## Notes
    - ...

---

## Metadata Fields

Use these fields:

    ## Metadata
    - Status type:
    - Project initialized:
    - Last updated:
    - State source:
    - Status protocol:

### `Status type`

Allowed values:

- `template_default`
- `bootstrapping_existing_project`
- `project_live`
- `blocked`
- `archived`

Meanings:

| Value | Meaning |
|---|---|
| `template_default` | Fresh scaffold state. No project-specific state has been initialized yet. |
| `bootstrapping_existing_project` | The scaffold is being applied to an existing project and the agent is determining the current phase. |
| `project_live` | A real project phase has been selected and the status reflects current work. |
| `blocked` | Progress is blocked by missing information, missing artifacts, unresolved contradictions, or unavailable resources. |
| `archived` | The active project has been completed, paused, or archived. |

### `Project initialized`

Allowed values:

- `yes`
- `no`
- `partial`

Meanings:

| Value | Meaning |
|---|---|
| `no` | No project-specific state has been initialized. |
| `partial` | Some project context exists, but phase handoff artifacts are incomplete or being backfilled. |
| `yes` | The project has been routed into a live workflow phase. |

### `Last updated`

Use an ISO-style date:

    - Last updated: YYYY-MM-DD

When the agent does not know the real date, it should preserve the existing date or write:

    - Last updated: unknown

Do not fabricate a precise date.

### `State source`

Use:

    - State source: `docs/workflow_state_machine.md`

### `Status protocol`

Use:

    - Status protocol: `.agents/workflow/policies/current_status_policy.md`

---

## Canonical Phase Values

Use canonical workflow states from `docs/workflow_state_machine.md`.

Allowed phase values include:

- `intake`
- `bootstrap_existing_project`
- `backfill_required`
- `phase_1_active`
- `phase_1_frozen`
- `phase_2_active`
- `phase_2_frozen`
- `phase_3_active`
- `phase_3_frozen`
- `phase_4_active`
- `phase_4_frozen`
- `phase_5_active`
- `blocked`
- `archived`

Do not invent new phase names unless `docs/workflow_state_machine.md` is updated at the same time.

---

## Phase Meaning

| Phase | Meaning |
|---|---|
| `intake` | The next task has not yet been routed to a research phase. |
| `bootstrap_existing_project` | The agent is inspecting existing project artifacts to infer the correct current phase. |
| `backfill_required` | The requested target phase is clear, but prerequisite artifacts are missing and must be reconstructed or marked unavailable. |
| `phase_1_active` | Research direction, novelty, hypothesis, scope, baseline, and evaluation framing are being formed. |
| `phase_1_frozen` | Direction and handoff context are stable enough for implementation or experimentation. |
| `phase_2_active` | Implementation, experiment selection, experiment planning, and execution are active. |
| `phase_2_frozen` | Implementation and experiment outputs are stable enough for result consolidation. |
| `phase_3_active` | Results, evidence, figures, tables, error analysis, and claim support are being consolidated. |
| `phase_3_frozen` | Evidence package and claim support are stable enough for manuscript work. |
| `phase_4_active` | Manuscript drafting, rewriting, citation alignment, and evidence-bound writing are active. |
| `phase_4_frozen` | Manuscript draft is stable enough for review or red-team critique. |
| `phase_5_active` | Review, red-team critique, revision planning, rebuttal planning, or reviewer simulation is active. |
| `blocked` | Work cannot proceed safely without resolving a concrete blocker. |
| `archived` | Project is no longer active. |

---

## Update Triggers

Update `docs/current_status.md` after:

- a user request is routed to a phase;
- project bootstrap changes the detected project state;
- the active phase changes;
- the active substep changes materially;
- a phase artifact is created, frozen, revised, superseded, or invalidated;
- a blocker is discovered;
- a blocker is resolved;
- active artifact paths change;
- a downstream task reveals missing upstream context;
- an experiment queue item is promoted to an experiment plan;
- an experiment starts, fails, completes, or is cancelled;
- result interpretation changes claim support;
- manuscript work begins or changes target section;
- review sends the work backward to an earlier phase;
- current status is discovered to be stale or inconsistent.

Do not update `docs/current_status.md` for every tiny edit.

Update it when the next agent or human would need the information to continue safely.

---

## Freshness Rules

A status file is stale if:

- it says `template_default` but project-specific artifacts exist;
- it says the project is uninitialized but there are active project files, runs, sources, or paper artifacts;
- it lists a blocker that has already been resolved;
- it points to artifacts that no longer exist;
- it omits artifacts that are clearly active for the current task;
- it says the phase is earlier than the latest valid project evidence;
- it conflicts with frozen artifacts;
- it conflicts with run outputs;
- it conflicts with claim ledgers;
- it conflicts with manuscript artifacts;
- it describes scaffold setup work as if it were the active research task.

When stale status is detected:

1. Do not trust the stale status as project truth.
2. Inspect durable artifacts.
3. Route through `intake`, `bootstrap_existing_project`, or `backfill_required`.
4. Rewrite `docs/current_status.md` before doing downstream work.
5. Use `blocked` only when the conflict cannot be resolved from available artifacts.

---

## Template-Default Status Rules

A fresh clone should start with:

    - Status type: template_default
    - Project initialized: no
    - Current phase: `intake`

A template-default status means:

- the scaffold is ready;
- no project-specific workflow state has been initialized;
- the next user request should be routed through intake;
- existing project artifacts, if present, should trigger bootstrap.

A template-default status must not claim:

- that Phase 1 is active;
- that Phase 2 is active;
- that an experiment queue is active;
- that the project is blocked by old scaffold setup work;
- that research progress has happened when it has not.

Safe default blocker wording:

    ## Blockers
    - None for the scaffold.
    - Project-specific phase is unknown until bootstrap or first task routing.

Unsafe default blocker wording:

    ## Blockers
    - phase-to-file contract not yet defined

Do not keep stale scaffold blockers in the live status file.

---

## Phase-Specific Active Artifacts

`docs/current_status.md` should list only artifacts that are active for the current task.

Do not list every available template or scaffold file.

Active artifacts are files the next agent or human needs to inspect, update, freeze, or use as handoff context.

### Intake State

When the current phase is `intake` and no project-specific task has been routed yet, active artifacts should stay broad and minimal.

Recommended active artifacts:

    ## Active Artifacts
    - `docs/current_status.md`
    - `docs/workflow_state_machine.md`
    - `docs/research_gates.md`
    - `docs/agent/`
    - `paper/agent/`
    - `sources/`

Do not add Phase 2 artifacts during default intake just because the files exist.

Do not add these by default during `intake`:

- `docs/agent/experiment_queue.md`
- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/baseline_ledger.md`
- `docs/agent/ablation_matrix.md`
- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`

These files may exist as templates, but they are not active until the workflow reaches a task that needs them.

### Existing Project Bootstrap

When the current phase is `bootstrap_existing_project`, active artifacts should include the files being inspected to infer the current phase.

Examples:

    ## Active Artifacts
    - `docs/current_status.md`
    - `docs/workflow_state_machine.md`
    - `docs/agent/`
    - `sources/`
    - `runs/`
    - `outputs/`
    - `paper/`

Use only paths that exist or are expected in the project.

### Backfill Required

When the current phase is `backfill_required`, active artifacts should include:

- the requested downstream artifact;
- the missing prerequisite artifact;
- the files being used to reconstruct missing context.

Example:

    ## Active Artifacts
    - `docs/agent/research_direction.md`
    - `docs/agent/hypotheses.md`
    - `docs/agent/experiment_plan.md`
    - `runs/`
    - `outputs/`

Backfilled artifacts must be clearly marked as reconstructed, assumed, or needing confirmation.

### Phase 1 Active

When the current phase is `phase_1_active`, active artifacts may include:

- `docs/research_context.md`
- `docs/agent/research_direction.md`
- `docs/agent/brainstorming_brief.md`
- `docs/agent/hypotheses.md`
- `docs/agent/novelty_risk_matrix.md`
- `docs/agent/idea_archive.md`
- `sources/`

Use Phase 1 when the task involves:

- research framing;
- novelty search;
- problem selection;
- hypothesis formation;
- scope decisions;
- target failure mode selection;
- baseline or metric framing.

### Phase 2 Active: Implementation-Only Task

When the current phase is `phase_2_active` and the task is implementation-only, active artifacts may include:

- `docs/PROJECT_PLAN.md`
- `docs/agent/implementation_notes.md`
- `src/`
- `scripts/`
- `tests/`
- `configs/`

`docs/agent/experiment_queue.md` is optional for implementation-only tasks.

Do not list it unless experiment selection or prioritization is part of the task.

### Phase 2 Active: Experiment Selection

When the current phase is `phase_2_active` and the active task is experiment selection or prioritization, active artifacts should include:

- `docs/agent/research_direction.md`
- `docs/agent/hypotheses.md`
- `docs/agent/experiment_queue.md`

Use this status when the user asks:

- what experiment should be run next;
- which candidate experiment has the highest value;
- how to prioritize multiple experiments;
- how to manage limited compute;
- whether to defer, cancel, or promote experiment ideas.

Example:

    ## Phase
    - Current phase: `phase_2_active`
    - Current substep: experiment selection and prioritization

    ## Active Artifacts
    - `docs/agent/research_direction.md`
    - `docs/agent/hypotheses.md`
    - `docs/agent/experiment_queue.md`

    ## Next Step
    - Select one candidate from `docs/agent/experiment_queue.md` and promote it to `docs/agent/experiment_plan.md`.

### Phase 2 Active: Approved Experiment Planning

When a queue item has been promoted into a concrete experiment plan, active artifacts should include:

- `docs/agent/research_direction.md`
- `docs/agent/hypotheses.md`
- `docs/agent/experiment_queue.md`
- `docs/agent/experiment_plan.md`

When relevant, also include:

- `docs/agent/baseline_ledger.md`
- `docs/agent/ablation_matrix.md`
- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`

Example:

    ## Phase
    - Current phase: `phase_2_active`
    - Current substep: approved experiment planning

    ## Latest Action
    - Queue item `QUEUE-001` was promoted to experiment `EXP-001`.

    ## Active Artifacts
    - `docs/agent/research_direction.md`
    - `docs/agent/hypotheses.md`
    - `docs/agent/experiment_queue.md`
    - `docs/agent/experiment_plan.md`
    - `docs/agent/baseline_ledger.md`

    ## Next Step
    - Complete the baseline/control check before running `EXP-001`.

### Phase 2 Active: Experiment Execution

When experiment execution has started, active artifacts should include:

- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- `runs/<experiment_or_run_id>/`
- `outputs/experiments/<experiment_or_run_id>/`

When relevant, also include:

- `docs/agent/baseline_ledger.md`
- `docs/agent/ablation_matrix.md`
- `docs/agent/dataset_card.md`
- `docs/agent/leakage_audit.md`

Example:

    ## Phase
    - Current phase: `phase_2_active`
    - Current substep: experiment execution

    ## Active Artifacts
    - `docs/agent/experiment_plan.md`
    - `docs/agent/run_registry.md`
    - `docs/agent/experiment_journal.md`
    - `runs/EXP-001/`
    - `outputs/experiments/EXP-001/`

    ## Next Step
    - Record completed run outputs in `docs/agent/run_registry.md` and update `docs/agent/experiment_journal.md`.

### Phase 3 Active

When the current phase is `phase_3_active`, active artifacts should include the relevant experiment and result evidence.

For result interpretation tasks, active artifacts may include:

- `docs/agent/experiment_plan.md`
- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- `docs/agent/result_cards/`
- `docs/agent/result_interpretation.md`

For claim support tasks, also include:

- `docs/agent/result_to_claim_map.md`
- `docs/agent/claim_ledger.md`

For error, failure, or limitation tasks, also include:

- `docs/agent/error_analysis.md`
- `docs/agent/negative_results.md`

For figure/table tasks, also include:

- `docs/agent/figure_review.md`
- relevant `outputs/` paths

Do not list all Phase 3 artifacts by default.

List only the artifacts needed for the active result consolidation task.

### Early Red-Team Active Artifacts

Use early red-team artifacts before review reaches the manuscript stage.

- `docs/agent/pre_mortem.md` — red-team the research direction before freezing Phase 1.
- `docs/agent/experiment_red_team.md` — red-team expensive or claim-critical experiments before running.
- `docs/agent/evidence_review.md` — red-team interpreted evidence before turning it into manuscript claims.
- `docs/agent/red_team_issue_ledger.md` — track red-team issues and decisions across phases.

Early red-team artifacts live in `docs/agent/`.

Manuscript-stage review artifacts live in `paper/agent/`.

Do not wait until Phase 5 to identify missing baselines, weak assumptions, leakage risk, unsupported claims, or likely reviewer objections.

### Tool Workflow Active Artifacts

When the active task involves meaningful tool use, MCP use, lookup, retrieval, code execution, experiment execution, automated review, or workflow validation, active artifacts may include:

- `.agents/workflow/policies/tool_workflow_policy.md`
- `docs/agent/tool_routing_matrix.md`
- `docs/agent/tool_use_log.md`

Use:

- `.agents/workflow/policies/tool_workflow_policy.md` when deciding how a tool output becomes durable workflow state.
- `docs/agent/tool_routing_matrix.md` when selecting a tool for a workflow situation.
- `docs/agent/tool_use_log.md` when a meaningful tool-assisted action affects direction, implementation, experiment design, evidence, claims, manuscript text, review, or phase routing.

Do not list tool workflow artifacts during default `intake` unless the active task involves tool-use policy, tool routing, workflow validation, or tool-assisted state changes.

### Phase 4 Active

When the current phase is `phase_4_active`, active artifacts may include:

- `paper/`
- `paper/agent/`
- `paper/agent/section_notes.md`
- `paper/agent/claim_support.md`
- `paper/agent/citation_support.md`
- `paper/agent/figure_support.md`
- `docs/agent/claim_ledger.md`
- `docs/agent/result_interpretation.md`
- `sources/`

Use Phase 4 when the task involves:

- manuscript drafting;
- section rewriting;
- citation-supported writing;
- evidence-bound paper polishing;
- related work;
- method section writing;
- result section writing.

### Phase 5 Active

When the current phase is `phase_5_active`, active artifacts may include:

- `paper/`
- `paper/agent/review_context.md`
- `paper/agent/reviewer_outputs.md`
- `paper/agent/score_ledger.md`
- `paper/agent/revision_plan.md`
- `paper/agent/response_to_reviewers_draft.md`
- `paper/agent/claim_audit.md`
- `docs/agent/claim_ledger.md`
- `docs/agent/result_interpretation.md`

Use Phase 5 when the task involves:

- review;
- red-team critique;
- simulated reviewers;
- rebuttal planning;
- revision planning;
- response-to-reviewer drafting.

### Source and Literature Active Artifacts

When the live task involves literature search, source triage, paper reading, baseline discovery, citation support, related work, or reviewer-risk analysis, active artifacts may include:

- `sources/reading_queue.md`
- `sources/paper_cards/`
- `sources/literature_matrix.md`
- `sources/baseline_candidates.md`
- `sources/citation_intent_map.md`
- saved lookup outputs under `sources/`

Use these artifacts when the current task involves:

- closest prior work;
- novelty assessment;
- baseline selection;
- benchmark or dataset selection;
- related work;
- citation support;
- literature-dependent experiment design;
- reviewer-risk analysis.

Do not list all source artifacts by default during `intake`.

List only the source artifacts needed for the active task.

---

## Experiment Queue Status Rules

`docs/agent/experiment_queue.md` is a Phase 2 triage artifact.

It should appear in `docs/current_status.md` only when the live task involves:

- selecting experiments;
- prioritizing experiments;
- promoting an experiment idea;
- deferring an experiment idea;
- cancelling an experiment idea;
- comparing experiment ideas;
- deciding what to run next.

A queue item is not:

- an approved experiment;
- a running experiment;
- a completed run;
- interpreted evidence;
- support for a paper claim.

Do not treat `experiment_queue.md` as active merely because it exists.

Do not list `experiment_queue.md` in default `intake` status.

When a queue item is promoted, update `docs/current_status.md` to include both:

- `docs/agent/experiment_queue.md`
- `docs/agent/experiment_plan.md`

When execution starts, also include:

- `docs/agent/run_registry.md`
- `docs/agent/experiment_journal.md`
- relevant `runs/` and `outputs/` paths.

---

## Backfill Rules

Backfill is allowed when the project clearly contains enough evidence to reconstruct missing handoff artifacts.

Examples:

- Existing code and experiment configs can backfill part of Phase 2 planning.
- Existing metrics and logs can backfill a result summary.
- Existing paper claims can backfill a draft claim ledger.
- Existing related-work notes can backfill source context.
- Existing run folders can backfill a run registry.
- Existing experiment notes can backfill an experiment queue or experiment plan.

Backfill must not pretend that reconstructed context was originally approved.

Use these labels when needed:

- `reconstructed`
- `assumed`
- `needs_user_confirmation`
- `needs_evidence`
- `safe_to_use`

A backfilled artifact may support progress, but it should not become frozen until reviewed or approved.

---

## Blocker Rules

Use a blocker when useful work cannot proceed safely.

Good blockers are concrete.

Examples:

- required dataset path is missing;
- run outputs are unavailable;
- manuscript file is missing;
- baseline/control is unknown and cannot be inferred;
- claim depends on a missing citation;
- frozen research direction conflicts with requested work;
- experiment output exists but metric computation is not reproducible;
- user approval is required before freezing a reconstructed direction.

Avoid vague blockers.

Bad blocker examples:

- need more research;
- project unclear;
- phase-to-file contract not defined;
- maybe not enough context;
- should ask user later.

When possible, convert vague blockers into specific open questions or next actions.

---

## Open Question Rules

Use open questions for unresolved but non-blocking issues.

Examples:

- Which of these candidate experiments has the highest priority?
- Should the ablation focus on the loss term or data augmentation?
- Is the target venue NeurIPS, ICLR, ACL, CVPR, or another venue?
- Should the claim be narrowed to this dataset only?
- Should literature-only baseline numbers be treated as comparable?

Do not use open questions to avoid progress when a reasonable next step exists.

Open questions should be small enough that a human or agent can answer them.

---

## Next Step Rules

The `Next Step` section should state the next concrete action.

Good examples:

- Select one candidate from `docs/agent/experiment_queue.md` and promote it to `docs/agent/experiment_plan.md`.
- Complete the baseline/control section for `EXP-001`.
- Add the completed run to `docs/agent/run_registry.md`.
- Interpret `RUN-001` in `docs/agent/result_interpretation.md`.
- Update `docs/agent/claim_ledger.md` based on the result interpretation.
- Draft the Method section using `paper/agent/section_notes.md` and `docs/agent/implementation_notes.md`.
- Run review using `paper/agent/review_context.md`.

Bad examples:

- continue;
- keep working;
- do research;
- finish project;
- ask user;
- update files.

---

## Content Rules

Keep `docs/current_status.md` short.

Do not store:

- full research notes;
- full paper summaries;
- full manuscript text;
- full experiment logs;
- raw source dumps;
- reviewer essays;
- long debates;
- full tables;
- detailed metric reports;
- full code snippets.

Instead, link to durable artifacts:

- `docs/agent/`
- `paper/agent/`
- `sources/`
- `runs/`
- `outputs/`
- `paper/`
- `src/`
- `scripts/`
- `configs/`

---

## Evidence and Claim Discipline

`docs/current_status.md` may summarize evidence status, but it must not be the only evidence artifact.

For evidence and claims, use:

- `docs/agent/result_interpretation.md`
- `docs/agent/claim_ledger.md`
- `paper/agent/claim_support.md`
- `paper/agent/claim_audit.md`
- `sources/`

Do not put unsupported research claims in `docs/current_status.md`.

When status mentions a claim, also point to the claim artifact.

Example:

    ## Latest Action
    - Result interpretation suggests Claim `CL-003` should be downgraded from supported to preliminary.

    ## Active Artifacts
    - `docs/agent/result_interpretation.md`
    - `docs/agent/claim_ledger.md`

---

## Frozen Artifact Conflict Rules

If `docs/current_status.md` conflicts with frozen artifacts:

1. Inspect the frozen artifact.
2. Inspect the live status.
3. Determine whether the status is stale or whether the frozen artifact has been superseded.
4. Update `docs/current_status.md` if stale.
5. Mark the task `blocked` only if the contradiction cannot be resolved.

Do not let a stale status file override a frozen research direction, frozen experiment result, claim ledger, or manuscript artifact.

Do not let an outdated frozen artifact override newer validated evidence without recording the change.

---

## Existing Project Bootstrap Rules

When the scaffold is cloned into an existing research project, do not assume the project starts at Phase 1.

During `bootstrap_existing_project`, inspect available artifacts such as:

- source code;
- configs;
- scripts;
- tests;
- run folders;
- output folders;
- existing notes;
- papers;
- source files;
- claim ledgers;
- result summaries;
- manuscript drafts.

Then route to the latest valid phase whose prerequisites exist.

Use:

- `phase_1_active` if no usable direction, hypothesis, baseline, metric, or evaluation target can be found;
- `phase_2_active` if direction exists and implementation or experiment work is next;
- `phase_3_active` if runs, logs, outputs, metrics, or evaluation tables exist and need consolidation;
- `phase_4_active` if stable evidence exists and manuscript drafting or revision is next;
- `phase_5_active` if a manuscript or review package exists and critique, revision, or rebuttal planning is next;
- `backfill_required` if the likely target phase is identifiable but handoff artifacts are missing;
- `blocked` if project state cannot be determined from available files.

---

## Safe Default `docs/current_status.md`

A safe fresh-clone status should look like this:

    # Current Status

    ## Metadata
    - Status type: template_default
    - Project initialized: no
    - Last updated: YYYY-MM-DD
    - State source: `docs/workflow_state_machine.md`
    - Status protocol: `.agents/workflow/policies/current_status_policy.md`

    ## Phase
    - Current phase: `intake`
    - Current substep: scaffold ready; waiting for project bootstrap or first user request

    ## Latest Action
    - Repository workflow scaffold is available.
    - No project-specific research state has been initialized in this workspace yet.

    ## Active Artifacts
    - `docs/current_status.md`
    - `docs/workflow_state_machine.md`
    - `docs/research_gates.md`
    - `docs/agent/`
    - `paper/agent/`
    - `sources/`

    ## Blockers
    - None for the scaffold.
    - Project-specific phase is unknown until bootstrap or first task routing.

    ## Open Questions
    - Has this scaffold been cloned into an existing research project?
    - Should the next task initialize a new project or bootstrap from existing project artifacts?

    ## Next Step
    - If this is a new project, route the next user request through `intake`.
    - If this is an existing project, run existing-project bootstrap before choosing Phase 1, 2, 3, 4, or 5.

    ## Notes
    - This file is a live state pointer, not a narrative log.
    - Do not infer project progress from template-default status.
    - Replace `Status type: template_default` with `project_live` after project bootstrap or first real phase routing.

---

## Unsafe Default Status Patterns

Avoid these patterns in a fresh scaffold:

    - Current phase: not started

Use instead:

    - Current phase: `intake`

Avoid:

    - Blockers:
      - phase-to-file contract not yet defined

Use instead:

    - Blockers:
      - None for the scaffold.
      - Project-specific phase is unknown until bootstrap or first task routing.

Avoid:

    - Active Artifacts:
      - `docs/agent/experiment_queue.md`
      - `docs/agent/experiment_plan.md`
      - `docs/agent/run_registry.md`

during default intake.

Use Phase 2 artifacts only after the workflow has routed to a Phase 2 task that needs them.

---

## Minimal Update Checklist

Before finishing a task that changes workflow state, check:

- Did the active phase change?
- Did the active substep change?
- Did a blocker appear or disappear?
- Did the active artifact set change?
- Was a queue item promoted to an experiment plan?
- Did an experiment start, fail, complete, or get cancelled?
- Did result interpretation change claim support?
- Did manuscript or review work start?
- Did review send the project backward to an earlier phase?
- Is `docs/current_status.md` now stale?

If yes, update `docs/current_status.md`.

If no, leave it unchanged.

---

## Core Rule

`docs/current_status.md` is a live pointer, not scaffold history.

A committed template status should be safe, minimal, and non-blocking.

If it is stale, refresh it from durable artifacts before routing work.

List only the artifacts that matter for the current task.

Do not list `docs/agent/experiment_queue.md` in intake status.

List `docs/agent/experiment_queue.md` only when the live task is selecting, prioritizing, promoting, deferring, or cancelling candidate experiments.

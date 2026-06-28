# AGENTS.md

## Agent role

You are a repo-native AI research and engineering assistant.

Your job is to help develop rigorous, well-scoped research or engineering work. Depending on the project, this may involve theoretical reasoning, architectural design, empirical evaluation, dataset construction, benchmarking, literature synthesis, system building, or manuscript preparation.

You must adapt your behavior to the current project type and research stage instead of assuming that every task is empirical model development.

Keep all claims grounded in appropriate evidence:
- theoretical claims require assumptions, derivations, definitions, or logical argument;
- architectural claims require motivation, comparison to prior work, and a validation strategy;
- empirical claims require experiment artifacts, metrics, and reproducible settings;
- literature claims require cited sources or project literature artifacts;
- paper claims require traceable support.

This repository is not for unfocused exploration. Prefer well-motivated, scoped, and verifiable progress.

---

## Project map

- `.agents/guidance/` contains repo-owned guidance files for general research and engineering workflows.
- `.agents/skills/` contains repo-owned skills and bundled workflow tooling.
- `baselines/` contains baseline implementations or baseline references.
- `data/` contains dataset-related files, metadata, or local dataset references.
- `docs/` contains project planning, research context, workflow gates, and status documents.
- `notebooks/` contains interactive research workflows: exploration, prototyping, baseline training, visual debugging, qualitative analysis, and guided experiments.
- `runs/` contains experiment runs, logs, checkpoints, or tracked outputs.
- `outputs/` contains generated artifacts, metrics, figures, tables, and summaries.
- `paper/` contains manuscript or publication artifacts, paper-specific guidance, figures, tables, and claim support.
- `src/` contains implementation code.
- `scripts/` contains utilities, experiment helpers, and automation scripts.
- `tests/` contains tests.
- `tests/agent/` contains workflow-skeleton tests.

---

## Workflow Memory

Use repository artifacts, not chat, for durable research state.

Core locations:

- `docs/current_status.md` = short live state pointer.
- `docs/PROJECT_PLAN.md` = canonical initialized project plan.
- `docs/agent/` = research workflow artifacts.
- `paper/agent/` = manuscript and review support artifacts.
- `sources/` = external evidence and source-trace artifacts.

For source reading, claim-status vocabulary, early red-team records, and tool-output promotion rules, load `.agents/workflow/policies/workflow_memory_policy.md` only when the task touches those concerns.

---

## Workflow Intake / Mode Selection

Before entering any phase, classify the user request and route it to the correct workflow mode.

Routing:

- Broad idea, problem framing, novelty check, or research direction request -> Phase 1.
- Approved plan execution, code changes, or experiment implementation request -> Phase 2.
- Result analysis, table building, failure analysis, or claim-status update request -> Phase 3.
- Manuscript drafting, section writing, citation polishing, or claim-supported rewriting request -> Phase 4.
- Reviewer-style critique, red-team review, or revision request -> Phase 5.

Default intake:

1. Read the user prompt.
2. Inspect `docs/current_status.md`.
3. Load the matching phase contract.
4. If `docs/current_status.md` is stale, template-default, contradictory, or the phase flow is genuinely unclear, load `.agents/workflow/policies/workflow_intake_policy.md`; do not load it for routine phase routing.

Phase contracts:

After routing the task, always load the matching phase contract before taking workflow actions.

- Phase 1 -> `.agents/workflow/phases/phase_1_research_formalization.md`
- Phase 2 -> `.agents/workflow/phases/phase_2_implementation.md`
- Phase 3 -> `.agents/workflow/phases/phase_3_result_consolidation.md`
- Phase 4 -> `.agents/workflow/phases/phase_4_writing.md`
- Phase 5 -> `.agents/workflow/phases/phase_5_review.md`

Do not load all phase contracts by default. If a task crosses phases, load the earliest missing prerequisite phase first.

---

## Primary context sources

Before proposing major research, architecture, training, evaluation, or paper-writing changes, consult the smallest relevant subset of:

- `docs/PROJECT_PLAN.md`
- `docs/research_context.md`
- `docs/current_status.md`

Before major research direction, implementation, experiment, evaluation, or paper-claim changes, apply the relevant gate from `docs/research_gates.md`.

When the task involves high-risk direction, experiment, evidence, claim, or review decisions, also check relevant early red-team artifacts in `docs/agent/`, especially `pre_mortem.md`, `experiment_red_team.md`, `evidence_review.md`, and `red_team_issue_ledger.md`.

Do not infer the current research direction from memory alone.

If these files conflict, prefer the most project-specific and most recent status document. If the conflict matters, state it explicitly before proceeding.

---

## Policy Loading

When a task matches a policy condition below, load that policy before making the related decision, edit, claim, tool call, or workflow-state change.

---

## Rule Precedence

`AGENTS.md` is the always-loaded router and summary.

When a referenced phase contract or policy file is loaded, follow that file for detailed procedure, required artifacts, and phase-specific exit conditions.

If `AGENTS.md` and a loaded phase or policy file appear to conflict, prefer the more specific loaded file unless it would violate the core evidence, scope, or safety rules in `AGENTS.md`.

---

## Research Task Lifecycle

For non-trivial research or engineering tasks:

1. Classify the task.
2. Check the smallest relevant context.
3. Identify the intended artifact.
4. Plan narrowly.
5. Execute minimally.
6. Validate narrowly.
7. Report outcome.

Load `.agents/workflow/policies/task_lifecycle_policy.md` only when the task is substantial, cross-phase, ambiguous, or needs a detailed execution checklist.

---

## Evidence And Claims

Never present unsupported research claims as fact.

Use `.agents/workflow/policies/evidence_and_claim_policy.md` when the task involves experimental claims, novelty claims, literature claims, manuscript claims, result interpretation, or claim auditing.

Default rule:
- experimental claims require saved run/output/result artifacts;
- literature and novelty claims require saved source artifacts, paper cards, citation records, or explicit gap analysis;
- paper claims must trace to cited literature, experiment results, documented limitations, documented hypotheses, or project-approved assumptions.

---

## Engineering Defaults

For code, config, script, data, training, evaluation, packaging, notebook, or reproducibility changes, preserve typing, error handling, logging, modularity, explicit data contracts, and narrow validation.

Load `.agents/workflow/policies/engineering_policy.md` only when the task materially changes engineering artifacts or execution behavior; it routes to the smallest relevant `.agents/guidance/` file for Python, CV, or ML engineering details.

---

## Research Defaults

Before changing research direction, implementation, training, evaluation, or manuscript claims, define the project type, task, inputs, outputs, constraints, contribution target, and validation strategy.

Load `.agents/workflow/policies/research_policy.md` only when proposing or changing research direction, architecture, method design, dataset/evaluation assumptions, training setup, or manuscript claims.

---

## MCP Usage

Use approved MCP servers only when they provide fresher or more authoritative context than local project artifacts or model memory.

Load `.agents/workflow/policies/mcp_policy.md` only for code/API/library lookup, GitHub/issue/PR context, Hugging Face model/dataset/paper lookup, browser verification, or MCP client configuration.

---

## Skill Usage

Use skills as task tools, not as general background instructions.

Load `.agents/workflow/policies/skill_usage_policy.md` only when skill choice is unclear, multiple skills may apply, or the task risks loading unnecessary skills.

Default rule: select the smallest relevant skill or skill combination, and do not invoke writing, venue, image, review, or citation skills during code-only tasks unless explicitly requested.

---

## Scope And Boundaries

This repository supports focused research or engineering work, not unfocused exploration.

Allowed by default:

- scoped literature, theory, architecture, implementation, evaluation, or writing improvements;
- baseline or reference-point strengthening;
- reproducibility and documentation improvements;
- failure analysis, limitation analysis, and claim auditing;
- targeted refinements with clear motivation and validation.

Default boundaries:

- Prefer small, reviewable, verifiable changes.
- Do not modify unrelated files.
- Do not expand project scope implicitly.
- Do not edit `paper/` during code-only tasks unless explicitly asked.
- Do not claim experimental outcomes without artifacts in `runs/`, `outputs/`, or documented result files.
- Do not present generated hypotheses as established findings.
- Do not introduce dependencies without a clear reason.
- Do not change dataset split logic without explicit justification.
- Do not remove baselines unless explicitly requested.
- Do not overwrite experiment artifacts.

For major research, architecture, dataset, benchmark, evaluation, or paper-claim changes, state:

1. why it fits the current scope;
2. what prior work, baseline, or reference point it relates to;
3. what contribution or failure mode it targets;
4. how it can be validated;
5. what risk or tradeoff it introduces.

---

## Default response format

For substantial tasks, respond with:

1. **Task stage**
2. **Context checked**
3. **Files changed**
4. **Validation**
5. **Uncertainty / risks**
6. **Next recommended step**

For small tasks, keep the response concise but still mention changed files and validation when applicable.

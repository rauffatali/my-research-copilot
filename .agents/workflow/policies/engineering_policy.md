# Engineering Policy

Use this policy when the task changes code, configs, scripts, tests, data pipelines, training/evaluation execution, packaging, notebooks, or reproducibility infrastructure.

## Core Engineering Defaults

- Preserve or improve typing, error handling, and logging.
- Keep code modular and testable.
- Separate training, validation, evaluation, and inference behavior.
- Separate distinct execution modes into dedicated modules or entry points when control flow, scale, or validation behavior differs materially.
- Avoid magic numbers; prefer config-driven behavior.
- Prefer explicit data contracts over implicit assumptions.
- Preserve backward compatibility unless the task requires otherwise.
- Do not silently swallow exceptions.
- Do not perform opportunistic cleanup unless it directly supports the task.
- When changing behavior, update or add the narrowest relevant tests.

## Research-Code Reproducibility

For research code, preserve or record:

- config;
- seed;
- dataset version;
- split definition;
- run identity;
- code version;
- metric definition;
- environment/package versions when relevant.

Every serious run should leave enough information for another agent or human to reproduce the result.

## Validation Discipline

After meaningful code, data, training, or evaluation changes, run the narrowest feasible validation:

- unit test;
- smoke test;
- config validation;
- data-loader sanity check;
- metric script dry run;
- small synthetic example;
- formatting/linting check.

If validation is not run, record why.

## Data and Evaluation Contracts

For data loaders, preprocessing, metrics, and evaluation scripts:

- keep train/validation/test behavior clearly separated;
- avoid leakage across splits;
- document annotation, label, and metric contracts;
- validate shape, dtype, coordinate, class-index, and missing-data assumptions;
- preserve train/evaluation preprocessing parity unless the difference is explicit and justified.

## Experiment Execution

For training or evaluation scripts:

- log config and run identity;
- make output paths explicit;
- avoid overwriting run artifacts;
- fail loudly on missing required inputs;
- distinguish debug/smoke runs from claim-supporting runs;
- save metrics, logs, configs, and outputs in durable paths.

## Notebook Policy

- Use notebooks for exploration, prototyping, visual debugging, qualitative analysis, and guided experiments.
- Keep notebook purpose clear at the top.
- Record key configs, dataset paths, seeds, and outputs when results matter.
- Promote stable or repeated workflows to `scripts/` or `src/`.
- Do not treat notebook results as final evidence unless outputs/configs are saved in `runs/`, `outputs/`, or documented result artifacts.

## When To Load Extra Guidance

Use the smallest relevant reusable domain-specific guidance file:

- `.agents/guidance/python-dev.md` for Python packaging, typing, testing, logging, and reliability.
- `.agents/guidance/cv-dev.md` for computer vision data/label contracts, train/serve parity, and deployment realism.
- `.agents/guidance/cv-researcher.md` for baselines, ablations, evaluation design, slice analysis, and qualitative failure analysis.
- `.agents/guidance/ai-ml-research-dev.md` for ML reproducibility, experiment tracking, leakage checks, monitoring, and deployability.

Prefer the smallest relevant guidance set.

Do not consult all guidance files by default.

If multiple guidance files apply, state which ones are being used and why.
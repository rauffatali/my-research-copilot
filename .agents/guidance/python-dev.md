---
description: Use for Python engineering tasks needing maintainable code, typed APIs, packaging discipline, testing, logging, error handling, dependency hygiene, and reliable I/O.
---

# PYTHON DEVELOPMENT GUIDANCE

## Role

You are a Python development assistant.

## Goal

Help build maintainable, testable, typed, and reliable Python code.

Support research, experimentation, tooling, scripts, libraries, and lightweight applications without forcing unnecessary production complexity.

Prefer simple, explicit, well-tested code over clever abstractions.

---

## 1. Applicability

Use this guidance when the task involves:

- Python package or module design;
- scripts, CLIs, utilities, or automation;
- data processing code;
- experiment helpers;
- configuration handling;
- tests and testability;
- type hints and static analysis;
- logging and error handling;
- dependency or packaging changes;
- refactoring Python code.

Do not use this file for pure research reasoning, literature review, paper writing, or experiment interpretation unless Python implementation is involved.

Do not assume every Python task requires production deployment, CI expansion, security hardening, or packaging changes.

---

## 2.5 MCP-backed documentation

When Python code depends on fast-moving libraries, SDKs, or APIs, prefer current official docs or approved MCP servers such as Context7 before changing implementation details.

If MCP output changes a code path, record the relevant library, version, or API detail in the task artifacts so the decision is reproducible.

---

## 2. Core engineering discipline

- Prefer clarity over cleverness.
- Keep changes small and reviewable.
- Avoid unrelated cleanup.
- Preserve existing project conventions unless there is a clear reason to change them.
- Prefer explicit inputs and outputs over hidden global state.
- Keep functions focused and composable.
- Separate pure logic from side effects such as file I/O, network calls, subprocesses, logging, or environment access.
- Avoid magic numbers; use named constants or configuration.
- Do not introduce abstractions before there is repeated structure or a clear testing benefit.

When a task has distinct execution modes, split them by responsibility instead of hiding them behind one overloaded script:

- keep the main `train.py` focused on orchestration;
- put model definitions in dedicated modules such as `models.py` or `backbones.py` when they are reusable;
- create separate entry points such as `smoke_train.py` when a smoke run has different behavior, scale, or safety guarantees than the full run;
- prefer a dedicated fold runner or cross-validation entry point when cross-validation is materially different from ordinary training;
- use a flag only when the behavior is the same and only the configuration changes.

For non-trivial changes, state:

1. what behavior changes,
2. why the change is needed,
3. which files are affected,
4. how the change will be validated,
5. what risk or compatibility concern remains.

---

## 3. Project structure and packaging

Follow the existing repository layout first.

When packaging or imports matter:

- prefer a `src/` layout when the project already uses one;
- keep import paths stable;
- avoid circular imports;
- keep public APIs narrow and documented;
- use `pyproject.toml` as the source of truth for package metadata, dependencies, and tool configuration when applicable;
- define supported Python versions with `requires-python` when the project is packaged;
- avoid changing build backends unless explicitly requested or clearly necessary.

Do not convert a research script into a full package unless the task requires reuse, testing, or distribution.

---

## 4. Typing

Use type hints for public functions, class constructors, returned data structures, and important internal boundaries.

Prefer:

- precise built-in generic types such as `list[str]`, `dict[str, float]`, and `tuple[int, int]`;
- `Path` instead of raw string paths when working with files;
- `TypedDict`, `dataclass`, `Protocol`, or small domain classes when they clarify contracts;
- `Literal` or enums for constrained string options;
- `Optional` only when `None` is a real supported state.

Avoid:

- unnecessary `Any`;
- over-complex generic abstractions;
- type ignores without a short explanation;
- runtime behavior that contradicts type hints.

For research code, typing should clarify data contracts without making rapid iteration painful.

---

## 5. Configuration

Keep configuration explicit and reproducible.

Prefer:

- config files, dataclasses, typed dictionaries, or structured argument parsing;
- clear defaults;
- validation of required fields;
- paths resolved through `pathlib.Path`;
- saving or logging important config values when they affect experiments or outputs.

Avoid:

- scattered global constants;
- hidden environment assumptions;
- hard-coded local paths;
- silently falling back to incorrect defaults.

For experiment-related code, preserve enough configuration to reproduce the run.

---

## 6. Error handling

Validate inputs at boundaries:

- CLI arguments;
- config files;
- environment variables;
- external files;
- dataset metadata;
- API or network responses;
- user-provided paths.

Use precise exceptions with helpful messages.

Preserve root causes when wrapping exceptions.

Do not silently swallow exceptions.

Avoid broad `except Exception` unless:

- the error is logged with context,
- the fallback behavior is intentional,
- the caller can still detect failure when needed.

Failure messages should help the next agent or developer fix the issue.

---

## 7. Logging and user feedback

Use `logging` for reusable code and production-like paths.

Use `print()` only for simple scripts, notebooks, demos, or intentionally user-facing CLI output.

Log useful context such as:

- input path;
- output path;
- config name;
- dataset or split name;
- run identifier;
- number of processed items;
- skipped or invalid records;
- elapsed time when relevant.

Do not log secrets, tokens, private data, or large raw payloads.

For long-running scripts, include progress or summary logging when useful.

---

## 8. File and I/O reliability

For file operations:

- use `pathlib.Path`;
- check that required inputs exist;
- create output directories intentionally;
- avoid overwriting important artifacts unless explicitly requested;
- write critical outputs atomically when feasible;
- use explicit encodings for text files;
- handle empty, malformed, or missing files intentionally.

For data or experiment artifacts:

- preserve existing outputs unless the task explicitly requests regeneration;
- write outputs to documented locations;
- include enough metadata to understand how the artifact was created.

For network calls:

- set timeouts;
- use bounded retries only when appropriate;
- make failures observable;
- avoid infinite retry loops.

---

## 9. Dependencies

Prefer the standard library when it is sufficient.

Before adding a dependency:

1. check whether the project already has a suitable dependency,
2. explain why the new dependency is needed,
3. update the relevant dependency file,
4. consider maintenance, size, license, and compatibility risk.

Avoid heavyweight dependencies for small utilities.

Do not change dependency managers or lockfile strategy unless explicitly requested.

For applications or reproducible environments, use lockfiles when the project already follows that pattern.

---

## 10. Testing

Use the narrowest useful validation for the task.

Prefer `pytest` for Python tests.

Add or update tests when changing:

- parsing;
- config loading;
- data validation;
- preprocessing;
- metrics;
- file I/O behavior;
- error handling;
- public APIs;
- non-trivial business or research logic.

Useful test types:

- unit tests for pure logic;
- regression tests for bug fixes;
- smoke tests for scripts or pipelines;
- golden tests for fixed input/output behavior;
- temporary synthetic examples for data or metric behavior.

Do not add heavy integration tests for small refactors.

If tests are not run, state why.

---

## 11. Formatting and linting

Follow the repository’s configured tools.

Prefer:

- `ruff format` for formatting when configured;
- `ruff check` for linting when configured;
- `mypy` or `pyright` when the project already uses static type checking.

Do not reformat unrelated files.

Do not introduce a new formatter, linter, or type checker without a clear project-level reason.

---

## 12. Performance

Optimize only after identifying a real bottleneck or expected scale issue.

When performance matters:

- measure before and after;
- prefer algorithmic improvements over micro-optimizations;
- avoid unnecessary disk reads, repeated parsing, or repeated model loading;
- use batching for data/model workflows when appropriate;
- use NumPy, PyTorch, pandas, or vectorized operations where they clearly improve clarity or speed;
- keep memory usage reasonable for expected dataset size.

Do not make code harder to read for unmeasured speed gains.

---

## 13. Scripts and CLIs

For scripts under `scripts/`:

- include a clear entry point;
- use `argparse`, Typer, or the project’s existing CLI pattern;
- document required inputs and generated outputs;
- validate paths and arguments early;
- return non-zero exit behavior on failure when appropriate;
- keep reusable logic in `src/` when it is shared or tested.

A script should be safe to run from a clean checkout if required inputs are available.

---

## 14. Notebooks and research code

For notebooks or exploratory code:

- keep exploratory logic understandable;
- record important paths, configs, seeds, and outputs;
- avoid treating notebook-only results as final evidence;
- move stable repeated logic into `scripts/` or `src/`;
- avoid hidden state that makes reruns misleading.

Research code may be lighter than production code, but it should still be reproducible enough to support later claims.

---

## 15. Final checklist

Before finalizing substantial Python work, check:

1. [ ] The change is scoped to the requested task.
2. [ ] Public or important functions have useful type hints.
3. [ ] Inputs, outputs, paths, and configs are explicit.
4. [ ] Errors fail loudly with useful messages.
5. [ ] Logging or user-facing output is appropriate for the code path.
6. [ ] Dependencies were not added unnecessarily.
7. [ ] Tests or the narrowest feasible validation were run, or skipping was explained.
8. [ ] Formatting/linting follows existing project tools.
9. [ ] Research or experiment code preserves reproducibility-relevant information.
10. [ ] No unrelated files or artifacts were changed.

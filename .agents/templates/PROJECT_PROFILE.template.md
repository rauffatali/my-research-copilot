# Project Profile

## Status
- `template_default`
- Allowed values: `template_default`, `configured`, `superseded`

## Operational Configuration

- `project_type`: `UNASSIGNED`
- `venue_or_output_target`: `UNASSIGNED`
- `main_manuscript_path`: `UNASSIGNED`
- `execution_mode`: `UNASSIGNED`
- `execution_target`: `UNASSIGNED`

## Field Semantics

### `project_type`

`project_type` is a compact operational classification used for routing. Generic examples include
`empirical_ml`, `computer_vision`, `theory`, `tooling`, `dataset`, `manuscript`, `mixed`, and `other`.
It is not a substitute for the richer scientific and narrative framing in `docs/research_context.md`.

If `project_type` conflicts materially with `docs/research_context.md`, do not silently choose one. Flag
the configuration inconsistency and resolve it explicitly.

### `venue_or_output_target`

`venue_or_output_target` is the project-local publication, benchmark, deliverable, product, or other
output target. Generic examples include a journal or conference name, an internal report, a software
release, a dataset release, or a benchmark. `UNASSIGNED` and `NOT_APPLICABLE` are valid values where
appropriate. Venue or output constraints may affect formatting, packaging, or style, but they do not
independently change evidence, claim strength, experimental interpretation, or truth conditions.

### `main_manuscript_path`

`main_manuscript_path` is the project-local protected manuscript integration target. When configured, it
must be a valid project-relative path. Example format only:

```text
relative/path/to/main-manuscript-file
```

Use `UNASSIGNED` when the target has not been resolved and `NOT_APPLICABLE` when protected manuscript
integration intentionally does not apply. Do not guess a filename from this template or from a generic
repository layout.

### `execution_mode`

`execution_mode` is a project-local execution-routing value. Allowed values are:

```text
UNASSIGNED
local
remote
hybrid
none
```

### `execution_target`

`execution_target` identifies the project-local execution environment when relevant. It may represent a
host alias, scheduler or environment name, container or environment identifier, or another project-local
infrastructure target. Do not put absolute machine paths, hostnames, cluster names, scheduler accounts,
cloud account identifiers, or local usernames in this reusable template. Use `UNASSIGNED` or
`NOT_APPLICABLE` where appropriate.

## Sentinel Semantics

`UNASSIGNED` means:

> This configuration has not yet been resolved.

`NOT_APPLICABLE` means:

> This configuration was intentionally determined not to apply to the project.

These sentinels belong to project configuration. They are not workflow states, evidence states, or claim
support statuses.

## Related Configuration

- Agent-role assignments and candidate-writer settings:
  `docs/agent/agent_role_profile.md`
- Research framing:
  `docs/research_context.md`
- Project plan:
  `docs/PROJECT_PLAN.md`
- Research Copilot provenance:
  `docs/copilot_upstream.md`

## Notes

- This profile stores stable operational configuration only; it does not store live experimental results,
  evidence states, claim verdicts, or manuscript support status.
- Role assignments and writer configuration remain canonical in `docs/agent/agent_role_profile.md`.
- Configure values only from explicit project decisions or authorized current-task instructions.

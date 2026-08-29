# Project Configuration Policy

## Purpose

Separate reusable Research Copilot kernel behavior from stable project-specific operational values and
mutable project research state. Project configuration routes work; it does not become a second research
state ledger or grant permissions.

## Layer boundary

### Upstream kernel

The reusable kernel includes policies, workflows, skills, templates, canonical guidance, and workflow
validation tooling. It must remain project-neutral unless an explicitly recorded local kernel override
exists.

### Project configuration

Project configuration contains stable operational values for one downstream project, including the
project type, output target, protected manuscript target, execution settings, role assignments, writer
configuration, and upstream provenance.

### Project state

Project state contains mutable research and workflow information, including current direction, plans,
implementation state, experiments, evidence, claims, manuscript drafts, support artifacts, and workflow
status.

Do not merge these layers or turn project state into kernel configuration.

## Canonical sources

```text
docs/project_profile.md
→ operational project configuration

docs/agent/agent_role_profile.md
→ role/model/harness assignments + writer configuration

docs/research_context.md
→ scientific framing

docs/PROJECT_PLAN.md
→ execution plan

docs/copilot_upstream.md
→ kernel provenance/sync record
```

`docs/project_profile.md` must not duplicate role or writer fields from the role profile, or live
experiment, evidence, result, claim, or manuscript-support fields from project-state artifacts.

## Loading rule

Do not load `docs/project_profile.md` for every trivial task. Load it when the operation depends on:

- project type;
- venue or output target;
- protected manuscript integration target;
- execution environment; or
- project-specific operational routing.

For upstream or kernel synchronization work, also load `docs/copilot_upstream.md` and
`.agents/workflow/policies/upstream_sync_policy.md`.

## Fail-closed rule

If a configuration field required for the current operation is `UNASSIGNED`, missing, invalid, or
contradictory, do not guess it. Resolve it through an explicit project-profile correction or explicit
current human instruction.

An explicit current human instruction may resolve the immediate operation without permanently changing the
project profile unless the human asks for a permanent profile change. Do not block unrelated work merely
because an unrelated configuration field remains unresolved.

If `project_type` conflicts materially with `docs/research_context.md`, flag the inconsistency and resolve
it rather than silently choosing one. If `main_manuscript_path` is unresolved, drafting in `paper/draft/`
may continue, but protected integration cannot proceed until a target is resolved.

## `NOT_APPLICABLE`

If the relevant value is `NOT_APPLICABLE`, do not attempt that operation under normal project configuration
unless the human explicitly changes the project configuration or authorizes a clearly scoped exception.

## Project-configuration precedence

For project-operational values, use this precedence:

```text
explicit current human instruction
→ configured project-local profile
→ canonical upstream/kernel default
```

This precedence does not override role or permission policy. Overall governance remains:

```text
human authority
+
active role permission boundary
+
project configuration
+
workflow policy
+
skill/tool behavior
```

A configured `main_manuscript_path` does not grant write permission. A `candidate_writer` or
`independent_reviewer` still cannot integrate into that path, and protected integration still requires
the normal role and human-authorization gate.

## No automatic project-profile mutation

Skills, tools, workflow phases, and models must not silently rewrite `docs/project_profile.md`,
`docs/copilot_upstream.md`, or `docs/agent/agent_role_profile.md` merely because they infer a value.
A durable configuration change requires explicit human instruction or a clearly authorized
project-configuration update. Current-task instructions may be treated as scoped overrides when
appropriate.

## Operational-only routing

`project_type`, `venue_or_output_target`, `execution_mode`, and `execution_target` are routing or
packaging inputs. They do not independently alter scientific evidence, claim strength, experimental
interpretation, or truth conditions. Substantive scientific changes remain under the normal research-lead,
evidence, and claim workflows.

## Ownership by artifact purpose

Do not infer ownership from a directory alone. For example, `docs/workflow_state_machine.md` is reusable
canonical workflow documentation, while `docs/current_status.md` is project state. Likewise,
`paper/AGENTS.md` may contain reusable manuscript workflow guidance, while `paper/draft/` and
`paper/agent/` contain project manuscript state and support artifacts.

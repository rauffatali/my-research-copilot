# Upstream Sync Policy

## Purpose

Allow downstream projects to receive future Research Copilot kernel improvements while preserving project
configuration and project state. This is reusable governance, not an automated sync script; do not create
a sync program from this policy alone.

## Version and Git revision separation

`RESEARCH_COPILOT_VERSION` is upstream/kernel-owned.

- Downstream projects do not normally edit it.
- Project-local changes do not automatically bump the kernel version.
- The kernel version changes only when maintaining or releasing the reusable Research Copilot kernel.
- Git revision is tracked separately from the version.
- A version may be known while an exact clean Git revision is unknown.
- Never fabricate an upstream revision for a dirty or uncommitted kernel snapshot.
- The current development version is `2.0.0-beta.1`.
- A future release may intentionally change the marker to an explicit released version such as `2.0.0`.

Do not treat the current Git HEAD as the exact v2 imported or synced revision when the v2 kernel is still
represented by uncommitted working-tree changes.

## Human authorization

Actual upstream synchronization is a high-impact repository-maintenance operation. Require explicit
`human_researcher` authorization before applying an upstream kernel sync.

- `research_lead` may assess compatibility and identify conflicts.
- `implementation_agent` may apply an authorized bounded sync.
- `independent_reviewer` remains strictly read-only.

## Before sync

Inspect and record, as applicable:

```text
current RESEARCH_COPILOT_VERSION
docs/copilot_upstream.md
current Git branch
current Git revision
working-tree status
target upstream version
target upstream revision when available
recorded local kernel overrides
```

Never automatically reset, clean, stash, discard project changes, or otherwise destroy local work because
the project is dirty. Dirty state is a condition to inspect, not permission to destroy local work.

## Protect project configuration and state

An upstream sync must not blindly overwrite project-local configuration or state, including:

```text
docs/project_profile.md
docs/copilot_upstream.md
docs/agent/agent_role_profile.md
docs/research_context.md
docs/PROJECT_PLAN.md
docs/current_status.md
docs/agent/ live research artifacts
sources/
runs/
outputs/
paper/draft/
paper/agent/
project source/data/results
```

These files and directories may be migrated only when the human explicitly authorizes a specific bounded
migration. “Copy upstream over project” is not a valid update strategy.

## Upstream-managed material

Kernel material may include:

```text
RESEARCH_COPILOT_VERSION
AGENTS.md
.agents/guidance/
.agents/workflow/
.agents/skills/
.agents/templates/
canonical workflow documentation/checkers
```

Some downstream projects may intentionally modify kernel files. Those changes become local kernel
overrides and should be recorded in `docs/copilot_upstream.md` before or while synchronizing. Do not
assume every `.agents/` file is pristine upstream material when an override is recorded.

Ownership is by artifact purpose, not by a simplistic directory-wide rule. For example,
`docs/workflow_state_machine.md` is reusable workflow documentation while `docs/current_status.md` is
project state; `paper/AGENTS.md` may be reusable guidance while `paper/draft/` and `paper/agent/` are
project manuscript state/support artifacts.

## Sync procedure

Use this bounded procedure:

```text
inspect current project
→ identify current upstream baseline
→ identify target upstream version/revision
→ diff upstream kernel changes
→ classify conflicts with local kernel overrides
→ apply bounded kernel changes
→ preserve project configuration/state
→ resolve conflicts explicitly
→ run workflow/skill validation
→ only after successful validation update docs/copilot_upstream.md
```

Do not update the provenance record before validation succeeds.

## Failure

If sync validation fails:

```text
do not claim successful sync
do not advance last_synced_version/revision
preserve failure details
```

Do not invent automatic rollback commands in this policy. Require a reversible diff or known recovery path
appropriate to the actual operation.

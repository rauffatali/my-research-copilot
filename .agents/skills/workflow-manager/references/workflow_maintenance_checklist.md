# Workflow Maintenance Checklist

Use this checklist when reviewing the workflow guidance itself, especially after adding or changing workflow docs, references, or phase rules.

## Checkpoints

- The skill description still matches the current workflow purpose.
- `SKILL.md` points to the current reference files only.
- `docs/workflow_state_machine.md` remains the canonical transition source.
- `docs/current_status.md` is still the live pointer, not a hidden project log.
- `docs/agent/` contains output artifacts, not workflow guidance.
- `paper/agent/` contains manuscript-support artifacts, not workflow guidance.
- Workflow examples live in the skill reference area, not in output folders.
- Naming rules live in the skill reference area, not in output folders.
- Phase ownership rules are explicit enough to prevent accidental cross-phase edits.
- The blocked state is used for missing dependencies, not for vague uncertainty.
- The archived state is terminal for the current thread.
- Review rollback paths are still correct and not contradictory.
- The validator and state checker are still described as structure checks, not proof of progress.
- Example prompts still cover phase routing, blocked cases, no-op cases, and cross-phase cases.
- If a new workflow file was added, it is referenced from the skill and not duplicated elsewhere.

## Pass condition

The workflow guidance passes audit when each checkpoint is true or when any exception is documented in `docs/current_status.md`.

## Fail condition

The workflow guidance needs revision when guidance is duplicated, references are stale, phase ownership is unclear, or the live state no longer matches the workflow rules.

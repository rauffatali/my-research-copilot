# Current Status

## Purpose

This is the shared live status file across all workflow phases.

The agent must update this file whenever the working state changes in a way that affects the next action, the active phase, the active artifacts, or the current blockers.

## Update rules

- Update this file after each user prompt that changes the active task or phase.
- Update this file after each meaningful action, decision, or artifact write.
- Update this file after each phase handoff.
- Update this file after any blocker is discovered or resolved.
- Update this file after any change to the active artifact paths.
- Keep this file concise and current; do not treat it as a long narrative log.
- Link to durable artifacts instead of repeating their full contents here.
- If the task moves backward to an earlier phase, record the reason explicitly.
- If the task is ambiguous, record the ambiguity and the smallest next question or decision needed.

## Required fields

Every status update should include:

- Current phase
- Current substep
- Latest action
- Active artifact paths
- Blockers or open questions
- Next recommended step

## Optional fields

Use these when they help the next step:

- Current reviewer role
- Current round number
- Latest evidence source
- Relevant skill in use
- Whether the current artifact is draft, frozen, or superseded

## Content rules

- Keep the status short enough to scan quickly.
- Prefer bullets over long paragraphs.
- Do not store full research notes, long summaries, or manuscript text here.
- Do not use this file as a substitute for `docs/agent/`, `paper/agent/`, or `sources/`.
- The file should always point to the latest durable artifact for the current phase.

## Suggested structure

```md
# Current Status

## Phase
- Current phase:
- Current substep:

## Latest Action
- Latest action:

## Active Artifacts
- [path]
- [path]

## Blockers
- [blocker or none]

## Next Step
- [next step]
```

## Status

- Current phase: not started
- Current substep: repository scaffold setup
- Latest action: created workflow memory scaffold files
- Active artifact paths:
  - `docs/current_status.md`
  - `docs/agent/README.md`
  - `paper/agent/README.md`
  - `sources/README.md`
- Blockers:
  - phase-to-file contract not yet defined
- Next recommended step:
  - define per-phase artifact ownership and transition rules

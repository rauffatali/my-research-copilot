# Agent Role Policy

## Purpose

The workflow phase answers what kind of research work is happening. The active agent role answers what the current invocation is permitted and responsible to do. Phase and role are orthogonal, and every invocation must obey both contracts.

The reusable workflow defines role semantics only. Project-local assignments belong in `docs/agent/agent_role_profile.md`.

## Canonical roles

| Identifier | Role |
|---|---|
| `human_researcher` | Human Researcher / Governor |
| `research_lead` | Research Lead / Adjudicator |
| `independent_reviewer` | Independent Reviewer / Critic |
| `implementation_agent` | Implementation Agent |
| `candidate_writer` | Candidate Writer |
| `integration_agent` | Integration Agent |

Projects need not instantiate every optional role at the same time.

## Human Researcher / Governor (`human_researcher`)

`human_researcher` is the final project authority. The human may:

- approve or reject research direction;
- authorize high-impact promotion decisions;
- authorize major protocol changes;
- authorize main-manuscript integration when manuscript rules are implemented;
- authorize destructive repository actions when applicable; and
- assign or change project-local agent-role mappings.

AI readiness or acceptance is not the same as human authorization. A readiness recommendation, reviewer agreement, draft acceptance, or validation result does not itself authorize a protected or high-impact promotion.

## Research Lead / Adjudicator (`research_lead`)

`research_lead` is primarily responsible for:

- reconstructing project state;
- scientific reasoning and architecture or research planning;
- identifying uncertainties;
- producing bounded execution briefs;
- evaluating evidence and comparing alternatives;
- adjudicating reviewer findings;
- reviewing execution-agent output;
- determining readiness; and
- recommending the next action.

The lead may write planning, adjudication, or status artifacts when normal project policy permits. It is not automatically the implementation agent or the integration agent, and it must not silently take over bounded execution work simply because it can.

## Independent Reviewer / Critic (`independent_reviewer`)

`independent_reviewer` is a strictly read-only role. This is a role invariant.

It may:

- read and search repository files;
- inspect source, evidence, manuscript, log, result, and Git artifacts using read-only operations, including Git status, history, and diffs;
- run genuinely read-only analysis where safe;
- independently reconstruct relevant context;
- challenge assumptions and report contradictions;
- identify missing evidence, methodological weaknesses, and likely failure modes; and
- recommend corrections in its response.

It must never:

```text
edit
create
delete
rename
patch
stage
commit
push
write status files
write review artifacts
write claim-audit artifacts
perform "small helpful fixes"
```

The reviewer returns findings in its response. A writable role may later record an accepted or adjudicated finding. A normally writable skill or tool cannot override this boundary; when acting as `independent_reviewer`, the role remains read-only. If the same underlying agent is later needed to edit, the new invocation must be explicitly reassigned to a writable role. Read-only reviewer mode and writable executor mode must not be blurred within one invocation.

## Implementation Agent (`implementation_agent`)

`implementation_agent` is a bounded writable execution role. It should:

- receive a scoped implementation or engineering task;
- modify only authorized files;
- follow relevant plans and repository rules;
- validate its changes;
- report exactly what changed; and
- avoid independently changing scientific direction.

It is an executor, not the final scientific authority.

## Candidate Writer (`candidate_writer`)

`candidate_writer` is a generic bounded execution role that produces manuscript candidates when a manuscript workflow requests them. Candidate writers are not final scientific authorities, and the canonical role does not impose a fixed count. For substantive semantic manuscript work:

- Multiple agents or invocations may simultaneously occupy the `candidate_writer` role.
- The required count is read from `docs/agent/agent_role_profile.md`, using the project-local `candidate_writers_required` field.
- Candidate slot IDs are project-local assignment identifiers and do not create new canonical roles.
- Candidate independence and cross-visibility follow the project-local `candidate_independence_required`
  and `candidate_cross_visibility_before_comparison` fields.
- Actual agent, model, provider, and harness identities remain project-local.

All candidate writers remain bounded execution agents and must obey manuscript-specific workflow rules when those rules are loaded. Detailed manuscript-writing policy is defined elsewhere and is not established by this role contract. The scaffold template may initialize a project with a default count, but canonical role semantics impose no fixed number.

## Integration Agent (`integration_agent`)

`integration_agent` is a writable promotion and execution role. It may execute an already-approved change into a protected or final target only when the required human authorization exists.

It must not infer authorization from:

- lead approval;
- reviewer approval;
- draft acceptance; or
- validation success.

Human authorization remains distinct from AI readiness and other internal approvals.

## One active role per invocation

An invocation operates under one active role contract at a time. An underlying agent, model, or harness may serve different roles in different invocations, but permissions are determined by the active role rather than by technical capability. A human may reassign the role between invocations; a skill or tool must not silently change it during an invocation.

## Permission precedence

Apply repository behavior in this order:

1. explicit human authorization or project instruction;
2. the active role permission boundary;
3. phase and workflow policy; and
4. skill or tool default behavior.

Human authorization for a protected action requires an appropriate writable role; it does not turn a read-only reviewer invocation into a writable invocation. A skill or tool must not silently override the active role's permission boundary. For example, `independent_reviewer` combined with a normally writable review skill remains read-only.

## Project-local role mapping

The reusable kernel defines role semantics only. Actual assignments of roles to agents, models, providers, or harnesses belong in `docs/agent/agent_role_profile.md`, including any project-specific permission notes. Multiple physical agents or models may be mapped to the same role class where appropriate. Canonical role-policy files must not contain project-specific assignments.

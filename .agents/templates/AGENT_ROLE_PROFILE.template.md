# Agent Role Profile

## Metadata
- Status: template_default
- Last updated: YYYY-MM-DD

## Role Assignments

| Role | Assigned agent/model/harness | Writable | Notes |
|---|---|---:|---|
| `human_researcher` | project owner | n/a | Final project authority |
| `research_lead` | UNASSIGNED | bounded | Scientific reasoning and adjudication |
| `independent_reviewer` | UNASSIGNED | no | Strictly read-only |
| `implementation_agent` | UNASSIGNED | yes, bounded | Code/config execution |
| `candidate_writer` | see candidate slots below | yes, bounded | Manuscript candidate execution; assignments are slot-based |
| `integration_agent` | UNASSIGNED | gated | Protected promotion/integration only after human authorization |

## Manuscript Candidate Writer Configuration

These are project-local configuration values. The reusable workflow does not universally require two
writers.

- `candidate_writers_required`: 2
  - number of initial candidate-writer outputs required for a substantive semantic writing slice
- `candidate_independence_required`: true
  - whether those required initial candidates must be produced independently
- `candidate_cross_visibility_before_comparison`: false
  - whether candidate writers may inspect one another's drafts before `research_lead` comparison

The template default is 2 because this scaffold initializes projects with dual independent candidate
drafting unless the project owner changes it.

### Candidate Writer Assignments

| Slot | Assigned agent/model/harness | Notes |
|---|---|---|
| `candidate_1` | UNASSIGNED | Candidate writer slot; independence follows project configuration |
| `candidate_2` | UNASSIGNED | Candidate writer slot; independence follows project configuration |

Adjust the number of assignment rows when project configuration changes. Slot names are local
identifiers; every slot still operates under the canonical `candidate_writer` role.

## Role Rules

- Assignments are project-local.
- Model, provider, and harness names belong here, not in canonical workflow policy.
- One underlying agent may occupy different roles in separate invocations.
- The active role's permission boundary applies for the entire invocation.
- `independent_reviewer` is always read-only.
- `integration_agent` requires explicit human authorization for the protected action.

## Project Notes

- Add project-specific role constraints here.
- Replace template-default assignments during project bootstrap or when a multi-agent workflow is first configured.

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

- `candidate_writers_required`: 2
- `candidate_independence_required`: true
- `candidate_cross_visibility_before_comparison`: false

These values are initialization defaults and may be changed project-locally without changing canonical
workflow files. They control the number of initial candidate-writer outputs required for a substantive
semantic writing slice, whether those required initial candidates are produced independently, and whether
candidates may see one another's drafts before `research_lead` comparison. This `template_default` profile
is not considered configured merely because defaults exist.

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

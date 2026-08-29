# Research Copilot Upstream Record

## Status
- Status: template_default
- Allowed values: `template_default`, `tracked`, `superseded`

## Upstream Identity

- `upstream_source`: `https://github.com/rauffatali/my-research-copilot.git`
- `initialized_from_version`: `2.0.0-dev`
- `initialized_from_revision`: `UNASSIGNED`

## Last Successful Sync

- `last_synced_version`: `2.0.0-dev`
- `last_synced_revision`: `UNASSIGNED`

## Version and Revision Semantics

`RESEARCH_COPILOT_VERSION` records the upstream kernel version lineage. Git revision is tracked
separately and is populated only when an exact upstream snapshot is known.

Revision fields are intentionally `UNASSIGNED` while the v2 kernel is represented by uncommitted
working-tree changes. Populate them only when an exact upstream snapshot is known. The pre-existing Git
HEAD is therefore not recorded as the exact v2 kernel revision.

## Local Kernel Overrides

| Path | Reason | Upstream-sensitive? | Notes |
|---|---|---|---|
| None recorded | | | |

The current uncommitted development patch is not classified as a downstream override; this repository is
currently being developed as the Research Copilot kernel/template.

## Sync Notes

- The current development version is `2.0.0-dev`.
- `last_synced_version` and `last_synced_revision` must advance only after a bounded upstream sync
  validates successfully.

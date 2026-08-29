# Research Copilot Upstream Record

## Status
- `template_default`
- Allowed values: `template_default`, `tracked`, `superseded`

## Upstream Identity

- `upstream_source`: `UNASSIGNED`
- `initialized_from_version`: `[read from RESEARCH_COPILOT_VERSION at initialization]`
- `initialized_from_revision`: `UNASSIGNED`

## Last Successful Sync

- `last_synced_version`: `[version]`
- `last_synced_revision`: `UNASSIGNED`

## Version and Revision Semantics

- `RESEARCH_COPILOT_VERSION` is the upstream/kernel-owned release or development-lineage marker.
- A Git revision identifies a repository snapshot when an exact snapshot is known; it is not the kernel
  version.
- A version may be known while the exact clean Git revision is unknown.
- Never fabricate an upstream revision for a dirty or uncommitted kernel snapshot.
- Downstream project configuration and state are not replaced by an upstream version or revision.

## Local Kernel Overrides

| Path | Reason | Upstream-sensitive? | Notes |
|---|---|---|---|
| None recorded | | | |

## Sync Notes

- Record local kernel overrides here before or during an authorized sync.
- Advance `last_synced_version` and `last_synced_revision` only after the bounded sync validates
  successfully.

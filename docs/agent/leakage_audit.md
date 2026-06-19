# Leakage Audit

## Status

- draft
- Allowed values: draft, passed, failed, partial, superseded

## Purpose

This file records leakage checks that affect whether experiment results are trustworthy.

Do not claim “no leakage” unless this file or an equivalent output artifact supports it.

## Audit Summary

| Audit ID | Dataset | Experiment | Status | Main risk | Decision |
|---|---|---|---|---|---|
| LEAK-001 | DATA-001 | EXP-001 | draft / passed / failed / partial | | proceed / fix / rerun / block claims |

---

## LEAK-001: [Audit Name]

### Status

- draft
- Allowed values: draft, passed, failed, partial, superseded

### Linked Dataset and Experiment

- Dataset card: `docs/agent/dataset_card.md#data-001`
- Experiment plan: `docs/agent/experiment_plan.md#exp-001`
- Run registry, if already run:

### Split Integrity

Check:

- [ ] train/validation/test split source is documented
- [ ] split generation code or file is saved
- [ ] no known duplicate IDs across splits
- [ ] no known near-duplicate samples across splits
- [ ] no repeated scenes/entities/users/patients/videos across splits when relevant
- [ ] no augmented copies cross splits
- [ ] no evaluation examples used for training, tuning, prompt iteration, or threshold selection

### Label and Metadata Leakage

Check:

- [ ] filenames do not encode labels
- [ ] folder paths do not encode labels in unintended ways
- [ ] metadata fields do not leak target labels
- [ ] timestamps/location/device/source fields are safe or explicitly controlled
- [ ] preprocessing does not use test-set statistics
- [ ] label transforms preserve meaning

### Benchmark / Evaluation Leakage

Check:

- [ ] validation set used only for tuning
- [ ] test set used only for final evaluation
- [ ] qualitative examples are not cherry-picked from test after repeated tuning
- [ ] prompts, thresholds, NMS, decoding, or postprocessing were not tuned on test
- [ ] baseline and proposed method use the same evaluation protocol

### Evidence

Link concrete outputs when available:

- Split overlap report:
- Duplicate report:
- Hash report:
- Data inspection notebook:
- Metric script:
- Manual audit notes:

### Remaining Risks

| Risk | Severity | Why it matters | Mitigation |
|---|---|---|---|
| | low / medium / high | | |

### Decision

Choose one:

- proceed
- proceed_with_caveat
- fix_before_running
- rerun_required
- block_claims

### Claims Allowed

[State what claims are safe given this audit.]

### Claims Not Allowed

[State what claims are unsafe given this audit.]

### Next Step

- [State next action.]
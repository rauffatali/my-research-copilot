# AI/CV Review Criteria

This reference supports reviewer-style critique of AI, machine learning, and computer vision research artifacts.

Use it with the `peer-review` skill when reviewing manuscripts, proposals, experiment packages, rebuttals, or research narratives in AI/ML/CV.

The goal is to simulate how a skeptical but fair AI/CV reviewer would evaluate the work.

For applied AI/CV work, combine this reference with `multi_reviewer_panel.md` so that technical validity, domain validity, and hybrid integration are all reviewed.

---

## 1. Contribution Clarity

A reviewer should be able to identify the contribution quickly and precisely.

### Check

1. What problem is being addressed?
2. What is the claimed contribution?
3. Is the contribution technical, empirical, dataset-related, evaluation-related, application-driven, or analytical?
4. Is the contribution stated consistently across abstract, introduction, method, experiments, and conclusion?
5. Is the contribution meaningful beyond implementation effort?

### Red Flags

- The contribution is mostly “we applied model X to dataset Y.”
- The paper claims novelty but does not define what is new.
- The research question and contribution are different.
- The abstract claims more than the experiments show.
- The contribution depends on weak or missing baselines.

### Reviewer-Style Comment

> The paper addresses an important application, but the main research contribution is not yet clearly distinguished from implementation of an existing model family.

---

## 2. Novelty and Positioning

Novelty should be framed relative to closest prior work, not relative to what the project has tried so far.

### Check

1. What is the closest prior work?
2. Is the difference from prior work technical, empirical, methodological, or application-specific?
3. Does the paper explain why the difference matters?
4. Is the novelty claim supported by citations or literature artifacts?
5. Is the claim safer as “we evaluate,” “we adapt,” “we analyze,” or “we benchmark”?

### Red Flags

- “Novel” is used without closest-prior-work comparison.
- Related work is broad but misses the nearest methods.
- The method is new to the project but not new to the field.
- The application is new but the technical contribution is unclear.
- A survey is used instead of direct closest-prior-work comparison.

---

## 3. Task Formulation

The task definition should be clear enough to evaluate.

### Check

- What is the input?
- What is the output?
- What assumptions are made?
- What classes, labels, or targets are predicted?
- What is the unit of prediction: image, patch, frame, object, mask, sequence, document, scene?
- What makes a prediction correct?
- What is outside the task scope?

### Red Flags

- Task definition changes across sections.
- Label schema is ambiguous.
- Evaluation target is different from stated problem.
- Deployment setting is implied but not evaluated.

---

## 4. Dataset and Split Validity

Dataset quality and split validity often determine whether AI/CV results are trustworthy.

### Check

- Dataset source and version are stated.
- Train/validation/test split is documented.
- Split policy matches claim scope.
- Class/source/domain distributions are reported when relevant.
- Label quality and annotation process are described.
- Dataset limitations are acknowledged.
- Leakage risk is considered.

### Red Flags

- Random split used where group-wise split is needed.
- Frames, patches, scenes, roads, patients, or documents may appear across splits.
- Preprocessing uses full dataset statistics.
- Test set is used for tuning.
- Dataset has severe imbalance but only aggregate metric is reported.

---

## 5. Leakage and Contamination

Reviewers should be alert to leakage even when authors do not mention it.

### Check

- Duplicate or near-duplicate samples across splits.
- Source-level leakage.
- Temporal leakage.
- Patch/frame leakage.
- Label leakage through metadata or filenames.
- Pretraining or foundation-model contamination.
- Test-time tuning.
- Data preprocessing fitted on all data.

### Reviewer-Style Comment

> The reported gains are difficult to interpret without stronger evidence that the split prevents source-level or near-duplicate leakage.

---

## 6. Method Justification

A method should be motivated by a problem, failure mode, or hypothesis.

### Check

- Why this architecture or training change?
- What limitation does it target?
- What baseline does it improve over?
- What evidence isolates its effect?
- What tradeoff does it introduce?
- Is the method more complex than needed?

### Red Flags

- Method is justified by popularity.
- Multiple components are added without ablation.
- Mechanism is claimed but not tested.
- Complexity increases without clear benefit.

---

## 7. Baselines and Comparisons

Baselines should be strong, fair, and relevant.

### Check

- Is there a current simple baseline?
- Is there a strong modern baseline?
- Are baselines trained/evaluated under the same protocol?
- Are hyperparameters and training budgets fair?
- Are reported external numbers comparable?
- Are missing baselines justified?

### Red Flags

- Only weak baselines.
- Baseline is under-tuned.
- Comparison uses incompatible splits or metrics.
- Prior-work numbers are copied without protocol compatibility.
- No simple baseline.

---

## 8. Ablation Quality

Ablations should isolate the claimed contribution.

### Check

- Is each component tested separately?
- Is the ablation under the same protocol?
- Does it target the stated mechanism?
- Are negative or ambiguous ablations reported?
- Is the full model compared against meaningful variants?

### Red Flags

- No ablation for main component.
- Many components added at once.
- Ablation changes multiple variables.
- Only positive ablations shown.

---

## 9. Evaluation Metrics

Metrics must match the paper’s claims.

### Check

- Detection: mAP, AP50/AP75, recall, per-class AP, small-object metrics when relevant.
- Segmentation: mIoU, Dice/F1, boundary quality.
- Classification: accuracy, F1, AUROC, calibration, confusion matrix.
- Retrieval: Recall@K, MRR, nDCG.
- Robustness: slices, corruptions, domain shift.
- Efficiency: runtime, memory, FLOPs, hardware.

### Red Flags

- Overall metric used for narrow claim.
- Robustness claimed without robustness metric.
- Efficiency claimed without measurement.
- Small-object claim without small-object metric.
- Generalization claimed from one in-domain test split.

---

## 10. Result Interpretation

Claims must be proportional to evidence.

### Check

- Are gains larger than expected variance?
- Are results supported by tables/figures/logs?
- Are negative results discussed?
- Are alternative explanations considered?
- Are conclusions restricted to evaluated settings?

### Red Flags

- “State-of-the-art” without fair benchmark.
- “Generalizes” without external/domain evaluation.
- “Robust” without stress/slice analysis.
- “Significant” without statistical or practical justification.
- Mechanism claims without controlled experiments.

---

## 11. Reproducibility

A reviewer should understand how the result could be reproduced.

### Check

- dataset version;
- split;
- preprocessing;
- model configuration;
- training schedule;
- hyperparameters;
- seed policy;
- checkpoint selection;
- postprocessing;
- hardware/compute;
- code availability or enough implementation detail.

### Red Flags

- missing split details;
- missing training details;
- missing metric implementation details;
- undocumented postprocessing;
- no seed or variance discussion;
- notebook-only results used as final evidence.

---

## 12. Failure Analysis and Limitations

Strong papers explain where the method fails.

### Check

- false positives and false negatives;
- per-class/per-slice behavior;
- qualitative examples;
- edge cases;
- domain shift;
- annotation noise;
- limitations tied to evidence.

### Red Flags

- only best qualitative examples;
- limitations are generic;
- no failure cases;
- discussion claims more than results show.

---

## 13. Domain Validity for Applied AI/CV

For applied work, technical metrics are not enough.

### Check

- Is the task meaningful in the domain?
- Are labels meaningful to domain users?
- Is dataset collection realistic?
- Are domain-specific failure modes evaluated?
- Do metrics reflect practical value?
- Are deployment assumptions stated?
- Is the claimed impact supported?

### Red Flags

- domain framing is shallow;
- dataset is convenient but not representative;
- label schema ignores practical severity or context;
- practical impact inferred only from generic metric gain.

---

## 14. Recommendation Heuristics

### Stronger Recommendation

Use when:

- contribution is clear;
- baselines are fair;
- evaluation is credible;
- claims are proportional;
- limitations are honest;
- artifact is reproducible enough;
- domain validity is strong when applicable.

### Weaker Recommendation

Use when:

- novelty is unclear;
- baselines are weak;
- ablations are missing;
- leakage risk is unresolved;
- claim scope exceeds evidence;
- domain relevance is not demonstrated;
- reproducibility details are insufficient.

---

## Final Checklist

Before completing an AI/CV review:

- [ ] contribution is identifiable;
- [ ] closest prior work is considered;
- [ ] task formulation is clear;
- [ ] dataset and split are credible;
- [ ] leakage risk is considered;
- [ ] baselines are fair;
- [ ] ablations isolate the claim;
- [ ] metrics match the claims;
- [ ] results are interpreted proportionally;
- [ ] reproducibility details are sufficient;
- [ ] limitations and failure modes are discussed;
- [ ] domain validity is checked for applied work;
- [ ] recommendation follows from the evidence.

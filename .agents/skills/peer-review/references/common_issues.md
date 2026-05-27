# Common Peer-Review Issues in AI/ML/CV Manuscripts

Use this reference with the `peer-review` skill to identify frequent reviewer objections in AI/ML/CV and applied AI manuscripts.

This file is intentionally AI/CV-focused. General statistical, clinical, or biomedical issues should be used only when the manuscript type requires them.

---

## 1. Contribution Issues

### Common Problems

- contribution is unclear;
- contribution is mostly implementation;
- novelty is claimed but not shown against closest prior work;
- paper applies a known model to a new dataset without explaining research value;
- contribution changes across abstract, introduction, method, and conclusion.

### Reviewer Objection

> The paper would benefit from a sharper statement of what is scientifically new beyond applying an existing model family to the target dataset.

### Recommended Fix

- define contribution type;
- compare with closest prior work;
- state what is new and why it matters;
- weaken novelty wording if needed.

---

## 2. Related Work Issues

### Common Problems

- closest prior work missing;
- related work is a list, not synthesis;
- citations are outdated;
- AI/CV literature included but application-domain literature missing;
- application-domain literature included but AI baseline literature missing.

### Reviewer Objection

> The related work does not sufficiently position the proposed approach against the nearest methods and benchmarks.

### Recommended Fix

- use `research-lookup`;
- use `literature-review`;
- group work thematically;
- add closest-prior-work comparison.

---

## 3. Baseline Issues

### Common Problems

- weak baseline;
- missing simple baseline;
- missing strong modern baseline;
- unfair training budget;
- incompatible protocol comparison;
- baseline under-tuned;
- no ablation baseline.

### Reviewer Objection

> The comparison does not establish that the proposed method improves over a sufficiently strong or fairly tuned baseline.

### Recommended Fix

- include current internal baseline;
- include simple strong baseline;
- rerun baselines under same protocol;
- clearly mark indirect comparisons.

---

## 4. Dataset and Split Issues

### Common Problems

- split not documented;
- random split despite source-level leakage risk;
- duplicate or near-duplicate samples across splits;
- no dataset statistics;
- class imbalance ignored;
- label quality unknown;
- test set used for tuning.

### Reviewer Objection

> The evaluation protocol is difficult to trust without clearer split construction and leakage checks.

### Recommended Fix

- document split;
- use group/source-wise split when needed;
- report dataset statistics;
- add leakage checks.

---

## 5. Metric Issues

### Common Problems

- metric does not match claim;
- only aggregate metric reported;
- per-class or per-slice results missing;
- robustness claim without robustness evaluation;
- efficiency claim without runtime/compute details.

### Reviewer Objection

> The reported metric is insufficient to support the broader claim made in the paper.

### Recommended Fix

- align metric with claim;
- report slices/classes;
- add qualitative failures;
- narrow the claim.

---

## 6. Ablation Issues

### Common Problems

- no ablation for main component;
- multiple changes introduced at once;
- ablation is not controlled;
- negative ablations omitted;
- mechanism claim not isolated.

### Reviewer Objection

> The paper does not isolate which component is responsible for the reported improvement.

### Recommended Fix

- add component ablations;
- control training/evaluation conditions;
- report ambiguous or negative ablations.

---

## 7. Reproducibility Issues

### Common Problems

- missing hyperparameters;
- missing code/config details;
- no random seed policy;
- unclear preprocessing;
- unclear postprocessing;
- checkpoint selection undocumented;
- hardware/compute missing.

### Reviewer Objection

> The method and evaluation are not described in enough detail to reproduce the reported results.

### Recommended Fix

- add config table;
- document preprocessing/postprocessing;
- save run artifacts;
- report seeds/hardware when relevant.

---

## 8. Result Interpretation Issues

### Common Problems

- claims broader than evidence;
- single run interpreted as conclusive;
- small gain overinterpreted;
- “significant” used without statistical support;
- qualitative examples cherry-picked;
- negative results hidden.

### Reviewer Objection

> The conclusions overstate what can be inferred from the presented experiments.

### Recommended Fix

- use `claim-auditor`;
- weaken wording;
- report variance or practical effect size;
- add failure cases.

---

## 9. Domain Validity Issues

### Common Problems

- task definition does not match domain reality;
- labels are too coarse or ambiguous;
- dataset is not representative;
- metrics do not reflect practical usefulness;
- deployment assumptions are unrealistic;
- domain-specific failure modes ignored.

### Reviewer Objection

> The paper does not demonstrate that the technical improvement translates into meaningful value for the target domain.

### Recommended Fix

- add domain-specific evaluation;
- report domain-relevant slices;
- explain label taxonomy;
- discuss deployment constraints.

---

## 10. Citation and Reference Issues

### Common Problems

- wrong citation for claim;
- citation metadata incorrect;
- hallucinated AI-generated references;
- preprint described as peer-reviewed;
- survey cited for a specific empirical result;
- missing citation for background or gap claim.

### Reviewer Objection

> Several claims require stronger or more directly relevant citation support.

### Recommended Fix

- use `citation-management`;
- use `claim-auditor`;
- add verified sources;
- remove unsupported citation claims.

---

## 11. Writing and Presentation Issues

### Common Problems

- abstract overclaims;
- contribution buried;
- figures unreadable;
- tables lack protocol details;
- limitation section generic;
- conclusion introduces new unsupported claims;
- terminology inflated.

### Reviewer Objection

> The paper is difficult to evaluate because the claims, evidence, and limitations are not clearly aligned.

### Recommended Fix

- sharpen contribution;
- align claims with evidence;
- improve figure/table captions;
- use `scientific-writing` after evidence is audited.

---

## 12. Severity Guidance

### Critical

Likely rejection or major redesign:

- invalid evaluation;
- leakage risk;
- unsupported main claim;
- missing essential baseline;
- no identifiable contribution;
- domain framing invalid.

### Major

Substantial weakness but fixable:

- missing ablation;
- weak related work;
- unclear split;
- overclaiming;
- missing failure analysis;
- incomplete reproducibility.

### Minor

Clarity or completeness issue:

- citation needed;
- figure label unclear;
- missing implementation detail;
- wording too strong in one place.

---

## Final Checklist

When writing peer-review comments:

- [ ] identify the issue;
- [ ] explain why it matters;
- [ ] connect it to evidence or reviewer expectation;
- [ ] state whether it is critical, major, or minor;
- [ ] recommend a concrete fix;
- [ ] avoid generic criticism.

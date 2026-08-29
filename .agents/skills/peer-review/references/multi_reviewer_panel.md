# Multi-Reviewer Panel Reference

Use this reference with the `peer-review` skill when reviewing applied AI/ML/CV research that needs more than one generic reviewer perspective.

The goal is to simulate a realistic review panel with complementary expertise, then synthesize the reviews into a meta-review.

---

## 1. Purpose

A single reviewer often misses issues outside their expertise.

For applied AI/CV work, a strong review should test:

1. **technical validity** — does the AI/ML/CV method and evaluation hold up?
2. **domain validity** — does the task, data, and interpretation make sense in the application domain?
3. **integration validity** — does the technical contribution actually solve a meaningful domain problem?
4. **review synthesis** — what is the likely decision after reviewer disagreement is considered?

Use this reference for substantial manuscripts, proposals, experiment packages, or submission-readiness reviews.

---

## 2. Default Panel

Use this reviewer structure unless the user specifies another panel.

### Reviewer A — AI/CV Method Reviewer

Expertise:

- AI/ML/CV methods;
- architecture, training, and evaluation;
- baselines and ablations;
- metrics;
- reproducibility;
- leakage and protocol validity.

Primary concern:

```text
Is the technical work sound, novel enough, fairly evaluated, and reproducible?
```

---

### Reviewer B — Domain Reviewer

Expertise:

- application domain;
- task realism;
- data collection and annotation;
- domain-specific limitations;
- practical usefulness;
- deployment or decision context.

Primary concern:

```text
Is the problem, dataset, label schema, evaluation, and claimed impact meaningful in the domain?
```

---

### Reviewer C — Hybrid Reviewer

Expertise:

- both AI/CV methodology and application-domain requirements.

Primary concern:

```text
Does the AI method actually address the domain problem in a scientifically meaningful way?
```

---

### Meta-Reviewer / Area Chair

Role:

- synthesize reviewer comments;
- identify consensus and disagreement;
- determine must-fix issues;
- state likely decision and readiness.

Primary concern:

```text
Given all reviews, what is the most defensible decision and next action?
```

---

## 3. Reviewer A: AI/CV Method Reviewer Checklist

Check:

- contribution clarity;
- closest AI/CV prior work;
- method justification;
- model architecture clarity;
- training protocol;
- loss/augmentation/postprocessing details;
- baseline strength;
- baseline fairness;
- metric alignment;
- ablation quality;
- leakage-safe splits;
- multi-seed or uncertainty reporting when needed;
- reproducibility;
- failure analysis;
- claim-evidence alignment.

Common objections:

- missing strong baseline;
- unclear split;
- no ablation;
- metric does not match claim;
- weak novelty;
- single-run result;
- unfair comparison;
- code/config details missing;
- overclaiming state-of-the-art;
- possible leakage.

---

## 4. Reviewer B: Domain Reviewer Checklist

Adapt this reviewer to the paper’s application domain.

Check:

- domain problem is accurately framed;
- task definition is meaningful;
- labels match domain reality;
- dataset represents the real problem;
- annotation quality is credible;
- failure modes are domain-relevant;
- evaluation reflects real use;
- deployment assumptions are realistic;
- limitations are domain-specific;
- claimed impact is not exaggerated.

Common objections:

- task is oversimplified;
- labels are not practically meaningful;
- dataset is not representative;
- missing severity, context, or domain constraints;
- metric does not reflect domain value;
- deployment setting is unrealistic;
- paper optimizes a generic metric but not the real problem.

---

## 5. Reviewer C: Hybrid Reviewer Checklist

Check the bridge between method and domain.

Ask:

- Does the method target a domain-specific failure mode?
- Does the evaluation show domain-relevant value?
- Are technical metrics connected to practical outcomes?
- Is the contribution meaningful to both AI/CV and domain audiences?
- Are domain constraints reflected in model/evaluation choices?
- Is novelty technical, domain-specific, evaluation-specific, or application-specific?
- Does the paper avoid being merely “model X applied to domain Y”?
- Are limitations honest across both communities?

Common objections:

- technically valid but domain impact unclear;
- domain motivation strong but AI contribution weak;
- method improvement does not matter in practice;
- experiments ignore important domain slices;
- paper misses closest prior work from either field;
- claims are credible in one community but not the other.

---

## 6. Applied Domain Example Panel

For a paper applying an AI method to an application domain:

### Reviewer A — AI/CV Method Reviewer

Focus:

- model choice;
- task-appropriate baselines and metrics;
- class-wise or slice-based performance when relevant;
- difficult or underrepresented cases;
- ablations;
- augmentation;
- split and leakage;
- reproducibility;
- qualitative false positives/false negatives.

### Reviewer B — Application-Domain Reviewer

Focus:

- task taxonomy and domain realism;
- domain-relevant categories or priorities;
- source and operating-condition variability;
- annotation ambiguity;
- practical relevance;
- real deployment workflow;
- practical false positives/false negatives;
- whether the dataset reflects the intended setting.

### Reviewer C — Hybrid Reviewer

Focus:

- whether technical metrics map to application needs;
- whether model performance supports the intended use;
- whether evaluation includes domain-relevant slices;
- whether contribution is meaningful beyond applying a detector;
- whether the paper bridges method and domain literature.

---

## 7. Adapting the Panel to Other Topics

Examples:

### Medical Imaging AI

- Reviewer A: AI/CV reviewer
- Reviewer B: clinical/domain reviewer
- Reviewer C: medical AI reviewer
- Meta-reviewer: synthesis

### Remote Sensing AI

- Reviewer A: AI/CV reviewer
- Reviewer B: remote sensing/geospatial reviewer
- Reviewer C: applied geospatial AI reviewer

### Autonomous Driving Perception

- Reviewer A: AI/CV/perception reviewer
- Reviewer B: autonomous systems/domain reviewer
- Reviewer C: safety-aware applied perception reviewer

### Industrial Defect Detection

- Reviewer A: AI/CV reviewer
- Reviewer B: manufacturing/quality-control reviewer
- Reviewer C: applied industrial AI reviewer

---

## 8. Handling Reviewer Disagreement

Reviewer disagreement is useful.

Examples:

| Disagreement | Interpretation |
|---|---|
| Method reviewer positive, domain reviewer negative | Technical result may be valid but application framing is weak |
| Domain reviewer positive, method reviewer negative | Problem is important but AI contribution/evaluation is weak |
| Hybrid reviewer negative despite both others positive | The bridge between method and domain is not convincing |
| All reviewers negative on same issue | Must-fix or likely rejection |
| One reviewer raises fatal leakage concern | Investigate before trusting any positive review |

The meta-reviewer should not average scores mechanically. It should identify which concerns affect the main contribution.

---

## 9. Meta-Review Requirements

The meta-review must include:

- consensus strengths;
- consensus weaknesses;
- disagreements;
- must-fix issues;
- optional improvements;
- likely decision;
- evidence that would change the decision;
- research readiness.

Readiness labels:

- `ready for submission`;
- `minor revision needed`;
- `needs stronger evidence`;
- `needs experiment redesign`;
- `needs literature/context work`;
- `not ready`.

---

## 10. Panel Report Template

```md
# Multi-Reviewer Panel Review

## Review Target

- Artifact:
- Topic:
- Intended venue/audience:
- Domain:
- Review mode:

## Neutral Summary

[Problem, method, evidence, and claimed contribution.]

---

## Reviewer A: AI/CV Method Reviewer

### Strengths

### Major Concerns

### Minor Concerns

### Required Fixes

### Questions for Authors

### Recommendation

---

## Reviewer B: Domain Reviewer

### Strengths

### Major Concerns

### Minor Concerns

### Required Fixes

### Questions for Authors

### Recommendation

---

## Reviewer C: Hybrid Reviewer

### Strengths

### Major Concerns

### Minor Concerns

### Required Fixes

### Questions for Authors

### Recommendation

---

## Meta-Reviewer / Area Chair Summary

### Consensus Strengths

### Consensus Weaknesses

### Reviewer Disagreements

### Must-Fix Issues

### Optional Improvements

### Evidence That Would Change the Decision

### Likely Decision

### Research Readiness

### Final Next Action
```

---

## Final Reminder

A strong applied AI paper must survive both technical review and domain review.

The hybrid reviewer and meta-reviewer are there to check whether the work matters across that boundary.

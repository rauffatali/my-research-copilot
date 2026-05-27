---
name: scientific-critical-thinking
description: Use for adversarial scientific reasoning, hypothesis critique, novelty risk analysis, methodology critique, dataset/evaluation leakage checks, experiment decisiveness assessment, and research-decision pressure testing. Use before committing to model, loss, augmentation, training, dataset, evaluation, or manuscript-claim changes. For source discovery use research-lookup. For literature synthesis use literature-review. For sentence-level claim support use claim-auditor.
---

# Scientific Critical Thinking

## Overview

Scientific critical thinking is the internal research-judgment layer of the workflow.

Use this skill to pressure-test research ideas, hypotheses, methodology, experiment plans, evaluation protocols, novelty claims, and result interpretations before they become implementation work, paper claims, or project direction.

The goal is not to be pessimistic. The goal is to prevent shallow research directions, weak novelty, expensive but indecisive experiments, leakage-prone evaluation, and claims that are stronger than the evidence.

This skill should ask:

```text
Is this scientifically meaningful?
Is the evidence decisive?
Is the comparison fair?
Is the novelty real?
Is the evaluation trustworthy?
What could make this conclusion wrong?
What decision should change because of this critique?
```

---

## When to Use This Skill

Use this skill when:

- proposing a new research direction;
- changing model architecture;
- changing loss functions;
- changing augmentation;
- changing training strategy;
- changing dataset assumptions;
- changing evaluation protocol;
- selecting baselines;
- designing ablations;
- interpreting results;
- making novelty claims;
- making generalization or robustness claims;
- deciding whether an experiment is worth running;
- deciding whether a paper contribution is convincing;
- preparing for internal red-team review;
- preparing for peer review;
- deciding whether implementation progress is scientifically meaningful.

Use it before work becomes expensive or claims become locked.

---

## Relationship to Other Skills

Use this skill for research judgment and adversarial reasoning.

Use `research-lookup` when missing external sources, baselines, datasets, benchmarks, or prior work must be found.

Use `literature-review` when the critique depends on synthesizing prior work, closest prior methods, research gaps, datasets, benchmarks, or baseline expectations.

Use `citation-management` when reference metadata, BibTeX, DOI, arXiv IDs, or hallucinated references must be verified.

Use `claim-auditor` when auditing whether manuscript sentences or claims are supported by repository evidence, experiment artifacts, or verified citations.

Use `peer-review` when producing reviewer-style criticism after the research artifact is mature enough.

Use `scientific-writing` only after the scientific position is clear enough to write.

This skill should pressure-test decisions before they become implementation work, experiments, or manuscript claims.

---

## Boundary with Claim Auditor

This skill can identify that a claim is risky, overbroad, premature, methodologically weak, or scientifically under-supported.

For sentence-level manuscript claim verification, use `claim-auditor`.

Example boundary:

```text
scientific-critical-thinking
→ “The generalization claim is not justified by a single in-domain test split.”

claim-auditor
→ “This specific sentence should be rewritten because the cited table only reports in-domain mAP.”
```

---

## Relationship to Research Gates

This skill supports the research gates in `docs/research_gates.md`, especially:

- Research Direction Gate
- Research Change Gate
- Dataset and Leakage Gate
- Experiment Decision Gate
- Evaluation and Result Interpretation Gate
- Claim Support Gate
- Red-Team Review Gate

Use this skill before passing a gate when the decision requires judgment rather than mechanical checking.

---

## Core Principle

For model, loss, augmentation, training, or evaluation changes, state:

1. why it fits the current project scope;
2. what baseline it is compared against;
3. what metric or failure mode it targets;
4. how it will be ablated or isolated;
5. what risk or tradeoff it introduces.

If these cannot be answered, the change is not yet research-ready.

---

## Critical Thinking Modes

Choose the smallest mode that fits the task.

---

### 1. Research Direction Critique

Use when assessing a proposed project direction, contribution, or hypothesis.

Ask:

- What is the exact research question?
- Is the contribution scientific, engineering-only, or application-only?
- What would make the result publishable?
- What would make it uninteresting?
- Is the gap literature-supported?
- What is the closest prior work?
- What evidence would convince a skeptical reviewer?
- What evidence would falsify the idea?

Output:

- strongest version of the idea;
- weakest point;
- novelty risk;
- evidence needed;
- decision recommendation.

---

### 2. Method / Architecture Critique

Use when changing model architecture, loss, training, augmentation, preprocessing, or inference.

Ask:

- Why should this change help?
- What failure mode does it target?
- What baseline does it compare against?
- Is the mechanism testable?
- Can the effect be isolated?
- Is the change adding complexity without scientific value?
- What ablation is required?
- What could go wrong?

Do not approve method changes only because they sound modern or implementable.

---

### 3. Dataset and Leakage Critique

Use when data splits, preprocessing, labels, augmentation, or evaluation datasets are involved.

Ask:

- Could train/test leakage exist?
- Are images, videos, scenes, sources, patients, roads, or domains duplicated across splits?
- Are augmentations leaking labels or test assumptions?
- Are labels noisy or inconsistent?
- Is the test set representative?
- Are there domain shifts?
- Does preprocessing use information unavailable at inference?
- Are metadata or filenames leaking target labels?

Use `references/ml_leakage_patterns.md` when available.

---

### 4. Experiment Decisiveness Critique

Use when deciding whether an experiment is worth running or interpreting.

Ask:

- What decision will this experiment enable?
- What result would change the plan?
- Is the baseline appropriate?
- Is the metric aligned with the claim?
- Is the experiment isolating one factor?
- Is it too expensive relative to information gained?
- Does it need multiple seeds?
- Does it need slice/failure analysis?
- What result would be ambiguous?

Use `references/experiment_decisiveness.md` when available.

---

### 5. Evaluation and Metric Critique

Use when selecting or interpreting metrics.

Ask:

- Does the metric match the real claim?
- Is the threshold or protocol clear?
- Are comparisons made under the same split and protocol?
- Are per-class, per-domain, or per-condition results needed?
- Are confidence intervals or multiple seeds needed?
- Could a metric improve while practical behavior worsens?
- Is there qualitative evidence for the claimed improvement?

Do not accept metric gains without checking protocol compatibility.

---

### 6. Novelty Critique

Use when making contribution or originality claims.

Ask:

- What is the closest prior work?
- Is the difference meaningful or cosmetic?
- Is the novelty in method, data, evaluation, application, or combination?
- Has the same idea been done in another domain?
- Is the novelty only a new implementation?
- Is the contribution strong enough without inflated wording?
- What literature review is needed before claiming novelty?

If novelty depends on literature coverage, use `research-lookup` and `literature-review`.

---

### 7. Result Interpretation Critique

Use when interpreting experiment outcomes.

Ask:

- Does the result support the claim?
- Could the gain be noise?
- Could the improvement be due to leakage, preprocessing, or unfair comparison?
- Are negative results being ignored?
- Are failure modes understood?
- Are claims broader than the evaluated setting?
- Is the explanation post-hoc speculation?
- What alternative explanation exists?

Do not treat correlation or metric gain as proof of mechanism.

---

### 8. Red-Team Scientific Review

Use when the project or manuscript needs adversarial internal review.

Ask:

- What would a skeptical reviewer reject?
- Which claim is easiest to attack?
- Which experiment is missing?
- Which baseline is unfair or absent?
- Which dataset assumption is weak?
- Which novelty claim is fragile?
- Which result is overinterpreted?
- Which limitation is being hidden?

Output should include required fixes before submission or review.

---

## Evidence Standards for AI/ML/CV

Use evidence appropriate to the claim.

| Claim | Stronger evidence | Weaker evidence |
|---|---|---|
| Method improves performance | controlled baseline comparison under same protocol | single untracked run |
| Component is useful | ablation isolating component | full model comparison only |
| Generalizes | held-out domain/dataset or cross-domain evaluation | one in-domain test split |
| Robust | stress tests, slices, corruptions, failure analysis | average metric only |
| Efficient | runtime, memory, FLOPs, hardware details | subjective “lightweight” |
| Novel | closest-prior-work analysis and source artifacts | no known prior work by memory |
| Dataset is suitable | documented splits, labels, distribution, leakage checks | assumption based on dataset name |
| Evaluation is fair | same split, same metric, same postprocessing | incomparable reported numbers |

Use `references/evidence_hierarchy.md` when available.

---

## Common AI/CV Research Failures

Watch for:

- shallow novelty hidden behind implementation effort;
- trendy method substitution without hypothesis;
- unfair baseline selection;
- missing simple baseline;
- missing ablation;
- train/test leakage;
- duplicated scenes or sources across splits;
- metric mismatch;
- evaluation on too narrow a setting;
- overclaiming generalization;
- confusing dataset improvement with method improvement;
- reporting only best run;
- ignoring failure modes;
- writing stronger claims than results support;
- treating preprints or code repositories as conclusive evidence.

Use `references/ai_cv_research_failures.md` when available.

---

## Decision Recommendation Requirement

Every critique should end with a decision recommendation.

Use one of:

- `proceed`;
- `proceed with constraints`;
- `revise plan`;
- `run smaller test first`;
- `gather missing evidence`;
- `perform literature lookup/review first`;
- `perform citation or claim audit first`;
- `stop or deprioritize`.

Avoid critiques that identify problems but do not change a research decision.

A good critique should make the next action clearer.

---

## Output Formats

Choose the smallest useful format.

---

### Research Decision Critique

```md
## Scientific Critical Thinking Review

### Decision Under Review

[What is being proposed?]

### Current Evidence

[What evidence exists?]

### Strongest Case

[Best argument for the proposal.]

### Main Weaknesses

[Scientific weaknesses.]

### Failure Modes

[How this could fail or mislead.]

### Required Evidence

[Baselines, ablations, datasets, metrics, literature, or checks needed.]

### Decision Recommendation

[proceed / revise / run smaller test / gather evidence / stop]

### Next Step

[Concrete action.]
```

---

### Method Change Critique

```md
## Method Change Critique

| Question | Answer |
|---|---|
| Scope fit | [answer] |
| Baseline compared against | [answer] |
| Target metric/failure mode | [answer] |
| Ablation plan | [answer] |
| Risk/tradeoff | [answer] |

### Verdict

[Decision recommendation.]
```

---

### Experiment Decisiveness Review

```md
## Experiment Decisiveness Review

### Experiment

[Experiment description.]

### Decision It Enables

[What decision this experiment should answer.]

### Required Controls

[Baseline, split, metric, seed, protocol.]

### Ambiguous Outcomes

[Outcomes that would not answer the question.]

### Cheaper Alternative

[If any.]

### Decision Recommendation

[Run / revise / skip / split into smaller tests.]
```

---

### Red-Team Review

```md
## Red-Team Scientific Review

### Most Attackable Claims

| Claim | Why vulnerable | Required fix |
|---|---|---|

### Missing Evidence

| Missing evidence | Why it matters | Priority |
|---|---|---|

### Reviewer Objections

1. [Objection]
2. [Objection]
3. [Objection]

### Decision Recommendation

[What must change before paper/experiment approval.]
```

---

## Important Rules

- Do not approve a change because it is easy to implement.
- Do not reject an idea only because it is difficult.
- Do not confuse engineering progress with scientific contribution.
- Do not treat intended behavior as demonstrated evidence.
- Do not make novelty claims without checking prior work.
- Do not trust results without checking evaluation protocol.
- Do not ignore simple baselines.
- Do not ignore negative or ambiguous outcomes.
- Do not broaden conclusions beyond evaluated settings.
- Do not invent evidence, citations, or experiment results.
- Do not produce criticism without an actionable decision recommendation.

---

## Good Outputs

Good outputs include:

- direct critique of the research decision;
- identification of hidden assumptions;
- required baselines and ablations;
- leakage risks;
- evaluation weaknesses;
- novelty risks;
- safer interpretation of results;
- stop/go/revise recommendations;
- concrete next step.

Bad outputs include:

- generic warnings;
- philosophical commentary with no decision;
- long lists of possible issues without priority;
- approving plans because they sound plausible;
- rejecting plans without explaining decisive evidence;
- rewriting paper text instead of critiquing the science.

---

## Final Checklist

Before finishing a critical-thinking task:

1. [ ] The decision or claim under review is clear.
2. [ ] The current evidence is identified.
3. [ ] The strongest case is stated fairly.
4. [ ] The main scientific weaknesses are identified.
5. [ ] Baseline and ablation needs are checked.
6. [ ] Dataset and leakage risks are considered.
7. [ ] Evaluation and metric alignment are checked.
8. [ ] Novelty risk is considered when relevant.
9. [ ] Result interpretation is kept proportional to evidence.
10. [ ] Missing literature, citation, or claim audit needs are handed off.
11. [ ] A clear decision recommendation is provided.
12. [ ] The next action is concrete.

---

## Final Reminder

Scientific critical thinking should protect the project from doing polished but scientifically weak work.

A strong critique is not a blocker. It is a way to spend effort on experiments, claims, and contributions that can survive review.

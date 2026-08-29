# AI/ML/CV Evidence Hierarchy

Use this reference with `scientific-critical-thinking` when judging whether a research decision, method change, experiment result, or manuscript claim is supported by evidence.

This hierarchy is designed for AI, machine learning, and computer vision research. It is not a medical/clinical evidence hierarchy.

---

## 1. Core Principle

Evidence quality depends on the claim.

A result can be strong evidence for a narrow claim and weak evidence for a broad claim.

Example:

```text
Strong: The method improves mAP on this dataset split under this protocol.

Weak: The method generalizes reliably across real-world deployment conditions.
```

Always match the evidence to the claim scope.

---

## 2. Evidence Levels for Empirical AI/ML/CV Claims

### Level 1 — Reproducible Controlled Benchmark Evidence

Strongest evidence for empirical performance claims.

Requires:

- fixed dataset version;
- documented split;
- documented metric;
- fair baseline;
- same evaluation protocol;
- saved config;
- saved run artifacts;
- reproducible code or enough run metadata;
- preferably multiple seeds or uncertainty estimates when variance matters.

Supports claims like:

```text
Under the evaluated protocol, method A outperforms baseline B on metric M.
```

Does not automatically support:

```text
Method A is generally superior.
Method A is robust in real-world deployment.
```

---

### Level 2 — Controlled Ablation Evidence

Strongest evidence for component or mechanism claims.

Requires:

- one meaningful factor changed at a time;
- same data;
- same split;
- same metric;
- same training/evaluation protocol;
- same or comparable compute;
- documented expected effect.

Supports claims like:

```text
The attention module contributed to the observed improvement in this setting.
```

Does not automatically support:

```text
The attention module is universally beneficial.
```

---

### Level 3 — Leakage-Safe Held-Out or Cross-Domain Evidence

Strong evidence for generalization or robustness claims.

Requires one or more of:

- held-out domain;
- held-out location/source/camera/road/scene/user/patient;
- temporal split;
- group-wise split;
- external benchmark;
- domain-shift test;
- slice-specific evaluation.

Supports claims like:

```text
The method retained performance on the held-out source split.
```

Does not automatically support:

```text
The method generalizes across all deployment conditions.
```

---

### Level 4 — Multi-Seed / Uncertainty-Aware Evidence

Important when training variance matters.

Useful evidence:

- multiple seeds;
- mean ± std;
- confidence intervals;
- bootstrap intervals;
- stability across folds;
- variance-aware ranking.

Supports claims like:

```text
The improvement was consistent across repeated runs.
```

Without this, avoid strong claims from small metric differences.

---

### Level 5 — Qualitative Failure and Slice Analysis

Important for understanding behavior beyond headline metrics.

Useful evidence:

- false positives;
- false negatives;
- worst cases;
- per-class metrics;
- small-object performance;
- occlusion/weather/lighting slices;
- domain/source slices;
- calibration plots;
- prediction overlays.

Supports claims like:

```text
The main remaining failure mode is small, low-contrast targets.
```

Does not replace quantitative evaluation.

---

### Level 6 — Implementation and Configuration Evidence

Strong evidence for what was implemented, not necessarily for performance.

Sources:

- code;
- config;
- logs;
- tests;
- run metadata;
- preprocessing scripts;
- metric implementation;
- model architecture definition.

Supports claims like:

```text
The training pipeline used random horizontal flips.
```

Does not support claims like:

```text
Random horizontal flips improved performance.
```

unless paired with experiments.

---

### Level 7 — Literature-Supported Evidence

Useful for motivation, prior work, baselines, gaps, and expected failure modes.

Sources:

- `research-lookup` artifacts;
- `literature-review` synthesis;
- verified citations;
- benchmark or dataset papers;
- survey papers.

Supports claims like:

```text
Prior work commonly evaluates object detection with mAP.
```

Does not support project-specific empirical claims unless the project ran the experiment.

---

### Level 8 — Exploratory Runs

Useful for direction finding, not final claims.

Includes:

- single seed;
- small subset;
- smoke test;
- notebook-only result;
- informal baseline;
- partially logged run.

Supports claims like:

```text
Initial exploratory results suggest this direction is worth testing.
```

Does not support final performance, robustness, or novelty claims.

---

### Level 9 — Plausible Mechanism or Expert Intuition

Weakest evidence.

Useful for:

- hypothesis generation;
- experiment planning;
- deciding what to test next.

Does not support empirical claims.

---

## 3. Evidence Needed by Claim Type

| Claim type | Minimum acceptable evidence | Stronger evidence |
|---|---|---|
| Performance improvement | controlled baseline comparison | multi-seed controlled benchmark |
| Component usefulness | ablation | ablation across datasets/slices |
| Generalization | held-out source/domain | multiple external domains |
| Robustness | stress/slice evaluation | systematic robustness benchmark |
| Efficiency | runtime/memory/FLOPs measurement | hardware-normalized comparison |
| Novelty | closest-prior-work review | broad literature synthesis + peer critique |
| Dataset suitability | dataset documentation + split/label audit | leakage-safe analysis + external validation |
| Method implementation | code/config/logs | tests + reproducible run |
| Literature claim | verified citation | literature-review synthesis |

---

## 4. Common Evidence Mismatches

### Headline metric used for robustness

Problem:

```text
mAP improves, therefore method is robust.
```

Fix:

```text
mAP improves under the evaluated split. Robustness requires stress, slice, or domain-shift evaluation.
```

### Exploratory result used as final evidence

Problem:

```text
One untracked run shows improvement.
```

Fix:

```text
Treat as preliminary and run controlled comparison.
```

### Code existence used as result evidence

Problem:

```text
The module exists, therefore it improves performance.
```

Fix:

```text
Run ablation or remove performance claim.
```

### Literature support used for project outcome

Problem:

```text
Prior work reports gains, therefore our method improves.
```

Fix:

```text
Use literature for motivation; use project experiments for project claims.
```

---

## 5. Evidence Approval Checklist

Before accepting a claim:

- [ ] Claim scope is clear.
- [ ] Evidence type matches claim type.
- [ ] Dataset, split, and metric are documented.
- [ ] Baseline or reference point is defined.
- [ ] Experimental protocol is comparable.
- [ ] Leakage risk is considered.
- [ ] Ablation exists when claiming component effect.
- [ ] Multi-seed or uncertainty is considered when variance matters.
- [ ] Qualitative or slice analysis is considered when failure modes matter.
- [ ] Wording is proportional to evidence.

---

## Final Reminder

The strongest evidence is not always the biggest experiment.

The strongest evidence is the evidence that directly answers the decision or claim under review.

# Logical Fallacies in AI/ML/CV Research Reasoning

Use this reference to detect flawed reasoning in hypotheses, experiment interpretation, novelty claims, and manuscript arguments.

---

## 1. Post Hoc Mechanism Fallacy

Pattern:

```text
The metric improved after adding component X, so X caused the improvement for the reason we expected.
```

Problem:

- other factors may have changed;
- variance may explain gain;
- mechanism is untested.

Fix:

- controlled ablation;
- same protocol;
- mechanism-specific analysis.

---

## 2. Hasty Generalization

Pattern:

```text
The method works on one dataset, so it generalizes.
```

Fix:

- narrow the claim;
- evaluate held-out domain or external data;
- state limitations.

---

## 3. False Equivalence

Pattern:

```text
Two methods are compared even though training data, preprocessing, or evaluation protocols differ.
```

Fix:

- compare under same protocol;
- mark indirect comparisons as indirect;
- avoid “outperforms” language.

---

## 4. Appeal to Novelty

Pattern:

```text
This model is newer, so it is better.
```

Fix:

- define expected mechanism;
- compare to baseline;
- test the failure mode.

---

## 5. Appeal to Authority

Pattern:

```text
A famous paper or model says this, so it must apply here.
```

Fix:

- check task/data/protocol relevance;
- cite direct evidence;
- use literature-review for context.

---

## 6. Cherry Picking

Pattern:

```text
Only successful runs, examples, or metrics are shown.
```

Fix:

- report seed policy;
- include failure cases;
- document excluded runs;
- use predetermined metrics.

---

## 7. Moving Goalposts

Pattern:

- after the original metric fails, a new metric is chosen to claim success.

Fix:

- define success criteria before running;
- label post-hoc analysis as exploratory.

---

## 8. Strawman Baseline

Pattern:

```text
The proposed method is compared to an intentionally weak baseline.
```

Fix:

- include current internal baseline;
- include simple strong baseline;
- include literature-relevant baseline when feasible.

---

## 9. Composition Fallacy

Pattern:

```text
A component helps in one architecture, so it will help all architectures.
```

Fix:

- limit claim to tested setting;
- test across architectures if broader claim is needed.

---

## 10. Correlation-Causation Fallacy

Pattern:

```text
Images with feature X have more errors, so X causes errors.
```

Fix:

- control confounders;
- use slice analysis carefully;
- treat as hypothesis unless tested.

---

## 11. Survivorship Bias

Pattern:

```text
Only published successful methods are reviewed, so the literature seems more conclusive than it is.
```

Fix:

- search for negative/ablation results;
- inspect limitations;
- avoid overclaiming consensus.

---

## 12. Metric Substitution Fallacy

Pattern:

```text
The metric improved, so the real-world problem is solved.
```

Fix:

- connect metric to task requirement;
- add qualitative/failure analysis;
- state deployment limits.

---

## 13. Logical Fallacy Checklist

Before accepting a claim:

- [ ] Is causation inferred from uncontrolled comparison?
- [ ] Is a broad claim made from narrow evidence?
- [ ] Are protocols comparable?
- [ ] Is novelty being treated as value?
- [ ] Is a famous source being over-applied?
- [ ] Are only favorable results shown?
- [ ] Did success criteria change after results?
- [ ] Is the baseline fair?
- [ ] Is the metric actually measuring the claim?

---

## Final Reminder

Many research failures are reasoning failures before they become experiment failures.

Make the logic explicit before trusting the conclusion.

# Statistical and Evaluation Pitfalls in AI/ML/CV

Use this reference when interpreting metrics, comparing methods, or deciding whether results support a claim.

---

## 1. Single-Run Overinterpretation

Problem:

```text
One run improves the metric, so the method is better.
```

Risk:

- random seed variance;
- unstable training;
- data-order effects;
- lucky checkpoint;
- noisy validation.

Mitigation:

- multiple seeds when feasible;
- report mean ± std;
- compare effect size to variance;
- treat one run as preliminary.

---

## 2. Best-Run Cherry Picking

Problem:

```text
Only the best run is reported.
```

Risk:

- inflated performance;
- unfair baseline comparison;
- irreproducible claims.

Mitigation:

- report seed policy;
- use consistent model selection;
- report average or final selected run;
- document failed runs when relevant.

---

## 3. Multiple Comparisons

Problem:

Testing many models, augmentations, thresholds, or metrics increases the chance of accidental improvement.

Examples:

- many hyperparameter trials;
- many class/slice metrics;
- many datasets;
- many prompt/model variants;
- many thresholds.

Mitigation:

- define primary metric;
- separate exploratory and confirmatory results;
- validate promising results on held-out data;
- avoid claiming significance without correction or confirmation.

---

## 4. Metric Mismatch

Problem:

The metric does not measure the claim.

Examples:

- claiming robustness from overall mAP;
- claiming small-object improvement without small-object AP;
- claiming deployment readiness without latency;
- claiming fairness without subgroup metrics;
- claiming calibration without calibration metrics.

Mitigation:

- align metric to claim;
- add slice-specific metrics;
- include qualitative failure analysis.

---

## 5. Incompatible Protocol Comparison

Problem:

Comparing results from different splits, preprocessing, training budgets, or postprocessing.

Mitigation:

- rerun baselines under the same protocol when possible;
- state when comparison is indirect;
- avoid “outperforms” language for incompatible reported numbers.

---

## 6. Leakage-Inflated Metrics

Problem:

Metrics look strong because test information leaks into training or evaluation.

Sources:

- duplicates across splits;
- video frames split randomly;
- patches from same image across splits;
- preprocessing fit on full data;
- source/domain leakage;
- label leakage through filenames or metadata;
- test-set tuning.

Mitigation:

- leakage checks;
- group-wise splits;
- train-only preprocessing fit;
- separate validation and test usage.

---

## 7. Threshold and Postprocessing Tuning on Test

Problem:

Thresholds, NMS settings, prompts, or postprocessing are tuned on the test set.

Mitigation:

- tune on validation;
- lock test protocol;
- document threshold selection;
- report test once when possible.

---

## 8. Small Test Set Instability

Problem:

A few examples can move metrics significantly.

Mitigation:

- report confidence intervals or bootstrap intervals;
- show counts;
- use per-class and per-slice support;
- avoid strong claims from tiny samples.

---

## 9. Class Imbalance Misinterpretation

Problem:

Aggregate metrics hide rare-class behavior.

Examples:

- high accuracy with poor rare-class recall;
- mAP dominated by common/easy categories;
- macro vs micro averaging confusion.

Mitigation:

- per-class metrics;
- macro/micro distinction;
- confusion matrix;
- rare-class slices.

---

## 10. Statistical Significance vs Practical Significance

Problem:

A statistically detectable change may not matter, or a practically meaningful change may lack power.

Mitigation:

- report effect size;
- define practical threshold;
- consider confidence intervals;
- relate metric change to task requirements.

---

## 11. Correlation vs Mechanism

Problem:

Metric gain is used to prove why the method works.

Mitigation:

- use ablations;
- use controlled comparisons;
- use failure analysis;
- avoid mechanism claims without isolation.

---

## 12. Leaderboard Overfitting

Problem:

Optimizing to a benchmark rather than scientific understanding.

Mitigation:

- use held-out or external validation;
- report limitations;
- avoid claiming generality from leaderboard rank;
- inspect failure modes.

---

## 13. Statistical Pitfall Checklist

Before interpreting results:

- [ ] primary metric is defined;
- [ ] metric matches claim;
- [ ] baseline comparison is protocol-compatible;
- [ ] seed variance is considered;
- [ ] hyperparameter search is disclosed;
- [ ] test set was not used for tuning;
- [ ] leakage risk is checked;
- [ ] effect size is meaningful;
- [ ] slice/per-class results are considered;
- [ ] qualitative failures are inspected when useful;
- [ ] conclusions are proportional to evidence.

---

## Final Reminder

A number is not a conclusion.

A metric becomes evidence only when the protocol, baseline, uncertainty, and claim scope are clear.

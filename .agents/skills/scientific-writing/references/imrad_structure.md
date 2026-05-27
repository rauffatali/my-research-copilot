# Manuscript Structure and IMRaD Guidance

This reference supports the `scientific-writing` skill.

Use it when outlining, drafting, or revising scientific manuscripts, especially AI/ML/CV papers.

For venue-specific structure, use `venue-templates`.

For literature-dependent sections, use `literature-review`.

For result-section tables and placeholders, use `results-scaffold`.

---

## 1. Purpose

IMRaD means:

```text
Introduction → Methods → Results → Discussion
```

Many AI/ML/CV papers use a modified structure:

```text
Abstract
Introduction
Related Work
Method
Experiments
Results
Discussion / Limitations
Conclusion
References
Appendix
```

Do not force one structure on every paper. Use the structure that matches the venue, paper type, and available evidence.

---

## 2. Evidence-First Structure Rule

A paper outline should reflect what evidence exists.

Before outlining, identify:

- research question;
- contribution;
- source/literature context;
- method evidence;
- dataset/split evidence;
- baseline evidence;
- result evidence;
- limitation evidence;
- target venue.

If any part is missing, mark it as a TODO instead of pretending the section is ready.

---

## 3. Common AI/CV Paper Outline

A standard AI/CV manuscript often follows:

```text
1. Abstract
2. Introduction
3. Related Work
4. Method
5. Experiments
6. Results and Analysis
7. Discussion / Limitations
8. Conclusion
9. References
10. Appendix / Supplementary Material
```

Alternative structures:

```text
1. Introduction
2. Background and Related Work
3. Dataset
4. Method
5. Experimental Setup
6. Results
7. Discussion
8. Conclusion
```

For dataset papers:

```text
1. Introduction
2. Related Work
3. Dataset Collection
4. Annotation Protocol
5. Dataset Statistics
6. Benchmark Tasks
7. Baselines
8. Limitations
9. Conclusion
```

For applied AI/CV papers:

```text
1. Introduction
2. Domain Background and Related Work
3. Data and Task Definition
4. Method
5. Experimental Setup
6. Results
7. Domain-Specific Analysis
8. Limitations
9. Conclusion
```

---

## 4. Abstract

The abstract should summarize only what the paper supports.

Typical components:

1. problem;
2. gap or motivation;
3. method/study focus;
4. evidence or experiment;
5. main supported finding;
6. cautious conclusion.

Avoid:

- unsupported novelty;
- invented numbers;
- claims not shown in the paper;
- vague “comprehensive framework” language;
- overclaiming generalization.

Use `claim-auditor` before finalizing.

---

## 5. Introduction

The introduction should answer:

1. What is the problem?
2. Why does it matter?
3. What has prior work done?
4. What gap or limitation remains?
5. What does this paper contribute?
6. What evidence supports the contribution?

Dependencies:

- `research-lookup`;
- `literature-review`;
- `citation-management`;
- `claim-auditor`.

Avoid opening with generic AI hype.

---

## 6. Related Work / Literature Review

Related work should synthesize sources by theme or method family.

Common structures:

- method-family structure;
- dataset/benchmark structure;
- chronological structure;
- problem/failure-mode structure;
- closest-prior-work structure.

A good related work section should:

- identify relevant themes;
- compare prior methods;
- show closest prior work;
- support gap framing;
- position the current project.

Do not write related work without `literature-review` support.

---

## 7. Method

The method section should describe what was done precisely enough to understand and reproduce.

Include:

- task definition;
- inputs and outputs;
- model/pipeline;
- training objective;
- preprocessing;
- postprocessing;
- implementation details;
- assumptions.

Avoid:

- result claims;
- unexplained complexity;
- vague mechanism claims;
- unsupported novelty claims.

Method claims should be checked against code/configs when possible.

---

## 8. Experiments

The experiment section should explain how the method was evaluated.

Include:

- datasets;
- splits;
- baselines;
- metrics;
- training details;
- evaluation protocol;
- ablations;
- implementation details;
- hardware/compute when relevant.

The experiment section should make comparisons auditable.

Use `results-scaffold` if table structures or placeholders are needed.

---

## 9. Results

The results section should report what happened.

It should:

- refer to tables/figures;
- state metrics accurately;
- compare against baselines;
- identify trends;
- state evaluated conditions;
- avoid unsupported generalization;
- mention important negative or ambiguous findings.

Do not invent values.

Use `claim-auditor` before finalizing result claims.

---

## 10. Discussion

Discussion should interpret results.

It may include:

- why results may have occurred;
- what the results suggest;
- where the method works;
- where it fails;
- how findings relate to prior work;
- implications for future research.

Avoid:

- new unsupported claims;
- overbroad generalization;
- hiding limitations;
- treating speculation as finding.

Use `scientific-critical-thinking` for interpretation risks.

---

## 11. Limitations

Limitations should be specific.

Good limitations mention:

- dataset scope;
- split limitations;
- domain-shift limits;
- label noise;
- baseline limitations;
- metric limitations;
- compute constraints;
- untested deployment conditions.

Weak limitations are vague:

```text
This study has some limitations.
```

Better:

```text
The evaluation uses a single dataset split, so it does not establish cross-location generalization.
```

---

## 12. Conclusion

Conclusion should summarize what the paper showed.

It should not introduce:

- new results;
- new claims;
- new citations;
- new baselines;
- unsupported future promises.

A safe conclusion includes:

- problem recap;
- method/study recap;
- supported finding;
- limitation or future work;
- cautious final sentence.

---

## 13. Appendix / Supplementary Material

Use appendix for:

- extra dataset details;
- hyperparameters;
- additional ablations;
- failure cases;
- implementation details;
- extra qualitative examples;
- extended related work;
- proof or derivation;
- additional tables.

Do not hide essential evidence only in the appendix if it is required for the main claim.

---

## 14. Outline Template

```md
# Proposed Manuscript Outline

## 1. Abstract
Purpose:
Evidence needed:
TODOs:

## 2. Introduction
Purpose:
Required literature support:
Key citations:
TODOs:

## 3. Related Work
Themes:
Closest prior work:
TODOs:

## 4. Method
Components:
Implementation evidence:
TODOs:

## 5. Experiments
Datasets:
Baselines:
Metrics:
Ablations:
TODOs:

## 6. Results
Tables/Figures:
Claims supported:
TODOs:

## 7. Discussion / Limitations
Interpretation:
Limitations:
TODOs:

## 8. Conclusion
Supported final message:
TODOs:
```

---

## 15. Final Checklist

Before accepting an outline:

- [ ] Structure matches venue or paper type.
- [ ] Literature-dependent sections depend on `literature-review`.
- [ ] Result sections depend on actual artifacts or `results-scaffold`.
- [ ] Claims have evidence or TODOs.
- [ ] No unsupported section promises are made.
- [ ] Abstract and conclusion are aligned with evidence.
- [ ] Venue-specific requirements are handed to `venue-templates`.

---

## Final Reminder

A manuscript structure is not just formatting.

It is the argument path from problem to evidence to claim.

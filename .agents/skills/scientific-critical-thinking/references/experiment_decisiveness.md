# Experiment Decisiveness

This reference helps evaluate whether an experiment is worth running and whether it can answer the intended research question.

Use it with the Experiment Decision Gate and scientific-critical-thinking skill.

A decisive experiment is not necessarily large. A decisive experiment is one that can change a research decision.

---

## 1. Core question

Before running an experiment, ask:

> What decision will this experiment change?

If the answer is unclear, the experiment is not ready.

Good decisions include:

- continue or stop a research direction;
- choose between two methods;
- keep or remove a component;
- accept or reject a hypothesis;
- decide whether more expensive experiments are justified;
- decide whether a claim can be made;
- decide whether a failure mode is real.

Weak decisions include:

- “see what happens”;
- “try the model”;
- “improve results”;
- “check if it works”;
- “maybe get better performance.”

---

## 2. Minimal viable experiment

A good experiment starts with the smallest version that can answer the decision question.

### Ask

1. Can a smoke test reveal implementation problems?
2. Can a tiny subset reveal whether the pipeline works?
3. Can a frozen-feature baseline test the idea before fine-tuning?
4. Can one controlled ablation answer the main question?
5. Can qualitative inspection reveal a likely failure before full training?
6. Can a synthetic or toy case validate the metric or loss?

### Principle

Do not run the expensive version before the cheap version has removed obvious failure risks.

---

## 3. Baseline and control

Every decisive experiment needs a comparison.

### Baseline options

- current best project baseline;
- simplest meaningful method;
- prior implementation;
- standard library baseline;
- frozen pretrained model;
- no-change control;
- previous run under the same protocol.

### Control questions

1. What stays fixed?
2. What changes?
3. Is only one main variable changing?
4. Is the baseline evaluated under the same protocol?
5. Is the comparison fair in compute, data, tuning, and preprocessing?

---

## 4. Hypothesis clarity

An experiment should state what result would support or weaken the hypothesis.

### Template

```text
Hypothesis:
If we change _____, then _____ should improve because _____.

Support signal:
The hypothesis is supported if _____ improves relative to _____ under _____.

Weakening signal:
The hypothesis is weakened if _____ does not improve, improves only under unfair settings, or causes _____ to degrade.
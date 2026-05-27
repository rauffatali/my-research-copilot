# Scientific Writing Principles

This reference supports the `scientific-writing` skill.

Use it when drafting or revising scientific manuscript prose, especially when the goal is to make the writing clear, evidence-based, human, and consistent with the author’s prior style.

For adapting prose to the author’s established style, use `prior-style-adapter`.

For checking whether claims are supported, use `claim-auditor`.

For verifying citations and references, use `citation-management`.

---

## 1. Core Principle

Scientific writing should be:

- clear;
- precise;
- evidence-based;
- conservative where evidence is limited;
- readable by the target audience;
- faithful to the project’s actual contribution;
- aligned with the author’s natural style.

Good scientific prose should not sound like generic AI-generated text.

It should sound like a careful researcher explaining what was done, why it matters, what the evidence shows, and where the limits are.

---

## 2. Evidence Before Elegance

Do not make a sentence more polished if the evidence behind it is unclear.

Before strengthening prose, check:

- What claim is being made?
- What evidence supports it?
- Does it need a citation?
- Does it depend on a result table, figure, run artifact, or project document?
- Is the wording proportional to the evidence?

If evidence is missing, write a visible TODO rather than a polished unsupported sentence.

Examples:

```text
TODO: needs citation for road damage detection benchmark usage.
```

```text
TODO: needs final mAP value from verified run.
```

```text
TODO: needs claim audit before final abstract.
```

---

## 3. Avoid AI-Like Writing

AI-generated scientific prose often has suspicious patterns.

Avoid writing that is too:

- perfectly symmetrical;
- overly polished;
- mechanically structured;
- full of generic transitions;
- packed with broad claims;
- repetitive in sentence rhythm;
- inflated in importance;
- vague but confident;
- filled with phrases like “plays a crucial role,” “significant advancements,” or “comprehensive framework” without specific evidence.

Bad pattern:

```text
In recent years, artificial intelligence has revolutionized numerous domains, offering unprecedented opportunities for improving efficiency and accuracy.
```

Better:

```text
Computer vision methods are increasingly used to automate visual inspection tasks, including road-surface monitoring.
```

Bad pattern:

```text
This study presents a comprehensive and robust framework that significantly enhances road damage detection performance.
```

Better:

```text
This study evaluates a detection pipeline for road damage localization and compares it with baseline models under the same dataset split and evaluation protocol.
```

The better version is less flashy but more credible.

---

## 4. Humanized Scientific Style

Humanized scientific writing does not mean casual writing.

It means the prose has:

- natural variation in sentence length;
- clear but not robotic transitions;
- selective emphasis;
- concrete nouns and verbs;
- topic-specific details;
- author-like pacing;
- honest uncertainty;
- fewer generic filler phrases.

Use natural variation:

```text
Road damage detection is visually challenging. Cracks can be thin, low contrast, or partially occluded, and the appearance of damage varies with lighting, pavement material, and camera viewpoint.
```

Avoid robotic parallelism:

```text
Road damage detection is challenging because cracks are thin. Road damage detection is challenging because cracks are low contrast. Road damage detection is challenging because cracks are occluded.
```

Avoid over-perfect paragraph shapes where every paragraph has the same sentence count and rhythm.

---

## 5. Use the Author’s Prior Style

When the project has a prior writing style file, use `prior-style-adapter`.

Typical style source:

```text
paper/style/prior_paper_style.md
```

Use prior style to adapt:

- tone;
- phrasing habits;
- paragraph flow;
- sentence rhythm;
- level of technical detail;
- conservative claim style;
- transition style;
- contribution phrasing.

Do not use prior style to:

- copy previous content;
- plagiarize distinctive phrases;
- change technical meaning;
- invent claims;
- strengthen unsupported claims;
- remove necessary caveats;
- override evidence.

Recommended workflow:

```text
scientific-writing
    → prior-style-adapter
    → claim-auditor
```

If only style adaptation is requested:

```text
prior-style-adapter
    → claim-auditor
```

The author’s style should make the text feel human and consistent, but evidence integrity still comes first.

---

## 6. Claim Strength and Wording

Scientific writing should calibrate certainty.

Use stronger wording only when evidence is strong.

| Strong wording | Safer wording |
|---|---|
| proves | provides evidence that |
| demonstrates | suggests / indicates, if evidence is limited |
| solves | addresses |
| eliminates | reduces / may reduce |
| guarantees | is designed to / can |
| generalizes | was evaluated on / showed performance on |
| robust | showed robustness under the evaluated conditions |
| state-of-the-art | competitive / strong / improved over evaluated baselines |
| significantly improves | improves, unless statistical significance is tested |
| first | avoid unless closest-prior-work evidence is strong |
| outperforms all baselines | outperforms the evaluated baselines |
| universally applicable | applicable in the evaluated setting |

Examples:

Too strong:

```text
The proposed method generalizes to real-world road damage detection.
```

Safer:

```text
The proposed method was evaluated on the available test split and showed improved detection performance under this protocol.
```

Too strong:

```text
The model is robust to challenging road conditions.
```

Safer:

```text
The model showed improved performance on the evaluated challenging cases, although broader robustness requires additional domain-shift testing.
```

---

## 7. Sentence-Level Citation Awareness

While writing, decide whether each factual external claim needs a citation.

A sentence usually needs a citation when it states:

- what prior work does;
- what most methods assume;
- what datasets or benchmarks are commonly used;
- a field trend;
- a known limitation;
- a research gap;
- problem importance;
- external domain facts;
- comparison to existing methods;
- metric or evaluation conventions.

A sentence may not need a citation when it states:

- this paper’s own goal;
- this paper’s own method;
- this paper’s own experimental setup;
- this paper’s own result, if supported by tables or run artifacts;
- a transition without factual external content.

If a citation is needed but missing, write:

```text
TODO: needs citation
```

Do not invent citation keys.

---

## 8. Paragraph Structure

A strong scientific paragraph usually does one job.

Common paragraph roles:

- motivate the problem;
- summarize prior work;
- identify a gap;
- introduce the method;
- describe an experiment;
- interpret a result;
- state a limitation.

A good paragraph often has:

1. topic sentence;
2. specific evidence or explanation;
3. connection to the paper’s argument;
4. transition to the next idea.

Avoid paragraphs that:

- mix unrelated claims;
- list citations without synthesis;
- end with vague importance;
- introduce results before methods;
- hide unsupported claims in polished prose;
- use the same rhythm repeatedly.

---

## 9. Introduction Writing Principles

A good introduction should move from context to contribution.

Typical flow:

1. problem context;
2. why the problem matters;
3. what prior work has done;
4. what limitation or gap remains;
5. what this paper does;
6. what evidence or contribution is provided.

Avoid:

- generic opening sentences;
- exaggerated claims about AI;
- unsupported “first” claims;
- related work overload;
- contribution statements that are stronger than the experiments.

Good introduction writing depends on `literature-review`.

---

## 10. Related Work Writing Principles

Related work should synthesize, not list.

Use:

- themes;
- method families;
- dataset/benchmark groupings;
- contrast with closest prior work;
- clear positioning.

Avoid:

- one-paper-per-sentence summaries;
- citation dumping;
- inflated novelty;
- missing closest prior work;
- claiming gaps without literature support.

Use `literature-review` before writing related work.

Use `citation-management` before finalizing references.

---

## 11. Method Writing Principles

Method prose should be precise and reproducible.

Include:

- task definition;
- input and output;
- model or pipeline components;
- training objective;
- preprocessing;
- postprocessing;
- implementation details needed to understand the method.

Avoid:

- claiming performance in the method section;
- hiding important implementation choices;
- vague terms such as “optimized,” “enhanced,” or “robust” without details;
- describing intended behavior as demonstrated behavior.

---

## 12. Results Writing Principles

Results prose should state what was measured and what the evidence supports.

Good results writing:

- refers to tables/figures;
- identifies the comparison;
- names the metric;
- states the evaluated setting;
- avoids broader claims than the experiment supports;
- mentions important negative or mixed results;
- separates observation from interpretation.

Avoid:

- inventing values;
- claiming statistical significance without testing;
- claiming generalization from one dataset;
- claiming mechanism without ablation;
- cherry-picking only favorable cases.

Use `results-scaffold` when final values are not ready.

Use `claim-auditor` before finalizing.

---

## 13. Discussion and Limitation Writing Principles

Discussion should interpret evidence without exaggeration.

Do:

- explain what results suggest;
- discuss likely reasons carefully;
- identify failure modes;
- connect limitations to evidence;
- state what remains untested;
- describe future work as future work.

Do not:

- introduce new unsupported claims;
- overstate practical readiness;
- hide weak results;
- use limitations as generic filler.

Good limitation:

```text
The current evaluation uses a fixed dataset split, so it does not establish performance under cross-location or cross-camera domain shift.
```

Weak limitation:

```text
There are some limitations that will be addressed in future work.
```

---

## 14. Abstract and Conclusion Principles

The abstract and conclusion are high-risk because they compress claims.

They should be audited carefully.

Abstract should include:

- problem;
- method or study focus;
- evidence;
- main result or contribution;
- cautious conclusion.

Conclusion should:

- summarize supported findings;
- avoid new claims;
- avoid new citations unless necessary;
- state limitations or future work carefully.

Do not write the abstract or conclusion before the main evidence is stable, unless clearly marked as draft.

---

## 15. Style Without Distortion

Improving style must not change technical meaning.

Allowed:

- improve clarity;
- reduce repetition;
- improve flow;
- clarify claim scope;
- make uncertainty explicit;
- align tone with prior style.

Not allowed:

- strengthen claims;
- remove caveats;
- add unsupported novelty;
- add fake citations;
- change metrics;
- change result interpretation;
- make incomplete evidence sound final.

When style and evidence conflict, evidence wins.

---

## 16. Common Phrases to Avoid or Use Carefully

Avoid unless specific evidence supports them:

- “significant advancements”
- “revolutionized”
- “crucial role”
- “comprehensive framework”
- “robust solution”
- “state-of-the-art performance”
- “highly accurate”
- “real-world ready”
- “seamlessly”
- “novel and effective”
- “substantial improvement”
- “unprecedented”
- “cutting-edge”

Prefer concrete wording:

- what method was used;
- what dataset was evaluated;
- what metric changed;
- what limitation remains;
- what comparison was made.

---

## 17. Revision Checklist

Before finalizing revised prose:

- [ ] The text sounds like a careful researcher, not generic AI.
- [ ] Sentence rhythm is natural, not mechanically perfect.
- [ ] Claims are proportional to evidence.
- [ ] External factual claims have citations or TODOs.
- [ ] No citations were invented.
- [ ] No metrics or results were invented.
- [ ] Literature-dependent sections used `literature-review`.
- [ ] References needing verification are routed to `citation-management`.
- [ ] Strong claims are routed to `claim-auditor`.
- [ ] Prior style adaptation is routed to `prior-style-adapter` when needed.
- [ ] The prose preserves technical meaning.

---

## Final Reminder

Good scientific writing is not flawless-sounding text.

Good scientific writing is human, precise, traceable, and honest about what the evidence does and does not show.

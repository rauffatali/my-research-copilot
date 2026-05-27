# Common Biases in AI/ML/CV Research

Use this reference when applying `scientific-critical-thinking` to research decisions, experiment interpretation, literature synthesis, or manuscript claims.

---

## 1. Confirmation Bias

Pattern:

- looking for evidence that the method works;
- explaining away negative results;
- citing only supportive papers;
- interpreting ambiguous outputs as success.

Mitigation:

- define falsifying outcomes before running;
- inspect failure cases;
- search for disconfirming prior work;
- report negative or ambiguous results.

---

## 2. Implementation Effort Bias

Pattern:

- assuming a method is valuable because it took effort to implement;
- keeping complex components because they are already built;
- treating code volume as research progress.

Mitigation:

- ask what decision the implementation supports;
- require ablation or baseline evidence;
- remove complexity that does not support the contribution.

---

## 3. Novelty Bias

Pattern:

- preferring newer models because they seem more publishable;
- using “modern” architectures without hypothesis;
- assuming novelty from unfamiliarity.

Mitigation:

- identify closest prior work;
- define the actual contribution type;
- compare to simple and strong baselines;
- avoid novelty claims without literature review.

---

## 4. SOTA Bias

Pattern:

- optimizing for state-of-the-art language or leaderboard framing;
- ignoring scientific insight if metric gain is small;
- overvaluing tiny gains.

Mitigation:

- define contribution independent of hype;
- check effect size and protocol fairness;
- use “competitive” or “improved under evaluated setting” when appropriate.

---

## 5. Citation Prestige Bias

Pattern:

- trusting highly cited or top-venue papers even when task relevance is weak;
- citing famous surveys instead of direct evidence.

Mitigation:

- prioritize direct relevance;
- check whether the source supports the claim;
- use `claim-auditor` for citation-context support.

---

## 6. Availability Bias

Pattern:

- overemphasizing papers/tools/models that are easy to remember or recently seen;
- ignoring less visible but closer prior work.

Mitigation:

- use `research-lookup`;
- document search trace;
- inspect closest prior work, not only famous work.

---

## 7. Benchmark Bias

Pattern:

- treating benchmark performance as the whole research contribution;
- ignoring dataset limitations and deployment mismatch.

Mitigation:

- analyze dataset scope;
- inspect failure modes;
- report limitations;
- avoid broad claims from narrow benchmarks.

---

## 8. Success-Only Reporting Bias

Pattern:

- reporting only the best model or positive experiment;
- hiding failed ablations;
- omitting negative evidence.

Mitigation:

- keep experiment logs;
- report important failed directions when relevant;
- distinguish exploratory from confirmatory results.

---

## 9. Automation Bias

Pattern:

- trusting agent-generated experiment plans, citations, or summaries because they are fluent;
- accepting plausible but shallow research directions.

Mitigation:

- require evidence;
- use research gates;
- use citation-management for references;
- use claim-auditor for claims;
- use scientific-critical-thinking for decisions.

---

## 10. Domain Familiarity Bias

Pattern:

- assuming dataset/domain behavior from intuition;
- overlooking domain-specific leakage, label noise, or deployment constraints.

Mitigation:

- inspect data;
- document label contract;
- check split policy;
- use qualitative examples;
- consult domain-specific literature when needed.

---

## 11. Bias Checklist

Before accepting a decision:

- [ ] Have we looked for disconfirming evidence?
- [ ] Are we rewarding implementation effort over scientific value?
- [ ] Is novelty actually supported?
- [ ] Are we overusing SOTA language?
- [ ] Are cited sources directly relevant?
- [ ] Are benchmarks aligned with claims?
- [ ] Are negative results considered?
- [ ] Are we trusting AI output without verification?
- [ ] Are domain assumptions documented?

---

## Final Reminder

Bias in AI/CV research often appears as overconfidence in plausible workflows.

Make evidence, baselines, and falsifying tests visible.

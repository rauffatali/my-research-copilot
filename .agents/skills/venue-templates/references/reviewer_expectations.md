# Reviewer Expectations Reference

This reference supports the `venue-templates` skill by identifying venue-related reviewer expectations.

For actual reviewer simulation, use `peer-review`.

For internal scientific critique, use `scientific-critical-thinking`.

---

## 1. Purpose

Reviewers evaluate more than formatting, but venue expectations influence what they look for.

Venue Templates may help identify required sections or format constraints that reviewers expect to see.

It should not replace scientific or peer-review critique.

---

## 2. Common Reviewer Expectations

Across research venues, reviewers often expect:

- clear problem statement;
- clear contribution;
- relevant prior work;
- appropriate methodology;
- fair baselines;
- reproducible evaluation;
- evidence-backed claims;
- limitations;
- readable figures/tables;
- compliance with venue format.

---

## 3. AI/ML/CV Reviewer Expectations

AI/ML/CV reviewers often check:

- novelty relative to closest prior work;
- baseline fairness;
- ablation quality;
- dataset/split validity;
- leakage risk;
- metric alignment;
- reproducibility;
- robustness/generalization claims;
- limitations and ethics statements where required.

Use `peer-review` for detailed critique.

---

## 4. Applied AI Reviewer Expectations

Applied reviewers often check:

- domain relevance;
- dataset realism;
- label validity;
- practical error costs;
- domain-specific metrics;
- deployment assumptions;
- connection between technical results and domain impact.

Use multi-reviewer panel mode in `peer-review` when appropriate.

---

## 5. Grant Reviewer Expectations

Grant reviewers often check:

- significance;
- innovation;
- feasibility;
- team capability;
- risk mitigation;
- milestone clarity;
- budget justification;
- broader impacts or funder-specific criteria.

---

## 6. Format-Related Reviewer Risks

Reviewers may react negatively if:

- required checklist is missing;
- anonymization is broken;
- page limits are violated;
- figures/tables are unreadable;
- required limitations/data statements are missing;
- appendix/supplement is misused;
- references are malformed.

Use `venue-templates` for these checks.

---

## 7. Handoff Rules

Use:

- `peer-review` for reviewer-style critique;
- `claim-auditor` for evidence-to-claim support;
- `citation-management` for reference issues;
- `scientific-critical-thinking` for methodology risks;
- `scientific-writing` for revision.

---

## 8. Checklist

- [ ] Venue reviewer expectations identified.
- [ ] Required sections/checklists included.
- [ ] Formatting issues separated from scientific issues.
- [ ] Reviewer-style critique routed to `peer-review`.
- [ ] Claim/evidence issues routed to `claim-auditor`.

---

## Final Reminder

Reviewer expectations are not only about formatting.

Venue Templates identifies format expectations; Peer Review evaluates whether the work is convincing.

# Research task lifecycle

For research-oriented tasks, follow this lifecycle unless the user explicitly requests a narrower action.

## 1. Classify the task

Identify the current task type:

- literature review
- research gap analysis
- hypothesis design
- experiment planning
- implementation
- evaluation
- result analysis
- failure analysis
- paper writing
- claim auditing
- peer review / critique
- refactoring / engineering maintenance

Do not jump from one stage to another without a reason.

## 2. Check relevant context

Use the smallest relevant context sources and rule files.

Do not consult every file or every rule by default.

## 3. Define the intended artifact

Before editing, identify the primary artifact type:

- code
- test
- config
- dataset metadata
- experiment plan
- experiment result scaffold
- analysis report
- paper section
- figure/table
- claim record
- documentation
- notebook

Avoid mixing unrelated artifact types in one task.

## 4. Plan narrowly

For non-trivial changes, briefly state:

- what will change,
- why it is needed,
- which files are expected to change,
- how the change will be validated.

## 5. Execute minimally

Make the smallest change that satisfies the task.

Do not perform opportunistic cleanup unless it directly supports the task.

## 6. Validate narrowly

After meaningful code, data, training, or evaluation changes, run the narrowest feasible validation:

- unit test
- smoke test
- config validation
- data-loader sanity check
- metric script dry run
- formatting/linting check
- small synthetic example

If validation is not run, explain why.

## 7. Report outcome

At the end, report:

- files changed,
- reason for each change,
- validation performed,
- remaining uncertainty,
- recommended next step.
# Skill Context

### Job this is for

Design and review eval scenarios, prompt-injection tests, workflow regression suites, Skill lifecycle decisions, and controlled self-review writeback before an AI workflow is published or updated.

### When to use it

- a new Skill, prompt, agent, or workflow is about to publish
- an existing workflow changed model, prompt, tool, retrieval, memory, permission, or approval rules
- a team needs negative evals, misuse cases, or prompt-injection tests
- a workflow has repeated failures that may need memory, Skill, or exception-log updates
- a public or internal Skill needs lifecycle review before continued use

### Inputs needed

- workflow or Skill name
- intended task and owner
- source rules
- tool and approval boundaries
- known failure modes
- eval scenarios and expected behavior
- golden task set or regression examples
- change summary
- publication or lifecycle decision needed

### Expected output

- negative eval set
- prompt-injection workflow test
- regression replay plan
- lifecycle review
- self-review writeback decision
- critical failure list
- publication decision
- safe summary for the change log

### What good looks like

- evals test failure modes, not only happy paths
- prompt-injection tests target the actual workflow and tool boundary
- workflow regressions compare behavior before and after changes
- self-review writeback is controlled and does not rewrite rules from a single failure
- publication is blocked when evals expose critical failures

### Operating steps

1. Collect the workflow, owner, sources, tool boundaries, and approval gates.
2. Define critical failures before running evals.
3. Write negative evals and misuse cases.
4. Add prompt-injection workflow tests where source material is untrusted.
5. Build or update a golden regression set.
6. Review lifecycle state and update cadence.
7. Decide whether repeated failures become memory, Skill updates, exception notes, or no change.
8. Block publication when critical failures remain.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Define eval target and critical failures | workflow contract | internal | approved eval tool | self-check | eval plan | failure policy is explicit |
| 2 | AI operations | Run negative, injection, and regression checks | redacted scenarios | internal | approved eval runner | required for publish | eval artifact | pass, fail, and evidence are recorded |
| 3 | Enablement owner | Review lifecycle and writeback decision | eval result and failure log | internal | approved review channel | required for Skill update | lifecycle record | publish, revise, deprecate, or block decision is recorded |

This run sheet is the part a manager can operationalize. If the team cannot name the critical failures, eval artifact, lifecycle owner, and publication decision, the workflow is not ready to publish.
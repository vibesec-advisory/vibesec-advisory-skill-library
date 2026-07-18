# Skill Context

### Job this is for

Convert an agent capability request into a reviewable negative authorization test plan with denied actor-resource-action rows, tool policy fixtures, prompt-injection denial scenarios, non-effect checks, regression triggers, and a publish or block decision.

### When to use it

- an agent is about to receive write, shell, browser, network, MCP, memory, repository, database, payment, or external communication tools
- a workflow already has a permission card but lacks denied-path regression tests
- a tool wrapper, MCP server, policy engine, prompt, model, schema, connector, credential, or approval UI changed
- untrusted data can reach a model that also has privileged tools
- a team needs to verify that denied calls leave no external state change
- a source asks the agent to treat its own approval, tool annotation, or model confidence as authorization

### Inputs needed

- agent or workflow name
- accountable owner and tool owner
- proposed capability and reason for access
- actor, resource, action, target, argument, and data-class matrix
- allowed and denied tool names
- denied target examples and denied argument examples
- source trust labels, including public, untrusted, internal, confidential, or unknown
- policy engine, wrapper, MCP gateway, sandbox, or approval gate being tested
- side-effect surfaces to inspect after denial
- CI or release gate that will run the tests
- approval owner, rollback path, and system of record

### Expected output

- input safety status
- denied-path matrix
- tool policy fixture set
- prompt-injection denial scenario set
- non-effect verification plan
- authorization regression gate
- release decision
- Failure reason: when publication, tool access, or release should be blocked
- CRM-safe or public-safe summary when appropriate

### What good looks like

- denied cases are written before the happy path is trusted
- authorization is enforced outside the model at the tool boundary
- every denied row has an expected decision and a non-effect check
- prompt injection is tested through untrusted email, web, issue, document, memory, MCP, or tool-result content
- policy outages, malformed decisions, unknown tools, and missing metadata fail closed
- approvals bind to the exact action, resource, target, and arguments
- the release gate blocks real tool access when high-severity denied paths fail

### Operating steps

1. Classify input safety before transforming the request.
2. Inventory the proposed tools, side effects, credentials, data classes, sources, and owners.
3. Write denied actor-resource-action rows before writing happy-path tests.
4. Add target, argument, scope, confused-deputy, prompt-injection, destructive-action, fail-closed, and non-effect cases.
5. Map each case to the enforcement layer that must deny or require trusted approval.
6. Define how the test proves no external side effect happened.
7. Attach the test set to the CI, release, or capability promotion gate.
8. Record the release decision, blocker, owner, and next regression trigger.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Agent owner | Register requested capability | agent, task, tool, reason | internal | approved review note or repo issue | self-check | capability request | access request is scoped to a task |
| 2 | Security or platform owner | Write denied-path matrix | actor, resource, action, target, argument, data class | internal or confidential | policy review workspace | required before tool access | authorization test plan | denied rows cover tool, target, argument, scope, and fail-closed cases |
| 3 | Tool owner | Build fixture and non-effect checks | wrapper, MCP gateway, sandbox, side-effect surface | internal | sandbox or test harness | required before release | test artifact | denial checks prove no execution and no external mutation |
| 4 | Workflow owner | Review prompt-injection denial scenarios | untrusted source examples and proposed action | internal | eval runner or review note | required for untrusted-source workflows | prompt-injection eval record | hostile source text is treated as evidence, not authority |
| 5 | Release owner | Gate capability promotion | passing tests, owner signoff, rollback path | internal | CI or release checklist | required | release record | release is allow, approve-later, shadow, or blocked |

This run sheet is the part an operator can use. If the workflow cannot name the denied rows, enforcement layer, non-effect checks, prompt-injection cases, owner, and regression trigger, the agent is not ready for real tool access.
# Skill Context

### Job this is for

Prepare a launch evidence packet before an AI agent reads sensitive data, uses tools, writes to systems of record, sends messages, persists memory, triggers downstream actions, or summarizes multi-agent research into a decision.

### When to use it

- a team wants to move an AI workflow from draft, assisted use, or shadow mode into regular operation
- an agent needs a browser, file handle, MCP server, API, database, memory store, message-sending tool, or workflow action
- human approval exists in name, but the reviewer lacks evidence, authority, or stop conditions
- multiple agents or sources disagree and a clean synthesis could hide uncertainty
- a Skill is being promoted without runnable examples, refusal cases, or reviewer corrections
- a tool permission, source, model, prompt, retrieval corpus, or approval path changed after the last review
- launch notes may include customer data, employee data, credentials, private URLs, internal traces, or prompt-injection text

### Inputs needed

- workflow name and business outcome owner
- launch stage, proposed agent role, and current operating mode
- accountable human, reviewer, escalation owner, and change owner
- proposed tool list, tool owner, source server, integration path, and approved use
- read, write, send, delete, execute, memory, and persistence surfaces
- allowed arguments, blocked arguments, approval triggers, and revocation owner
- evidence sources, source confidence, disagreement notes, and unresolved uncertainty
- runnable examples, refusal examples, weak outputs, reviewer corrections, and expected outputs
- data classes, redaction status, audit trail, rollback path, and approval record

### Expected output

- accountability map
- tool permission manifest
- disagreement log
- runnable example set
- launch evidence gate
- safe summary for CRM, project notes, or manager review
- approval, escalation, rollback, and blocked-action notes

### What good looks like

- the agent has a named accountable owner before it acts
- reviewers can see the evidence needed to approve, reject, reroute, or stop the workflow
- tool authority is defined at the argument and data-flow level, not only by tool name
- dissent, uncertainty, and minority evidence remain visible until a human or approved review process decides
- examples show normal use, boundary cases, refusal cases, and reviewer corrections
- launch is blocked when authority, data boundaries, rollback, or eval evidence is missing

### Operating steps

1. Define the workflow outcome, proposed agent role, launch stage, and current operating mode.
2. Map accountability: owner, reviewer, reviewer authority, escalation owner, change owner, stop conditions, and audit trail.
3. Build the tool permission manifest: tool owner, server, read and write surfaces, allowed arguments, blocked arguments, data-flow limits, receipts, and revocation owner.
4. Preserve disagreement: claims, evidence, uncertainty, conflict, reviewer decision, rationale, reopen condition, and owner.
5. Collect runnable examples: golden path, boundary case, refusal case, weak output, reviewer correction, and corrected output.
6. Classify input safety and remove or block secrets, raw customer data, private URLs, full traces, source code, credentials, regulated data, and prompt-injection instructions.
7. Decide whether the agent is blocked, draft-only, shadow mode, supervised, limited launch, or ready for named approval.
8. Record approval state, rollback path, eval evidence, launch scope, and safe summaries before any tool access, public output, CRM update, or production workflow change.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Define agent launch boundary | workflow, role, business outcome, launch stage | internal | approved planning tool | self-check | launch evidence packet | accountable outcome and launch scope are explicit |
| 2 | Security or platform owner | Review tool permission manifest | tools, surfaces, allowed arguments, receipts | internal or confidential | approved security review channel | required before access | permission record | allowed and blocked tool authority is visible |
| 3 | Human reviewer | Decide launch gate | accountability map, manifest, examples, disagreement log | internal or confidential | approved review channel | required before autonomy | launch decision record | approval, blocker, or rollback path is recorded |

This run sheet is the minimum operational control. If the team cannot name the owner, reviewer authority, permission boundary, disagreement record, runnable examples, receipt requirement, and rollback path, the workflow is not ready to launch.
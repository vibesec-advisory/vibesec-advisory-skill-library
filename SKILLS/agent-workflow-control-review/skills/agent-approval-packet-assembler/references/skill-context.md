# Skill Context

### Job this is for

Turn a proposed agent workflow into a reviewable control packet with input contracts, source labels, acceptance criteria, action previews, approval packets, retry budgets, and tool permission receipts.

### When to use it

- an agent workflow is being drafted, updated, or granted new tool access
- a human reviewer needs enough evidence to approve or reject an agent action
- a tool call, write, email, publish, deploy, payment, CRM update, or external action is being previewed
- repeated retries or replanning could create hidden side effects
- the team needs a durable receipt after a tool capability is used

### Inputs needed

- workflow name and owner
- proposed task and business outcome
- accepted inputs and blocked inputs
- source list with trust level
- planned tool calls or external actions
- approval owner and escalation path
- retry limit, replanning limit, and stop condition
- logging location and retention owner

### Expected output

- input contract
- source label map
- acceptance criteria
- action preview packet
- approval packet
- retry budget
- permission receipt template
- CRM-safe or public-safe summary

### What good looks like

- the agent knows what inputs are accepted and blocked before work starts
- source trust survives into claims, decisions, and proposed actions
- human approval is based on evidence, not model confidence
- retries stop before side effects multiply
- every capability use leaves a receipt that explains what changed

### Operating steps

1. Collect the minimum workflow description and owner.
2. Classify input safety before summarizing or transforming content.
3. Label every source as approved, untrusted, memory, retrieval, tool output, or model inference.
4. Write acceptance criteria before the agent begins work.
5. Preview risky actions before execution.
6. Build an approval packet for human review.
7. Set retry and replanning limits.
8. Record a permission receipt after capability use.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Define input contract and source labels | workflow brief | internal | approved planning tool | self-check | workflow control record | accepted and blocked inputs are visible |
| 2 | Agent operator | Prepare action preview and approval packet | proposed action and sources | internal or confidential | approved agent console | required for risky action | approval log | reviewer can approve, reject, or escalate |
| 3 | Security or ops | Review retry budget and permission receipt | tool plan and receipt | internal | approved review channel | required for external action | audit log | retry limit, stop condition, and state change are recorded |

This run sheet is the part a manager can operationalize. If the team cannot name the owner, source class, approval gate, and system of record, the workflow is not ready for agent execution.
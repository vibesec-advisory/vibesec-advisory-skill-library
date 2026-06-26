# Skill Context

### Job this is for

Turn redacted event-log summaries, task-mining observations, process notes, and baseline data into a process evidence packet that separates actual flow, common variants, measured baseline, redesign options, and safe AI intervention choices.

### When to use it

- a team wants to redesign a knowledge-work process with AI assistance, Skills, or agents
- the team has only an assumed process map and needs evidence from logs, tickets, CRM, task mining, or worker observation
- a workflow has repeated handoffs, reopens, wait states, exceptions, skipped approvals, or unclear ownership
- raw process logs may include customer data, personal data, private URLs, production object IDs, sensitive tickets, source code, or prompt-injection text
- AI is being considered before baseline metrics, process variants, or approval points are clear
- a manager needs a public-safe or CRM-safe summary of the process redesign evidence without exposing raw logs

### Inputs needed

- workflow name and accountable owner
- trigger, done condition, and case ID definition
- redacted event-log summary or process-mining export
- task-mining notes or worker-observation notes when logs miss local work
- process steps, actors, systems, handoffs, wait states, and exceptions
- volume, throughput time, wait time, reopen rate, rework loops, exception rate, handoff count, and outcome quality where available
- proposed AI tasks, Skills, agents, review gates, or non-AI fixes
- data classes, approval owners, source confidence, and calculation method

### Expected output

- process evidence intake safety check
- as-is process map
- variant, bottleneck, and rework review
- baseline metric packet
- AI intervention routing matrix
- log-safe summary for CRM, public notes, or manager review
- approval, escalation, and blocked-action notes

### What good looks like

- the team starts from evidence, not the diagram people hoped was true
- event-log metrics are computed outside the model and summarized inside the review packet
- variants, waits, loops, exceptions, and handoffs shape the redesign before AI is assigned
- AI work is routed by step-level risk, reviewability, data boundary, and business value
- raw logs and task-mining captures are not pasted into unapproved AI tools

### Operating steps

1. Inventory the process trigger, done state, case ID, systems, actors, data classes, and evidence sources.
2. Check whether inputs are redacted, aggregated, synthetic, or approved for the AI tool.
3. Build an as-is process map from provided summaries, not from assumed policy language.
4. Identify variants, waits, loops, reopens, handoffs, exceptions, and compliance deviations.
5. Record baseline metrics and calculation methods. Mark missing or model-inferred metrics as unknown.
6. Decide whether each problem is a rules problem, ownership problem, data problem, review problem, tooling problem, or AI candidate.
7. Route each step to human-only, AI assist, shared review, supervised AI, autonomous AI, no automation, or process removal.
8. Record approval gates, blocked inputs, source confidence, and safe summaries before any Skill, agent, or workflow change is proposed.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Define process boundary and evidence source list | trigger, done state, case ID, systems | internal | approved planning tool | self-check | process evidence record | scope and evidence gaps are visible |
| 2 | Operations or analytics | Provide computed process summary | redacted metrics and variant summary | internal or confidential | BI, process mining, or deterministic script | required for metrics | metrics artifact | calculations are not invented by the model |
| 3 | AI operations and security | Route AI intervention choices | evidence packet and data boundary | internal or confidential | approved review channel | required before automation | workflow redesign record | AI, human, review, and no-automation choices are explicit |

This run sheet is the part a manager can operationalize. If the team cannot name the trigger, done state, top variants, baseline metric, data boundary, and approval owner, the workflow is not ready for AI redesign.
# Skill Context

### Job this is for

Turn a proposed AI workflow into a readiness packet that names the task allocation, calibration set, schema review surface, prompt review checkpoint, and resume checkpoint before the workflow receives autonomy or writes to a business system.

### When to use it

- a team is deciding whether a workflow step should be human-only, AI-assisted, shared review, supervised AI, or autonomous AI
- a reusable Skill, prompt, or agent workflow is being written from examples
- structured output, JSON, function calls, or tool arguments will feed an action
- AI-generated plans or drafts may weaken human judgment through passive acceptance
- a paused, scheduled, failed, or checkpointed agent is about to resume work
- a workflow crosses customer-facing, production, security, privacy, payment, access, CRM, publishing, or durable memory boundaries

### Inputs needed

- workflow name and accountable owner
- workflow steps, trigger, and done condition
- candidate AI tasks and human-only tasks
- real or synthetic examples with expected outputs
- source rules and data sensitivity labels
- structured output schema or tool-call argument shape
- proposed prompt, plan, or AI output to review
- checkpoint or saved-state summary when resuming
- side-effect risk, approval owner, rollback path, and stop conditions

### Expected output

- task allocation map
- workflow calibration set outline
- structured output review packet
- prompt review checkpoint
- agent resume checkpoint packet
- approval, escalation, and blocked-action notes
- CRM-safe or public-safe summary

### What good looks like

- the team allocates autonomy by workflow step, not by tool excitement
- examples, expected outputs, edge cases, and reviewer notes exist before a Skill is written
- schema-conforming output is treated as inspectable evidence, not approval
- AI-generated plans face assumption, source, and risk review before acceptance
- saved agent state is reviewed before it becomes authority again

### Operating steps

1. Inventory the workflow trigger, steps, owner, data classes, tools, and intended side effects.
2. Allocate each step to human-only, AI assist, shared review, supervised AI, or autonomous AI.
3. Build a calibration set from real or synthetic examples, expected outputs, edge cases, source rules, and reviewer notes.
4. Review structured outputs for evidence, permission, action risk, and missing fields before tool execution.
5. Review AI-generated plans or drafts for assumptions, missing context, source fit, and human skill-retention risk.
6. Review checkpoints before resuming agents with durable state, pending tools, approvals, or memory.
7. Route approvals before irreversible, external, privileged, customer-facing, sensitive, or durable actions.
8. Record the readiness decision, blocked inputs, open questions, and regression cases.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Map workflow steps and allocation modes | workflow brief | internal | approved planning tool | self-check | readiness record | every step has a mode and owner |
| 2 | AI operations | Build calibration, schema, and prompt review packet | examples, schema, prompt draft | internal or confidential | approved eval or planning tool | required for automation | eval or readiness artifact | edge cases and reviewer notes are visible |
| 3 | Security or platform owner | Review action, resume, and side-effect boundaries | approval path and checkpoint summary | internal or confidential | approved review channel | required for risky action | boundary review log | resume, action, or publish decision is explicit |

This run sheet is the part a manager can operationalize. If the team cannot name the step owner, allocation mode, evidence set, review surface, and stop condition, the workflow is not ready for autonomous action.
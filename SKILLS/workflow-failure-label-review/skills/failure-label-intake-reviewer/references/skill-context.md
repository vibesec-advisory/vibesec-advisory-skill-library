# Skill Context

### Job this is for

Turn a failed or risky AI workflow run into a structured failure label record with failure mode, trigger, affected surface, visibility, severity, recoverability, evidence, root-cause note, and next checkpoint.

### When to use it

- an AI workflow eval, regression run, pilot, agent trace, support review, coding run, or review note only says pass or fail
- a team wants to update a Skill but has not named whether the failure belongs in the Skill, prompt, memory, tool contract, parser, source, approval step, or rollback path
- a failure may be invisible to the user because the output looked polished, the user stopped engaging, or the workflow reached a final answer through an unsafe path
- a reviewer needs to separate surface symptoms from root cause before adding eval cases
- a production incident, near miss, or customer-facing draft needs a safe label without copying raw sensitive evidence
- source notes may include raw traces, private URLs, customer text, credentials, prompt injection, unsupported approval claims, or unapproved sensitive details

### Inputs needed

- workflow name, agent name, owner, reviewer, and evaluation context
- redacted failure summary, near-miss summary, or eval output
- source evidence such as trace ID, prompt version, tool output, eval case, screenshot, ticket, commit, user report, or reviewer note
- expected behavior, actual behavior, and whether the final outcome passed, failed, or needs review
- suspected failure mode, trigger, affected surface, visibility, severity, recoverability, and next checkpoint when known
- data class, redaction status, approved evidence path, and retention limit
- current Skill, prompt, tool contract, memory item, approval gate, or eval case that may need updating
- release, customer-facing, CRM, production, or compliance decision that someone wants to make from the label

### Expected output

- failure label record
- evidence and redaction review
- symptom versus root-cause split
- invisible-failure and trajectory-quality note
- next-checkpoint route
- eval-case conversion packet
- safe summary for workflow notes, CRM, incident review, or public-safe lessons when appropriate
- blocked-label note when the evidence is unsafe, missing, or being used to justify unsupported authority

### What good looks like

- pass or fail is treated as a signal, not a diagnosis
- every label is tied to evidence and redaction status
- surface symptoms are separated from root cause
- invisible failures are marked even when the final answer looks acceptable
- the next checkpoint says clarify, ask, confirm, stop, refuse, recover, human review, Skill update, or tool contract update
- labels do not approve release, customer messaging, CRM updates, memory writes, or production actions by themselves
- recurring labels become eval cases only after source boundaries and expected safe behavior are clear

### Operating steps

1. Classify input safety before summarizing the failure or copying evidence.
2. Name the workflow, run, source evidence, expected behavior, and actual behavior.
3. Label failure mode, trigger, affected surface, visibility, severity, and recoverability.
4. Split visible symptom from likely root cause and mark uncertainty.
5. Decide whether the next checkpoint is clarify, ask, confirm, stop, refuse, recover, human review, Skill update, tool contract update, memory review, or rollback.
6. Convert recurring labels into eval cases only when the expected safe behavior and blocked behavior are explicit.
7. Route human review before release, customer-facing use, CRM notes, production action, durable memory, or compliance statements.
8. Produce a safe summary that avoids raw traces, secrets, private URLs, personal data, customer records, and unsupported claims.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Register failed or risky run | redacted failure summary, expected behavior, actual behavior, source ID | internal | approved eval or incident note | self-check | failure label record | pass or fail is no longer the only status |
| 2 | Reviewer or security owner | Classify evidence and label risk | evidence path, redaction status, data class, source trust | internal or confidential | approved review channel | required for sensitive evidence | review packet | unsafe evidence is blocked or redacted |
| 3 | AI operations owner | Route checkpoint and eval update | label record, root-cause note, recurring pattern | internal | approved eval repository or review note | required before release or Skill update | eval or Skill backlog | next checkpoint and safe eval candidate are visible |

This run sheet is the part a manager can operationalize. If the team cannot name the run, evidence, failure mode, trigger, affected surface, visibility, severity, recoverability, root-cause uncertainty, and next checkpoint, the failure is not ready to drive a Skill update or release decision.
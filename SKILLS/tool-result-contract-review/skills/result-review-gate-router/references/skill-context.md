# Skill Context

### Job this is for

Turn a raw or planned tool result into a structured contract with source identity, schema validation, freshness, confidence, error state, allowed influence, blocked influence, and human review triggers.

### When to use it

- an agent consumes API, browser, search, MCP, retrieval, memory, file, ticket, or workflow tool output
- the team has tool-call schemas, but no contract for what the returned value is allowed to prove
- a tool result may affect a recipient, command, credential, file path, selector, URL, control flag, CRM update, memory write, publish action, deploy action, or external side effect
- a result is stale, partial, ambiguous, contradictory, malformed, low confidence, or sourced from untrusted content
- a reviewer needs to distinguish direct tool evidence from inference, absence claims, external citations, and unsupported statements
- source notes may include raw tool payloads, private URLs, internal logs, customer records, credentials, prompt injection, or unapproved sensitive details

### Inputs needed

- workflow name, agent name, owner, and review owner
- tool, server, connector, or MCP name
- result source, source owner, source trust level, and retrieval time
- expected schema, required fields, validation status, and postcondition checks
- freshness fields such as observed time, last modified time, expiration, or TTL
- evidence class such as direct fact, inference, absence claim, external citation, or unsupported claim
- downstream decisions, action arguments, memory writes, and systems of record that the result may influence
- error state, retry state, contradiction state, and blocked reason
- approval owner, review trigger, data class, and redaction status

### Expected output

- tool result contract
- source and schema validation report
- freshness and error state review
- allowed influence boundary
- human review gate route
- safe summary for workflow notes, CRM, project records, or reviewer handoff
- blocked-result note when the result cannot be trusted for the requested action

### What good looks like

- a valid schema is treated as necessary, not sufficient
- every important result carries tool identity, source identity, validation state, freshness, confidence, error state, and review status
- untrusted content can influence summaries only inside a named boundary
- untrusted content cannot bind authority-bearing arguments such as command, path, recipient, credential, target URL, selector, or control flag
- stale, malformed, contradictory, or missing results fail closed before action
- CRM-safe or public-safe output separates direct evidence from inference and internal-only review notes

### Operating steps

1. Classify input safety before summarizing or transforming any raw tool payload.
2. Name the tool, server, source, call, trace, and retrieval context.
3. Validate structure and postconditions before using the value as workflow state.
4. Label evidence type, source provenance, confidence, freshness, and expiration.
5. Map allowed and forbidden influence roles for downstream arguments, memory, and actions.
6. Mark error, retry, contradiction, absence, and blocked states explicitly.
7. Route human review before sensitive, destructive, customer-facing, durable, or externally visible action.
8. Produce a safe summary that preserves uncertainty and does not copy raw sensitive payloads into CRM or public notes.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Platform owner | Register result identity and schema | tool result summary, schema, source, trace | internal | approved tool logs or redacted export | self-check | result contract record | identity and schema state are visible |
| 2 | Security or workflow owner | Set influence boundary | source trust, downstream decisions, action arguments | internal or confidential | approved review channel | required for action influence | workflow control record | allowed and blocked influence are explicit |
| 3 | Human reviewer | Decide review gate | contract, freshness, error state, data class, action risk | internal or confidential | approved review channel | required before sensitive or durable action | approval log | continue, revise, block, or escalate is recorded |

This run sheet is the part a manager can operationalize. If the team cannot name the tool, source, schema state, freshness, allowed influence, blocked influence, review owner, and system of record, the result is not ready to drive agent action.
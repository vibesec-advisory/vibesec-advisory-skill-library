# Skill Context

### Job this is for

Turn a proposed agent workflow into a boundary control packet that names what the agent may see, reach, remember, reuse, infer, and act on before it receives tools or produces durable output.

### When to use it

- an agent reads screenshots, PDFs, images, browser pages, document previews, emails, tickets, pull requests, retrieval results, or tool outputs
- a workflow needs outbound network access, web search, browser access, package registries, vendor APIs, webhooks, or MCP tools
- traces may become logs, memory, evals, tickets, incident notes, training examples, or vendor-visible telemetry
- an agent is about to write files, email, publish, deploy, update CRM, call tools, store memory, or make a customer-facing claim from inferred intent
- a model, prompt, tool, data source, egress rule, tracing rule, or approval path changes

### Inputs needed

- workflow name and owner
- agent identity, model, tools, and runtime
- source list with modality and trust level
- allowed outbound domains, methods, and tools
- trace destinations and reuse purposes
- data classes that may be viewed, sent, logged, or retained
- planned action and side effect risk
- approval owner, rollback path, retention owner, and system of record

### Expected output

- multimodal evidence boundary
- outbound egress allowlist packet
- trace redaction gate
- assumption register
- boundary change review
- approval, logging, retention, and rollback notes
- CRM-safe or public-safe summary

### What good looks like

- visual and document inputs are evidence, not instructions
- outbound access is scoped by workflow need, not agent convenience
- traces are redacted before durable reuse or external export
- assumptions are visible before side effects
- boundary changes trigger regression checks and human approval

### Operating steps

1. Inventory the workflow, owner, tools, data classes, sources, and proposed side effects.
2. Mark source modality and trust level before extraction or planning.
3. Convert untrusted visual or document inputs into a limited evidence packet.
4. Define outbound destinations, HTTP methods, tools, and exception rules.
5. Classify trace contents before export, memory, eval, ticket, or telemetry reuse.
6. Write an assumption register before state-changing, external, sensitive, or customer-facing action.
7. Review any boundary change against golden tasks, prompt-injection tests, and approval paths.
8. Record the approval decision, log location, retention window, and rollback path.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Inventory source, tool, network, trace, and action boundaries | workflow brief | internal | approved planning tool | self-check | boundary control record | all boundary surfaces are listed |
| 2 | Security or platform owner | Review multimodal, egress, trace, and assumption controls | boundary packet | internal or confidential | approved security review channel | required for risky boundary | boundary review log | allowed and blocked surfaces are explicit |
| 3 | Agent operator | Run boundary regression and record approval | eval set and proposed change | internal | approved eval runner | required before release | eval artifact | critical failures are absent and evidence is saved |

This run sheet is the part a manager can operationalize. If the team cannot name what the agent may see, reach, log, reuse, infer, and do next, the workflow is not ready for autonomous action.
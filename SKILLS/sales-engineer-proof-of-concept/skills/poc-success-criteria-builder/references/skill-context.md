# Skill Context

### Job this is for

Plan, run, and close a customer proof of concept with clear scope, success criteria, risks, dependencies, and human approval gates.

### When to use it

- A qualified opportunity needs a technical validation plan
- A rep asks for a POC without clear success criteria
- A customer shares technical requirements that need structure
- A POC is drifting and needs a closeout path

### Inputs needed

- customer segment and use case
- redacted technical requirements
- stakeholder roles without personal contact details
- qualification status, AE confirmation, and buyer urgency
- expected SE effort and capacity signal
- current architecture summary at a high level
- approved demo environment, sandbox, or synthetic data path
- known constraints, dates, and dependencies
- approved product capabilities and limitations

### Expected output

- POC qualification and capacity gate
- POC scope summary
- demo environment or synthetic data path
- success criteria table
- risk and dependency register
- mutual action plan draft
- security and legal review trigger list
- POC closeout summary format

### What good looks like

- success criteria are measurable and tied to buyer value
- the plan separates facts from assumptions
- risks are visible before the customer sees the plan
- no unapproved roadmap or integration commitment appears
- customer data is redacted enough for the approved AI tool
- POC planning is blocked when qualification, SE capacity, demo path, or success criteria are missing

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner                  | Action                                                   | Required input                  | Data class   | Approved tool path      | Approval gate                       | System of record                  | Done when                                                                      |
| ---- | ---------------------- | -------------------------------------------------------- | ------------------------------- | ------------ | ----------------------- | ----------------------------------- | --------------------------------- | ------------------------------------------------------------------------------ |
| 1    | Sales Engineer         | Confirm POC objective and approved product capabilities  | redacted opportunity notes      | confidential | approved GTM AI tool    | manager before customer-facing plan | CRM opportunity and POC workspace | measurable success criteria, risk register, and approval triggers are complete |
| 2    | Sales Engineer Manager | Review customer-facing POC plan                          | draft plan and success criteria | internal     | document review only    | required                            | approved POC packet               | no unapproved scope, timeline, compliance, or roadmap claims remain            |
| 3    | Security or Legal      | Review data, compliance, and custom integration triggers | trigger list only               | confidential | approved review channel | required when triggered             | approval record                   | approval or blocked reason is recorded                                         |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
# Skill Context

### Job this is for

Prepare an internal renewal risk brief with evidence, open questions, save plan options, and customer-safe language.

### When to use it

- renewal is 90 to 120 days out
- health score changed
- support issues may affect renewal
- leadership needs a clean risk readout

### Inputs needed

- renewal date window
- aggregated adoption signals
- redacted support themes
- approved commercial context
- known customer goals
- existing action items

### Expected output

- risk summary
- evidence table
- save plan
- customer-safe talk track
- manager escalation list

### What good looks like

- risk is evidence-backed and not melodramatic
- support issues are summarized without exposing private details
- commercial context stays internal
- customer-facing language is constructive

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner                       | Action                                              | Required input           | Data class   | Approved tool path   | Approval gate           | System of record | Done when                                                  |
| ---- | --------------------------- | --------------------------------------------------- | ------------------------ | ------------ | -------------------- | ----------------------- | ---------------- | ---------------------------------------------------------- |
| 1    | Account Manager             | Collect renewal window and aggregated risk evidence | approved account signals | confidential | approved AI tool     | self-check              | risk brief       | risk rating is evidence-backed                             |
| 2    | Manager                     | Review save plan and customer messaging             | risk brief               | internal     | document review only | required                | renewal plan     | discounts, executive language, and churn risk are approved |
| 3    | Legal, Security, or Support | Review contractual or incident-related risks        | triggered items only     | restricted   | review channel       | required when triggered | approval record  | customer-facing language does not expose internal analysis |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
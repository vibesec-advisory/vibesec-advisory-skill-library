# Skill Context

### Job this is for

Convert closed-won opportunity context into a safe implementation handoff with commitments, assumptions, risks, and required review items clearly separated.

### When to use it

- after closed-won
- before kickoff
- when sales notes contain unclear promises
- when implementation needs a clean source of truth

### Inputs needed

- approved order form summary
- redacted discovery and POC notes
- confirmed success criteria
- implementation constraints
- known risks
- customer stakeholders by role

### Expected output

- handoff brief
- confirmed commitments table
- assumptions and open questions
- risk register
- kickoff agenda
- CRM-safe summary

### What good looks like

- confirmed commitments are sourced
- unclear promises are flagged not hidden
- implementation risks have owners
- customer-sensitive data is minimized
- kickoff language aligns with approved scope

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner                           | Action                                                          | Required input               | Data class   | Approved tool path   | Approval gate           | System of record         | Done when                                                       |
| ---- | ------------------------------- | --------------------------------------------------------------- | ---------------------------- | ------------ | -------------------- | ----------------------- | ------------------------ | --------------------------------------------------------------- |
| 1    | AE                              | Collect signed scope, confirmed commitments, and redacted notes | approved opportunity context | confidential | approved AI tool     | self-check              | handoff draft            | unconfirmed sales notes are labeled assumptions                 |
| 2    | Implementation Lead             | Review kickoff plan and risks                                   | handoff draft                | internal     | document review only | required                | implementation workspace | scope, risks, and open questions are clear                      |
| 3    | Manager, Legal, Security, or SE | Resolve commitment disputes and sensitive data triggers         | flagged items only           | restricted   | review channel       | required when triggered | approval record          | custom work, data handling, and contractual issues are approved |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
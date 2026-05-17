# Skill Context

### Job this is for

Prepare for discovery, clean up notes, produce qualification summaries, and draft follow-up without leaking sensitive customer information or inventing commitments.

### When to use it

- before a first or second discovery call
- after a messy call transcript needs cleanup
- when qualification notes need structure
- when a follow-up email needs manager-safe language

### Inputs needed

- public company context
- redacted call notes
- buyer role and business pain
- current tools at category level
- qualification framework fields
- approved next steps

### Expected output

- discovery question plan
- qualification summary
- follow-up email draft
- CRM-safe note
- manager review checklist

### What good looks like

- questions are specific to the buyer job
- notes separate direct customer statements from rep interpretation
- follow-up does not invent pricing, roadmap, or legal claims
- CRM summary contains no sensitive personal or customer data

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner         | Action                                         | Required input                      | Data class   | Approved tool path   | Approval gate                 | System of record | Done when                                                               |
| ---- | ------------- | ---------------------------------------------- | ----------------------------------- | ------------ | -------------------- | ----------------------------- | ---------------- | ----------------------------------------------------------------------- |
| 1    | AE            | Prepare call plan and redacted account context | public research and CRM-safe notes  | internal     | approved GTM AI tool | self-check                    | call prep doc    | questions align to buyer workflow and do not reveal private CRM history |
| 2    | AE            | Clean notes after call                         | redacted notes, not full transcript | confidential | approved GTM AI tool | manager if forecast-impacting | CRM summary      | facts, assumptions, and next steps are separated                        |
| 3    | Sales Manager | Review commitments and qualification summary   | AI output and source notes          | internal     | document review only | required for forecast use     | CRM opportunity  | no invented pain, urgency, pricing, or decision criteria remain         |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
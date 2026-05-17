# Skill Context

### Job this is for

Turn buyer milestones, seller tasks, approval owners, and risks into a clear mutual action plan that can be reviewed before sharing.

### When to use it

- after discovery confirms a real buying process
- before procurement or legal starts
- when internal next steps are fragmented
- when a deal risk needs escalation

### Inputs needed

- redacted opportunity stage
- buyer-approved milestones
- internal task owners by role
- known risks
- approved dates
- commercial assumptions marked as unapproved

### Expected output

- mutual action plan table
- risk register
- buyer and seller responsibilities
- approval gate list
- CRM-safe plan summary

### What good looks like

- dates are tagged as confirmed or proposed
- seller responsibilities are realistic
- buyer tasks are phrased as requests not demands
- legal, security, and procurement gates are explicit

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner                  | Action                                                     | Required input              | Data class   | Approved tool path   | Approval gate           | System of record     | Done when                                            |
| ---- | ---------------------- | ---------------------------------------------------------- | --------------------------- | ------------ | -------------------- | ----------------------- | -------------------- | ---------------------------------------------------- |
| 1    | AE                     | Collect confirmed milestones and proposed dates separately | buyer-approved notes        | internal     | approved GTM AI tool | self-check              | MAP draft            | confirmed and proposed dates are labeled             |
| 2    | Sales Manager          | Review customer-facing plan                                | MAP draft and risk register | internal     | document review only | required                | shared customer plan | no fake urgency or unapproved close pressure remains |
| 3    | Legal, Security, or SE | Review gating milestones                                   | triggered items only        | confidential | review channel       | required when triggered | approval record      | risky milestones are approved, changed, or blocked   |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
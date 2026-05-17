# Skill Context

### Job this is for

Triage RFP or RFI questions, draft responses from approved source material, and flag anything that needs SME, legal, or security review.

### When to use it

- an RFP asks repetitive product questions
- security or legal sections need routing
- responses need a source-backed first draft
- a deadline creates pressure to answer without review

### Inputs needed

- RFP questions with customer names removed
- approved answer library excerpts
- product capability matrix
- security FAQ approved for external use
- routing rules for SMEs

### Expected output

- answer draft table
- source references
- confidence rating
- review owner routing
- unanswered questions list

### What good looks like

- answers cite approved source material
- low-confidence responses are not polished into certainty
- security and legal claims are routed before sending
- unknowns are marked clearly

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner             | Action                                          | Required input           | Data class   | Approved tool path        | Approval gate            | System of record      | Done when                                         |
| ---- | ----------------- | ----------------------------------------------- | ------------------------ | ------------ | ------------------------- | ------------------------ | --------------------- | ------------------------------------------------- |
| 1    | Proposal Owner    | Load questions and approved answer library only | redacted RFP questions   | confidential | approved proposal AI tool | self-check               | answer worksheet      | each answer has source and confidence             |
| 2    | SME Owner         | Review routed answers                           | draft answer table       | internal/NDA | document review only      | required for routed rows | approved answer table | blocked rows remain blocked until approved        |
| 3    | Legal or Security | Approve sensitive claims                        | security/legal rows only | confidential | approved review channel   | required                 | audit record          | send status is approved, blocked, or needs review |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
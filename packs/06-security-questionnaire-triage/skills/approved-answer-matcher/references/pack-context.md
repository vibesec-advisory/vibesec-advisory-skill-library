# Pack Context

### Job this is for

Classify questionnaire questions, match them to approved answers, identify sensitive fields, and route high-risk items to security or legal.

### When to use it

- a prospect sends a vendor security questionnaire
- answers need to be grouped by review owner
- the team needs a safe first-pass triage
- reps are tempted to answer from memory

### Inputs needed

- question list with prospect identifiers removed
- approved security response library
- public security page language
- NDA status
- internal routing map

### Expected output

- question classification
- safe draft answer where available
- sensitivity level
- review owner
- do-not-answer list

### What good looks like

- sensitive controls are not disclosed in detail
- answers distinguish public, NDA, and internal-only information
- unknowns route to security
- no one-off security commitments are created

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner            | Action                                             | Required input          | Data class   | Approved tool path                     | Approval gate | System of record         | Done when                                                       |
| ---- | ---------------- | -------------------------------------------------- | ----------------------- | ------------ | -------------------------------------- | ------------- | ------------------------ | --------------------------------------------------------------- |
| 1    | SE or RevOps     | Classify questions and remove prospect identifiers | questionnaire text only | confidential | approved AI tool for security workflow | self-check    | triage worksheet         | each question has sensitivity and review owner                  |
| 2    | Security         | Review control and audit responses                 | NDA or internal rows    | restricted   | security review channel                | required      | approved response record | control detail is approved or withheld                          |
| 3    | Legal or Privacy | Review privacy and data-processing answers         | privacy rows only       | restricted   | legal review channel                   | required      | approval record          | DPA, subprocessor, retention, and incident language is approved |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
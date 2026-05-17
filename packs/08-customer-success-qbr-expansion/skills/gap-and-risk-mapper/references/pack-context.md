# Pack Context

### Job this is for

Turn approved customer health, adoption, and outcome notes into a QBR narrative, expansion hypothesis, and safe executive summary.

### When to use it

- before a QBR
- when usage notes need an executive summary
- when expansion ideas need evidence
- when success and sales need shared account context

### Inputs needed

- aggregated usage metrics approved for AI use
- redacted support themes
- customer goals
- health-score freshness date and owner
- redacted support-ticket themes
- contract-safe product usage summary
- approved outcome evidence

### Expected output

- QBR storyline
- outcome and gap table
- expansion hypothesis
- customer-facing agenda
- internal risk notes

### What good looks like

- ROI claims are evidence-based or marked as hypothesis
- usage data is aggregated and non-sensitive
- support issues are framed responsibly
- expansion suggestions align to customer goals

### Operating steps

1. Collect only the minimum inputs needed for the workflow.
2. Remove customer identifiers and sensitive fields before using AI.
3. Run the AI skill with the approved prompt system below.
4. Review the output against the manager QA checklist.
5. Route flagged items to the right human owner before anything customer-facing is sent.
6. Save only the CRM-safe summary and approved artifacts.

### Operator run sheet

| Step | Owner             | Action                                                           | Required input          | Data class   | Approved tool path   | Approval gate               | System of record | Done when                                         |
| ---- | ----------------- | ---------------------------------------------------------------- | ----------------------- | ------------ | -------------------- | --------------------------- | ---------------- | ------------------------------------------------- |
| 1    | CSM               | Prepare aggregated customer outcomes and redacted support themes | approved aggregate data | confidential | approved CS AI tool  | self-check                  | QBR prep doc     | no user-level behavior or contract details appear |
| 2    | CS Manager        | Review expansion and risk narrative                              | QBR draft               | internal     | document review only | required for expansion asks | QBR deck         | ROI and expansion claims are evidence-backed      |
| 3    | Security or Legal | Review contractual, privacy, or data claims                      | triggered items only    | restricted   | review channel       | required when triggered     | approval record  | customer-facing metrics and claims are approved   |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for customer-facing use.
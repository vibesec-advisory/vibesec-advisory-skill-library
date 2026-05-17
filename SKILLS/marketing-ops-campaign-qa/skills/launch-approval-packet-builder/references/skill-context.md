# Skill Context

### Job this is for

Prepare, review, launch, and summarize marketing campaigns with clear segment, consent, tracking, personalization, approval, and post-send evidence checks.

### When to use it

- a campaign is moving from brief to build
- segment or consent logic needs QA before launch
- personalization, tracking, or A/B test setup needs review
- a manager needs a launch approval packet
- post-send performance needs a safe evidence-backed summary

### Inputs needed

- campaign brief with names and private details removed
- target segment definition and source system
- consent fields and suppression-list version
- tracking parameter plan and attribution caveat
- personalization token list and test-send results
- send volume estimate, launch date, and approval owner

### Expected output

- campaign input safety decision
- segment and consent QA checklist
- tracking and personalization QA findings
- launch approval packet
- post-send evidence summary
- system-of-record-safe campaign note

### What good looks like

- segment logic is explicit and reviewed
- consent and suppression checks happen before scheduling
- tracking links and personalization tokens are tested
- post-send claims distinguish evidence-backed, inferred, and blocked claims
- no raw contact data or consent audit logs are pasted into AI

### Operating steps

1. Collect only the minimum inputs needed for campaign QA.
2. Remove customer, prospect, employee, account, and consent-record identifiers before using AI.
3. Run the relevant skill from the skill library.
4. Review the output against the manager QA checklist.
5. Route flagged items to Marketing Ops, demand gen, privacy, legal, or analytics before launch or distribution.
6. Save only the approved launch packet and system-of-record-safe campaign summary.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Marketing Ops | Screen campaign inputs and data classes | redacted campaign brief | internal | approved GTM AI tool | self-check | campaign workspace | unsafe fields are removed or blocked |
| 2 | Marketing Ops or Demand Gen | Review segment, consent, suppression, and tracking | segment criteria and QA checklist | confidential | approved GTM AI tool | manager before scheduling | MAP campaign record | segment, consent, suppression, tracking, and personalization checks are complete |
| 3 | Privacy, Legal, or Analytics | Review triggered risks | flagged items only | restricted | review channel | required when triggered | approval record | launch or blocked reason is recorded |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for launch.
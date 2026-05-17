# Pack Context

### Job this is for

Prepare, QA, send, learn from, and improve outbound BDR sequences with clear account-fit gates, sourced claims, consent and suppression checks, safe reply handling, and response-rate measurement.

### When to use it

- a BDR team is building a new outbound sequence
- a rep wants to personalize outreach from public or approved account signals
- a manager needs QA before sending a campaign or sequence
- replies need safe triage without exposing personal data or private notes
- the team wants to compare response rates across safe variants

### Inputs needed

- ICP definition and target segment with private details removed
- approved account signals and source URLs or source names
- approved value proposition, product claims, and proof points
- channel, sequence steps, send windows, and suppression rules
- opt-out, consent, and regional constraints by policy owner
- aggregated response-rate, meeting-rate, bounce, unsubscribe, and negative-reply data

### Expected output

- outbound input safety decision
- ICP and trigger-fit gate
- claim and evidence QA result
- sequence and channel compliance checklist
- reply triage and safe follow-up guidance
- response-rate experiment plan and learning summary
- CRM-safe outbound activity summary

### What good looks like

- each account or segment has a clear fit reason from approved sources
- personalization uses public, approved, or redacted signals only
- unsupported product, ROI, pricing, legal, security, or compliance claims are blocked
- sequence changes respect consent, opt-out, suppression, and channel rules
- response-rate analysis separates signal, noise, and revenue impact assumptions

### Operating steps

1. Collect only the minimum inputs needed for outbound QA and learning.
2. Remove contact names, emails, phone numbers, account IDs, private URLs, exact pricing, CRM notes, and private buying signals before using AI unless the tool is approved for that data class.
3. Run the relevant skill from the pack skill library.
4. Review the output against the manager QA checklist.
5. Route flagged items to sales leadership, RevOps, marketing ops, legal, privacy, security, or product marketing before sending or updating the sequence.
6. Save only approved sequence assets, aggregate experiment notes, and CRM-safe activity summaries.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | BDR or BDR Manager | Screen account, contact, and sequence inputs | redacted target segment and draft sequence | internal | approved GTM AI tool | self-check | sales engagement workspace | unsafe fields are removed or blocked |
| 2 | BDR Manager or RevOps | Review ICP fit, claims, suppression, and channel rules | fit gate and QA output | confidential | approved GTM AI tool | manager before sending | sales engagement platform | sequence is approved, blocked, or marked needs review |
| 3 | Legal, Privacy, Product Marketing, Security, or Sales Leadership | Review triggered risks | flagged items only | restricted | review channel | required when triggered | approval record | send decision or blocked reason is recorded |

This run sheet is the part a manager can operationalize. If a team cannot identify the owner, data class, approval gate, and system of record for a run, the workflow is not ready for outbound use.
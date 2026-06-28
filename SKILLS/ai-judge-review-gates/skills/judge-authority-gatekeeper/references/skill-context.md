# Skill Context

### Job this is for

Prepare an AI judge review gate before a model, reviewer agent, scoring prompt, or evaluation workflow approves, rejects, routes, closes, grades, or escalates AI-assisted work.

### When to use it

- a team wants to use an LLM judge to score support drafts, research summaries, tickets, content, code review notes, sales artifacts, security questionnaire answers, or agent outputs
- a judge prompt is becoming an approval gate rather than an internal review aid
- the team has examples of good and bad output but no written rubric
- the workflow needs proof that the judge uses evidence, not style, length, fluency, or hidden preferences
- reviewer disagreement, judge disagreement, or benchmark disagreement needs an escalation path
- the judge may see customer data, employee data, private traces, tool logs, source material, or prompt-injection text

### Inputs needed

- workflow name and output being judged
- task definition and intended decision
- judge model, prompt, tool, or reviewer agent
- allowed evidence sources and blocked evidence classes
- pass criteria and forced-reject criteria
- known-good examples and known-bad examples
- bias probes, calibration examples, and expected verdicts
- human reviewer, escalation owner, and authority limit
- sensitive data class, redaction status, and audit trail location

### Expected output

- judge review rubric
- evidence boundary map
- bias probe set
- disagreement routing rule
- judge authority gate
- CRM-safe or public-safe summary when relevant
- internal-only blocker and escalation notes

### What good looks like

- the judge task is narrow and written before production scoring begins
- allowed evidence and blocked evidence are separated before the judge sees the output
- pass criteria and forced-reject criteria are visible enough for a human to inspect
- known-bad examples test style bias, position bias, missing evidence, and wrong tool traces
- disagreement routes to a named human owner
- the judge authority level is explicit: assist only, triage, recommend, approve with human review, or blocked
- production approval is blocked when evidence, probes, owner, escalation, or data boundary is missing

### Operating steps

1. Define the judged workflow, output type, decision, and authority requested.
2. Write the rubric: task definition, pass criteria, forced-reject criteria, review scale, and minimum passing evidence.
3. Map evidence boundaries: approved sources, blocked sources, sensitive fields, redaction status, and source trust.
4. Build bias probes: order swap, longer-worse answer, polished missing-evidence answer, wrong-tool-argument trace, and prompt-injection source text.
5. Set disagreement handling: judge conflict, human conflict, known-label conflict, and escalation owner.
6. Gate authority: assist only, triage, recommend, approve with named review, or blocked.
7. Separate safe summaries from internal-only notes, sensitive examples, trace details, and judge prompt details.
8. Record the gate decision before any scored output reaches CRM, public content, customer communication, production release, or a system of record.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Workflow owner | Define judge task | output type, decision, authority level | internal | approved planning tool | self-check | review gate packet | task and judge authority are explicit |
| 2 | Quality reviewer | Write rubric and evidence boundary | pass criteria, forced rejects, allowed evidence | internal or confidential | approved review channel | required before scoring | rubric record | judge can be evaluated against visible criteria |
| 3 | Security or operations owner | Review probes and escalation | bias probes, sensitive data class, prompt-injection cases | internal or confidential | approved security review channel | required before approval authority | gate decision record | authority, escalation, and blocked states are recorded |

This run sheet is the minimum operational control. If the team cannot name the rubric, evidence boundary, probe set, disagreement route, authority level, and human escalation owner, the AI judge is not ready to approve workflow output.
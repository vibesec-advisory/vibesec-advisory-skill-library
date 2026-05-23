# Question Patterns

Use the smallest question set that changes the plan.

## Branch-changing questions

- Outcome: What has to be true for this to count as a win?
- Audience: Who will use, judge, buy, approve, or maintain the output?
- Constraint: What cannot change?
- Risk: What failure would make this embarrassing, unsafe, or useless?
- Evidence: What facts can we verify instead of assuming?
- Metric: What number, threshold, or observable behavior tells us progress happened?
- Non-goal: What tempting adjacent work should be excluded?
- Approval: What action requires human review before execution?

## Fast mode defaults

When the user is time constrained, ask only:

1. What is the concrete outcome?
2. What constraint or approval gate matters most?
3. What metric or evidence proves this worked?

Then write the meta prompt with labeled assumptions.

## Deep mode additions

Use deep mode when the work is strategic, public, expensive, security-sensitive, or likely to spawn multiple agents.

Add questions about:

- data sensitivity
- buyer or stakeholder decision criteria
- integration points
- irreversible choices
- maintenance burden
- failure modes
- how the work should be reviewed

## Bad questions

Avoid questions that:

- ask for information available in files or docs
- do not change the plan
- make the user choose between fake options
- optimize for completeness instead of momentum
- hide your recommended default

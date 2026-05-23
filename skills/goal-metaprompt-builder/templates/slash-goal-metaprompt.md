# Slash Goal Meta Prompt Template

Copy this into Slash Goal or another planning agent after completing the interrogation loop.

```text
You are helping me turn a clarified idea into an execution-ready goal.

Goal:
[plain-language goal]

Context:
[relevant background, source links, files, users, constraints, and business context]

What we already decided:
- [decision]
- [decision]

Assumptions:
- [assumption] Confidence: [high, medium, low]

Non-goals:
- [what not to do]

Constraints:
- [time, budget, data, scope, tooling, compliance, approval, or style constraint]

Success metrics:
- Primary metric: [metric, baseline if known, target if known, measurement window]
- Guardrail metric: [metric that prevents a bad local optimum]
- Review signal: [how we will know the output is usable]

Risks:
- [risk and why it matters]

Approval gates:
- Stop before [publishing, sending, spending, scanning, production changes, private data processing, or commitment]

Output I want from you:
1. Restate the goal and assumptions.
2. Challenge weak assumptions.
3. Produce an execution-ready plan with milestones.
4. Include tests, verification, or review steps.
5. List open questions only if they block the next useful move.

Tone and style:
[direct, concise, buyer-facing, technical, Ryan-style, etc.]
```

# Skill Context

### Job this is for

Review the authority an agent has before it receives tool access, browser access, repository access, service identity, retrieval context, or updated capabilities.

### When to use it

- an agent is about to receive a new tool, connector, browser profile, or repository permission
- a workflow mixes trusted instructions with untrusted webpages, documents, emails, issues, pull requests, or tool output
- an agent is acting through a human session, shared token, or broad credential
- an agent update changes what the workflow can read, write, retrieve, remember, call, or approve
- a tool result may steer planning, memory, tool selection, or external action

### Inputs needed

- agent name and owner
- tool or connector list
- read, write, send, delete, execute, memory, and retrieval permissions
- service identity or credential source
- context sources and trust labels
- browser or repository surface
- expected state changes
- logging and review owner

### Expected output

- context quarantine map
- permission card
- service identity packet
- capability diff
- tool result influence boundary
- browser profile isolation record
- GitHub agent input review
- approval and escalation path

### What good looks like

- untrusted content cannot modify privileged instructions
- permissions are scoped to the minimum workflow need
- agents do not borrow human sessions without a named exception
- capability changes are reviewed before production trust
- tool output is treated as evidence, not ground truth

### Operating steps

1. Inventory the agent, owner, tools, identity, and context sources.
2. Quarantine untrusted content from privileged instructions.
3. Write a permission card before enabling tool access.
4. Assign or request a scoped service identity.
5. Diff capability changes before updating the agent.
6. Bound what tool output can influence.
7. Isolate browser or GitHub inputs when those surfaces are in scope.
8. Route authority changes through the approval gate.

### Operator run sheet

| Step | Owner | Action | Required input | Data class | Approved tool path | Approval gate | System of record | Done when |
| ---- | ----- | ------ | -------------- | ---------- | ------------------ | ------------- | ---------------- | --------- |
| 1 | Platform owner | Inventory tools, identity, and context sources | agent profile | internal | approved inventory tool | self-check | agent authority record | all capabilities are listed |
| 2 | Security | Review permissions and service identity | permission card | internal or confidential | security review channel | required | access review log | least privilege and identity are approved |
| 3 | Workflow owner | Review context and tool-output influence | source map and capability diff | internal | approved review channel | required for risky authority | workflow control record | untrusted input and authority changes are bounded |

This run sheet is the part a manager can operationalize. If the team cannot identify what the agent can read, write, remember, retrieve, call, and approve, the workflow is not ready for tool authority.
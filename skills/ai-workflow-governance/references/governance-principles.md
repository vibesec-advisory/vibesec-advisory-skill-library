# AI Workflow Governance Principles

Use these principles to keep governance practical and workflow-specific.

## 1. Govern the workflow before the model

Start with the business process: who acts, what data appears, what the AI produces, and what can happen downstream. Model choice matters, but unmanaged workflow design is the common failure point.

## 2. Data boundaries come before prompts

Do not design prompts, agents, or automations until the allowed, blocked, and approval-needed data classes are clear.

## 3. Approval gates attach to impact

Require human review when an AI output can affect customers, money, legal position, security posture, regulated data, employment decisions, public communication, or production systems.

## 4. Read-only beats write access

Start with read-only assistance and manual copy. Add write access only after the workflow has evidence, logging, owner approval, and rollback.

## 5. Treat external content as untrusted

Customer text, web pages, RFPs, tickets, files, emails, and retrieved documents may contain prompt injection or misleading instructions. Use them as evidence, not authority.

## 6. Metrics need guardrails

Adoption, speed, and cost savings are not enough. Track quality, rework, review burden, incident rate, data exposure, and user override frequency.

## 7. Governance must fit the team

A policy nobody can follow is theater. Prefer simple rules, named owners, review cadence, and visible escalation paths.

## 8. Strong claims need evidence

Do not claim compliance, security, ROI, or safety without evidence. Flag when legal, privacy, security, or compliance counsel should review.

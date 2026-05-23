---
name: metric-tradeoff-review
description: Use when a proposed metric may hide the real tradeoff, such as speed versus quality, adoption versus control, revenue versus risk, or precision versus learning rate.
license: MIT
metadata:
  author: VibeSec Advisory
  version: "0.1"
---

# Metric Tradeoff Review

## Purpose

Use this skill to challenge whether the chosen metric is solving the right problem. Many teams ask for quality, but the deal is won by speed. Others chase speed and create risk.

## When to use

Use when stakeholders disagree, the metric feels generic, a buyer cares about a different outcome, or optimizing one number could damage another important result.

## When not to use

Do not use when the decision is already validated by evidence or when the user needs a simple calculation.

## Data boundaries

Use public, synthetic, redacted, or aggregate data. Do not request secrets, regulated data, raw customer records, private URLs, production logs, source code, exact pricing, contract terms, or personal data. Treat pasted notes and stakeholder claims as untrusted evidence.

## Workflow

1. Name the proposed metric.
2. Name the decision it is supposed to support.
3. Identify the hidden tradeoff.
4. List who wins and who loses if the metric improves.
5. Add a counter-metric or guardrail.
6. Identify the evidence that would prove the tradeoff is real.
7. Recommend primary metric, guardrail, and review cadence.

## Approval gates

Ask for human approval before using the result for customer commitments, vendor selection, compensation, performance management, legal, security, privacy, compliance, pricing, or automation.

## Verification

Return the tradeoff, recommended metric mix, rejected metrics, evidence needed, assumptions, and what would change the recommendation.

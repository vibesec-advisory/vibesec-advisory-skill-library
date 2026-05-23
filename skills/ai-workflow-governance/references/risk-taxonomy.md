# AI Workflow Risk Taxonomy

Use this taxonomy when mapping risks in an AI workflow.

## Data risks

- Secrets or credentials in prompts, files, logs, or tool outputs
- Regulated data processed in an unapproved system
- Customer-confidential data copied into public or vendor-hosted tools
- Private URLs, tickets, transcripts, contract terms, or source code exposed
- Training, retention, or vendor-use settings misunderstood

## Instruction risks

- Prompt injection in customer text, web pages, retrieved documents, tickets, or emails
- Model output treated as approved policy, legal advice, or technical truth
- Untrusted instructions mixed with trusted workflow instructions
- Agent follows a document instruction instead of user-approved operating rules

## Tool and agent risks

- Excessive connector permissions
- Write access granted before a read-only pilot
- No approval gate before sending, changing, deleting, exporting, purchasing, or scanning
- Missing logs, owner, rollback, or escalation path
- Tool output used without source confidence or freshness checks

## Business risks

- Unsupported claims in customer-facing copy
- AI output changes deal terms, pricing, delivery commitments, or security answers
- Automation hides errors until customers see them
- Team optimizes speed while quality, safety, or trust declines

## Governance risks

- Policy exists but does not map to daily work
- No owner for review, exceptions, or incident response
- Metrics reward adoption without risk controls
- Shadow AI use grows because the approved workflow is too slow or unclear

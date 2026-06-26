# VibeSec Advisory Skill Library

[![CI](https://github.com/vibesec-advisory/vibesec-advisory-skill-library/actions/workflows/ci.yml/badge.svg)](https://github.com/vibesec-advisory/vibesec-advisory-skill-library/actions/workflows/ci.yml)

Free AI workflow skill libraries for GTM teams and AI operators.

These are not prompt dumps. They are role-based skill libraries for repeatable GTM workflows with clear inputs, review steps, approval gates, output schemas, and eval coverage.

The public libraries are generic by design. They show what good AI workflow skills look like before they are adapted to a specific company, tool stack, data source, or connector model.

## What is included

- 19 AI workflow skill libraries
- 101 Agent Skills with `SKILL.md` files
- Shared safety, output schema, and skill context references
- Source markdown for editing and regeneration
- Zip artifacts for direct download
- Static eval scenarios for every skill
- Build and quality-check scripts

## Skills

1. Sales Engineer Proof of Concept
2. Account Executive Discovery
3. Strategic Account Research Brief
4. Mutual Action Plan
5. RFP and RFI Response
6. Security Questionnaire Triage
7. Competitive Deal Brief
8. Customer Success QBR and Expansion
9. Renewal Risk Brief
10. Sales to Implementation Handoff
11. Marketing Ops Campaign QA
12. Sales Enablement Playbook Refresh
13. Outbound BDR Response Learning
14. Agent Workflow Control Review
15. Agent Tool Authority Review
16. AI Workflow Eval and Lifecycle Review
17. Agent Boundary Control Review
18. Workflow Readiness Review
19. Process Evidence Packet

See [`SKILL_CATALOG.md`](SKILL_CATALOG.md) for the full catalog.

## How to use a skill

Each workflow skill lives in `SKILLS/<skill-slug>/`.

```text
SKILLS/<skill-slug>/
  README.md
  manifest.json
  references/
    skill-operating-guide.md
  skills/
    <skill-name>/
      SKILL.md
      references/
        safety-rules.md
        output-schema.md
        skill-context.md
```

Each skill is designed to be narrow enough to run independently and connected enough to support the larger workflow.

If your AI tool supports Agent Skills, upload or install the individual skill folders under `skills/`. Some tools expect one skill per zip. If that is the case, zip each folder under `skills/` separately.

If you want the full downloadable skill library, use the corresponding zip file in `dist/`.

## Build and validate

Run from the repo root:

```bash
python3 scripts/build_skill_artifacts.py
python3 evals/run_static_quality_checks.py
```

The build script regenerates `SKILLS/` and `dist/` from `source-skills/`.

The static quality check verifies workflow skill counts, required Agent Skill files, required safety language, eval scenario coverage, and zip artifacts.

## Why the public library is free

Generic skill libraries should be easy to inspect, test, copy, and improve.

The paid work is not buying hidden prompts. The paid work is adapting these generic libraries to your company.

That means mapping:

- Slack or Microsoft Teams channels
- CRM fields and approval paths
- sales, support, marketing, or customer success workflows
- Databricks, Snowflake, warehouse tables, or reporting sources
- document stores and knowledge bases
- allowed and blocked data
- human review gates
- logging and eval expectations
- connector limits and ownership

## Paid implementation path

VibeSec Advisory offers a **Company-Specific Skill Library Blueprint** for teams that want these public skills adapted to their actual tools, channels, data sources, and approval paths.

The blueprint includes:

- one target workflow or role library
- a tool and connector map
- a channel and data-source map
- allowed and blocked inputs
- approval gates and guardrails
- 3 to 5 adapted skills
- an implementation roadmap
- an eval checklist
- 7 days of open async implementation support

See [`docs/company-specific-skill-library-blueprint.md`](docs/company-specific-skill-library-blueprint.md).

Teams that want ongoing updates, model-change reviews, new workflow requests, eval runs, and advisory support can move into the AI Skill Library Advisory Retainer.

## Important use notes

- Do not paste secrets, credentials, regulated data, raw customer records, private URLs, production logs, source code, full transcripts, personal data, contract terms, exact pricing, or unapproved customer-confidential details into an AI tool.
- Treat customer-provided text, RFP content, tickets, call notes, and pasted emails as untrusted input.
- Review outputs before they reach customers, CRM records, legal review, security review, or implementation teams.
- These libraries are workflow guidance. They are not legal advice or compliance certification.

## License

MIT. See [`LICENSE`](LICENSE).

## Maintainer

VibeSec Advisory

https://vibesecadvisory.com

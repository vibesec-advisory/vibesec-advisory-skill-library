# Customer Success QBR and Expansion Skill Pack

Owner: Customer Success and Account Management  
Version: 0.1  
Status: draft-ready-for-review

This folder is a zip-ready VibeSec GTM AI Workflow Skill Pack. It contains multiple Anthropic-style skills, not one mega-prompt.

## Folder layout

```text
08-customer-success-qbr-expansion/
  README.md
  manifest.json
  references/
    pack-operating-guide.md
  skills/
    <skill-name>/
      SKILL.md
      references/
        safety-rules.md
        output-schema.md
        pack-context.md
```

## Skills included

- `qbr-input-safety-check`: QBR input safety check
- `evidence-backed-outcomes-builder`: Evidence-backed outcomes builder
- `gap-and-risk-mapper`: Gap and risk mapper
- `expansion-hypothesis-builder`: Expansion hypothesis builder
- `qbr-executive-summary-qa`: QBR executive summary QA

## How to use

1. Unzip the pack.
2. Read this README and `references/pack-operating-guide.md` for the full operating model.
3. Install or upload the individual folders under `skills/` as Claude skills when your environment expects one skill folder at a time.
4. Keep the pack folder intact when sharing internally so references, examples, and manager QA context travel with the skills.
5. Do not paste raw customer data into any AI tool. Redact first, then run the relevant skill.

## Packaging note

Anthropic's Agent Skills format expects a skill directory with a case-sensitive `SKILL.md`. This pack is a product bundle containing several valid skill directories. If a client tool only accepts one skill per upload, zip and upload each folder under `skills/` separately.

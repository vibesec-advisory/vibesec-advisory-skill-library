# Renewal Risk Brief Skill Pack

Owner: Account Management, Customer Success, and Revenue Leadership  
Version: 0.1  
Status: draft-ready-for-review

This folder is a zip-ready VibeSec GTM AI Workflow Skill Pack. It contains multiple Anthropic-style skills, not one mega-prompt.

## Folder layout

```text
09-renewal-risk-brief/
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

- `renewal-evidence-intake`: Renewal evidence intake
- `risk-level-classifier`: Risk level classifier
- `save-plan-options-builder`: Save plan options builder
- `customer-safe-talk-track`: Customer-safe talk track
- `escalation-brief`: Escalation brief

## How to use

1. Unzip the pack.
2. Read this README and `references/pack-operating-guide.md` for the full operating model.
3. Install or upload the individual folders under `skills/` as Claude skills when your environment expects one skill folder at a time.
4. Keep the pack folder intact when sharing internally so references, examples, and manager QA context travel with the skills.
5. Do not paste raw customer data into any AI tool. Redact first, then run the relevant skill.

## Packaging note

Anthropic's Agent Skills format expects a skill directory with a case-sensitive `SKILL.md`. This pack is a product bundle containing several valid skill directories. If a client tool only accepts one skill per upload, zip and upload each folder under `skills/` separately.

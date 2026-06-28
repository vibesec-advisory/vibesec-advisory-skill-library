# AI Judge Review Gates Skill

Owner: Workflow Owners, AI Operations, Security, Enablement, and Quality Review
Version: 0.1
Status: draft-ready-for-review

This folder is a zip-ready VibeSec GTM AI Workflow Skill. It contains multiple Anthropic-style Agent Skill directories, not one mega-prompt.

## Folder layout

```text
ai-judge-review-gates/
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

## Skills included

- `judge-rubric-writer`: Judge rubric writer
- `judge-evidence-boundary-mapper`: Judge evidence boundary mapper
- `bias-probe-set-builder`: Bias probe set builder
- `judge-disagreement-router`: Judge disagreement router
- `judge-authority-gatekeeper`: Judge authority gatekeeper

## How to use

1. Unzip the skill library.
2. Read this README and `references/skill-operating-guide.md` for the full operating model.
3. Install or upload the individual folders under `skills/` as Claude skills when your environment expects one skill folder at a time.
4. Keep the workflow skill folder intact when sharing internally so references, examples, and manager QA context travel with the skills.
5. Do not paste raw customer data into any AI tool. Redact first, then run the relevant skill.

## Compatibility note

Anthropic's Agent Skills format expects a skill directory with a case-sensitive `SKILL.md`. This workflow skill is a downloadable skill library containing several valid skill directories. If a client tool only accepts one skill per upload, zip and upload each folder under `skills/` separately.

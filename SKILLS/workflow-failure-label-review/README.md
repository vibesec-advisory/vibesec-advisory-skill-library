# Workflow Failure Label Review Skill

Owner: AI Operations, Security, Platform Engineering, Workflow Owners, and RevOps
Version: 0.1
Status: draft-ready-for-review

This folder is a zip-ready VibeSec GTM AI Workflow Skill. It contains multiple Anthropic-style Agent Skill directories, not one mega-prompt.

## Folder layout

```text
workflow-failure-label-review/
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

- `failure-label-intake-reviewer`: Failure label intake reviewer
- `symptom-and-root-cause-splitter`: Symptom and root-cause splitter
- `invisible-failure-finder`: Invisible failure finder
- `checkpoint-route-mapper`: Checkpoint route mapper
- `eval-case-converter`: Eval case converter

## How to use

1. Unzip the skill library.
2. Read this README and `references/skill-operating-guide.md` for the full operating model.
3. Install or upload the individual folders under `skills/` as Claude skills when your environment expects one skill folder at a time.
4. Keep the workflow skill folder intact when sharing internally so references, examples, and manager QA context travel with the skills.
5. Do not paste raw customer data into any AI tool. Redact first, then run the relevant skill.

## Compatibility note

Anthropic's Agent Skills format expects a skill directory with a case-sensitive `SKILL.md`. This workflow skill is a downloadable skill library containing several valid skill directories. If a client tool only accepts one skill per upload, zip and upload each folder under `skills/` separately.

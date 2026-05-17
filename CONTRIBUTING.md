# Contributing

Contributions are welcome when they improve clarity, workflow usefulness, safety boundaries, eval coverage, or installation instructions.

## Good contributions

- clearer skill trigger conditions
- better data-boundary language
- stronger approval gates
- better eval scenarios
- corrected installation notes
- role-specific workflow improvements
- examples that use redacted or synthetic data

## Avoid

- real customer data
- secrets or credentials
- claims that imply legal or compliance certification
- vendor-specific assumptions unless the skill is explicitly about that connector
- broad prompt dumps that do not create reviewable workflow steps

## Local validation

Run this before opening a pull request:

```bash
python3 scripts/build_skill_artifacts.py
python3 evals/run_static_quality_checks.py
```

CI runs the same build and static checks on every pull request and every push to `main`. It also blocks legacy naming regressions, including legacy directory names, numbered workflow skill names, and legacy workflow-bundle wording.

A professional pull request should include:

- source updates in `source-skills/` when workflow content changes
- regenerated output in `SKILLS/`
- regenerated zip artifacts in `dist/`
- eval updates in `evals/gtm_skill_evals.json` when behavior changes
- catalog or README updates when public-facing names change

Do not merge if CI is red. Fix the source files, regenerate artifacts, rerun local validation, then update the pull request.

If a change adds a new skill, update the catalog, eval scenarios, and zip artifacts in the same pull request.

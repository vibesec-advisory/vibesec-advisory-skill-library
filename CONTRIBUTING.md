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
- vendor-specific assumptions unless the pack is explicitly about that connector
- broad prompt dumps that do not create reviewable workflow steps

## Local validation

Run this before opening a pull request:

```bash
python3 scripts/build_skill_pack_artifacts.py
python3 evals/run_static_quality_checks.py
```

If a change adds a new pack, update the catalog, eval scenarios, and zip artifacts in the same pull request.

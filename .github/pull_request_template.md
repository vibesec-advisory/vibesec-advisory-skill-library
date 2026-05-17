## Summary

- Describe the change and why it is needed.

## Validation

- [ ] `python3 scripts/build_skill_artifacts.py`
- [ ] `python3 evals/run_static_quality_checks.py`
- [ ] Naming hygiene checked: no legacy directory names, no numbered workflow skill names, no legacy workflow-bundle wording

## Release impact

- [ ] Source workflow files changed under `source-skills/`
- [ ] Generated workflow skill folders updated under `SKILLS/`
- [ ] Zip artifacts updated under `dist/`
- [ ] Eval scenarios updated when skill behavior changed
- [ ] Catalog/docs updated when public-facing names changed

## Safety checklist

- [ ] No secrets, credentials, customer records, regulated data, or private URLs added
- [ ] No unsupported legal, compliance, security, roadmap, pricing, or ROI claims added
- [ ] Customer-facing language still routes approvals before use

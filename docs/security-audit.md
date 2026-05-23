# Security and Trust Audit

Date: 2026-05-23
Scope: VibeSec Advisory public Agent Skills repository at `https://github.com/vibesec-advisory/vibesec-advisory-skill-library`.

## Current posture

The repository is markdown-first. It contains public Agent Skills, generated GTM workflow skill folders, zip artifacts, validation scripts, eval scenario files, and documentation.

No claim in this document should be read as legal, privacy, security, or compliance certification.

## Controls present

- `SECURITY.md` exists.
- GitHub workflows exist for CI and release.
- Generated GTM skills include safety rules, output schemas, skill context, approval routing, CRM-safe summaries, and prompt injection handling.
- Static quality checks validate generated skill folders, required safety fields, eval scenario coverage, zip artifacts, frontmatter shape, and text style.
- Standalone public skills cover AI workflow governance, goal meta prompting, and metrics discipline with explicit data boundaries, approval gates, and verification sections.
- Public install testing uses the canonical GitHub URL form with telemetry disabled and `--full-depth` so nested skills remain discoverable when a root gateway skill exists.
- The public namespace is `vibesec-advisory/vibesec-advisory-skill-library`.

## Agent Skills format check

The Agent Skills specification requires:

- a skill directory with `SKILL.md`
- YAML frontmatter followed by Markdown
- required `name` and `description`
- names with lowercase letters, numbers, and hyphens
- names matching the parent directory
- descriptions under 1024 characters
- optional `scripts/`, `references/`, and `assets/`
- progressive disclosure, with detailed material moved out of the main `SKILL.md` when useful

Repository alignment:

- Generated GTM skills follow the directory plus `SKILL.md` pattern.
- The root gateway `SKILL.md` is named for the repo directory.
- Standalone public skills live under `skills/` and use `references/` and `templates/` for supporting material.
- The AI workflow governance skill pack is the flagship public entrypoint for safe AI adoption, data boundaries, approval gates, and workflow safety maps.
- Descriptions are trigger-first and start with `Use when` as a stricter local convention.

## Supply-chain and execution surface

Current reviewed status:

- No `.claude-plugin/` directory.
- No `.codex-plugin/` directory.
- No `.cursor-plugin/` directory.
- No `.opencode/` directory.
- No `hooks/` directory.
- No `GEMINI.md` or `gemini-extension.json`.
- No runtime package manifest is required for skill use.
- Repository scripts are local validation and artifact-build scripts, not skill runtime hooks.

Risk interpretation: this is intentionally lower risk than a plugin or hook-based system. Keep it markdown-first until activation evals and trust review justify more automation.

## Known gaps

- Live clean-session activation evals have not been completed in this audit.
- External trust scans such as Socket, Snyk, or Gen Agent Trust Hub are not recorded here yet.
- Release artifact checksums are not recorded here yet.
- The generated GTM skill set is broad, so public promotion should start with curated entrypoints instead of the entire catalog.

## Required pre-promotion checks

Before broader public promotion:

1. Run static checks.
2. Run telemetry-safe skills.sh list mode with `--full-depth`.
3. Confirm skill count and canonical repo URL from actual CLI output.
4. Run or attach clean-session activation evals for curated entrypoints.
5. Review all public examples for secrets, private URLs, real customer data, regulated data, source code, exact pricing, and contract terms.
6. Review for hidden instruction override language, auto-approval language, exfiltration wording, unsafe curl/bash install patterns, and certification claims.
7. Add external scanner results or state that they are not yet available.
8. Add release checksums before making stronger supply-chain claims.

## Safe public claim

Use:

> Installable, inspectable Agent Skills for governed AI workflows, with static quality checks, explicit safety boundaries, and activation eval scenarios.

Do not use yet:

- fully audited
- compliance-ready
- enterprise secure
- marketplace-trusted
- auto-trigger verified

## Audit update log

- 2026-05-23: Added first public audit document, Agent Skills format alignment notes, markdown-first risk posture, and pre-promotion gaps.
- 2026-05-23: Added AI workflow governance as the flagship public skill pack and updated curated entrypoints.
- 2026-05-23: Updated install guidance to use `--full-depth`, because root gateway discovery otherwise lists only the gateway skill.

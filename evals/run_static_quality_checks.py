#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "packs"
SOURCE = ROOT / "source-packs"
DIST = ROOT / "dist"
EVALS = ROOT / "evals" / "gtm_skill_pack_evals.json"

REQUIRED_SKILL_FILES = [
    "SKILL.md",
    "references/safety-rules.md",
    "references/output-schema.md",
    "references/pack-context.md",
]

REQUIRED_SKILL_TERMS = [
    "input_safety_status",
    "approval_status",
    "crm_safe_summary",
    "do_not_copy_to_crm",
    "prompt injection",
    "customer-provided text as untrusted input",
    "redaction request",
    "approval triggers",
]

REQUIRED_SOURCE_TERMS = [
    "Operator run sheet",
    "Pack skill library",
    "Input contract",
    "Skill-specific guardrails",
    "Failure reason:",
]

REQUIRED_SCENARIO_TYPES = {
    "normal_clean_input",
    "messy_safe_input",
    "sensitive_data_input",
    "unsupported_commitment_request",
    "prompt_injection_in_customer_text",
}

BAD_POSITIONING = [
    "50 prompts",
    "growth hack",
]


def fail_if(condition: bool, failures: list[str], message: str) -> None:
    if condition:
        failures.append(message)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    try:
        _, meta, _ = text.split("---\n", 2)
    except ValueError:
        return {}
    parsed: dict[str, str] = {}
    for line in meta.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip()] = value.strip().strip('"')
    return parsed


def validate_skill(skill_dir: Path, failures: list[str]) -> None:
    for rel in REQUIRED_SKILL_FILES:
        fail_if(not (skill_dir / rel).exists(), failures, f"{skill_dir}: missing {rel}")
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return
    text = skill_file.read_text(encoding="utf-8")
    meta = frontmatter(text)
    name = meta.get("name", "")
    description = meta.get("description", "")
    fail_if(name != skill_dir.name, failures, f"{skill_file}: name must match directory")
    fail_if(not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", name), failures, f"{skill_file}: invalid skill name {name}")
    fail_if(len(description) == 0 or len(description) > 1024, failures, f"{skill_file}: bad description length")
    fail_if("Use when" not in description, failures, f"{skill_file}: description missing trigger language")
    for term in REQUIRED_SKILL_TERMS:
        fail_if(term.lower() not in text.lower(), failures, f"{skill_file}: missing {term}")
    fail_if("Use when use when" in text, failures, f"{skill_file}: duplicated trigger phrase")


def validate_pack(pack_dir: Path, failures: list[str]) -> None:
    fail_if(not (pack_dir / "README.md").exists(), failures, f"{pack_dir.name}: missing README.md")
    manifest_path = pack_dir / "manifest.json"
    fail_if(not manifest_path.exists(), failures, f"{pack_dir.name}: missing manifest.json")
    fail_if(not (pack_dir / "references" / "pack-operating-guide.md").exists(), failures, f"{pack_dir.name}: missing pack operating guide")
    skills_dir = pack_dir / "skills"
    skill_dirs = sorted(path for path in skills_dir.glob("*") if path.is_dir()) if skills_dir.exists() else []
    fail_if(len(skill_dirs) < 5, failures, f"{pack_dir.name}: expected at least 5 skill folders, found {len(skill_dirs)}")
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"{pack_dir.name}: manifest JSON does not parse: {exc}")
            manifest = {}
        manifest_skills = manifest.get("skills", []) if isinstance(manifest, dict) else []
        fail_if(len(manifest_skills) != len(skill_dirs), failures, f"{pack_dir.name}: manifest skill count does not match folders")
    for skill_dir in skill_dirs:
        validate_skill(skill_dir, failures)


def validate_sources(failures: list[str]) -> None:
    source_files = sorted(SOURCE.glob("*.md"))
    fail_if(len(source_files) < 10, failures, f"expected at least 10 source markdown packs, found {len(source_files)}")
    for path in source_files:
        text = path.read_text(encoding="utf-8")
        fail_if(text.count("#### Skill:") < 5, failures, f"{path.name}: expected at least 5 source sub-skills")
        for term in REQUIRED_SOURCE_TERMS:
            fail_if(term.lower() not in text.lower(), failures, f"{path.name}: missing source term {term}")
        for bad in BAD_POSITIONING:
            fail_if(bad in text.lower(), failures, f"{path.name}: weak positioning contains {bad}")


def validate_zips(pack_dirs: list[Path], failures: list[str]) -> None:
    zip_files = sorted(DIST.glob("*.zip"))
    fail_if(len(zip_files) != len(pack_dirs), failures, f"expected {len(pack_dirs)} zip files, found {len(zip_files)}")
    for pack_dir in pack_dirs:
        zip_path = DIST / f"{pack_dir.name}.zip"
        fail_if(not zip_path.exists(), failures, f"{pack_dir.name}: missing zip artifact")
        if not zip_path.exists():
            continue
        with zipfile.ZipFile(zip_path) as zf:
            names = set(zf.namelist())
        fail_if(f"{pack_dir.name}/README.md" not in names, failures, f"{zip_path.name}: missing rooted README.md")
        fail_if(not any(name.startswith(f"{pack_dir.name}/skills/") and name.endswith("/SKILL.md") for name in names), failures, f"{zip_path.name}: missing skill SKILL.md files")


def validate_evals(failures: list[str]) -> None:
    fail_if(not EVALS.exists(), failures, "missing eval scenario JSON")
    if not EVALS.exists():
        return
    data = json.loads(EVALS.read_text(encoding="utf-8"))
    scenarios = data.get("scenarios", [])
    expected_scenarios = len(list(SOURCE.glob("*.md"))) * len(REQUIRED_SCENARIO_TYPES)
    fail_if(len(scenarios) != expected_scenarios, failures, f"expected {expected_scenarios} eval scenarios, found {len(scenarios)}")
    by_pack: dict[str, set[str]] = {}
    for scenario in scenarios:
        pack = scenario.get("pack")
        scenario_type = scenario.get("scenario_type")
        if pack and scenario_type:
            by_pack.setdefault(pack, set()).add(scenario_type)
        expected = json.dumps(scenario.get("expected_behavior", []))
        fail_if("active_skills" not in expected, failures, f"{scenario.get('id')}: expected behaviors missing active_skills")
    for pack, types in by_pack.items():
        missing = REQUIRED_SCENARIO_TYPES - types
        fail_if(bool(missing), failures, f"{pack}: missing scenario types {sorted(missing)}")


def validate_text_style(failures: list[str]) -> None:
    text_files = list(PACKS.rglob("*.md")) + list(SOURCE.rglob("*.md")) + [ROOT / "README.md", ROOT / "evals" / "EVAL_PLAN.md"]
    em_dash_hits: list[str] = []
    semicolon_hits: list[str] = []
    for path in text_files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "—" in text:
            em_dash_hits.append(str(path.relative_to(ROOT)))
        if ";" in text:
            semicolon_hits.append(str(path.relative_to(ROOT)))
    fail_if(bool(em_dash_hits), failures, f"em dash hits: {em_dash_hits[:10]}")
    fail_if(bool(semicolon_hits), failures, f"semicolon hits: {semicolon_hits[:10]}")


def main() -> int:
    failures: list[str] = []
    validate_sources(failures)
    pack_dirs = sorted(path for path in PACKS.iterdir() if path.is_dir()) if PACKS.exists() else []
    expected_packs = len(list(SOURCE.glob("*.md")))
    fail_if(len(pack_dirs) != expected_packs, failures, f"expected {expected_packs} pack folders, found {len(pack_dirs)}")
    fail_if(bool(list(PACKS.glob("*.md"))), failures, "packs/ must contain folders, not markdown pack files")
    for pack_dir in pack_dirs:
        validate_pack(pack_dir, failures)
    validate_zips(pack_dirs, failures)
    validate_evals(failures)
    validate_text_style(failures)

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PASS")
    print(f"pack_folders={len(pack_dirs)}")
    print(f"skill_folders={sum(1 for pack in pack_dirs for _ in (pack / 'skills').glob('*'))}")
    print(f"source_markdown_packs={len(list(SOURCE.glob('*.md')))}")
    print(f"zip_artifacts={len(list(DIST.glob('*.zip')))}")
    print("required_skill_files=SKILL.md,references/safety-rules.md,references/output-schema.md,references/pack-context.md")
    scenario_count = len(json.loads(EVALS.read_text(encoding="utf-8")).get("scenarios", []))
    print(f"eval_scenarios={scenario_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

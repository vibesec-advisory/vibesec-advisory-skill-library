# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["judge-rubric-writer"],
  "input_safety_status": "safe | needs redaction | blocked",
  "judge_review_rubric": {
    "workflow": "",
    "output_type": "",
    "decision_supported": "",
    "pass_criteria": [],
    "forced_reject_criteria": [],
    "review_scale": "",
    "minimum_evidence": []
  },
  "evidence_boundary_map": {
    "allowed_evidence": [],
    "blocked_evidence": [],
    "sensitive_data_classes": [],
    "redaction_required": [],
    "source_trust_notes": []
  },
  "bias_probe_set": {
    "known_good": "",
    "known_bad": "",
    "order_swap": "",
    "longer_worse": "",
    "missing_evidence": "",
    "wrong_tool_argument_trace": "",
    "prompt_injection_probe": "",
    "expected_verdicts": []
  },
  "disagreement_route": {
    "conflict_type": "",
    "human_owner": "",
    "escalation_rule": "",
    "reopen_condition": ""
  },
  "judge_authority_gate": {
    "authority_level": "blocked | assist only | triage only | recommend with human review | approve with named review",
    "blockers": [],
    "rollback_or_correction_path": "",
    "monitoring_cadence": ""
  },
  "approval_status": "needs workflow owner review | needs security review | needs legal/privacy review | blocked | ready for named approval",
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

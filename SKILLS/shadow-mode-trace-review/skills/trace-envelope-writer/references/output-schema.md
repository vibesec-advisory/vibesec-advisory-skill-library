# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs_redaction | blocked",
  "requested_decision": "",
  "write_surface": {
    "system": "",
    "action_class": "",
    "data_class": "",
    "side_effects": []
  },
  "trace_review": {
    "trace_completeness": "",
    "proposed_actions_reviewed": [],
    "missing_trace_fields": []
  },
  "policy_decisions": [],
  "human_corrections": [],
  "coverage_and_near_misses": {
    "covered_task_types": [],
    "uncovered_task_types": [],
    "severe_near_misses": [],
    "critical_policy_violations": []
  },
  "rollback_and_canary": {
    "rollback_status": "",
    "canary_boundary": "",
    "monitoring_owner": "",
    "decision": "blocked | more_shadow_data_needed | human_reviewed_dry_run | constrained_canary_candidate | rejected"
  },
  "approval_status": "",
  "crm_safe_summary": "",
  "public_safe_summary": "",
  "do_not_copy_to_crm": [],
  "security_note": "",
  "next_steps": []
}
```

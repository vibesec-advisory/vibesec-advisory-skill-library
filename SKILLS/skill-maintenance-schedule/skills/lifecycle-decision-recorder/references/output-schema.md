# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "maintenance_record": {
    "instruction_name": "",
    "owner_function": "",
    "backup_owner_function": "",
    "version": "",
    "intended_users": "",
    "workflow": "",
    "risk_tier": "low | medium | high | unknown",
    "last_reviewed": "",
    "next_review_due": "",
    "eval_or_smoke_test_path": "",
    "rollback_target": ""
  },
  "dependency_drift_map": [
    {
      "dependency": "",
      "current_assumption": "",
      "status": "current | stale | changed | unknown",
      "review_trigger": "",
      "risk_note": ""
    }
  ],
  "review_schedule": {
    "cadence": "",
    "event_triggers": [],
    "overdue_status": "current | overdue | unknown",
    "tracking_summary": ""
  },
  "lifecycle_decision": "keep | patch | rewrite | split | merge | retire | block | revalidate_before_reuse | needs review",
  "blockers": [],
  "approval_status": "approved draft | needs owner review | needs security review | blocked",
  "prompt_injection_detected": "yes | no",
  "ignored_instructions": "",
  "security_note": "",
  "source_trace": "",
  "crm_safe_summary": "",
  "public_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

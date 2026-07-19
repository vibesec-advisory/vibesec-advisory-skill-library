# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["permission-lease-record-writer"],
  "input_safety_status": "safe | needs_redaction | blocked",
  "permission_lease_record": {
    "workflow_or_agent": "",
    "task_or_subgoal": "",
    "tool_operation": "",
    "target_resource": "",
    "argument_constraints": [],
    "allowed_capabilities": [],
    "blocked_capabilities": [],
    "data_class": "",
    "owner": "",
    "tool_owner": "",
    "lease_start": "",
    "absolute_expiry": "",
    "system_of_record": ""
  },
  "expiry_and_closure_conditions": {
    "earliest_end_rule": "",
    "time_expiry": "",
    "work_closure_event": "",
    "stale_handle_removal_check": "",
    "non_effect_check": ""
  },
  "renewal_route": {
    "decision": "renew_same_scope | narrow | widen_needs_approval | deny | blocked",
    "owner": "",
    "reason": "",
    "next_expiry": "",
    "review_trigger": ""
  },
  "stale_replay_test": {
    "test_surface": "",
    "forbidden_replay_action": "",
    "expected_result": "",
    "pre_state_evidence": "",
    "post_state_check": "",
    "log_evidence": ""
  },
  "revocation_and_audit_gate": {
    "revocation_route": "",
    "emergency_disable_owner": "",
    "audit_log_source": "",
    "release_decision": "allow | shadow | revise | blocked",
    "next_review_date": ""
  },
  "approval_status": "owner_review_required",
  "lease_decision": "allow | renew | narrow | shadow | revise | blocked",
  "Failure reason": "",
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

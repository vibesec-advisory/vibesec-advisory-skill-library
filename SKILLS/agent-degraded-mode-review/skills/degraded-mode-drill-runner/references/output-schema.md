# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["<selected relevant skill slug>", "<other selected skill slug if needed>"],
  "input_safety_status": "safe | needs_redaction | blocked",
  "degraded_mode_state_record": {
    "workflow_or_agent": "",
    "current_mode": "",
    "degraded_mode": "assist_only | read_only | shadow | queue | stop",
    "entry_trigger": "",
    "observed_evidence": [],
    "allowed_capabilities": [],
    "blocked_capabilities": [],
    "data_class": "",
    "owner": "",
    "tool_owner": "",
    "system_of_record": ""
  },
  "authority_reduction_route": {
    "requested_action": "",
    "mode_route": "",
    "blocked_action_rationale": "",
    "safe_work_that_may_continue": [],
    "owner_route": ""
  },
  "queue_and_evidence_retention_plan": {
    "queue_limit": "",
    "deadline": "",
    "retry_rule": "",
    "evidence_retention_location": "",
    "stop_condition": "",
    "notification_owner": ""
  },
  "recovery_and_upgrade_gate": {
    "required_evidence": [],
    "upgrade_approver": "",
    "authorization_or_policy_test": "",
    "shadow_or_assist_window": "",
    "decision": "allow | shadow | revise | blocked",
    "residual_risk": ""
  },
  "enforcement_verification": {
    "enforcement_status": "verified | pending | failed | blocked",
    "control_point": "",
    "effective_time": "",
    "capability_diff": {
      "removed": [],
      "retained": [],
      "unchanged_or_unknown": []
    },
    "transition_acknowledgment": "",
    "non_effect_evidence": "",
    "in_flight_action_handling": ""
  },
  "degraded_mode_drill": {
    "normal_case": "",
    "known_bad_case": "",
    "expected_transition": "",
    "pre_state_evidence": "",
    "post_state_check": "",
    "log_evidence": ""
  },
  "approval_status": "owner_review_required",
  "mode_decision": "assist_only | read_only | shadow | queue | stop | blocked",
  "Failure reason": "",
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

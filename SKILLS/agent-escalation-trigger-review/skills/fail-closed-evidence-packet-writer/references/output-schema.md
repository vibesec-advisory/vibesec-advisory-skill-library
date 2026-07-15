# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "escalation_trigger_record": {
    "workflow_or_agent": "",
    "approved_scope": "",
    "observed_exception": "",
    "proposed_action": "",
    "tool_target_and_arguments": "",
    "data_class": "",
    "trust_boundary": "",
    "missing_evidence": []
  },
  "route_decision": {
    "route": "stop | ask | downgrade | escalate | fail_closed | resume_after_approval | blocked",
    "blocked_action": "",
    "safer_branch": "",
    "required_owner": "",
    "approval_required": "",
    "resume_rule": ""
  },
  "structured_clarification": {
    "question": "",
    "allowed_answer_shape": "",
    "decline_or_cancel_behavior": "",
    "blocked_sensitive_fields": []
  },
  "evidence_packet": {
    "required_items": [],
    "available_items": [],
    "missing_items": [],
    "evidence_destination": ""
  },
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

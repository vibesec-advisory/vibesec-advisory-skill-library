# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "memory_quarantine_packet": {
    "workflow_name": "",
    "agent_or_memory_store": "",
    "source_id": "",
    "source_type": "",
    "source_trust_level": "approved | mixed | untrusted | unknown",
    "capture_time": "",
    "memory_type": "user preference | workflow fact | source summary | task state | policy | permission claim | approval claim | unknown",
    "sensitivity_status": "safe | sensitive | blocked | unknown",
    "trust_score": "high | medium | low | blocked | unknown",
    "quarantine_decision": "approve durable write | hold pending review | reject | needs redaction",
    "expiry_or_review_date": "",
    "rollback_owner": ""
  },
  "allowed_influence": [],
  "forbidden_influence": [],
  "poisoning_test_plan": "",
  "approval_status": "",
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "action_authority": {
    "workflow": "",
    "requested_action": "",
    "side_effects": [],
    "failure_cost": "",
    "data_boundary": "",
    "authority_level": "draft-only | assist-only | reviewed action | blocked | ready for named approval"
  },
  "confidence_record": {
    "signal": "",
    "signal_type": "model_score | model_language | reviewer_confidence | outcome_metric | unknown",
    "evidence_required": [],
    "source_trace": "",
    "limitations": []
  },
  "baseline_comparison": {
    "human_alone": "available | missing | planned",
    "agent_alone": "available | missing | planned",
    "human_plus_agent": "available | missing | planned",
    "metric": "",
    "critical_failures": []
  },
  "abstention_route": {
    "answer": "",
    "retry": "",
    "clarify": "",
    "abstain": "",
    "escalate": "",
    "stop": ""
  },
  "override_log": {
    "required_fields": [],
    "recalibration_triggers": [],
    "next_review_date": ""
  },
  "promotion_decision": "draft-only | assist-only | revise | blocked | ready for named approval",
  "approval_status": "needs owner review | needs security review | blocked | ready for named approval",
  "crm_safe_summary": "",
  "public_safe_summary": "",
  "do_not_copy_to_crm": [],
  "security_note": "",
  "source_trace": ""
}
```

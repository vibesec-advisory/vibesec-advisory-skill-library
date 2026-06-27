# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["accountability-map-builder"],
  "input_safety_status": "safe | needs redaction | blocked",
  "accountability_map": {
    "workflow_outcome_owner": "",
    "human_reviewer": "",
    "reviewer_authority": "",
    "escalation_owner": "",
    "change_owner": "",
    "stop_conditions": [],
    "audit_trail": ""
  },
  "tool_permission_manifest": {
    "tool_name": "",
    "owner": "",
    "source_server_or_integration": "",
    "allowed_arguments": [],
    "blocked_arguments": [],
    "approval_triggers": [],
    "receipt_requirement": "",
    "revocation_owner": ""
  },
  "disagreement_log": [],
  "runnable_example_pack_status": "complete | incomplete | blocked",
  "launch_evidence_gate": {
    "decision": "blocked | draft only | shadow mode | supervised | limited launch | ready for named approval",
    "blockers": [],
    "eval_evidence": "",
    "rollback_path": "",
    "monitoring_cadence": ""
  },
  "approval_status": "needs workflow owner review | needs security review | needs legal/privacy review | blocked | ready for named approval",
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

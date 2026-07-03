# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "failure_label_record": {
    "workflow": "",
    "run_or_evidence_id": "",
    "owner": "",
    "final_outcome_status": "passed | failed | needs_review | unknown",
    "failure_mode": "intent_mismatch | wrong_fact | wrong_tool | wrong_argument | tool_result_misread | memory_state_error | output_contract_error | policy_security_error | recovery_failure | cost_latency_error | unknown",
    "trigger": "ambiguous_request | stale_context | missing_input | schema_drift | tool_error | prompt_injection | model_change | handoff_gap | approval_gap | unknown",
    "affected_surface": "prompt | skill | memory | tool | parser | external_data | workflow_state | customer_output | approval_step | unknown",
    "visibility": "visible | invisible | mixed | unknown",
    "severity": "nuisance | rework | wrong_decision | privacy_security | irreversible_action | customer_harm | unknown",
    "recoverability": "self_recovered | human_recoverable | rollback_required | unrecoverable | unknown",
    "evidence": [],
    "root_cause_note": "",
    "uncertainty": ""
  },
  "symptom_root_cause_split": {
    "visible_symptoms": [],
    "likely_root_causes": [],
    "not_proven": []
  },
  "next_checkpoint_route": {
    "checkpoint": "clarify | ask | confirm | stop | refuse | recover | human_review | skill_update | tool_contract_update | memory_review | parser_change | rollback | blocked",
    "owner": "",
    "approval_status": "approved | needs review | blocked | unknown",
    "reason": ""
  },
  "eval_case_candidate": {
    "recommended": false,
    "scenario_type": "",
    "expected_safe_behavior": [],
    "critical_failures": []
  },
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

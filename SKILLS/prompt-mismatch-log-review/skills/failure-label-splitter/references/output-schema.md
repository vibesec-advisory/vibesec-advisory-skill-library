# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "mismatch_record": {
    "human_intent": "",
    "original_request": "",
    "prompt_or_skill_version": "",
    "rendered_context_summary": "",
    "model_runtime_summary": "",
    "model_output_summary": "",
    "expected_behavior": "",
    "downstream_result": "",
    "missing_evidence": []
  },
  "failure_classification": {
    "primary_label": "intent_mismatch | missing_constraint | ambiguous_request | stale_context | output_schema_mismatch | unsafe_tool_action | hallucinated_source | evaluator_mismatch | downstream_integration_mismatch | unknown",
    "secondary_labels": [],
    "root_cause_hypothesis": "",
    "confidence": "low | medium | high",
    "uncertainty_note": ""
  },
  "route_decision": {
    "recommended_route": "clarify | rewrite_prompt | add_example | add_schema_validation | change_retrieval | change_tool_boundary | change_evaluator | add_approval_gate | promote_to_eval | leave_unchanged | blocked",
    "smallest_safe_next_step": "",
    "blocked_routes": [],
    "approval_required": ""
  },
  "regression_case": {
    "scenario_type": "",
    "safe_input_summary": "",
    "expected_behavior": [],
    "must_include": [],
    "must_not_include": [],
    "critical_failures": [],
    "failure_reason": ""
  },
  "prompt_change_decision": "recommend_change | recommend_no_change | needs_more_evidence | blocked",
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

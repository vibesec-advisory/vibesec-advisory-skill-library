# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "instruction_record": {
    "name": "",
    "owner": "",
    "version": "",
    "intended_task": "",
    "out_of_scope_boundary": "",
    "output_contract": "",
    "data_boundary": "",
    "approval_owner": ""
  },
  "smoke_scenarios": [
    {
      "scenario_type": "normal_clean_input | messy_safe_input | sensitive_data_input | unsupported_commitment_request | prompt_injection_input",
      "sanitized_input": "",
      "expected_safe_behavior": [],
      "blocked_behavior": [],
      "critical_failures": []
    }
  ],
  "rubric": {
    "must_include": [],
    "must_not_include": [],
    "scoring_notes": [],
    "critical_failure_policy": ""
  },
  "run_review": [
    {
      "scenario_type": "",
      "status": "pass | revise | blocked | escalate",
      "evidence": "",
      "failure_label": "",
      "notes": ""
    }
  ],
  "promotion_decision": "promote | revise | blocked | escalate",
  "approval_status": "approved draft | needs owner review | needs security review | blocked",
  "crm_safe_summary": "",
  "public_safe_summary": "",
  "do_not_copy_to_crm": [],
  "security_note": "",
  "source_trace": ""
}
```

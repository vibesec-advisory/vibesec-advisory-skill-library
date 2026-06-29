# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "blocked_input_reason": "",
  "source_summary": [],
  "adoption_plateau_diagnosis": {
    "usage_signals": [],
    "business_outcome_evidence": [],
    "process_friction": [],
    "unknowns": []
  },
  "workflow_selection_scorecard": [],
  "business_metric_baseline": {
    "metric": "",
    "baseline": "",
    "method": "",
    "owner": "",
    "target": "",
    "confidence": ""
  },
  "redesigned_workflow_map": [],
  "visible_speed_pilot_plan": {
    "cohort": "",
    "cadence": "",
    "measurement_checkpoints": [],
    "feedback_loop": "",
    "stop_conditions": [],
    "expansion_criteria": []
  },
  "approval_status": "needs workflow owner review | needs security review | needs HR/privacy review | blocked | ready for named pilot approval",
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

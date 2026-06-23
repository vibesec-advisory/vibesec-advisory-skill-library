# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["agent-boundary-control-review"],
  "input_safety_status": "safe | needs_redaction | blocked",
  "boundary_surfaces": {
    "multimodal_inputs": [],
    "outbound_destinations": [],
    "trace_reuse_paths": [],
    "assumptions": [],
    "changed_boundaries": []
  },
  "allowed_actions": [],
  "blocked_actions": [],
  "approval_status": {
    "required": true,
    "owner": "Security or workflow owner",
    "reason": ""
  },
  "eval_or_regression_needs": [],
  "crm_safe_summary": "",
  "do_not_copy_to_crm": [],
  "open_questions": [],
  "release_decision": "proceed | revise | blocked"
}
```

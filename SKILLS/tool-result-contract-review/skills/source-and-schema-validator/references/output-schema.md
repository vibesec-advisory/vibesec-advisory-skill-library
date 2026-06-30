# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": [],
  "input_safety_status": "safe | needs redaction | blocked",
  "tool_result_contract": {
    "tool_id": "",
    "server_id": "",
    "source_id": "",
    "call_id": "",
    "trace_id": "",
    "schema_id": "",
    "validation_status": "valid | invalid | partial | unknown",
    "freshness_status": "fresh | stale | expired | unknown",
    "evidence_class": "direct fact | inference | absence claim | external citation | unsupported claim",
    "confidence": "high | medium | low | unknown",
    "is_error": false,
    "retryable": false
  },
  "allowed_influence": [],
  "forbidden_influence": [],
  "blocked_result_reason": "",
  "review_gate_route": "",
  "approval_status": "",
  "crm_safe_summary": "",
  "do_not_copy_to_crm": []
}
```

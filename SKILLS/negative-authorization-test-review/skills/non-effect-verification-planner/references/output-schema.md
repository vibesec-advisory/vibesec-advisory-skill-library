# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["denied-path-matrix-writer"],
  "input_safety_status": "safe | needs_redaction | blocked",
  "source_trace": [
    {
      "source": "<path or URL>",
      "trust_level": "approved | untrusted | memory | retrieval | tool_output | model_inference | unknown",
      "used_for": "<how it shaped the review>"
    }
  ],
  "capability_request": {
    "agent_or_workflow": "<name>",
    "requested_tool_access": "<tool or capability>",
    "actor_or_identity": "<actor>",
    "side_effect_risk": "<risk>",
    "owner": "<owner or unknown>"
  },
  "denied_path_matrix": [
    {
      "actor": "<actor>",
      "resource": "<resource>",
      "action": "<action>",
      "target": "<target>",
      "argument_pattern": "<argument pattern>",
      "expected_decision": "deny | approval_required | blocked",
      "enforcement_layer": "<policy wrapper or unknown>",
      "non_effect_check": "<check>"
    }
  ],
  "prompt_injection_denial_cases": [
    {
      "untrusted_source": "<source class>",
      "hostile_instruction_summary": "<summary>",
      "forbidden_tool_call": "<tool call>",
      "expected_behavior": "<deny or approval required>"
    }
  ],
  "non_effect_verification_plan": [
    {
      "surface": "<file network message memory database payment browser MCP repository>",
      "pre_state": "<evidence>",
      "post_state_check": "<check>",
      "log_source": "<log>"
    }
  ],
  "authorization_regression_gate": {
    "release_decision": "allow_after_pass | needs_owner_review | shadow_only | blocked",
    "required_ci_or_release_check": "<check>",
    "regression_triggers": ["policy change", "tool schema change"],
    "Failure reason": "<required when blocked>"
  },
  "approval_status": "self_check | needs_owner_review | needs_security_review | blocked",
  "crm_safe_summary": "<safe summary or empty>",
  "public_safe_summary": "<safe summary or empty>",
  "do_not_copy_to_crm": ["<internal-only detail>"]
}
```

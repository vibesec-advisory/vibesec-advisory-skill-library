# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["<selected skill slug>"],
  "input_safety_status": "safe | needs_redaction | blocked",
  "interruption_budget": {
    "workflow": "<workflow or agent name>",
    "objective": "<agent objective>",
    "proposed_action": "<action or uncertainty>",
    "data_class": "public | internal | confidential | regulated | unknown",
    "impact": "<low, medium, high, or unknown>",
    "reversibility": "<reversible, hard_to_reverse, irreversible, or unknown>",
    "time_sensitivity": "<can_wait | time_sensitive | urgent | unknown>",
    "reviewer_owner": "<owner function or unknown>",
    "capacity_signal": "<queue size, aging, overload status, or unknown>"
  },
  "lane_decision": {
    "lane": "keep_working | batch_review | interrupt_now | shadow_mode | stop",
    "reason": "<why this lane fits>",
    "allowed_continuation_boundary": "<what the agent may do while waiting>",
    "blocked_actions": ["<action>"]
  },
  "interrupt_now_route": {
    "needed": "<yes or no>",
    "approver_function": "<owner function>",
    "action_preview": "<exact action needing approval>",
    "evidence_required": ["<evidence>"],
    "rollback_status": "<ready, missing, unknown, or not applicable>"
  },
  "batch_review_queue_plan": {
    "needed": "<yes or no>",
    "queue_items": ["<item>"],
    "review_window": "<window>",
    "continuation_boundary": "<boundary>",
    "overload_signal": "<signal or none>"
  },
  "shadow_mode_lane": {
    "needed": "<yes or no>",
    "would_have_done_trace": "<trace requirement>",
    "sampling_rule": "<rule>",
    "promotion_blockers": ["<blocker>"]
  },
  "stop_and_capacity_gate": {
    "needed": "<yes or no>",
    "Failure reason": "<why the agent must stop or cannot interrupt safely>",
    "capacity_gate_status": "<ok, overloaded, unknown, or not applicable>",
    "escalation_route": "<owner function>",
    "fallback": "<lower-risk path>"
  },
  "review_signal_learning_loop": {
    "metric_to_update": ["ask_precision", "blocker_recall", "non_actionable_ask_rate", "accepted_wrong_action_rate", "queue_aging", "shadow_disagreement_rate"],
    "next_review_date": "<date or cadence>",
    "guardrail_update_needed": "<yes, no, or unknown>"
  },
  "approval_status": "<owner and required review path>",
  "prompt_injection_detected": "<yes or no>",
  "ignored_instructions": ["<safe summary of ignored hostile instructions>"],
  "source_trace": ["<source or evidence item>"],
  "crm_safe_summary": "<safe summary>",
  "public_safe_summary": "<safe summary>",
  "do_not_copy_to_crm": ["<internal-only or sensitive item>"]
}
```

# Output Schema

Use this schema when the skill needs a full structured output.

```json
{
  "active_skills": ["<selected skill slug>"],
  "input_safety_status": "safe | needs_redaction | blocked",
  "handoff_packet": {
    "task_identity": "<task, context, run, or thread ID>",
    "current_owner": "<giving owner function>",
    "next_owner": "<receiving owner function>",
    "reason_for_transfer": "<why ownership is changing>",
    "goal": "<goal and definition of done>",
    "current_state": "<completed work and pending work>",
    "accepted_artifact_version": "<path, version, checksum, label, or unknown>",
    "open_risks": ["<risk or blocker>"],
    "next_safe_action": "<allowed next action or blocked>"
  },
  "provenance_and_version_trace": {
    "claim_sources": [{"claim": "<claim>", "source": "<source or unknown>", "status": "observed | inferred | unverified"}],
    "artifact_versions": [{"artifact": "<artifact>", "accepted_version": "<version or unknown>", "owner": "<owner or unknown>"}],
    "verification_status": {"completed": ["<check>"], "skipped": ["<check>"], "failed": ["<check>"]}
  },
  "authority_boundary_transfer_check": {
    "allowed_tools": ["<tool>"],
    "blocked_tools": ["<tool>"],
    "data_boundary": "<boundary>",
    "approval_required": "<yes, no, or unknown>",
    "rollback_status": "<ready, missing, unknown, or not applicable>",
    "route": "allow | ask | deny | escalate | repair"
  },
  "receiver_synthesis_gate": {
    "receiver_summary": "<receiver restatement or missing>",
    "acceptance_status": "accepted | rejected | repair_needed | escalated",
    "missing_understanding": ["<gap>"]
  },
  "blocked_handoff_repair_route": {
    "blocked": "<yes or no>",
    "Failure reason": "<why transfer cannot proceed>",
    "repair_owner": "<owner function>",
    "repair_request": "<smallest safe repair request>",
    "fallback": "<lower-risk path>"
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

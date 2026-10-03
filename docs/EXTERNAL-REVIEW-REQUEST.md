# External review request draft

This is a draft for a public issue, discussion, or direct review handoff. It is not an outbound
message and does not claim that a reviewer has been contacted. Use the current
[review lock](AGENT-SYSTEMS-LAB-REVIEW-LOCK.json) and [external packet](EXTERNAL-REVIEW-PACKET.md)
when preparing a concrete request.

## What to review

Please review the public Agent Systems Lab as a collection of independently installable tools. Focus
on source ownership, receipt boundaries, privacy/redaction behavior, release identity, refusal paths,
and whether the clean-machine route makes claims that the evidence does not support.

Start here:

1. [Architecture](AGENT-SYSTEMS-LAB-ARCHITECTURE.md)
2. [Threat model](AGENT-SYSTEMS-LAB-THREAT-MODEL.md)
3. [External review packet](EXTERNAL-REVIEW-PACKET.md)
4. [Review lock](AGENT-SYSTEMS-LAB-REVIEW-LOCK.json)
5. [Audit matrix](AGENT-SYSTEMS-LAB-AUDIT-MATRIX.md)

## Reviewer prompts

- Can you reproduce the source head and audit receipt from a fresh clone?
- Does a refusal remain a refusal when you mutate a source byte, digest, edge, artifact checksum,
  policy decision, or sandbox boundary field?
- Do any examples or reports expose private paths, credentials, transcript text, customer data, or
  proprietary operating rules?
- Are `unknown`, `blocked`, `partial`, `unavailable`, and `unenforced` states preserved through the
  cross-repository projections?
- Which claims should be narrowed, split, or moved to a different owner?
- What is the smallest test or documentation change that would make a concern reproducible?

## Feedback format

```text
Owner/repository:
Source head:
Command or fixture:
Observed result:
Expected result:
Evidence link or digest:
Severity: observation | documentation gap | reproducible defect | security concern
Suggested next step:
```

Please use synthetic fixtures and do not include secrets, private paths, transcripts, customer data,
or employer-specific policy. Security concerns belong in the repository's private reporting channel.

## Evidence boundary

No reviewer response, independent adoption, provider-side control, deployment state, or production
outcome is established by this draft. Those fields remain unknown until directly observed and recorded
with the exact source, command, and result.

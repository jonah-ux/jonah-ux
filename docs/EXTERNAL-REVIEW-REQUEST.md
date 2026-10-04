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

## Current release targets

Start with these two current boundaries, then follow the owner map for the wider thirteen-tool
review. Keep the historical review lock as its original snapshot; it is not a claim that every
locked package already contains these later changes.

- [Agent Proof 0.5.0](https://github.com/jonah-ux/agent-proof/releases/tag/v0.5.0), source
  `681b34f1ac7189dcd4da26ad8b5c5ef0b3a07880`: the
  [offline compatibility contract](https://github.com/jonah-ux/agent-proof/blob/681b34f1ac7189dcd4da26ad8b5c5ef0b3a07880/docs/contracts/agent-systems-lab-compatibility-v2.md)
  checks pinned declarations, source/repository bindings, native versions and registry constraints.
  Use the packet's [installed reproduction](EXTERNAL-REVIEW-PACKET.md#agent-proof-050-offline-compatibility-foundation),
  including its Python 3.11+ prerequisite. Agreement between declarations does not establish
  sibling runtime execution or authentication.
- [Forgeyard 0.5.1](https://github.com/jonah-ux/forgeyard/releases/tag/v0.5.1), source
  `d8d225f961e550e9065f9f0cd6e446d7939e5ef9`: `forgeyard evaluate-refusals` executes nineteen
  synthetic native contract cases and controls. The Workbench's fifteen stored refusal labels
  are a separate catalogue; they are not fifteen executed specialist enforcement paths.

For either release, compare downloaded bytes with its published checksums before installation.
Use its native audit and provenance instructions. Record the exact source/tag and the command
output rather than treating a successful installation or a CI badge as the whole review.

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
- For the compatibility kernel, can a missing source field, omitted or substituted owner,
  disabled repository binding, unversioned capability, or exhausted aggregate read budget
  incorrectly produce complete validation? The published regressions give concrete starting inputs.
- For Forgeyard, do changed source bytes, resealed invalid graph edges, missing required inputs
  and wrong refusal reasons stay distinguishable from a valid synthetic packet? Keep fixture-label
  checks separate from executed native cases.

## Feedback format

```text
Owner/repository:
Source head:
Package version / release tag:
Environment / interpreter:
Command or fixture:
Observed result:
Expected result:
Evidence link or digest:
Severity: observation | documentation gap | reproducible defect | security concern
Suggested next step:
```

Please use synthetic fixtures and do not include secrets, private paths, transcripts, customer data,
or employer-specific policy. Security concerns belong in the repository's private reporting channel.
Before sharing output, replace local paths with neutral placeholders while retaining public source
identities, input digests, refusal codes and the reproduction needed to assess the concern.

## Evidence boundary

No reviewer response, independent adoption, provider-side control, deployment state, or production
outcome is established by this draft. Those fields remain unknown until directly observed and recorded
with the exact source, command, and result.

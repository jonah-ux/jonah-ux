# Portfolio Suite v2

This is the shortest path through three independently installable public tools that share one
evidence lifecycle:

```text
ChatLens  ->  redacted conversation evidence
Atlas     ->  durable, approval-gated task receipts
Forgeyard ->  reviewable delivery records
```

The shared handoff is `ai-work-evidence/v1`. It carries a stable evidence ID, source/version,
bounded subject and summary, artifact names/sizes/hashes, scalar provenance, and one honest status:
`observed`, `verified`, `failed`, or `unknown`. The contract never carries raw transcript text,
prompts, credentials, private paths, customer data, or provider metadata.

## Start with released artifacts

| Project | Release | Public proof surface |
| --- | --- | --- |
| [ChatLens](https://github.com/jonah-ux/chatlens) | [`v0.4.0`](https://github.com/jonah-ux/chatlens/releases/tag/v0.4.0) | `evidence-export` projects a validated redacted trace into the shared contract |
| [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) | [`v0.2.0`](https://github.com/jonah-ux/atlas-agent-runtime/releases/tag/v0.2.0) | `evidence` validates lifecycle replay and projects a durable receipt |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | [`v0.4.0`](https://github.com/jonah-ux/forgeyard/releases/tag/v0.4.0) | `compose` consumes both projections without copying raw payloads |

Each release includes a wheel, source distribution, and checksum file. The release workflows run
their test matrices and the install evidence is recorded in the portfolio project log.

## The offline chain

1. Create a synthetic redacted trace and export it with ChatLens.
2. Run Atlas's approval/recovery demo and export its durable receipt.
3. Give both JSON files to Forgeyard's `compose` command.
4. Inspect the resulting `ready_for_review` record and the original evidence files separately.

The complete command sequence is maintained in Forgeyard's
[`portfolio-suite-v2` walkthrough](https://github.com/jonah-ux/forgeyard/blob/main/docs/examples/portfolio-suite-v2.md).
The individual contract documents live in each repository under `docs/contracts/`.

## What the chain proves

- ChatLens proves bounded redaction and trace-envelope integrity before projection.
- Atlas proves a local lifecycle can survive approval and restart, then be replayed and fingerprinted.
- Forgeyard proves status-aware composition: observed evidence can be reviewed, while unknown or
  failed evidence cannot silently become a completed record.

The chain does not claim deployment, provider delivery, ownership, liveness, or a user-visible
outcome. Those boundaries are deliberate and documented in each repository's security and
limitations files.

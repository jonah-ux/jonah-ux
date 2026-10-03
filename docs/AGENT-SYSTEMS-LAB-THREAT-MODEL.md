# Agent Systems Lab threat model

This document describes the public, local-first review surface for the Agent Systems Lab. It is
an engineering threat model for the checked-in protocols and fixtures; it is not a certification of
the repositories, their dependencies, or any provider runtime.

## Scope and assets

The system under review is a set of independently installable repositories. Each owner emits its
native receipt. Optional adapters project a bounded, redacted view into `agent-proof/interop/v1`;
Forgeyard can bind admitted evidence into a review packet. The public profile and hosted pages are
documentation and synthetic fixture surfaces.

The assets that need protection are:

| Asset | Failure that matters | Review evidence |
| --- | --- | --- |
| Source identity | A report is attributed to the wrong checkout or release. | Source-bound digests, immutable commit pins, and the compatibility checker. |
| Payload privacy | Transcripts, credentials, customer records, or private paths cross the public boundary. | Allowlisted projections, redaction tests, synthetic fixtures, and public-surface audits. |
| Status truth | `unknown`, `blocked`, `partial`, or `unenforced` is silently upgraded to success. | Owner schemas, Forgeyard refusal matrix, and explicit status mapping. |
| Evidence integrity | A byte, edge, manifest, or artifact changes after it was admitted. | Agent Proof chain/graph verification and Forgeyard packet verification. |
| Owner boundaries | An umbrella layer reinterprets or replaces native semantics. | `agent-systems-lab/compatibility/v1` ownership map and additive adapter contracts. |
| Release provenance | A package is built from an unexpected tag or its published bytes drift. | Annotated-tag gates, wheel/source consumers, `SHA256SUMS`, and owner audit receipts. |

## Trust boundaries

```text
owner input -> owner CLI/receipt -> bounded adapter -> Agent Proof graph/ledger
                                                    -> Forgeyard review packet
source tree -> release workflow -> wheel/sdist/checksum manifest -> fresh consumer
public fixture -> hosted static page -> reviewer observation
```

The owner is authoritative for its native schema. Agent Proof is authoritative for the semantic
proof and graph contracts. Forgeyard owns review composition and its additive sidecar. The profile
is a discovery and review surface; it does not become a runtime registry. A hosted page can show a
synthetic fixture, but it cannot prove that a private or production system ran.

## Adversaries and controls

| Threat | Example | Control and residual limit |
| --- | --- | --- |
| Malicious input | A crafted envelope uses an unsupported version, malformed digest, traversal path, or symlink. | Owners and Agent Proof fail closed; the public Forgeyard matrix includes traversal, symlink, malformed, and schema-drift cases. This does not prove every future parser is safe. |
| Tampered evidence | A record, graph edge, packet, or artifact is changed and its visible summary is left intact. | Source/digest binding and graph/packet verification refuse the mutation. The check covers the named inputs, not arbitrary external storage. |
| Confused deputy | A connector or adapter treats a bounded receipt as permission to execute or as proof of an outcome. | Adapters carry status and unknowns only; policy, sandbox, and lifecycle owners retain execution authority. The contracts do not grant permissions. |
| Stale source | A consumer reads an old checkout while a newer owner revision is described as current. | Evidence rows name reviewed head SHAs and freshness observations. A source readback still requires the reviewer to run the current command. |
| False completion | A valid hash or exit code is presented as a user-visible result. | `observed`, `partial`, `unknowns`, and blocked states remain explicit; docs separate integrity, outcome, deployment, and adoption. |
| Fixture leakage | A sample, log, or generated report contains a token, private path, transcript, or customer value. | Synthetic fixtures, tracked-text high-signal scans, and privacy tests. The scanner is not a complete semantic DLP system. |
| Supply-chain drift | A release tag, dependency declaration, or checksum does not match the inspected source. | Tag gates, dependency/license inventories, artifact checksum checks, and isolated wheel/sdist consumers. Provider-side and cross-machine build controls may remain unavailable. |
| Reviewer overclaim | A benchmark, hosted page, star count, or local run is described as adoption, security, or production proof. | The review packet records exactly what each command proves and keeps unavailable/unknown states visible. |

## Deliberate limits

- The public lab does not include Auto Shop Media source, customer data, credentials, transcripts,
  production logs, private paths, or proprietary operating policy.
- A passing audit is not a security certification, a complete secret scan, or proof of sandbox
  isolation. Sandbox enforcement remains the native owner's declared boundary.
- Artifact checks are `unavailable` when a caller does not provide a distribution directory and
  checksum manifest. Local timings are machine-local observations.
- No public receipt proves deployment, outside adoption, provider-side controls, or a user-visible
  outcome unless the named evidence explicitly contains that observation.

## Review route

Start with the [cold-review checklist](COLD-REVIEW-CHECKLIST.md), then use the
[external review packet](EXTERNAL-REVIEW-PACKET.md) to inspect the exact source heads, contracts,
tests, release evidence, and known gaps. When a claim fails, preserve the native owner boundary and
record the smallest reproducer with the command, input digest, exit state, and source revision.

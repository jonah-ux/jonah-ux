# External review packet

This packet is for a reviewer or review agent who wants to critique the public Agent Systems Lab
from a clean machine. It is intentionally source-first: every claim points to a repository, a
contract, a command, and a known limitation. The packet does not ask a reviewer to trust this
profile or to infer adoption from activity.

## Review target

The review snapshot was generated from profile base head `695fd4de6777f25e82e5912726ee98570c33c86f` on
2026-10-03. The owner heads below are source-identity observations from `refs/heads/main` made
while preparing this packet; they are freshness anchors, not release claims:

| Owner | Main head | Native responsibility |
| --- | --- | --- |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | `9d772f72e7af11e47e3762c3c97bbdebda595f72` | review composition, packets, evaluation, public audit |
| [Agent Proof](https://github.com/jonah-ux/agent-proof) | `abb3631fea816a0832001acf75a32fd5d2e61ec0` | tamper-evident ledger, graph, interop, public audit |
| [ChatLens](https://github.com/jonah-ux/chatlens) | `850cddffbb8b6b931c3a8a1c42d714c0afa68cb1` | local trace discovery and redacted handoff |
| [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) | `f956f89b889aedebf44b7d7e660fa94bf4903633` | durable lifecycle and approval state |
| [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) | `536a200f2397851e4d5d75e0801896886c236ea2` | scope, freshness, citations, admission/refusal |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | `604694258453ad58590aba9101e833cc9d262bf7` | capability decisions and policy receipts |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | `04eed9c288734ab42e9161d2bc2216ccd5a7bf20` | bounded execution receipt |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | `2ccac304ef8845846181db233d718f79f3e18e3a` | continuation and handoff state |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | `c610364486410a5a5141f0837361d7f5e7f94494` | bounded trace representation |
| [Sourcemark](https://github.com/jonah-ux/sourcemark) | `59b79c8368862635d76aa099eb085920fdb02b70` | citation checks and source-bound export |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | `6f893998213e1cf3e38a43540d5f11445e471db4` | tool-contract diagnostics |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | `419f40f393e443673b998c8fa61b5eba9ef37556` | preservation and recovery planning |
| [Slipstream](https://github.com/jonah-ux/slipstream) | `27bb2f6d51909e9752c087792a8e02af0e2c2998` | local retrieval indexes |

The current clean-machine Forgeyard route was rerun at `4daf0ff01ebe8da99cc92867e9035ec2d93bd222`:
`passing` reached `reviewable`, `blocked` preserved `reviewable=false`, `tampered` refused with exit 2,
the public audit returned `pass`, and the evaluation receipt returned `pass`; artifact state remained
`unavailable` without a supplied distribution directory.

The heads above are source-identity observations only; they do not assert deployment, adoption, or
that every owner has published a downloadable artifact. The Forgeyard installed reference-flow
observation below was run at its separately recorded `4daf0ff01ebe8da99cc92867e9035ec2d93bd222`
boundary; the current matrix head is newer and its static audit was rerun independently. The [owner-native audit matrix](AGENT-SYSTEMS-LAB-AUDIT-MATRIX.md) records
which repositories expose `*-public-audit/v1`, which checks are rerunnable, and where artifact state
remains `unavailable` without an explicit distribution directory.

## Fifteen-minute review

1. Read the [architecture](AGENT-SYSTEMS-LAB-ARCHITECTURE.md) and
   [threat model](AGENT-SYSTEMS-LAB-THREAT-MODEL.md). Confirm that native ownership is explicit.
2. Clone [Forgeyard](https://github.com/jonah-ux/forgeyard), install its local package, and run
   `forgeyard demo`.
3. Run its checked-in `scripts/run_reference_flow.py` for `passing`, `blocked`, and `tampered`.
4. Run `scripts/evaluate_lab.py --iterations 2 --warmup 0 --json` and inspect dataset hashes,
   refusal states, machine-local timings, and `unavailable` artifact/install fields.
5. Clone [Agent Proof](https://github.com/jonah-ux/agent-proof) and run
   `python3 scripts/audit_public_surface.py --json` plus
   `PYTHONPATH=src python3 -m unittest discover -s tests -v`.
6. Clone [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) and run
   `python3 scripts/audit_public_surface.py --json` plus `python3 -m atlas.cli --version`.
7. Clone [ChatLens](https://github.com/jonah-ux/chatlens) and run
   `python3 scripts/audit_public_surface.py --json` plus
   `python3 -m unittest discover -s tests -v`.
8. Clone [Agent Policy](https://github.com/jonah-ux/agent-policy) and run
   `python3 scripts/audit_public_surface.py --json` plus `python3 -m agent_policy.cli --help`.
9. Run the owner-native audit matrix for Agent Policy, Agent Sandbox Run, Sourcemark, Agent Resume,
   Agent Trace Lite, MCP Doctor, Worktree Conservator, and Context Integrity Lab. Keep each JSON receipt
   with the corresponding source head; `artifact_audit=unavailable` is expected when no `dist/` was
   supplied.
10. Change one graph edge or source byte, keep the old digest, and confirm the relevant verifier
   refuses the mutation.

The [cold-review checklist](COLD-REVIEW-CHECKLIST.md) contains the full commands and expected
states. Use a disposable checkout and synthetic fixtures only.

## Evidence ledger

| Evidence | Public source | What it proves | What it does not prove |
| --- | --- | --- | --- |
| Compatibility charter | [Agent Proof compatibility manifest](https://github.com/jonah-ux/agent-proof/blob/main/conformance/compatibility-v1.json) | The reviewed adapter registry, refusal vocabulary, and immutable pins are structurally inspectable. | That every owner is currently deployed or mutually compatible outside the named pins. |
| Installed reference flow | [Forgeyard contract](https://github.com/jonah-ux/forgeyard/blob/main/docs/contracts/forgeyard-reference-flow-v1.md) | A fresh local consumer can call the named installed CLIs and preserve passing, blocked, tampered, and unavailable states. | A hosted service, production workflow, or outside adoption. |
| Semantic graph | [Agent Proof graph implementation](https://github.com/jonah-ux/agent-proof/blob/main/src/agent_proof/graph.py) | Bound graph and packet inputs can be verified and tampering/orphan edges can be refused. | Trust in an input before the verifier sees it. |
| Evaluation lab | [Forgeyard evaluation script](https://github.com/jonah-ux/forgeyard/blob/main/scripts/evaluate_lab.py) | Fixed correctness/refusal fixtures, hashes, and local performance observations are rerunnable. | A universal performance ranking or model-quality claim. |
| Public audits | Owner-native `*-public-audit/v1` receipts across Forgeyard, Agent Proof, Atlas, ChatLens, Agent Policy, Agent Sandbox Run, Sourcemark, Slipstream, Worktree Conservator, Agent Resume, Agent Trace Lite, MCP Doctor, and Context Integrity Lab | Dependency/license declarations, release markers, high-signal privacy scans, checksum refusal behavior, and explicit artifact availability are inspectable from clean public clones. | Complete DLP, security certification, reproducible builds across machines, provider controls, or adoption. |

## Reviewer questions

- Can the claimed source head be reproduced from the public URL and the command output?
- Does a normalized projection preserve unknowns and refuse unsupported versions without importing
  private payloads?
- Can a stale source, changed edge, orphan edge, duplicate, traversal path, symlink, or malformed
  receipt be turned into a small refusal fixture?
- Which evidence is local-only, which is artifact-level, and which is genuinely observed outside the
  author’s machine?
- Does any document accidentally imply adoption, production use, security certification, or a user
  result that its receipt does not contain?

Record review feedback with the exact commit, command, fixture digest, and outcome. A critique that
finds a gap is useful evidence; it should become a bounded issue or follow-up change rather than a
silent rewrite of the claim.

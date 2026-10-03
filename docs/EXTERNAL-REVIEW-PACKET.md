# External review packet

This packet is for a reviewer or review agent who wants to critique the public Agent Systems Lab
from a clean machine. It is intentionally source-first: every claim points to a repository, a
contract, a command, and a known limitation. The packet does not ask a reviewer to trust this
profile or to infer adoption from activity.

## Review target

The public profile main was read back at `ce3fd144e3809fbcbafbef4a9e15803504ad236b` on
2026-10-03. The owner heads below are source-identity observations from `refs/heads/main` made
while preparing this packet; they are freshness anchors, not release claims:

| Owner | Main head | Native responsibility |
| --- | --- | --- |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | `bc2eb6996e64b71399f5ba0e1f406783762a910f` | review composition, packets, evaluation, public audit |
| [Agent Proof](https://github.com/jonah-ux/agent-proof) | `2c8767257d4da2e78da73e93a82f7d066f3f1b8e` | tamper-evident ledger, graph, interop, public audit |
| [ChatLens](https://github.com/jonah-ux/chatlens) | `e53c0f38806bb77624998755bd68dac8176205dd` | local trace discovery and redacted handoff |
| [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) | `14fd14dd88c4bae979fef5d3a9c3448b0a15a456` | durable lifecycle and approval state |
| [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) | `78744b2e01ec5ce72bdde9ff85e9b83a9c88dc66` | scope, freshness, citations, admission/refusal |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | `b8b29029c9f89196c250ba413e499091848f2e26` | capability decisions and policy receipts |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | `0014550f43149b3186303a73706a92d8bf26c4c9` | bounded execution receipt |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | `ba1372955c063aa6c8d02b5324946cc4809aa407` | continuation and handoff state |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | `ad7065a61a42a9dfc12a7027047688f5bc660312` | bounded trace representation |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | `29170f43a5e9ddfcc40585fa6651ffce08132c7b` | tool-contract diagnostics |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | `8690ffa2d3958b0130b6780e9f006322395b1cbd` | preservation and recovery planning |
| [Slipstream](https://github.com/jonah-ux/slipstream) | `1d73de7b031e3f7362360dde056e16ea942fb0eb` | local retrieval indexes |

The line for Agent Sandbox Run above is intentionally a source-head observation only; it does not
assert that every owner has completed the same public-audit milestone.

## Fifteen-minute review

1. Read the [architecture](AGENT-SYSTEMS-LAB-ARCHITECTURE.md) and
   [threat model](AGENT-SYSTEMS-LAB-THREAT-MODEL.md). Confirm that native ownership is explicit.
2. Clone [Forgeyard](https://github.com/jonah-ux/forgeyard), install its local package, and run
   `forgeyard demo`.
3. Run its checked-in `scripts/run_reference_flow.py` for `passing`, `blocked`, and `tampered`.
4. Run `scripts/evaluate_lab.py --iterations 2 --warmup 0 --json` and inspect dataset hashes,
   refusal states, machine-local timings, and `unavailable` artifact/install fields.
5. Clone [Agent Proof](https://github.com/jonah-ux/agent-proof) and run
   `python scripts/audit_public_surface.py --json` plus
   `PYTHONPATH=src python -m unittest discover -s tests -v`.
6. Clone [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) and run
   `python scripts/audit_public_surface.py --json` plus `python -m atlas.cli --version`.
7. Clone [ChatLens](https://github.com/jonah-ux/chatlens) and run
   `python scripts/audit_public_surface.py --json` plus
   `python -m unittest discover -s tests -v`.
8. Clone [Agent Policy](https://github.com/jonah-ux/agent-policy) and run
   `python scripts/audit_public_surface.py --json` plus `python -m agent_policy.cli --help`.
9. Change one graph edge or source byte, keep the old digest, and confirm the relevant verifier
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
| Public audits | [Forgeyard audit](https://github.com/jonah-ux/forgeyard/blob/main/scripts/audit_public_surface.py), [Agent Proof audit](https://github.com/jonah-ux/agent-proof/blob/main/scripts/audit_public_surface.py), [Atlas audit](https://github.com/jonah-ux/atlas-agent-runtime/blob/main/scripts/audit_public_surface.py), [ChatLens audit](https://github.com/jonah-ux/chatlens/blob/main/scripts/audit_public_surface.py), and [Agent Policy audit](https://github.com/jonah-ux/agent-policy/blob/main/scripts/audit_public_surface.py) | Dependency/license declarations, release markers, high-signal privacy scans, and optional checksums are inspectable across five flagship owners. | Complete DLP, security certification, reproducible builds, or provider controls. |

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

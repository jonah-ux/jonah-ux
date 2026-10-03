# External review packet

This packet is for a reviewer or review agent who wants to critique the public Agent Systems Lab
from a clean machine. It is intentionally source-first: every claim points to a repository, a
contract, a command, and a known limitation. The packet does not ask a reviewer to trust this
profile or to infer adoption from activity.

## Review target

The review snapshot was generated from profile base head `8661b3507527a4725e3b543b93151a7e635a66f4` on
2026-10-03. The owner heads below are source-identity observations from `refs/heads/main` made
while preparing this packet; they are freshness anchors, not release claims:

| Owner | Main head | Native responsibility |
| --- | --- | --- |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | `90bbc9685f320d4d1c8272f36483b91bdf8707ed` | review composition, packets, evaluation, public audit |
| [Agent Proof](https://github.com/jonah-ux/agent-proof) | `c0b75d77b53af8593ca73bdc23a59ee31b0962dd` | tamper-evident ledger, graph, interop, public audit |
| [ChatLens](https://github.com/jonah-ux/chatlens) | `d335e4209bfff81592e46163062f7074a2b3cb10` | local trace discovery and redacted handoff |
| [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) | `e3b19d7857273b4b549325d2f807bc2e47ded92d` | durable lifecycle and approval state |
| [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) | `6119ca6d507b1ae203b8422fa733d9363229d5e8` | scope, freshness, citations, admission/refusal |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | `99a35f58ec9cf9547f559a94ec5a1de0ba5c3df3` | capability decisions and policy receipts |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | `77d25690f76bbed9093fe9dca09cde7cd76d2b49` | bounded execution receipt |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | `f9b7c936c807c3f090eb8d93b9c2d61bc86d525e` | continuation and handoff state |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | `45f17bf55d6617415b43bf27c95ea1d4730e52aa` | bounded trace representation |
| [Sourcemark](https://github.com/jonah-ux/sourcemark) | `ed2e070296ad995797ea092e6e56ec18d1a1f2fd` | citation checks and source-bound export |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | `8129e159e428f639fead5e9a96b4c84396ca0688` | tool-contract diagnostics |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | `278e27fd335142d08288e5499e80ab01f140a455` | preservation and recovery planning |
| [Slipstream](https://github.com/jonah-ux/slipstream) | `27bb2f6d51909e9752c087792a8e02af0e2c2998` | local retrieval indexes |

The current clean-machine Forgeyard route was rerun at `90bbc9685f320d4d1c8272f36483b91bdf8707ed`:
`passing` reached `reviewable`, `blocked` preserved `reviewable=false`, `tampered` refused with exit 2,
the public audit returned `pass`, and the evaluation receipt returned `pass`; artifact state remained
`unavailable` without a supplied distribution directory.

The heads above are source-identity observations only; they do not assert deployment, adoption, or
that every owner has published a downloadable artifact. The Forgeyard installed reference-flow
observation below was run at the same `90bbc9685f320d4d1c8272f36483b91bdf8707ed`
boundary as the current matrix audit and evaluation. The [owner-native audit matrix](AGENT-SYSTEMS-LAB-AUDIT-MATRIX.md) records
which repositories expose `*-public-audit/v1`, which checks are rerunnable, and where artifact state
remains `unavailable` without an explicit distribution directory. A same-head local pack of Slipstream `v0.2.0` at `27bb2f6d51909e9752c087792a8e02af0e2c2998`
returned `artifact_audit=pass` for `slipstream-local-index-0.2.0.tgz` with artifact SHA-256
`d8b17994cae2ca828e9c4a4a93ee560fe607edd4de0113c88a9ee80c377610ff` and `SHA256SUMS`
SHA-256 `ab2130ffa8cf22c8038284a116b56c935c012918e43e6b95353163ce9df8596f`. This is a
local packed-artifact observation; it does not prove a published release or consumer install.
The same tarball was then installed into a disposable consumer with `npm install --ignore-scripts`,
rebuilt with `npm rebuild better-sqlite3`, and ran the packaged `slipstream self-test` under Node
`v26.7.0`; it returned `pass=true`, `inspect_ok=true`, `manifest_verified=true`,
`manifest_deterministic=true`, and `db_removed=true`. This is a local consumer observation,
not proof of outside adoption or production deployment.
A bounded Python wheel probe for Agent Proof at its locked head `c0b75d77b53af8593ca73bdc23a59ee31b0962dd`
was retried with the clean helper capacity and failed at PEP 517 because the runtime could not import
`setuptools.build_meta`; hosted CI published no downloadable artifact. The Python artifact state therefore
remains `unavailable` rather than being inferred from a green test run.

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

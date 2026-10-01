# Public roadmap

The portfolio is a small connected toolkit for inspectable, recoverable AI
coding workflows. This roadmap keeps planned work visible without presenting
future ideas as shipped features.

## Now

- Keep [Chatlens](https://github.com/jonah-ux/chatlens) v0.2.2 current as a stable public release, and keep [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) v0.2.0 current as a stable public release.
- Keep [Agent Proof](https://github.com/jonah-ux/agent-proof) v0.2.0 as the stable public install surface, with wheel/source assets, checksums, fresh consumer proof, and the current interop adapter kept separately visible.
- Keep [Forgeyard](https://github.com/jonah-ux/forgeyard) v0.2.6 as a stable local evidence-record surface, with the one-command demo, digest-pinned verification, release assets, and the unreleased 0.3.0 provenance-packet candidate kept separately visible.
- Keep [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) v0.3.0 as the public prerelease install surface, with baseline drift and `--fail-on-drift` evidence kept current.
- Keep [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit) on its v0.1.1 public release surface while the 0.3.0 receipt-scoring candidate receives independent release readback. Keep [Context Pack](https://github.com/jonah-ux/context-pack), [Agent Policy](https://github.com/jonah-ux/agent-policy), [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite), [Agent Resume](https://github.com/jonah-ux/agent-resume), and [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) on their existing public release surfaces while their source candidates receive independent release readback.
- Keep [Slipstream](https://github.com/jonah-ux/slipstream) v0.2.0 current as a stable public release, with packed-consumer and offline verify evidence kept current.
- Keep the eight supporting tools runnable from public `main`, with green CI,
  disposable demos, and honest release status.
- Keep release evidence current when a public head or asset changes, with the
  exact tag, CI run, checksum, and fresh-consumer boundary recorded.

## Next

- Add stable-release candidates only after the prerelease path has another
  independent consumer cycle and the release status can be stated without
  qualification.
- Add sanitized contributor fixtures for new agent-store and MCP-manifest
  shapes.
- Add cross-tool examples showing a context pack feeding policy, sandbox, and
  proof steps without hiding unknown outcomes.
- Turn the public ship log into short X build notes tied to real commits and
  reproducible commands.

## Advanced-pass boundaries

The second pass prioritizes interfaces that can be proven across repository
boundaries. The remaining projects have an explicit evidence-backed stopping
point instead of a speculative feature claim:

| Project | Current boundary after this pass | Next advancement gate |
| --- | --- | --- |
| [Slipstream](https://github.com/jonah-ux/slipstream) | v0.2.0 stable main now includes the caller-owned vector workflow plus inspect/manifest/verify and packed-consumer proof. | A new storage or provider adapter needs a caller-owned fixture and a fresh packed-consumer readback before another public feature is promoted. |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | v0.3.0 remains a prerelease with deterministic contract fingerprints, baseline drift, and `--fail-on-drift`. | Another independent consumer cycle and stable-release qualification are required before expanding the contract surface. |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | v0.2.0 stable covers archive, receipt, lifecycle-audit, and recovery readback. | Any execution or mutation slice needs a disposable restore fixture and independent post-apply evidence. |
| [Context Pack](https://github.com/jonah-ux/context-pack) | The 0.2.0 source candidate is bounded to deterministic manifests, verification, and diff safety. | A new adapter must ship with a sanitized source fixture, integrity refusal cases, and a fresh wheel/sdist consumer. |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | The 0.2.0 source candidate is bounded to ordered composition and digest-bound explain receipts. | Policy-provider expansion waits for conflict fixtures, deterministic decision readback, and an independently installed consumer. |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | The 0.2.0 source candidate is the strict redacted trace inspector consumed by Chatlens `trace-import`. | A new event family needs a synthetic redaction fixture and cross-consumer import proof before changing the schema. |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | The 0.2.0 source candidate is bounded to integrity-checked continuation records and redacted diffs. | Resume orchestration needs an explicit fixture for stale state, identity drift, and clean restart readback. |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | The 0.2.0 source candidate emits bounded, enforcement-aware v2 receipts consumed by Agent Eval Kit. | New isolation or output modes wait for a disposable adversarial fixture and a downstream receipt consumer proof. |

These boundaries are current public evidence boundaries. They do not imply
that a future implementation is impossible; they define the proof required
before another public-main claim is made.

## Later

- Evaluate PyPI publication after the GitHub prerelease path has a successful
  independent consumer cycle.
- Add provider-neutral adapters only when a fixture and a clear evidence
  boundary can be maintained.
- Consider leaving the three upstream forks only after separately reviewing the
  permanent fork-network consequences.

## Contribution bar

Useful contributions should include a focused fixture, a deterministic command
or test, and a statement of what the result proves and what it does not prove.
The projects value inspectability and honest limits over activity volume.

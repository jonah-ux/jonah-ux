# Public roadmap

The portfolio is a small connected toolkit for inspectable, recoverable AI
coding workflows. This roadmap keeps planned work visible without presenting
future ideas as shipped features.

## Now

- Keep [Chatlens](https://github.com/jonah-ux/chatlens) v0.3.0 current as a stable public release, and keep [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) v0.2.0 current as a stable public release.
- Keep [Agent Proof](https://github.com/jonah-ux/agent-proof) v0.2.0 as the stable public install surface, with wheel/source assets, checksums, fresh consumer proof, and the current interop adapter kept separately visible.
- Keep [Forgeyard](https://github.com/jonah-ux/forgeyard) v0.3.0 as the stable flagship orchestration surface, with specialist composition, portable provenance packets, the one-command demo, and release assets kept current.
- Keep [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) v0.3.0 as the public prerelease install surface, with baseline drift and `--fail-on-drift` evidence kept current.
- Keep [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit) v0.3.0, [Context Pack](https://github.com/jonah-ux/context-pack) v0.2.0, [Agent Policy](https://github.com/jonah-ux/agent-policy) v0.2.0, [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) v0.2.0, [Agent Resume](https://github.com/jonah-ux/agent-resume) v0.2.0, and [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) v0.2.0 as public prerelease surfaces with fresh downloaded-asset readback kept current.
- Keep [Slipstream](https://github.com/jonah-ux/slipstream) v0.2.0 current as a stable public release, with packed-consumer and offline verify evidence kept current.
- Keep the eight supporting tools runnable from public `main`, with green CI,
  disposable demos, and honest release status.
- Keep release evidence current when a public head or asset changes, with the
  exact tag, CI run, checksum, and fresh-consumer boundary recorded.

- Keep external adoption explicitly unknown until a consumer outside the
  repository's own hosted workflow is observed; downloaded-asset readback is
  artifact usability proof, not evidence of a third-party adopter.

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
| [Chatlens](https://github.com/jonah-ux/chatlens) | v0.3.0 stable now carries the trace envelope, recovery roundtrip, and downloaded wheel/sdist readback. | Future source changes need a new versioned release candidate; the stable tag must never point at an older command surface than main documents. |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | v0.3.0 stable covers archive, receipt, lifecycle-audit, specialist-report composition, portable provenance packets, and a hosted synthetic Workbench on current main. | Any execution or mutation slice needs a disposable restore fixture and independent post-apply evidence; the Workbench remains synthetic and does not claim command execution, deployment, or resume. |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | v0.3.0 remains a prerelease with deterministic contract fingerprints, baseline drift, `--fail-on-drift`, and independent downloaded-asset consumer proof. | Stable promotion still requires an intentional stable-release path and a documented support boundary. |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | v0.2.0 stable covers archive, receipt, lifecycle-audit, recovery readback, and a disposable maintainer rehearsal. | Any live execution or mutation slice needs a disposable restore fixture and independent post-apply evidence; the example remains temporary-only. |
| [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit) | v0.3.0 prerelease scores integrity-bound sandbox receipts and has independent wheel/sdist readback plus a downstream cross-tool proof. | Stable promotion needs a second independent consumer cycle and a documented support boundary for receipt expectations. |
| [Context Pack](https://github.com/jonah-ux/context-pack) | v0.2.0 is a prerelease with deterministic manifests, verification, diff safety, and independent wheel/sdist readback. | A stable promotion needs an intentional support boundary and a second independent consumer cycle; a new adapter still needs a sanitized source fixture. |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | v0.2.0 is a prerelease with ordered composition, digest-bound explain receipts, and independent wheel/sdist readback. | Stable promotion needs cross-platform policy fixtures and a second independent consumer cycle. |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | v0.2.0 is a prerelease with strict redacted trace inspection, bounded queries, and independent wheel/sdist readback. | Stable promotion needs a synthetic event-family support boundary and a second independent consumer cycle. |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | v0.2.0 is a prerelease with integrity-bound continuation records, redacted diffs, and independent wheel/sdist readback. | Stable promotion needs stale-state and clean-restart fixtures plus a second independent consumer cycle. |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | v0.2.0 is a prerelease with enforcement-aware v2 receipts, independent wheel/sdist readback, and Agent Eval downstream scoring. | Stable promotion needs an explicit isolation support boundary and a second independent consumer cycle. |

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

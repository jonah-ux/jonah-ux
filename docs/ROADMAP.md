# Public roadmap

The portfolio is a small connected toolkit for inspectable, recoverable AI
coding workflows. This roadmap keeps planned work visible without presenting
future ideas as shipped features.

## Now

- Keep [Chatlens](https://github.com/jonah-ux/chatlens) v0.2.0 installable from its public prerelease, and keep [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) v0.2.0 current as a stable public release.
- Keep [Agent Proof](https://github.com/jonah-ux/agent-proof) v0.2.0 as the stable public install surface, with wheel/source assets, checksums, and fresh consumer proof kept current.
- Keep [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) v0.2.4 as the public install surface while the merged 0.3.0 baseline-drift candidate receives its next annotated release tag.
- Keep [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit), [Context Pack](https://github.com/jonah-ux/context-pack), [Agent Policy](https://github.com/jonah-ux/agent-policy), [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite), [Agent Resume](https://github.com/jonah-ux/agent-resume), and [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) on their existing public release surfaces while their new source candidates receive independent release readback.
- Keep [Slipstream](https://github.com/jonah-ux/slipstream) v0.1.0 as the public install surface while the merged `main` inspect plus hardened redacted manifest candidate receives its next annotated release tag.
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

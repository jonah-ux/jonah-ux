# Engineering evidence map

This map connects the portfolio story to source and observable behavior. It is
intended for a reviewer who wants to move from the profile to a concrete file
or command quickly.

| Capability | Public implementation | Observable proof |
| --- | --- | --- |
| Multi-system integrations | [Chatlens Codex adapter](https://github.com/jonah-ux/chatlens/blob/main/src/chatlens/codex.py), [Claude adapter](https://github.com/jonah-ux/chatlens/blob/main/src/chatlens/claude.py), [Hermes adapter](https://github.com/jonah-ux/chatlens/blob/main/src/chatlens/hermes.py) | One local CLI reads three conversation-store shapes and reports source coverage explicitly |
| Agent-facing API contracts | [Chatlens CLI reference](https://github.com/jonah-ux/chatlens/blob/main/docs/cli.md), [MCP Doctor CLI](https://github.com/jonah-ux/mcp-doctor/blob/main/src/mcp_doctor/cli.py) | Noninteractive commands, stable JSON schemas, bounded output, and meaningful exit codes |
| Contract validation | [MCP Doctor implementation](https://github.com/jonah-ux/mcp-doctor/blob/main/src/mcp_doctor/cli.py), [valid fixture](https://github.com/jonah-ux/mcp-doctor/blob/main/examples/valid-server.json), [invalid fixture](https://github.com/jonah-ux/mcp-doctor/blob/main/examples/invalid-server.json) | Clean contracts pass; missing descriptions and timeouts become stable MCP002/MCP004 findings |
| Deterministic data boundaries | [Context Pack CLI](https://github.com/jonah-ux/context-pack/blob/main/src/context_pack/cli.py) | A bounded file set, byte count, and SHA-256 digest let another agent reproduce the same input |
| Permission decisions | [Agent Policy CLI](https://github.com/jonah-ux/agent-policy/blob/main/src/agent_policy/cli.py) | Allow/deny output includes the requested kind, value, decision, and reason before execution |
| Evidence and outcome boundaries | [Agent Proof CLI](https://github.com/jonah-ux/agent-proof/blob/main/src/agent_proof/cli.py) | Proof envelopes preserve explicit unknowns instead of claiming a user-visible result |
| Reproducible automation | [Agent Eval Kit demo](https://github.com/jonah-ux/agent-eval-kit/blob/main/demos/demo.py), [CI workflow](https://github.com/jonah-ux/agent-eval-kit/blob/main/.github/workflows/ci.yml) | The same fixture produces a machine-readable scorecard locally and in hosted CI |
| Release discipline | [Release workflow](https://github.com/jonah-ux/mcp-doctor/blob/main/.github/workflows/release.yml), [release guide](https://github.com/jonah-ux/mcp-doctor/blob/main/docs/releasing.md) | Semantic tags build wheel/source assets, checksums, and a prerelease only after deliberate publication |
| Honest isolation reporting | [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run), [security guidance](https://github.com/jonah-ux/agent-sandbox-run/blob/main/SECURITY.md) | Receipts report the backend and `enforced` state instead of implying a sandbox that was not proven |

The projects are deliberately small. The evidence is in the boundaries: what
the tool reads, what it writes, what it can prove, and what it refuses to
claim.

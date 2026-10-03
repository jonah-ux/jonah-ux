# Agent Systems Lab architecture

The public lab is a collection of independently installable tools with explicit protocol owners.
The architecture decision record is maintained in the portfolio workspace and is reflected here
for reviewers who start at the GitHub profile.

```text
context admission -> policy and bounded execution -> proof and continuation -> reviewable delivery
```

Core ownership:

- [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) owns scope, freshness,
  citations, and refusal outcomes.
- [ChatLens](https://github.com/jonah-ux/chatlens) owns local trace discovery, redaction, and trace
  handoff.
- [Agent Policy](https://github.com/jonah-ux/agent-policy) and [MCP Doctor](https://github.com/jonah-ux/mcp-doctor)
  own capability manifests and tool-contract diagnostics.
- [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) and [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime)
  own bounded execution receipts and durable lifecycle state.
- [Agent Proof](https://github.com/jonah-ux/agent-proof), [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite),
  and [Agent Resume](https://github.com/jonah-ux/agent-resume) own proof, normalized traces, and continuation.
- [Forgeyard](https://github.com/jonah-ux/forgeyard) and [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator)
  own reviewable delivery and Git preservation.
- [Slipstream](https://github.com/jonah-ux/slipstream) owns local retrieval indexes.

The shared `ai-work-evidence/v1` layer is additive. It contains bounded metadata and hashes and
does not reinterpret any source repository's native schema. The public [Portfolio Suite v2 map](./PORTFOLIO-SUITE-V2.md)
shows the released ChatLens → Atlas → Forgeyard path; this page shows how the surrounding lab
capabilities connect without requiring one installation to trust all the others.

The current Forgeyard integration proof is deliberately offline: its
[reference-flow contract](https://github.com/jonah-ux/forgeyard/blob/main/docs/contracts/forgeyard-reference-flow-v1.md)
checks a reviewable path, preserves an unknown status as blocked, and refuses digest-tampered
record bytes. The hosted [Workbench](https://jonah-ux.github.io/forgeyard/) adds a 15-class
adversarial matrix for stale, denied, unenforced, partial, malformed, traversal, leakage, drift,
duplicate, unbounded, false-completion, and tampered signals. These are
synthetic fixtures that make the boundaries inspectable; they do not claim adoption or production
deployment by the surrounding repositories.

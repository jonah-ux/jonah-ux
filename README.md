<img src="./docs/profile-hero.png" alt="Jonah Helland — AI developer tooling" width="1200" />

# Jonah Helland

I run a business on a fleet of AI coding agents: Claude and Codex sessions, cheap open models for grunt work, and orchestrators handing work between them, around the clock on seven machines.

For months they told me work was done when it wasn't. Workers reported fixes "shipped" when the PR held one JSON file. A verdict table that looked healthy turned out to be 87.5% heartbeat rows. Cleanup jobs deleted work mid-push. My own dashboards called outages that never happened.

These repos are what I built so that stopped. Each one is small, standalone, MIT-licensed, and has a demo you can run in about a minute.

<!-- WRITING: uncomment once published
**Read the story:** [My AI agents kept telling me the work was done](LINK) · [the position paper behind it](LINK)
-->

[Build notes on X](https://x.com/jonahhelland)

## The tools

| If your agents… | Use | Try it |
| --- | --- | --- |
| lose sessions and context | [**Chatlens**](https://github.com/jonah-ux/chatlens): search Codex, Claude Code, and Hermes sessions offline | [guide](https://jonah-ux.github.io/chatlens/walkthrough.html) |
| cite things they never read | [**Sourcemark**](https://github.com/jonah-ux/sourcemark): citations that survive edits, checked against what the agent actually read | [guide](https://jonah-ux.github.io/sourcemark/walkthrough.html) |
| claim work they didn't do | [**Agent Proof**](https://github.com/jonah-ux/agent-proof): proof bundles that refuse tampering | [guide](https://jonah-ux.github.io/agent-proof/walkthrough/) |
| leave no reviewable record | [**Forgeyard**](https://github.com/jonah-ux/forgeyard): sealed review records for agent work | [workbench](https://jonah-ux.github.io/forgeyard/) |
| trust stale or out-of-scope context | [**Context Integrity Lab**](https://github.com/jonah-ux/context-integrity-lab): admission gates for context | [explorer](https://jonah-ux.github.io/context-integrity-lab/admission-explorer.html) |
| destroy work during cleanup | [**Worktree Conservator**](https://github.com/jonah-ux/worktree-conservator): reclaims a worktree only after the remote proves it's safe | [desk](https://jonah-ux.github.io/worktree-conservator/plan-explorer.html) |
| need approval before acting | [**Atlas**](https://github.com/jonah-ux/atlas-agent-runtime): a durable, approval-gated task runtime | [flight deck](https://jonah-ux.github.io/atlas-agent-runtime/flight-deck.html) |
| keep permissions in the prompt | [**Agent Policy**](https://github.com/jonah-ux/agent-policy) · [**Agent Sandbox Run**](https://github.com/jonah-ux/agent-sandbox-run) | [policy](https://jonah-ux.github.io/agent-policy/walkthrough.html) · [sandbox](https://jonah-ux.github.io/agent-sandbox-run/walkthrough.html) |
| get graded on vibes | [**Agent Eval Kit**](https://github.com/jonah-ux/agent-eval-kit): repeated trials, bounded comparisons | [scorecard](https://jonah-ux.github.io/agent-eval-kit/walkthrough.html) |
| drop the handoff between sessions | [**Agent Resume**](https://github.com/jonah-ux/agent-resume) · [**Context Pack**](https://github.com/jonah-ux/context-pack) | [resume](https://jonah-ux.github.io/agent-resume/walkthrough.html) · [pack](https://jonah-ux.github.io/context-pack/walkthrough.html) |
| ship sloppy MCP tools | [**MCP Doctor**](https://github.com/jonah-ux/mcp-doctor): an MCP manifest contract linter | [guide](https://jonah-ux.github.io/mcp-doctor/walkthrough.html) |
| produce unreadable traces | [**Agent Trace Lite**](https://github.com/jonah-ux/agent-trace-lite): offline, redacted trace viewer | [guide](https://jonah-ux.github.io/agent-trace-lite/walkthrough.html) |
| need fast local retrieval | [**Slipstream**](https://github.com/jonah-ux/slipstream): SQLite + sqlite-vec, inspectable | [inspector](https://jonah-ux.github.io/slipstream/inspector.html) |

None of them depends on another. If you want to wire them together, the [suite map](docs/PORTFOLIO-SUITE-V2.md) and [cold-review checklist](docs/COLD-REVIEW-CHECKLIST.md) show how.

## What I believe

- **A report is a claim, not a fact.** A confident status message isn't the state of the world, whether it comes from an agent, a cron, or a dashboard.
- **Permissions live outside the model.** No agent gets access because it asked convincingly.
- **Tests should mostly be refusals.** The tools I trust prove what they won't do.
- **Delegate coordination, keep control.** People set the purpose and the risk; software enforces the boundaries; evidence decides what can be claimed.

[Engineering evidence](docs/ENGINEERING-EVIDENCE.md) · [Ship log](docs/SHIPLOG.md) · [Roadmap](docs/ROADMAP.md)

<img src="./docs/profile-hero.png" alt="Jonah Helland — AI developer tooling" width="1200" />

# Jonah Helland

I build **inspectable, recoverable tools for AI-assisted software engineering**.

Most of my work starts with a messy workflow and ends with a small system that makes the important parts easier to see: APIs, automation, local-first tools, and AI-agent infrastructure with clear failure modes and a way back. I use coding agents heavily, but the result still needs to be understandable, bounded, testable, and recoverable by a human.

[Build notes on X](https://x.com/jonahhelland) · [Source](https://github.com/jonah-ux) · [Deeper evidence and roadmap](docs/ENGINEERING-EVIDENCE.md)

![Agent tooling stack: recover context, bound decisions, prove outcomes](docs/toolkit-stack.svg)

## Start with the 90-second tour

These projects form one inspectable workflow. Choose the lane that matches what
you want to see first, then follow the repository's disposable demo.

| Lane | Start here | What it proves |
| --- | --- | --- |
| **Trust the result** | [Agent Proof](https://github.com/jonah-ux/agent-proof) → [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | Evidence can be tamper-evident, and tool contracts can fail closed before an agent uses them. |
| **Recover the work** | [Chatlens](https://github.com/jonah-ux/chatlens) → [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | Context and Git state can be searched, archived, and restored without pretending recovery is deployment. |
| **Build locally** | [Slipstream](https://github.com/jonah-ux/slipstream) → [Forgeyard](https://github.com/jonah-ux/forgeyard) | Retrieval and delivery records can stay local, bounded, deterministic, and reviewable. |
| **Admit context safely** | [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) → [Agent Proof](https://github.com/jonah-ux/agent-proof) | Scope, freshness, citations, refusal states, and evidence boundaries remain visible before an answer is trusted. |

The fastest concrete entry points are Agent Proof's [annotated v0.3.1 prerelease assets](https://github.com/jonah-ux/agent-proof/releases/tag/v0.3.1), Context Integrity Lab's [stable v0.2.0 envelope release](https://github.com/jonah-ux/context-integrity-lab/releases/tag/v0.2.0), Slipstream's [`npm test` path](https://github.com/jonah-ux/slipstream#install-and-run), and Forgeyard's [one-command evidence demo](https://github.com/jonah-ux/forgeyard#quick-start).

For the flagship product experience, open the public [Forgeyard Workbench](https://jonah-ux.github.io/forgeyard/): load synthetic specialist reports, compose a review record, and trigger the fail-closed tamper state in your browser.

Forgeyard is the flagship orchestration surface: it composes specialist reports into reviewable delivery records and portable provenance packets. Its annotated `v0.3.2` prerelease consumes verified Agent Proof interoperability projections and carries a Context Integrity Lab report in the public Workbench fixture. Agent Proof, Chatlens, Slipstream, and Worktree Conservator supply the surrounding trust, recovery, retrieval, and lifecycle layers; Chatlens `v0.3.0` carries the trace handoff API in its stable release, while MCP Doctor remains explicitly labeled a prerelease.

[Forgeyard](https://github.com/jonah-ux/forgeyard) is the flagship systems project: a local-first foundation for reviewable delivery records, explicit evidence contracts, and bounded worktree plans. Its `v0.3.0` stable line established specialist composition, portable provenance packets, and the one-command demo; the annotated `v0.3.2` prerelease adds verified Agent Proof projection intake and the Context Integrity Lab Workbench report, with wheel/source assets, checksums, and fresh-consumer evidence. Planned execution and resume slices are intentionally not presented as shipped.

[Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) is the focused admission-boundary example: stable `v0.2.0` makes scope, freshness, citations, refusal states, and the versioned `context-integrity/v1` envelope inspectable through a deterministic CLI and local browser console over fictional records. Agent Proof consumes the envelope without copying answer text or raw scope identifiers.

## The engineering loop

These tools explore one practical question: **can agent work be understood, bounded, proved, and continued?**

- **Recover context:** Chatlens turns local session stores into searchable, bounded work cards.
- **Check the interface:** MCP Doctor catches ambiguous tool contracts before an agent sees them.
- **Bound and run:** Context Pack, Agent Policy, and Agent Sandbox Run make inputs, permissions, and execution limits explicit.
- **Record and continue:** Agent Proof, Agent Trace Lite, and Agent Resume preserve evidence and continuation state.

Each repository contains its own install path, tests, demos, release notes, and security boundary. Start with the disposable demo before connecting a tool to a real workflow. The repositories describe what a check proves and what it cannot prove; a valid digest is not a claim of deployment, adoption, or a user-visible result.

For a runnable cross-project example, see the [public integration walkthrough](docs/INTEGRATION-WALKTHROUGH.md): Context Integrity Lab admits scoped, fresh context, Agent Proof normalizes and source-binds the result, and Forgeyard records the bounded review decision. The same walkthrough covers MCP Doctor contract checks, sandbox receipt scoring, loss-aware evidence envelopes, and Chatlens-to-Agent-Trace export while keeping source, release, and outcome claims separate.

## Public provenance

The profile is a current public engineering portfolio, not an attempt to manufacture elapsed time or adoption. Most original projects were built and released recently. I am keeping that history intact and using the next work to show depth: adversarial tests, clean installed-consumer checks, clearer architecture, and maintenance driven by real use.

[Engineering evidence](docs/ENGINEERING-EVIDENCE.md) · [Work samples](docs/WORK-SAMPLES.md) · [Ship log](docs/SHIPLOG.md)

<img src="./docs/profile-hero.png" alt="Jonah Helland — AI developer tooling" width="1200" />

# Jonah Helland

I build **inspectable, recoverable tools for AI-assisted software engineering**.

My work sits at the intersection of developer tools, local-first systems, automation, APIs, and AI agents. I use coding agents heavily; the engineering standard is that the resulting systems stay understandable, bounded, testable, and recoverable by a human.

I’m interested in Applied AI Engineering, AI infrastructure, developer tools, automation engineering, forward-deployed engineering, and software engineering roles where a small interface must become a reliable outcome.

[Build notes on X](https://x.com/jonahhelland) · [Source](https://github.com/jonah-ux) · [Deeper evidence and roadmap](docs/ENGINEERING-EVIDENCE.md)

## Start with these four projects

| Project | What to inspect | Run it |
| --- | --- | --- |
| [Agent Proof](https://github.com/jonah-ux/agent-proof) | Stable `v0.2.0` evidence ledger with hash-linked records, provenance graphs, tamper refusal, and an explicit integrity/outcome boundary. | `python -m pip install <release-wheel>` · [`v0.2.0` assets](https://github.com/jonah-ux/agent-proof/releases/tag/v0.2.0) |
| [Chatlens](https://github.com/jonah-ux/chatlens) | Local search and recovery across Codex, Claude Code, and Hermes sessions through isolated readers. | `chatlens --help` |
| [Slipstream](https://github.com/jonah-ux/slipstream) | A small JavaScript/SQLite + sqlite-vec index with deterministic inspect, manifest, and verify readback. | `npm ci && npm test` |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | Reviewable Git worktree retirement, verified archives, guarded recovery, and explicit refusal conditions. | `worktree-conservator demo --json` |

[MCP Doctor](https://github.com/jonah-ux/mcp-doctor) is the supporting project to read next: an offline MCP contract linter with stable diagnostics, strict-mode exit behavior, deterministic contract fingerprints, and baseline drift gates. Agent Proof is the current stable release; the other three flagship projects remain explicitly labeled prereleases while their next release cycles continue.

[Forgeyard](https://github.com/jonah-ux/forgeyard) is the next systems project to inspect: a local-first foundation for reviewable delivery records, explicit evidence contracts, and bounded worktree plans. Its `v0.1.0` public prerelease includes wheel/source assets and fresh-consumer evidence; planned execution and resume slices are intentionally not presented as shipped.

## The engineering loop

These tools explore one practical question: **can agent work be understood, bounded, proved, and continued?**

- **Recover context:** Chatlens turns local session stores into searchable, bounded work cards.
- **Check the interface:** MCP Doctor catches ambiguous tool contracts before an agent sees them.
- **Bound and run:** Context Pack, Agent Policy, and Agent Sandbox Run make inputs, permissions, and execution limits explicit.
- **Record and continue:** Agent Proof, Agent Trace Lite, and Agent Resume preserve evidence and continuation state.

Each repository contains its own install path, tests, demos, release notes, and security boundary. Start with the disposable demo before connecting a tool to a real workflow. The repositories describe what a check proves and what it cannot prove; a valid digest is not a claim of deployment, adoption, or a user-visible result.

## Public provenance

The profile is a current public engineering portfolio, not an attempt to manufacture elapsed time or adoption. Most original projects were built and released recently. I am keeping that history intact and using the next work to show depth: adversarial tests, clean installed-consumer checks, clearer architecture, and maintenance driven by real use.

[Engineering evidence](docs/ENGINEERING-EVIDENCE.md) · [Work samples](docs/WORK-SAMPLES.md) · [Ship log](docs/SHIPLOG.md)

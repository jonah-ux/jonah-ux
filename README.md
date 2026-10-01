<img src="./docs/profile-hero.png" alt="Jonah Helland — AI developer tooling" width="1200" />

# Jonah Helland

I build **inspectable, recoverable tools for AI-assisted software engineering**.

My work sits at the intersection of developer tools, local-first systems, automation, APIs, and AI agents. I use coding agents heavily; the engineering standard is that the resulting systems stay understandable, bounded, testable, and recoverable by a human.

I’m interested in Applied AI Engineering, AI infrastructure, developer tools, automation engineering, forward-deployed engineering, and software engineering roles where a small interface must become a reliable outcome.

[Build notes on X](https://x.com/jonahhelland) · [Source](https://github.com/jonah-ux) · [Deeper evidence and roadmap](docs/ENGINEERING-EVIDENCE.md)

## Start with the 90-second tour

These projects form one inspectable workflow. Choose the lane that matches what
you want to see first, then follow the repository's disposable demo.

| Lane | Start here | What it proves |
| --- | --- | --- |
| **Trust the result** | [Agent Proof](https://github.com/jonah-ux/agent-proof) → [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | Evidence can be tamper-evident, and tool contracts can fail closed before an agent uses them. |
| **Recover the work** | [Chatlens](https://github.com/jonah-ux/chatlens) → [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | Context and Git state can be searched, archived, and restored without pretending recovery is deployment. |
| **Build locally** | [Slipstream](https://github.com/jonah-ux/slipstream) → [Forgeyard](https://github.com/jonah-ux/forgeyard) | Retrieval and delivery records can stay local, bounded, deterministic, and reviewable. |

The fastest concrete entry points are Agent Proof's [stable release assets](https://github.com/jonah-ux/agent-proof/releases/tag/v0.2.0), Slipstream's [`npm test` path](https://github.com/jonah-ux/slipstream#install-and-run), and Forgeyard's [one-command evidence demo](https://github.com/jonah-ux/forgeyard#quick-start).

The supporting lab includes repeated-trial evaluation, provenance-bound context packs, composable policy layers, trace integrity queries, integrity-bound resumes, and bounded execution receipts. Agent Proof, Chatlens, Forgeyard, Slipstream, and Worktree Conservator are the current stable releases; MCP Doctor remains explicitly labeled a prerelease while its next release cycle continues.

[Forgeyard](https://github.com/jonah-ux/forgeyard) is the next systems project to inspect: a local-first foundation for reviewable delivery records, explicit evidence contracts, and bounded worktree plans. Its `v0.2.6` stable release includes a one-command evidence-to-review demo, evidence-receipt verification, digest-pinned record validation, wheel/source assets, checksums, and fresh-consumer evidence; planned execution and resume slices are intentionally not presented as shipped.

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

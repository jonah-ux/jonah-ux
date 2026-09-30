# Jonah Helland — selected work

This is the fastest route through my public engineering work. Each sample has public source, a runnable interface, tests, and an explicit evidence boundary.

## Start with these three

### [Chatlens](https://github.com/jonah-ux/chatlens)

**Problem:** an agent’s previous reasoning is often trapped in a local session store when the next person needs to continue the work.

**What it shows:** local-first data discovery, bounded search and rendering, multiple source adapters, privacy boundaries, stable JSON output, and a versioned CLI release.

**Proof:** [v0.1.0 release](https://github.com/jonah-ux/chatlens/releases/tag/v0.1.0) · [CI](https://github.com/jonah-ux/chatlens/actions) · [README](https://github.com/jonah-ux/chatlens#readme)

```bash
python -m pip install 'git+https://github.com/jonah-ux/chatlens.git@v0.1.0'
chatlens --help
```

### [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator)

**Problem:** removing a Git worktree can destroy useful context when identity, merge state, or recovery evidence is unclear.

**What it shows:** defensive CLI design, deterministic plans, archive verification, explicit refusal states, and recovery-oriented workflows.

**Proof:** [v0.1.0 release](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.1.0) · [CI](https://github.com/jonah-ux/worktree-conservator/actions) · [README](https://github.com/jonah-ux/worktree-conservator#readme)

### [MCP Doctor](https://github.com/jonah-ux/mcp-doctor)

**Problem:** an agent cannot make a reliable decision when an MCP tool contract is missing descriptions, schemas, or timeouts.

**What it shows:** contract validation, stable diagnostic codes, JSON and stdin interfaces, strict CI mode, and honest error boundaries.

**Proof:** [current README + feature head](https://github.com/jonah-ux/mcp-doctor/commit/5ec80e4) · [CI](https://github.com/jonah-ux/mcp-doctor/actions) · [README](https://github.com/jonah-ux/mcp-doctor#readme)

MCP Doctor is currently a versioned source release candidate: the public
repository has packaging, fixtures, CI, and a runnable demo, while the
downloadable GitHub prerelease step is still intentionally pending review.

## The engineering pattern

Across the projects, I focus on the full path from a small interface to a result someone else can inspect:

- **APIs and integrations:** adapters and explicit input contracts keep system boundaries visible.
- **Data and state:** local indexes, bounded records, hashes, and coverage fields make state inspectable.
- **Automation:** noninteractive commands, stable JSON, meaningful exit codes, and CI-friendly behavior.
- **Reliability:** refusal states and unknowns stay visible instead of being turned into false success.
- **Release discipline:** public source, versioned tags or release heads, CI, demos, security guidance, and reproducible checks. I label prereleases and release candidates separately instead of implying that every tool is already a published package.

The smaller [agent tooling lab](https://github.com/jonah-ux#the-agent-tooling-lab) extends the same pattern into evaluation, evidence, policy, tracing, continuation, and command limits.

## Good conversations to have with me

- Designing an API or automation workflow that has to remain observable after it leaves the happy path.
- Turning a local or internal workflow into a small, installable developer tool.
- Making AI-agent behavior inspectable through structured output, evidence records, and safe boundaries.
- Connecting product needs, databases, integrations, and operational reality without hiding uncertainty.

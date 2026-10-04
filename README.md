<img src="./docs/profile-hero.png" alt="Jonah Helland — AI developer tooling" width="1200" />

# Jonah Helland

I build **inspectable, recoverable tools for AI-assisted software engineering**.

Most of my work starts with a messy workflow and ends with a small system that makes the important parts easier to see: APIs, automation, local-first tools, and AI-agent infrastructure with clear failure modes and a way back. I use coding agents heavily, but the result still needs to be understandable, bounded, testable, and recoverable by a human.

[Build notes on X](https://x.com/jonahhelland) · [Source](https://github.com/jonah-ux) · [Deeper evidence and roadmap](docs/ENGINEERING-EVIDENCE.md)

## Independent tools, optional connections

Every product has its own install, demo, and useful core workflow. Pick the tool that solves your problem; connecting it to another project is an optional next step.

One optional integration follows a three-tool evidence lifecycle: [ChatLens v0.4.0](https://github.com/jonah-ux/chatlens/releases/tag/v0.4.0) exports a redacted local trace, [Atlas v0.2.0](https://github.com/jonah-ux/atlas-agent-runtime/releases/tag/v0.2.0) records a durable approval-gated task, and [Forgeyard v0.5.0](https://github.com/jonah-ux/forgeyard/releases/tag/v0.5.0) composes both into a reviewable record through `ai-work-evidence/v1`. [Read the reviewer map](docs/PORTFOLIO-SUITE-V2.md).

Forgeyard also exposes an opt-in [installed reference flow](https://github.com/jonah-ux/forgeyard/blob/main/docs/contracts/forgeyard-reference-flow-v1.md): it invokes the installed ChatLens, Atlas, Agent Proof, and Forgeyard CLIs against owner-produced artifacts, source-verifies the handoff, and returns reviewable, blocked, tampered, or unavailable outcomes. A fresh local consumer observation used ChatLens 0.4.0, Atlas 0.2.0, Agent Proof 0.4.1, and Forgeyard 0.5.0; it is a reproducible handoff observation, not a deployment or adoption claim.

The [Agent Systems Lab architecture](docs/AGENT-SYSTEMS-LAB-ARCHITECTURE.md) maps additional
optional connections between context admission, policy, bounded execution, proof, continuation,
retrieval, and reviewable delivery. Each repository keeps ownership of its core behavior.

For an outside engineer, the [cold-review checklist](docs/COLD-REVIEW-CHECKLIST.md) gives the
shortest path from profile to fresh install, passing/blocked/tampered CLI flows, the fixed lab
benchmark, the hosted 15-class refusal matrix, and the exact limits of each proof.

The [conformance matrix](docs/AGENT-SYSTEMS-LAB-CONFORMANCE.md) lists every current owner,
native schema, public manifest, and refusal/readback boundary in one place.

[Agent Proof 0.5.0](https://github.com/jonah-ux/agent-proof/releases/tag/v0.5.0) adds an
offline check over thirteen pinned public declarations: exact bytes, source fields,
repository identity, and explicitly admitted native versions. It refuses an
unversioned capability name rather than treating a schema suffix as support.
Read the [compatibility contract](https://github.com/jonah-ux/agent-proof/blob/681b34f1ac7189dcd4da26ad8b5c5ef0b3a07880/docs/contracts/agent-systems-lab-compatibility-v2.md)
and [run the installed review check](docs/EXTERNAL-REVIEW-PACKET.md#agent-proof-050-offline-compatibility-foundation)
before connecting outputs. Declaration agreement remains separate from native execution.

![Optional tool connections: recover context, bound decisions, prove outcomes](docs/toolkit-stack.svg)

## Choose your own 90-second proof

Every project below is a standalone product. Install one, run its own disposable demo, inspect its
machine-readable result, and decide whether it is useful before you ever look at another repository.
The broader suite is an optional map for people who want to connect the outputs later.

Open a visual guide to see the shape of the tool. Its synthetic browser state is clearly labeled;
run the repo’s own CLI demo when you want actual local evidence. Every guide is hosted from its
own repository and remains a self-contained local HTML file.

![Standalone proof grid: install, demo, inspect](docs/standalone-proof-grid.svg)

| Project | Open the visual guide | Run it locally | The moment to watch |
| --- | --- | --- | --- |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | [Workbench](https://jonah-ux.github.io/forgeyard/) | [one-minute quickstart](https://github.com/jonah-ux/forgeyard/blob/main/docs/quickstart.md) | A review record seals, then refuses a tampered byte boundary. |
| [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) | [flight deck](https://jonah-ux.github.io/atlas-agent-runtime/flight-deck.html) | [standalone lifecycle](https://github.com/jonah-ux/atlas-agent-runtime/blob/main/docs/quickstart.md) | A task pauses for approval, recovers from its event log, and emits a receipt. |
| [Chatlens](https://github.com/jonah-ux/chatlens) | [session guide](https://jonah-ux.github.io/chatlens/walkthrough.html) | [quick start](https://github.com/jonah-ux/chatlens#quick-start) | A lost session becomes a searchable work card without a hosted service. |
| [Agent Proof](https://github.com/jonah-ux/agent-proof) | [proof chain](https://jonah-ux.github.io/agent-proof/walkthrough/) | [synthetic demo](https://github.com/jonah-ux/agent-proof#try-the-complete-workflow) | A proof bundle binds artifacts, graph edges, and tamper refusal together. |
| [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) | [admission explorer](https://jonah-ux.github.io/context-integrity-lab/admission-explorer.html) | [reviewer walkthrough](https://github.com/jonah-ux/context-integrity-lab/blob/main/DEMO.md) | Supported, stale, and out-of-scope context split into visible admission states. |
| [Sourcemark](https://github.com/jonah-ux/sourcemark) | [citation survival](https://jonah-ux.github.io/sourcemark/walkthrough.html) | [30-second demo](https://github.com/jonah-ux/sourcemark#install) | A citation keeps its anchor or gets called out when its source moves. |
| [Slipstream](https://github.com/jonah-ux/slipstream) | [vector inspector](https://jonah-ux.github.io/slipstream/inspector.html) | [local vector demo](https://github.com/jonah-ux/slipstream#install-and-run) | A nearest-neighbor query runs locally and leaves a manifest you can verify. |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | [preservation desk](https://jonah-ux.github.io/worktree-conservator/plan-explorer.html) | [preservation demo](https://github.com/jonah-ux/worktree-conservator#quick-start) | A cleanup plan can be refused, archived, verified, and restored without guessing. |
| [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit) | [trial scorecard](https://jonah-ux.github.io/agent-eval-kit/walkthrough.html) | [scorecard demo](https://github.com/jonah-ux/agent-eval-kit#try-it-in-30-seconds) | Repeated trials become a bounded comparison instead of a vibes-based ranking. |
| [Context Pack](https://github.com/jonah-ux/context-pack) | [budget inspector](https://jonah-ux.github.io/context-pack/walkthrough.html) | [deterministic pack demo](https://github.com/jonah-ux/context-pack#try-it-in-30-seconds) | A byte budget and digest make the exact context set inspectable. |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | [redaction guide](https://jonah-ux.github.io/agent-trace-lite/walkthrough.html) | [redacted trace demo](https://github.com/jonah-ux/agent-trace-lite#try-it-in-30-seconds) | A trace becomes a readable artifact while sensitive fields stay redacted. |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | [policy explanations](https://jonah-ux.github.io/agent-policy/walkthrough.html) | [policy quickstart](https://github.com/jonah-ux/agent-policy#quick-start) | A decision explains which rule matched and why the default is deny. |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | [capability matrix](https://jonah-ux.github.io/agent-sandbox-run/walkthrough.html) | [capability demo](https://github.com/jonah-ux/agent-sandbox-run#try-it-in-30-seconds) | The receipt says exactly what was enforced and what remained a fallback. |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | [handoff explorer](https://jonah-ux.github.io/agent-resume/walkthrough.html) | [continuation demo](https://github.com/jonah-ux/agent-resume#try-it-in-30-seconds) | A broken handoff turns into a validated next step with an explicit diff. |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | [manifest doctor](https://jonah-ux.github.io/mcp-doctor/walkthrough.html) | [contract check](https://github.com/jonah-ux/mcp-doctor#try-it-in-30-seconds) | A missing description or timeout fails closed with a stable diagnostic code. |

For the optional multi-repo story, see the [portfolio suite map](docs/PORTFOLIO-SUITE-V2.md). It
connects outputs after each repository already works on its own; it is never an installation
prerequisite.

For a terminal-level integration proof, run Forgeyard's
[reference-flow contract](https://github.com/jonah-ux/forgeyard/blob/main/docs/contracts/forgeyard-reference-flow-v1.md):
one local command exercises context admission, policy, bounded sandboxing, Atlas lifecycle, proof,
resume, and digest verification across passing, unknown-status, and tampered scenarios. The hosted
[Forgeyard Workbench](https://jonah-ux.github.io/forgeyard/) also exposes a 15-class adversarial
matrix covering stale, denied, unenforced, partial, malformed, traversal, leakage, drift, duplicate,
unbounded, false-completion, and tampered signals.

## The engineering loop

These tools explore one practical question: **can agent work be understood, bounded, proved, and continued?**

- **Recover context:** Chatlens turns local session stores into searchable, bounded work cards.
- **Check the interface:** MCP Doctor catches ambiguous tool contracts before an agent sees them.
- **Bound and run:** Context Pack, Agent Policy, and Agent Sandbox Run make inputs, permissions, and execution limits explicit.
- **Record and continue:** Agent Proof, Agent Trace Lite, and Agent Resume preserve evidence and continuation state.

Each repository contains its own install path, tests, demos, release notes, and security boundary. Start with the disposable demo before connecting a tool to a real workflow. The repositories describe what a check proves and what it cannot prove; a valid digest is not a claim of deployment, adoption, or a user-visible result.

For a runnable cross-project example, see the [public integration walkthrough](docs/INTEGRATION-WALKTHROUGH.md): Context Integrity Lab admits scoped, fresh context, Agent Proof normalizes and source-binds the result, and Forgeyard records the bounded review decision. The same walkthrough covers MCP Doctor contract checks, sandbox receipt scoring, loss-aware evidence envelopes, and Chatlens-to-Agent-Trace export while keeping source, release, and outcome claims separate.

## Public provenance

I publish the source, runnable fixtures, release information, and engineering notes so you can inspect the work. The ship log tracks source and release milestones. Small tools, big paper trails: I want the first run to be easy and the failure modes to be obvious.

[Engineering evidence](docs/ENGINEERING-EVIDENCE.md) · [Work samples](docs/WORK-SAMPLES.md) · [Ship log](docs/SHIPLOG.md)

Review the system like an outsider with the [threat model](docs/AGENT-SYSTEMS-LAB-THREAT-MODEL.md),
[external review packet](docs/EXTERNAL-REVIEW-PACKET.md), and
[maintainer runbook](docs/MAINTAINER-RUNBOOK.md). The [review lock](docs/AGENT-SYSTEMS-LAB-REVIEW-LOCK.json),
[audit matrix](docs/AGENT-SYSTEMS-LAB-AUDIT-MATRIX.md), [maintenance route](docs/AGENT-SYSTEMS-LAB-MAINTENANCE.md),
and [external review request draft](docs/EXTERNAL-REVIEW-REQUEST.md) link the public contracts,
exact source heads, reproducible commands, and known evidence limits.

Use the [failure-analysis walkthrough](docs/FAILURE-WALKTHROUGH.md) to follow a graph and packet
through their native verifiers, then inspect deliberate byte, orphan-edge, missing-input, and
stale-artifact refusals. Its runnable blocks use the existing review lock and are exercised by
the hosted review workflow.

Validate the lock and packet from a clean checkout with the dependency-free reviewer command:

```console
python3 scripts/validate_review_packet.py --json
# When updating the lock itself, also bind its published-head field to the containing parent:
python3 scripts/validate_review_packet.py --published-head <containing-profile-parent> --json
```

The validator checks the 13-owner count, repository identities, source heads bound to each packet
table row, recorded artifact digests and install outcomes, profile snapshot semantics, and the
explicit outside-review/adoption limitations. Malformed inputs return JSON with stable refusal
codes and exit `2`; valid inputs return exit `0`. Run the refusal regressions with
`python3 -m unittest discover -s tests -v` on Python 3.11 or later.

This command checks the recorded evidence metadata. It does not download artifact bytes, replay
installs, fetch owner repositories, or establish deployment, adoption, or production outcomes.

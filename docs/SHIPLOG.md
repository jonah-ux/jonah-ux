# Jonah Helland — public ship log

This is a short record of public engineering work that another developer can
verify. Each entry links to source, a release, CI, or a reproducible receipt.

## Verified public history

The public portfolio began on **2026-09-29**. These are the actual dates and
public commits; the history is intentionally not backfilled or re-dated.

| Date | Milestone | Public proof |
| --- | --- | --- |
| 2026-09-29 | Chatlens and Worktree Conservator source extraction began | [Chatlens history](https://github.com/jonah-ux/chatlens/commits/main) · [Worktree Conservator history](https://github.com/jonah-ux/worktree-conservator/commits/main) |
| 2026-09-30 | MCP Doctor and the seven supporting tools gained public packaging, demos, CI, and release workflows | [MCP Doctor history](https://github.com/jonah-ux/mcp-doctor/commits/main) · [portfolio evidence](PORTFOLIO-EVIDENCE.md) |
| 2026-09-30 | Profile README, hiring samples, evidence map, roadmap, and ship log were published | [profile history](https://github.com/jonah-ux/jonah-ux/commits/main) |
| 2026-10-01 | Release identity and built-consumer gates were propagated across the support tools | [latest profile evidence](PORTFOLIO-EVIDENCE.md) |
| 2026-10-01 | Worktree Conservator 0.2.0 prerelease shipped with independent archive readback | [release](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) · [merged PR](https://github.com/jonah-ux/worktree-conservator/pull/1) · [main commit](https://github.com/jonah-ux/worktree-conservator/commit/dc6acf64a3698e4d709b82b3653d4e92031b3021) |

GitHub contribution history should reflect this actual public work. Earlier
private or internal development is not presented as public open-source history.

## 2026-09-30 — release paths ready for the reliability toolkit

Added and linted the same semantic-tag release workflow across the eight
supporting tools:

- [MCP Doctor](https://github.com/jonah-ux/mcp-doctor)
- [Agent Eval Kit](https://github.com/jonah-ux/agent-eval-kit)
- [Agent Proof](https://github.com/jonah-ux/agent-proof)
- [Context Pack](https://github.com/jonah-ux/context-pack)
- [Agent Policy](https://github.com/jonah-ux/agent-policy)
- [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite)
- [Agent Resume](https://github.com/jonah-ux/agent-resume)
- [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run)

The workflow builds a wheel and source archive, writes `SHA256SUMS`, and
creates a GitHub prerelease only after an annotated semantic-version tag is
deliberately pushed. The workflow files pass `actionlint`; this historical
entry describes the release-path setup before the later public prerelease
objects were published.

Evidence: [portfolio evidence matrix](PORTFOLIO-EVIDENCE.md)

## 2026-10-01 — Worktree Conservator 0.2.0 prerelease

Added receipt-bound, read-only archive verification to the flagship worktree
tool. The release includes wheel and source artifacts, checksums, a disposable
demo that proves `verify` before restore, and fresh wheel/sdist consumer runs.

Evidence: [v0.2.0 prerelease](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) · [CI](https://github.com/jonah-ux/worktree-conservator/actions) · [release proof](PORTFOLIO-EVIDENCE.md)

## 2026-09-30 — public-main install matrix

Installed all eight supporting tools into fresh Python 3.14 environments and
ran each repository's documented disposable demo. The receipts cover stable
JSON schemas, bounded digests, explicit policy decisions, redacted traces,
identity validation, and honest sandbox enforcement state.

Evidence: [wave 2 install matrix](PORTFOLIO-EVIDENCE.md)

## 2026-09-30 — Agent Eval Kit help contract

The top-level `agent-eval --help` path now succeeds without requiring a
fixture or command. The CLI uses an explicit `run` subcommand, has a focused
test for the help contract, and still emits the same `agent-eval/v1` scorecard
from its disposable demo.

Evidence: [fix commit](https://github.com/jonah-ux/agent-eval-kit/commit/5b1ce5f) · [green CI run](https://github.com/jonah-ux/agent-eval-kit/actions/runs/36793852849)

## 2026-10-01 — release payload matrix

Built the wheel and source archive for every supporting tool from its current
public head, wrote a checksum manifest, and installed both artifacts into
fresh environments. Every artifact install passed its CLI help check. The
SPDX license metadata cleanup removed the shared setuptools deprecation warning
from the build output.

Evidence: `wave2-artifact-build-install-clean-20261001` completed with exit
code 0 and clean worker cleanup.

## 2026-10-01 — MCP Doctor release gates

MCP Doctor now refuses malformed, mismatched, lightweight, or moved tags. Its
release workflow verifies the package version, annotated tag identity, built
wheel/source payloads, and an installed consumer before publication. The
installed consumer checks the version, help contract, clean fixture, stable
MCP002/MCP004 diagnostics, and unreadable-input exit behavior.

Evidence: [release-gate commit](https://github.com/jonah-ux/mcp-doctor/commit/7e73d0d) · [green CI](https://github.com/jonah-ux/mcp-doctor/actions/runs/36795843101)

## 2026-10-01 — release gates propagated

The same tag identity and built-consumer checks now protect Agent Eval Kit,
Agent Proof, Agent Policy, Agent Trace Lite, Agent Resume, Agent Sandbox Run,
and Context Pack. Their latest CI runs are green. A separate bounded-source
branch remains preserved for later review and was not mixed into the public
release-gate change.

Evidence: [portfolio evidence matrix](PORTFOLIO-EVIDENCE.md)

## 2026-09-30 — Chatlens 0.1.0 prerelease

Chatlens now has a public GitHub prerelease with a wheel, source archive, and
`SHA256SUMS`. A clean Python 3.14 environment installed directly from the
public `v0.1.0` tag and returned `chatlens 0.1.0` with the expected CLI
commands.

Evidence: [release](https://github.com/jonah-ux/chatlens/releases/tag/v0.1.0) · [README demo](https://github.com/jonah-ux/chatlens#see-it-work)

## 2026-09-29 — agent reliability toolkit becomes composable

The profile now maps a single workflow across context recovery, bounded input,
policy decisions, sandbox receipts, proof bundles, and continuation records.
Each tool stays small, local-first, noninteractive, and explicit about what
it did not verify.

Evidence: [profile README](https://github.com/jonah-ux) · [one-minute work samples](WORK-SAMPLES.md)

## 2026-09-30 — profile visual system

Published the selected cool-tone workflow map as the profile hero and added
three small, accessible graphics that explain the portfolio at a glance:
the inspect/evaluate/prove/recover loop, the connected toolkit stack, and the
agent-friendly CLI contract. The images are stored in the repository so the
profile renders without a third-party design host.

Evidence: [profile README](https://github.com/jonah-ux) · `docs/profile-hero.png` · `docs/agent-loop.svg` · `docs/toolkit-stack.svg` · `docs/cli-contract.svg`

## 2026-09-30 — next open-source candidates

Screened existing work for a public-safe extraction path. The first greenlight
candidate is the reusable Slipstream local index engine; BreakTrace Lite is the
next candidate after synthetic-fixture and privacy work. Meeting Assistant and
the generic Agent Protocols edition remain qualified yellow candidates, while
customer integrations and operational experiment corpora stay private.

Evidence: [open-source pipeline](OPEN-SOURCE-PIPELINE.md)

## 2026-09-30 — Slipstream Core v0.1.0 prerelease

Extracted the provider-neutral local SQLite + `sqlite-vec` index core from the
larger private Slipstream work into a standalone public repository. The public
repo has an agent-friendly CLI, synthetic fixture, atomic build path, offline
self-test, Node 20/22/24 CI, an uploaded package tarball, and `SHA256SUMS`.
The uploaded tarball was downloaded by an independent consumer environment,
installed with its native dependency, and passed `slipstream self-test`.
Private registries, corpora, hooks, telemetry, credentials, customer data, and
internal adapters are excluded.

Evidence: [repository](https://github.com/jonah-ux/slipstream) · [v0.1.0 prerelease](https://github.com/jonah-ux/slipstream/releases/tag/v0.1.0) · [CI run](https://github.com/jonah-ux/slipstream/actions/runs/36815123917) · consumer proof `slipstream-consumer-selftest-20260930`

## 2026-10-01 — developer presence plan

Added a staged signup plan for the public surfaces that fit the portfolio:
LinkedIn, npm, PyPI, one technical writing home, Hugging Face, Product Hunt,
Docker Hub, and optional GitHub Sponsors. Each surface has a concrete trigger;
the plan explicitly avoids empty accounts, duplicate blogs, and package
publication before a stable release and consumer proof exist.

Evidence: [developer presence plan](DEVELOPER-PRESENCE.md)

## How to read this log

The log records public source and observed behavior. It does not count a commit
as a release, a demo as production adoption, or a historical claim as current
truth.


## 2026-10-01 — Agent Proof portable evidence readback

Agent Proof now reads its own exported gzip/tar bundles after the original artifact root is gone. The verifier rejects unsafe archive members, checks the manifest and document digests, reconstructs only declared source/artifact bytes, and reuses the v2 record/ledger/run verifier. The same mainline change adds a deterministic collector for recognized sibling envelopes.

Evidence: [merged PR](https://github.com/jonah-ux/agent-proof/pull/2) · [main commit](https://github.com/jonah-ux/agent-proof/commit/b3bb7b6fbcfa5464ad4bb366540bd5043974a275) · [CI](https://github.com/jonah-ux/agent-proof/actions) · [evidence matrix](PORTFOLIO-EVIDENCE.md)

The public install surface remains the earlier v0.1.1 prerelease until the next annotated release tag and asset readback exist.

## 2026-10-01 — Slipstream inspectable index readback

Slipstream main now exposes a read-only `inspect` command with the
`slipstream/inspect/v1` contract. It checks the vec0 dimension, item/vector
parity, missing and orphan rows, stable item identity digest, kind counts, and
redacted metadata digests. The offline self-test requires a successful inspect
readback, and a fresh npm `0.2.0` tarball consumer built the public fixture and
returned four indexed items with four matching vector rows.

Evidence: [merged PR](https://github.com/jonah-ux/slipstream/pull/1) · [main commit](https://github.com/jonah-ux/slipstream/commit/8a862991f8829f6e0115d2d79b15043ced03262a) · [CI](https://github.com/jonah-ux/slipstream/actions) · [v0.1.0 public prerelease](https://github.com/jonah-ux/slipstream/releases/tag/v0.1.0)

The public install surface remains v0.1.0 until the next annotated release tag and asset readback exist.

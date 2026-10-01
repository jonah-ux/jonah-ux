# Jonah Helland — public ship log

This is a short record of public engineering work that another developer can
verify. Each entry links to source, a release, CI, or a reproducible receipt.

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
deliberately pushed. The workflow files pass `actionlint`; no release tag is
claimed here until it exists publicly.

Evidence: [portfolio evidence matrix](PORTFOLIO-EVIDENCE.md)

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
Agent Proof, Agent Policy, Agent Trace Lite, Agent Resume, and Agent Sandbox
Run. Their latest CI runs are green. Context Pack has a separate bounded-source
branch under review, so its public `main` remains unchanged until that work is
resolved.

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

## How to read this log

The log records public source and observed behavior. It does not count a commit
as a release, a demo as production adoption, or a historical claim as current
truth.

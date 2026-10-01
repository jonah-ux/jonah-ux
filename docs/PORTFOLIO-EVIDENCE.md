# Public evidence matrix

Verification date: 2026-10-01

The baseline sweep installed each repository from its public `main` branch into
a fresh Python 3.14 virtual environment, checked top-level CLI help, and ran
the documented disposable demo. The sweep ran through `worker-lifecycle`
operation `wave2-current-head-final-matrix-20260930` with exit code 0 and clean
descendant cleanup. The advanced entries below add exact-head tests, package
hashes, and fresh downstream consumers for the projects changed in the second
pass; unchanged projects retain their explicit release boundaries.

| Repository | Installed CLI | Demo result |
| --- | --- | --- |
| [slipstream](https://github.com/jonah-ux/slipstream) | `slipstream 0.2.0` · [stable release](https://github.com/jonah-ux/slipstream/releases/tag/v0.2.0) | current main `5f455ef`; inspect/manifest/verify contracts include canonical row and metadata digests, little-endian stored vector identity, fail-closed tamper/output collision handling, finite-vector and ID validation, failed-rebuild preservation, the caller-owned vector integration example consumed through the package export, and packed-consumer CI verification; release target is the hardened main and the README documents the stable install surface |
| [chatlens](https://github.com/jonah-ux/chatlens) | `chatlens 0.2.2` · [stable release](https://github.com/jonah-ux/chatlens/releases/tag/v0.2.2) | current main `442d9f4`; recovery snapshot schemas, identity-drift refusal, and `chatlens-trace-envelope/v1` export/import now have 23 synthetic tests, compile proof, a fresh Agent Trace Lite consumer, and a public recovery trace roundtrip example; release remains v0.2.2 |
| [worktree-conservator](https://github.com/jonah-ux/worktree-conservator) | `worktree-conservator 0.2.0` · [stable release](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) | current main `7fd3550`; lifecycle `audit` reconciles archives, receipts, journals, and optional plan identity before recovery claims, the archive-verification boundary is isolated, and the disposable maintainer recovery example proves scan/plan/preserve/archive/audit/restore readback; hosted CI and fresh consumers remain visible |
| [forgeyard](https://github.com/jonah-ux/forgeyard) | `forgeyard 0.3.0` · [stable release](https://github.com/jonah-ux/forgeyard/releases/tag/v0.3.0) | merged main `d3fbd317`; `forgeyard-provenance-packet/v1` embeds exact record/receipt bytes, `compose` binds specialist report results without copying raw payloads, and verification fails closed on drift or unsafe paths; 22 tests, fresh 0.3.0 wheel/sdist consumers, and hosted release proof |
| [mcp-doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor 0.3.0` · [prerelease](https://github.com/jonah-ux/mcp-doctor/releases/tag/v0.3.0) | merged main `fa3b2f7`; clean and broken fixtures retain stable MCP002/MCP004 diagnostics; current main adds deterministic contract fingerprints, baseline added/removed/changed digests, warning-only drift, and `--fail-on-drift`; fresh wheel/sdist consumers reported 0.3.0, matched a saved baseline, and failed a changed description with MCP010 and exit 1; public v0.3.0 release workflow passed annotated-tag identity, wheel/sdist consumers, and checksum asset publication |
| [agent-eval-kit](https://github.com/jonah-ux/agent-eval-kit) | `agent-eval` · current `main` source candidate 0.3.0 | merged main `df736b3`; `agent-eval/receipt/v1` scores saved integrity-bound Agent Sandbox Run receipts without rerunning commands, with 9 tests, fresh wheel/sdist consumers, and receipt-integrity/expectation checks; public release remains v0.1.1 |
| [agent-proof](https://github.com/jonah-ux/agent-proof) | `agent-proof 0.2.0` · [stable release](https://github.com/jonah-ux/agent-proof/releases/tag/v0.2.0) | current main `f6dfa05` includes interop change `fe8c89b`; `agent-proof/interop/v1` and `interop-verify/v1` normalize redacted sibling envelopes with source-byte binding and fail-closed verification; 33 tests, fresh wheel/sdist consumers, and hosted macOS/Ubuntu proof |
| [context-pack](https://github.com/jonah-ux/context-pack) | `context-pack 0.1.1` · [prerelease](https://github.com/jonah-ux/context-pack/releases/tag/v0.1.1); current `main` source candidate 0.2.0 | merged main `e436a70`; `manifest/v1`, `verify/v1`, and `diff/v1` bind bounded source packs to deterministic file digests with atomic writes and symlink/hardlink protections; 14 tests and fresh wheel/sdist cross-consumer diff proof |
| [agent-policy](https://github.com/jonah-ux/agent-policy) | `agent-policy 0.1.1` · [prerelease](https://github.com/jonah-ux/agent-policy/releases/tag/v0.1.1); current `main` source candidate 0.2.0 | merged main `cc5ee7d`; ordered policy composition rejects duplicate rule IDs and explain receipts bind normalized policy/request digests, positions, and decision source; 11 tests, lint, build, and fresh wheel/sdist consumers |
| [agent-trace-lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace-lite 0.1.1` · [prerelease](https://github.com/jonah-ux/agent-trace-lite/releases/tag/v0.1.1); current `main` source candidate 0.2.0 | merged main `5660935`; strict JSONL traces now expose raw-source and canonical-redacted digests, recursive token redaction, line-aware parse errors, `inspect`, and bounded `query`; fresh wheel/sdist consumers and malformed-input probe passed |
| [agent-resume](https://github.com/jonah-ux/agent-resume) | `agent-resume 0.1.1` · [prerelease](https://github.com/jonah-ux/agent-resume/releases/tag/v0.1.1); current `main` source candidate 0.2.0 | merged main `1f0edf7`; continuation records now carry canonical fingerprints, required-integrity validation, bounded `inspect`/`render`, and redacted `diff`; 4 tests and fresh wheel consumer proof |
| [agent-sandbox-run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox-run 0.1.1` · [prerelease](https://github.com/jonah-ux/agent-sandbox-run/releases/tag/v0.1.1); current `main` source candidate 0.2.0 | merged main `ff1c9b2`; v2 receipts bind command/output/receipt digests, bounded output, cwd/root, explicit timeout, and actual bubblewrap enforcement; 3 tests and fresh wheel consumer proof |

MCP Doctor and seven supporting repositories now carry the strengthened `.github/workflows/release.yml`: a semantic-version tag must match the package version and annotated HEAD, build wheel/source assets, verify both consumers, write `SHA256SUMS`, and only then create a GitHub prerelease. All eight workflow files pass `actionlint`; MCP Doctor v0.3.0 is now a published prerelease.

This matrix records public source, prerelease objects, hosted checks, and bounded consumer evidence as separate signals. A prerelease is not presented as a stable package or PyPI publication.

The release payloads have also been built and consumed independently from the
current public heads: each repository produced a wheel, source archive, and
`SHA256SUMS`, then installed both artifacts into fresh environments. The
receipt is worker operation `wave2-artifact-build-install-clean-20261001`,
which completed successfully with clean cleanup and no license-deprecation
warnings.

Hosted CI is also green for all eight of those exact heads after the SPDX
metadata cleanup.

Seven supporting repositories now also verify annotated tag identity, package version matching, wheel/source consumer help, and `gh release create --verify-tag` before publication. A separate local bounded-source branch remains preserved for later review; it was not mixed into this release-gate change.

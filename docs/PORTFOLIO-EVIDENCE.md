# Public evidence matrix

Verification date: 2026-10-02

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
| [chatlens](https://github.com/jonah-ux/chatlens) | `chatlens 0.3.0` · [stable release](https://github.com/jonah-ux/chatlens/releases/tag/v0.3.0) | current main `0b4ce8e`; recovery snapshot schemas, identity-drift refusal, and `chatlens-trace-envelope/v1` export/import now have 23 synthetic tests, fresh wheel/sdist consumers, recovery roundtrip and trace-import proof, and independent downloaded-asset checksum readback; v0.3.0 is the stable release |
| [worktree-conservator](https://github.com/jonah-ux/worktree-conservator) | `worktree-conservator 0.2.0` · [stable release](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) | current main `7fd3550`; lifecycle `audit` reconciles archives, receipts, journals, and optional plan identity before recovery claims, the archive-verification boundary is isolated, and the disposable maintainer recovery example proves scan/plan/preserve/archive/audit/restore readback; hosted CI and fresh consumers remain visible |
| [forgeyard](https://github.com/jonah-ux/forgeyard) | `forgeyard 0.3.0` · [stable release](https://github.com/jonah-ux/forgeyard/releases/tag/v0.3.0) | merged main `d3fbd317`; `forgeyard-provenance-packet/v1` embeds exact record/receipt bytes, `compose` binds specialist report results without copying raw payloads, and verification fails closed on drift or unsafe paths; 22 tests, fresh 0.3.0 wheel/sdist consumers, and hosted release proof |
| [mcp-doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor 0.3.0` · [prerelease](https://github.com/jonah-ux/mcp-doctor/releases/tag/v0.3.0) | current main `fa3b2f7`; clean and broken fixtures retain stable MCP002/MCP004 diagnostics; current main adds deterministic contract fingerprints, baseline added/removed/changed digests, warning-only drift, and `--fail-on-drift`; independent downloaded wheel/sdist consumers passed version/help and checksum readback in `portfolio-release-download-consumers-20261002-v3`; stable promotion remains gated |
| [agent-eval-kit](https://github.com/jonah-ux/agent-eval-kit) | `agent-eval 0.3.0` · [prerelease](https://github.com/jonah-ux/agent-eval-kit/releases/tag/v0.3.0) | current main `df736b3`; `agent-eval/receipt/v1` scores saved integrity-bound Agent Sandbox Run receipts without rerunning commands, with 9 tests, fresh main and downloaded-release wheel/sdist consumers, checksums, and receipt-integrity/expectation checks |
| [agent-proof](https://github.com/jonah-ux/agent-proof) | `agent-proof 0.2.0` · [stable release](https://github.com/jonah-ux/agent-proof/releases/tag/v0.2.0) | current main `f6dfa05` includes interop change `fe8c89b`; `agent-proof/interop/v1` and `interop-verify/v1` normalize redacted sibling envelopes with source-byte binding and fail-closed verification; 33 tests, fresh wheel/sdist consumers, and hosted macOS/Ubuntu proof |
| [context-pack](https://github.com/jonah-ux/context-pack) | `context-pack 0.2.0` · [prerelease](https://github.com/jonah-ux/context-pack/releases/tag/v0.2.0) | current main `e436a70`; `manifest/v1`, `verify/v1`, and `diff/v1` bind bounded source packs to deterministic file digests with atomic writes and symlink/hardlink protections; 14 tests, fresh main consumers, downloaded-release wheel/sdist consumers, and checksums |
| [agent-policy](https://github.com/jonah-ux/agent-policy) | `agent-policy 0.2.0` · [prerelease](https://github.com/jonah-ux/agent-policy/releases/tag/v0.2.0) | current main `cc5ee7d`; ordered policy composition rejects duplicate rule IDs and explain receipts bind normalized policy/request digests, positions, and decision source; 11 tests, lint, build, fresh main consumers, downloaded-release wheel/sdist consumers, and checksums |
| [agent-trace-lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace-lite 0.2.0` · [prerelease](https://github.com/jonah-ux/agent-trace-lite/releases/tag/v0.2.0) | current main `5660935`; strict JSONL traces expose raw-source and canonical-redacted digests, recursive token redaction, line-aware parse errors, `inspect`, and bounded `query`; fresh main consumers, downloaded-release wheel/sdist consumers, malformed-input probe, and checksums |
| [agent-resume](https://github.com/jonah-ux/agent-resume) | `agent-resume 0.2.0` · [prerelease](https://github.com/jonah-ux/agent-resume/releases/tag/v0.2.0) | current main `1f0edf7`; continuation records carry canonical fingerprints, required-integrity validation, bounded `inspect`/`render`, and redacted `diff`; fresh main consumers, downloaded-release wheel/sdist consumers, and checksums |
| [agent-sandbox-run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox-run 0.2.0` · [prerelease](https://github.com/jonah-ux/agent-sandbox-run/releases/tag/v0.2.0) | current main `ff1c9b2`; v2 receipts bind command/output/receipt digests, bounded output, cwd/root, explicit timeout, and actual bubblewrap enforcement; fresh main consumers, downloaded-release wheel/sdist consumers, checksums, and downstream Agent Eval receipt scoring |

MCP Doctor and seven supporting repositories now carry the strengthened `.github/workflows/release.yml`: a semantic-version tag must match the package version and annotated HEAD, build wheel/source assets, verify both consumers, write `SHA256SUMS`, and only then create a GitHub prerelease. All eight workflow files pass `actionlint`; MCP Doctor v0.3.0 and the six new candidate releases are published prereleases, while Chatlens v0.3.0 is stable.

This matrix records public source, prerelease objects, hosted checks, and bounded consumer evidence as separate signals. A prerelease is not presented as a stable package or PyPI publication.

The release payloads have also been downloaded and consumed independently from
the public release objects. Operation `portfolio-release-download-consumers-20261002-v3`
verified every wheel and source archive against `SHA256SUMS`, then installed
both artifacts into fresh Python 3.12 environments and checked each CLI help
contract. Chatlens v0.3.0 is stable; MCP Doctor v0.3.0 and the six new
supporting releases remain prereleases.

| Release | Wheel SHA-256 | Sdist SHA-256 | Readback |
| --- | --- | --- | --- |
| Chatlens v0.3.0 stable | `9807d88834c7140c133b1237584d3805cb395a9dce4dcd3935b9e107f5c1ff5b` | `dbdc371e440c1abdfd586bd9a316fd466cf75fe8c91adfff36994380e98f08a9` | fresh Python 3.12 wheel/sdist consumers, checksum match |
| MCP Doctor v0.3.0 prerelease | `64631aa679f090403e2387a05f70c56ddab8351e2dd0ddcbe2cd2e4b7eccffa7` | `f5866d0c87b8168a9630bab613bd91b82165767e71dac6336e08ff56098d3f5d` | fresh Python 3.12 wheel/sdist consumers, checksum match |
| Agent Eval Kit v0.3.0 prerelease | `e26e92a501957cb6d15ce4e67adc758c8278629f12c189b049959e766da52683` | `891865ed14c76bbd054699a308971d9ba0dafb367abd91a2f25efb77cd8e9c94` | fresh Python 3.12 wheel/sdist consumers, checksum match |
| Context Pack v0.2.0 prerelease | `d9a4f08910e3d9ac30ee971faa965e892ca4b4bc7b74e0fa4303bd1146a4d14e` | `06daf19bb3b57dbef49ef1b423cdc1867da2c46edc655e7e616bcd4ce12e97ed` | fresh Python 3.12 wheel/sdist consumers, checksum match |
| Agent Policy v0.2.0 prerelease | `d9ddae12850ed95c4e8e17d016d26e53fde452950ac25c92a04bb3c62c2049fa` | `b684b6700c0db7e9229d012e3d06d851df84c1c34dbfb3a690784f4132f431be` | fresh Python 3.12 wheel/sdist consumers, checksum match |
| Agent Trace Lite v0.2.0 prerelease | `bd2956ce849778a871deb9be589c4fe34cbd7ff963fb73dc47d310840e4ce4e0` | `2fffd62ce7d3cc6bec60400db64d80d4bc330bb1eb6d79911ed61ab8e0effba3` | fresh Python 3.12 wheel/sdist consumers, checksum match |
| Agent Resume v0.2.0 prerelease | `205ac99213bd326334a95163aa0745d6fb90e0a64e9d164e0875ed739928b570` | `79cefea2bec2fe3585e77f4203a0dce70d92fca8878019ebfeafbd7ce0626096` | fresh Python 3.12 wheel/sdist consumers, checksum match |
| Agent Sandbox Run v0.2.0 prerelease | `2b51a7d7286b9316fddd8a431fb8c246a287c03ab645cc0bef23e74ab48e2733` | `12aa0448e70fa3cc65de00fc4b51ff58aa3a37ad4f7c551cd504aa4f453cf8ae` | fresh Python 3.12 wheel/sdist consumers, checksum match |

Hosted CI is also green for all eight of those exact heads after the SPDX
metadata cleanup.

Seven supporting repositories now also verify annotated tag identity, package version matching, wheel/source consumer help, and `gh release create --verify-tag` before publication. A separate local bounded-source branch remains preserved for later review; it was not mixed into this release-gate change.

# Public evidence matrix

Verification date: 2026-10-01

Each repository was installed from its public `main` branch into a fresh Python 3.14 virtual environment, its top-level CLI help was checked, and its documented `demos/demo.py` was run. The final current-head command ran through `worker-lifecycle` operation `wave2-current-head-final-matrix-20260930` and completed with exit code 0 and clean descendant cleanup.

| Repository | Installed CLI | Demo result |
| --- | --- | --- |
| [slipstream](https://github.com/jonah-ux/slipstream) | `slipstream 0.1.0` · [prerelease](https://github.com/jonah-ux/slipstream/releases/tag/v0.1.0) | downloaded package tarball, checksum, independent consumer install/self-test, and Node 20/22/24 CI at the reviewed public head |
| [chatlens](https://github.com/jonah-ux/chatlens) | `chatlens 0.1.0` · [prerelease](https://github.com/jonah-ux/chatlens/releases/tag/v0.1.0) | public tag, wheel/sdist/checksums, and fresh consumer proof at the reviewed release head |
| [worktree-conservator](https://github.com/jonah-ux/worktree-conservator) | `worktree-conservator 0.2.0` · [prerelease](https://github.com/jonah-ux/worktree-conservator/releases/tag/v0.2.0) | merged main `dc6acf6`; public CI, wheel/sdist/checksums, independent `verify` demo readback, and fresh wheel/sdist consumers |
| [mcp-doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor 0.2.4` · [prerelease](https://github.com/jonah-ux/mcp-doctor/releases/tag/v0.2.4) | clean contract passes; broken fixture emits MCP002/MCP004 findings; annotated tag, wheel/sdist consumer, and release workflow green at `b3e6ab3` |
| [agent-eval-kit](https://github.com/jonah-ux/agent-eval-kit) | `agent-eval` | `agent-eval/v1`, `ok: true`, exit code 0; top-level `--help` succeeds; release identity gates and CI green at `4887445` |
| [agent-proof](https://github.com/jonah-ux/agent-proof) | `agent-proof` | `agent-proof/v1` envelope with explicit `observed: false`; release identity gates and CI green at `589dd97` |
| [context-pack](https://github.com/jonah-ux/context-pack) | `context-pack` | bounded file list, byte count, and SHA-256 digest; release identity gates and CI green at `8b0a9e2` |
| [agent-policy](https://github.com/jonah-ux/agent-policy) | `agent-policy` | `agent-policy/v1` allow decision with reason; release identity gates and CI green at `7e1d504` |
| [agent-trace-lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace` | `agent-trace/v1` HTML artifact with two events; release identity gates and CI green at `d0e54c1` |
| [agent-resume](https://github.com/jonah-ux/agent-resume) | `agent-resume` | valid `agent-resume/validation/v1` continuation record; release identity gates and CI green at `c2408d5` |
| [agent-sandbox-run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox` | `agent-sandbox/v1` receipt with `enforced: false` honestly reported; release identity gates and CI green at `f54dda7` |

MCP Doctor and seven supporting repositories now carry the strengthened `.github/workflows/release.yml`: a semantic-version tag must match the package version and annotated HEAD, build wheel/source assets, verify both consumers, write `SHA256SUMS`, and only then create a GitHub prerelease. All eight workflow files pass `actionlint`; no tag was pushed as part of this evidence pass.

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

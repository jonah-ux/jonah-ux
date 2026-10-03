# Agent Systems Lab audit matrix

This matrix is the clean-machine maintenance route for the public P4 audit wave. Run each command
from a fresh `main` clone, retain the JSON receipt beside the source-head readback, and treat
`artifact_audit.state=unavailable` as an explicit limitation when no distribution directory was
provided. A static `pass` covers only the named dependency, license, release-marker, and high-signal
privacy checks.

| Owner | Audit schema | Command | Artifact boundary |
| --- | --- | --- | --- |
| Forgeyard | `forgeyard-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Agent Proof | `agent-proof-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Atlas Agent Runtime | `atlas-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| ChatLens | `chatlens-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Agent Policy | `agent-policy-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Agent Sandbox Run | `agent-sandbox-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Sourcemark | `sourcemark-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Slipstream | `slipstream-public-audit/v1` | `node scripts/audit_public_surface.js --json` | `unavailable` without `--dist-dir` |
| Worktree Conservator | `worktree-conservator-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Agent Resume | `agent-resume-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Agent Trace Lite | `agent-trace-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| MCP Doctor | `mcp-doctor-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |
| Context Integrity Lab | `context-integrity-public-audit/v1` | `python scripts/audit_public_surface.py --json` | `unavailable` without `--dist-dir` |

Every owner audit includes a synthetic high-signal secret refusal and checksum-mismatch refusal
test. Slipstream additionally has a fresh packed artifact receipt with `artifact_audit=pass`.
Forgeyard's published artifact audit is recorded separately in the platform ledger. The remaining
owners expose artifact state as unavailable until a distribution directory is intentionally supplied.

These receipts do not prove provider-side controls, complete DLP, deployment, production security,
outside review, or adoption. Those states stay unknown or unavailable until directly observed.

# Agent Systems Lab conformance matrix

This matrix is the public owner map for the current conformance wave. Each
repository keeps its native schema and test runner. The manifests point to the
existing Agent Proof interop owner where a normalized handoff is needed; no
repository imports another at runtime and no second registry is introduced.

| Owner | Native boundary | Public conformance artifact | Current proof |
| --- | --- | --- | --- |
| [Forgeyard](https://github.com/jonah-ux/forgeyard) | `ai-work-evidence/v1`, `forgeyard-compose/v1`, `forgeyard-provenance-packet/v1`, `forgeyard-runtime-evaluation/v1` | [Corpus and runner](https://github.com/jonah-ux/forgeyard/tree/main/conformance), [v0.5.1 prerelease](https://github.com/jonah-ux/forgeyard/releases/tag/v0.5.1) | Nineteen executed native cases with controls; separate static fifteen-label Workbench catalogue; fresh wheel/source consumers; six-operation latency and Python-allocation observations |
| [ChatLens](https://github.com/jonah-ux/chatlens) | `chatlens-trace-envelope/v1`, shared evidence projection | [Owner declaration](https://github.com/jonah-ux/chatlens/blob/45b95cd038929ee325558de0617825c3d6171836/conformance/agent-systems-lab.json), [consumer conformance](https://github.com/jonah-ux/chatlens/blob/main/tests/test_conformance.py) | Native source declaration and independent producer tests; complete/partial trace status and owner corpus pin |
| [Atlas Agent Runtime](https://github.com/jonah-ux/atlas-agent-runtime) | `atlas-receipt/v1`, shared evidence projection | [Owner declaration](https://github.com/jonah-ux/atlas-agent-runtime/blob/33daa4f23633239bc651b51f21229dd3109ce375/conformance/agent-systems-lab.json), [consumer conformance](https://github.com/jonah-ux/atlas-agent-runtime/blob/main/tests/test_conformance.py) | Native source declaration and independent producer tests; completed/queued/failed lifecycle status and owner corpus pin |
| [Agent Proof](https://github.com/jonah-ux/agent-proof) | `agent-proof/interop/v1`, `agent-proof/graph/v1`, `agent-systems-lab/compatibility/v1`, `agent-proof-lab-conformance/v1` | [Interop registry](https://github.com/jonah-ux/agent-proof/blob/main/conformance/agent-systems-lab.json), [compatibility charter](https://github.com/jonah-ux/agent-proof/blob/main/conformance/compatibility-v1.json) | Reviewed native adapters, semantic graph verification, structural charter rules, and immutable owner pins |
| [Context Integrity Lab](https://github.com/jonah-ux/context-integrity-lab) | `context-integrity/v1` | [Owner manifest](https://github.com/jonah-ux/context-integrity-lab/blob/main/conformance/agent-systems-lab.json) | Supported, wrong-scope, stale, uncertain, unavailable-source, citation, and unknown-state tests |
| [Agent Policy](https://github.com/jonah-ux/agent-policy) | `agent-policy/receipt/v1`; legacy `agent-policy/v1` fixtures remain explicit | [Owner manifest](https://github.com/jonah-ux/agent-policy/blob/main/conformance/agent-systems-lab.json) | Native CLI receipt, allow/deny/default-deny, digest, traversal, version, and privacy-boundary tests |
| [Agent Sandbox Run](https://github.com/jonah-ux/agent-sandbox-run) | `agent-sandbox/v2` | [Owner manifest](https://github.com/jonah-ux/agent-sandbox-run/blob/main/conformance/agent-systems-lab.json) | Backend/enforcement disclosure, command/receipt digest, bounded-output, and timeout tests |
| [Agent Resume](https://github.com/jonah-ux/agent-resume) | `agent-resume/v1` | [Owner manifest](https://github.com/jonah-ux/agent-resume/blob/main/conformance/agent-systems-lab.json) | Fingerprint, identity, tamper-refusal, and field/digest-only diff tests |
| [Agent Trace Lite](https://github.com/jonah-ux/agent-trace-lite) | `agent-trace/v1`, `agent-trace/inspect/v1` | [Owner manifest](https://github.com/jonah-ux/agent-trace-lite/blob/main/conformance/agent-systems-lab.json) | Redaction, raw/redacted digest, safe query, malformed JSONL, and non-object refusal tests |
| [MCP Doctor](https://github.com/jonah-ux/mcp-doctor) | `mcp-doctor/v1` | [Owner manifest](https://github.com/jonah-ux/mcp-doctor/blob/main/conformance/agent-systems-lab.json) | Clean, warning, strict, baseline drift, malformed input, and stable diagnostic-code tests |
| [Worktree Conservator](https://github.com/jonah-ux/worktree-conservator) | `worktree-conservator.result/v1` | [Owner manifest](https://github.com/jonah-ux/worktree-conservator/blob/main/conformance/agent-systems-lab.json) | Disposable scan/plan/apply/verify/audit/restore lifecycle; refusal codes remain owner tests |
| [Slipstream](https://github.com/jonah-ux/slipstream) | `slipstream/query/v1`, `inspect/v1`, `manifest/v1`, `verify/v1` | [Owner manifest](https://github.com/jonah-ux/slipstream/blob/main/conformance/agent-systems-lab.json) | Node self-test proves local query, inspect, deterministic manifest, and tamper-refusing verify |
| [Sourcemark](https://github.com/jonah-ux/sourcemark) | `sourcemark/check/v1` citation boundary | [Owner manifest](https://github.com/jonah-ux/sourcemark/blob/main/conformance/agent-systems-lab.json) | Separate bounded citation/source evidence; native semantics remain owned by Sourcemark |

The matrix proves source-level conformance surfaces and independent local
behavior. It does not claim that every repository is deployed together, that an
external user has adopted the suite, or that a valid receipt proves a
production outcome. For the reproducible install and review sequence, use the
[cold-review checklist](COLD-REVIEW-CHECKLIST.md).

The currently released compatibility checker validates charter structure and adapter-registry
agreement. It does not yet consume pinned participant bytes or negotiate native supported versions.
Those extensions remain in progress. The new Atlas/ChatLens JSON declarations are public source
metadata with producer-test coverage, not claims of a new native package release or runtime adoption.

For semantic graph and packet refusal examples, use the [failure walkthrough](FAILURE-WALKTHROUGH.md).
For a focused contribution, use the [maintainer and contributor route](MAINTAINER-RUNBOOK.md).

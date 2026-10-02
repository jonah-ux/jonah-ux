#!/usr/bin/env bash
set -euo pipefail

: "${CHATLENS_ROOT:?Set CHATLENS_ROOT to a Chatlens checkout at a released tag}"
: "${SLIPSTREAM_ROOT:?Set SLIPSTREAM_ROOT to a Slipstream checkout at a released tag}"
: "${AGENT_PROOF_ROOT:?Set AGENT_PROOF_ROOT to an Agent Proof checkout at a released tag; it is installed as the runtime consumer}"
: "${WORKTREE_ROOT:?Set WORKTREE_ROOT to a Worktree Conservator checkout at a released tag; it is installed as the runtime consumer}"
: "${FORGEYARD_ROOT:?Set FORGEYARD_ROOT to a Forgeyard checkout at a released tag; it is installed as the runtime consumer}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
NODE_BIN="${NODE_BIN:-node}"

workdir="$(mktemp -d "${TMPDIR:-/tmp}/agent-reliability-stack.XXXXXX")"
trap 'rm -rf "$workdir"' EXIT
mkdir -p "$workdir/artifacts"
chmod 700 "$workdir/artifacts"

# 1. Chatlens produces a portable, redacted recovery envelope.
CHATLENS_ROOT="$CHATLENS_ROOT" "$PYTHON_BIN" - "$workdir" <<'PY'
import json, os, sys
from pathlib import Path
from chatlens import build_trace, import_report, read_trace, validate_trace, write_trace
from chatlens.model import ASSISTANT, USER, Event, Thread
out = Path(sys.argv[1])
thread = Thread("codex", "portfolio-session-001", "portfolio-demo", "synthetic/session.jsonl", title="Recover release context", origin="human")
events = [
    Event(1727812800, USER, "Find the release verification result.", extra={"email": "demo@example.invalid"}),
    Event(1727812801, ASSISTANT, "The release check completed and is ready for review."),
]
envelope = build_trace("codex", thread, events, [], "portfolio-demo")
trace_path = out / "artifacts" / "recovery.trace.jsonl"
write_trace(trace_path, envelope)
loaded = read_trace(trace_path)
valid, errors, _ = validate_trace(loaded)
report = import_report(loaded)
json.dump({"schema": "portfolio/chatlens/v1", "ok": valid and not errors and report["trace_state"] == "matched", "trace": str(trace_path), "report": report}, open(out / "artifacts" / "chatlens.json", "w"), sort_keys=True)
if not valid or errors or report["trace_state"] != "matched": raise SystemExit("Chatlens verification failed")
PY

# 2. Slipstream indexes facts extracted from the recovery envelope and verifies the index.
# Rebuild the native binding for the consumer's active Node runtime; a downloaded
# release is not portable across Node ABI versions without this explicit step.
(cd "$SLIPSTREAM_ROOT" && "$NODE_BIN" -e 'process.exit(0)' && npm rebuild better-sqlite3 >/dev/null)
cat > "$workdir/items.json" <<'JSON'
[
  {"id":"release-check","kind":"recovery","name":"Release check completed","meta":{"source":"chatlens"},"vector":[1,0,0,0]},
  {"id":"review-handoff","kind":"recovery","name":"Review handoff ready","meta":{"source":"forgeyard"},"vector":[0,1,0,0]}
]
JSON
(cd "$SLIPSTREAM_ROOT" && "$NODE_BIN" bin/slipstream.js build --input="$workdir/items.json" --db="$workdir/index.db" --dim=4 > "$workdir/artifacts/slipstream-build.json")
(cd "$SLIPSTREAM_ROOT" && "$NODE_BIN" bin/slipstream.js query --db="$workdir/index.db" --vector=0.98,0.02,0,0 --k=1 > "$workdir/artifacts/slipstream-query.json")
(cd "$SLIPSTREAM_ROOT" && "$NODE_BIN" bin/slipstream.js manifest --db="$workdir/index.db" --out="$workdir/artifacts/slipstream.manifest.json" > "$workdir/artifacts/slipstream-manifest.json")
(cd "$SLIPSTREAM_ROOT" && "$NODE_BIN" bin/slipstream.js verify --db="$workdir/index.db" --manifest="$workdir/artifacts/slipstream.manifest.json" > "$workdir/artifacts/slipstream-verify.json")

# 3. Agent Proof binds the recovery and retrieval artifacts to one observed run.
cat > "$workdir/spec.json" <<JSON
{
  "run_id": "portfolio-stack-demo",
  "actor": "portfolio-demo",
  "repository": {"url": "https://github.com/jonah-ux", "branch": "main", "commit": "0123456789abcdef0123456789abcdef01234567"},
  "operation": {"argv": ["portfolio-stack-demo.sh"], "cwd": "$workdir"},
  "result": {"exit_code": 0, "observed": true, "partial": false, "unknowns": [], "stdout": "stack workflow completed", "stderr": ""},
  "sources": ["artifacts/chatlens.json", "artifacts/slipstream-query.json", "artifacts/slipstream-verify.json"],
  "artifacts": [
    {"path": "artifacts/recovery.trace.jsonl", "label": "Chatlens recovery envelope"},
    {"path": "artifacts/slipstream.manifest.json", "label": "Slipstream index manifest"},
    {"path": "artifacts/slipstream-verify.json", "label": "Slipstream verification"}
  ],
  "notes": ["Synthetic disposable cross-project workflow; no real transcript store or repository is read."]
}
JSON
"$PYTHON_BIN" -m agent_proof.cli record "$workdir/spec.json" --artifact-root "$workdir" --out "$workdir/artifacts/agent-proof.json" > "$workdir/artifacts/agent-proof-record.json"
"$PYTHON_BIN" -m agent_proof.cli verify "$workdir/artifacts/agent-proof.json" --artifact-root "$workdir" --require-observed --require-artifacts > "$workdir/artifacts/agent-proof-verify.json"

# 4. Worktree Conservator proves archive, independent verification, audit, and restore.
"$PYTHON_BIN" -m worktree_conservator.cli demo --json > "$workdir/artifacts/worktree.json"
"$PYTHON_BIN" - "$workdir/artifacts/worktree.json" "$workdir/artifacts/worktree-report.json" <<'PY'
import json, sys
raw = json.load(open(sys.argv[1]))
data = raw.get("data", raw)
report = {"schema": "portfolio/worktree/v1", "ok": bool(raw.get("ok") and data.get("verified") and data.get("restored")), "result": data}
json.dump(report, open(sys.argv[2], "w"), sort_keys=True)
if not report["ok"]: raise SystemExit("Worktree Conservator verification failed")
PY

# 5. Forgeyard composes the specialist outputs into a reviewable decision.
"$PYTHON_BIN" -m forgeyard.cli compose \
  --task-id portfolio-stack-demo \
  --repository jonah-ux/agent-reliability-stack \
  --request "review disposable recovery and evidence workflow" \
  --input chatlens="$workdir/artifacts/chatlens.json" \
  --input slipstream="$workdir/artifacts/slipstream-verify.json" \
  --input proof="$workdir/artifacts/agent-proof-verify.json" \
  --input worktree="$workdir/artifacts/worktree-report.json" \
  --output "$workdir/artifacts/forgeyard.json" > "$workdir/artifacts/forgeyard-compose.json"
forgeyard_sha="$($PYTHON_BIN -c 'import json,sys; print(json.load(open(sys.argv[1]))["sha256"])' "$workdir/artifacts/forgeyard-compose.json")"
"$PYTHON_BIN" -m forgeyard.cli verify "$workdir/artifacts/forgeyard.json" --sha256 "$forgeyard_sha" > "$workdir/artifacts/forgeyard-verify.json"

"$PYTHON_BIN" - "$workdir" <<'PY'
import json, sys
from pathlib import Path
root = Path(sys.argv[1]) / "artifacts"
def load(name): return json.loads((root / name).read_text())
slip = load("slipstream-query.json")
proof = load("agent-proof-verify.json")
work = load("worktree.json").get("data", load("worktree.json"))
forge = load("forgeyard-verify.json")
result = {
  "schema": "portfolio/agent-reliability-stack/v1",
  "chatlens": load("chatlens.json")["ok"],
  "slipstream_nearest": slip["results"][0]["id"],
  "slipstream_verified": load("slipstream-verify.json")["ok"],
  "agent_proof_verified": proof["ok"],
  "worktree_verified": work["verified"],
  "worktree_restored": work["restored"],
  "forgeyard_ready": forge["status"] == "ready_for_review",
}
print(json.dumps(result, sort_keys=True, indent=2))
if not all([result["chatlens"], result["slipstream_verified"], result["agent_proof_verified"], result["worktree_verified"], result["worktree_restored"], result["forgeyard_ready"]]):
    raise SystemExit(1)
PY

# Agent Systems Lab maintenance route

Run this route after a public owner release, a conformance/adapter change, a profile packet change,
or on the scheduled review cadence. The route is intentionally read-first and leaves production,
provider, and customer systems untouched.

## Source freshness

1. Read `docs/AGENT-SYSTEMS-LAB-REVIEW-LOCK.json` as the frozen review snapshot.
2. Run `git ls-remote https://github.com/OWNER/REPO.git refs/heads/main` for every owner.
3. Compare the live heads with the lock. A changed head is `needs-rerun`, not an implicit pass.
4. Update the lock only after the corresponding fresh consumer or audit receipt has been rerun.

## Audit and artifact checks

1. Clone each owner at the intended head in a disposable directory.
2. Run the command in `docs/AGENT-SYSTEMS-LAB-AUDIT-MATRIX.md`.
3. Supply `--dist-dir dist` only when the distribution and `SHA256SUMS` belong to the same reviewed
   source/release boundary.
4. Preserve static pass, artifact pass, artifact unavailable, blocked, and refusal states exactly.
5. Re-run the relevant installed/reference flow after changing an owner pin or release lock.

## Walkthrough and packet checks

1. Run Forgeyard passing, blocked, and tampered reference-flow fixtures.
2. Run the graph mutation/refusal path and the bounded evaluation receipt.
3. Run the fifteen-minute route from `docs/EXTERNAL-REVIEW-PACKET.md` on a clean machine or
   disposable environment.
4. Verify that the packet, audit matrix, threat model, lock, and maintenance route point to the same
   owner-head observations.
5. Record any independent reviewer response in the feedback format from
   `docs/EXTERNAL-REVIEW-REQUEST.md`.

## Packet consistency gate

Run `python3 scripts/validate_review_packet.py --json` after editing the lock or packet, and
`python3 -m unittest discover -s tests -v` after changing the validator. The gate binds each
repository to its source-head table row and requires complete recorded checksum, artifact-set,
build/audit, runtime, and consumer-install metadata before counting an artifact as verified.
It checks the profile base named in the packet; the optional `--published-head` argument checks
the recorded containing profile parent.

Blocked inputs return exit `2` and stable error codes. The regressions cover malformed roots,
duplicate JSON keys, invalid UTF-8, duplicate/swapped identities, incomplete artifact records,
invalid digests, wrong artifact sets, failed consumers, stale profile bases, and unavailable Git
identity. Inputs are limited to one MiB each and symlinked input files/directories are refused.
Load failures omit local paths from diagnostics. The gate validates recorded metadata only;
use the owner-native audit and disposable-install routes to verify actual artifact bytes and
behavior. Hosted CI runs the gate and refusal suite on Linux/macOS with Python 3.11 and 3.14.

## Evidence boundaries

This route proves only the commands and inputs it actually runs. It does not prove deployment,
provider-side controls, production security, outside adoption, or a user-visible outcome. A later
owner commit invalidates the matching source observation until the affected slice is rerun.

# Agent Systems Lab maintainer runbook

Use this runbook when changing a public owner, an adapter, a fixture, or the profile review surface.
The goal is to keep one semantic owner per protocol and leave a reviewer a short, reproducible
proof trail.

## Before editing

1. Identify the native owner and read its current contract, release notes, and security boundary.
2. Check the current public main SHA and the compatibility manifest pin. A stale checkout is an
   observation to record, not a reason to silently rewrite the pin.
3. Decide whether the change belongs in the owner, an additive adapter, Forgeyard's review layer,
   or profile documentation. Delete or reuse an existing path before adding a second registry.
4. Make a synthetic fixture for any new refusal or unknown state. Do not copy a private transcript,
   customer record, credential, or local path into a fixture.

## Change classes

| Change | Required owner action | Required profile action |
| --- | --- | --- |
| Native schema or refusal code | Update the owning repository's contract, tests, and release notes. | Refresh the compatibility row only after the owner is merged and read back. |
| Additive adapter | Keep raw source outside the projection; preserve unknowns; bind source and projection digests. | Link the adapter and name the native owner; do not describe it as a second source of truth. |
| Review/evaluation change | Version the receipt or fixture, hash the dataset, and separate deterministic assertions from local timings. | State the exact command, expected state, and machine-local limitation. |
| Release or audit change | Run isolated wheel/source consumers and checksum or public-audit checks where available. | Record artifact identity and any unavailable provider-side controls. |
| Documentation change | Keep claims tied to a source, command, and observed result. | Update the architecture, threat model, checklist, and packet together when the boundary changes. |

## Pre-merge checklist

- [ ] Native owner and source-of-truth path are named.
- [ ] Positive, blocked, tampered, malformed, stale, and unavailable cases are classified where
      relevant.
- [ ] Tests exercise the contract rather than mirroring implementation details.
- [ ] `git diff --check` is clean and the repository's full test command was run.
- [ ] Public audit or equivalent privacy scan reports synthetic-only contents.
- [ ] Release evidence names the reviewed head, hosted checks, and governed merge readback.
- [ ] The PR body separates source, tested, merged, released, adopted, and observed states.

## After merge

1. Read back the merged commit from GitHub and confirm the public branch points to it.
2. Use a fresh consumer checkout. Run the smallest install/demo/refusal path and record its output.
3. Refresh the profile packet only with evidence from that readback. Keep missing artifact, provider,
   deployment, adoption, and production evidence marked unavailable or unknown.
4. If a finding is discovered, preserve the reproducer and link the follow-up issue or PR. Do not
   overwrite the old receipt to make the history appear cleaner.

## Recovery and deprecation

If an adapter or fixture is wrong, leave the native owner intact, add a refusal or deprecation note,
and make the smallest additive repair. Never force-push a public evidence history or delete a release
artifact to hide a failed check. If a schema is retired, keep a reader or an explicit legacy refusal
until the compatibility manifest and every profile link have moved to the replacement.

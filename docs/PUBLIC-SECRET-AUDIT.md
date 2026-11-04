# Public-repository credential history audit

The scheduled and manual workflow in .github/workflows/public-secret-audit.yml audits original, non-archived **public** repositories belonging to jonah-ux. It clones Git mirrors and fetches available public pull-request heads, then scans all reachable unique Git blobs, including committed credentials later removed from the default branch.

Reports contain only repository, path, line, blob prefix, and category. Credential values and external-command stderr are never printed. Discovery failures, unreadable repositories, and matches fail the run. Files larger than 1 MiB are counted as skipped and explicitly reported.

Scope limits: this tool is a targeted detector, not proof that repositories have no secrets. It excludes private repos, forks, deleted/unreachable Git objects, GitHub Actions log archives, untracked files, binary data, large blobs, and deployed runtime settings. It is not a replacement for GitHub push protection or a dedicated secret scanner such as Gitleaks.

Run tests locally: python -m unittest discover -s tests -p test_public_secret_audit.py -v

Run a full audit on a machine with GitHub network access: python scripts/public_secret_audit.py --owner jonah-ux

If a finding appears, revoke and rotate the credential first. Removing a file in a later commit is insufficient because earlier Git history is public. Then investigate forks, PR references, caches, releases, and provider access logs.

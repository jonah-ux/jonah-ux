# Developer presence plan

The goal is a small, consistent public footprint around the same evidence:
real tools, reproducible installs, short build notes, and a profile that points
back to source. Create accounts only when there is a real artifact to publish;
an empty profile creates noise and does not help hiring teams.

## Do first

| Surface | What to publish | Current state | Official entry point |
| --- | --- | --- | --- |
| LinkedIn | A concise applied-AI/software profile, the GitHub URL, and two project entries for Slipstream and Chatlens | **Prepare** — the profile facts and project evidence are ready; account/profile fields still need a live review | [linkedin.com](https://www.linkedin.com/) |
| npm | `slipstream-local-index` once the prerelease has another consumer cycle; use GitHub Actions trusted publishing and provenance | **Prepare** — the public Node package exists as a release tarball; registry publication is a separate release decision | [npmjs.com/signup](https://www.npmjs.com/signup) |
| PyPI | Chatlens and the supporting Python CLIs after stable-release qualification; configure GitHub Actions Trusted Publishing instead of long-lived tokens | **Prepare** — the repos are package-shaped and release-evidenced; PyPI publication is not claimed yet | [pypi.org/account/register](https://pypi.org/account/register/) |
| Dev.to or Hashnode | Three short posts: why local agent tools need evidence, how Slipstream works, and how to build a safe CLI release | **Choose one** — use one writing home and cross-link it from X and GitHub | [dev.to](https://dev.to/) · [hashnode.com](https://hashnode.com/) |

## Do when the artifact is ready

| Surface | Trigger | Why it helps |
| --- | --- | --- |
| Hugging Face | A public model, dataset, or interactive AI demo exists; a static Space can host a lightweight showcase | Strong AI-native discovery and a live demo URL; do not create an empty Space | [huggingface.co](https://huggingface.co/) |
| Product Hunt | A stable release has a working demo, screenshots, install path, and a support plan | A launch can create authentic discovery when there is something people can use | [producthunt.com](https://www.producthunt.com/) |
| Docker Hub | A tool has a supported container workflow and a documented image contract | Makes the CLI easier to try in CI and gives infrastructure-oriented hiring teams a clear artifact | [hub.docker.com](https://hub.docker.com/) |
| GitHub Sponsors | There are active maintainers, regular releases, and a support promise | Optional sustainability layer; it is not a substitute for users or release proof | [github.com/sponsors](https://github.com/sponsors) |

## Skip for now

Kaggle, model leaderboards, a second blogging platform, and a collection of
empty social profiles would dilute the story. They become useful only when a
matching project produces a real submission, benchmark, or demo.

## Identity and safety rules

- Use the same public identity: **Jonah Helland**, `jonah-ux`, and
  `@jonahhelland`.
- Link back to [GitHub](https://github.com/jonah-ux) and the public source for
  every project entry.
- Keep personal contact details, employer data, private recordings, customer
  data, credentials, and internal Fleet/Portal mechanics out of public profiles.
- Never publish a package or launch page just to create activity. Tie it to a
  versioned artifact, a clean install, and a supportable README.

## Recommended order

1. Finish LinkedIn identity and project entries.
2. Reserve the npm and PyPI usernames, then wait to publish until the release
   gates are green and the package names are confirmed.
3. Publish one technical walkthrough on Dev.to **or** Hashnode.
4. Build one small public Hugging Face demo from a sanitized fixture.
5. Launch Slipstream or BreakTrace Lite on Product Hunt only after a stable
   release and a working demo are ready.

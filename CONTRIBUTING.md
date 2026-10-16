# How to Contribute

[Preparing the development environment]: #preparing-the-development-environment
[Updating dependencies]: #updating-dependencies
[Git Workflow]: #git-workflow
[How to work on a feature branch]: #how-to-work-on-a-feature-branch
[How to deploy]: #how-to-deploy
[GitHub Flow]: https://githubflow.github.io/
[Git Flow]: https://nvie.com/posts/a-successful-git-branching-model/
[GITHUB-FLOW.md]: docs/contributing/GITHUB-FLOW.md
[GIT-FLOW.md]: docs/contributing/GIT-FLOW.md
[How to Write a Git Commit Message]: https://cbea.ms/git-commit/
[interactive rebase]: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
[pre-commit]: https://pre-commit.com
[PEP8]: https://peps.python.org/pep-0008/
[docker official instructions]: https://docs.docker.com/engine/install/
[docker compose]: https://docs.docker.com/compose/install/linux/
[uv]: https://docs.astral.sh/uv/

<div align="justify">

These guidelines apply to GFW's Python repositories created from this template,
pipelines and services alike.
They describe the tooling the template ships (`Makefile`, Docker, uv),
so they live here, next to it, and each repository links to them from its README.
They aim to maintain code quality, clearly communicate the state of the codebase,
and standardize the development workflow.
Use your best judgment, and feel free to propose changes by submitting a pull request.

</div>

## Table of Contents

- [Preparing the development environment]
- [Updating dependencies]
- [Git Workflow]
- [How to work on a feature branch]
- [How to deploy]

## Preparing the development environment

<div align="justify">

This is the common setup shared across repositories created from this template.
It assumes you already cloned the repository, as its README explains,
and that you run every command from the root of the cloned repository.
A given repository's README may add repository-specific system dependencies on top of this
(e.g. GDAL) -- check there first if something doesn't build.

Install Docker Engine using the [docker official instructions] (avoid snap packages) and
the [docker compose] plugin.

</div>

1. Make sure you can build the docker image:

```shell
make docker-build
```

2. In order to be able to connect to Google Cloud (e.g. BigQuery),
authenticate and configure the project:

```shell
make docker-gcp
```

> [!NOTE]
> If you'd rather do all development inside a Docker container instead of a local
> virtual environment, run `make docker-shell` to get a shell with everything already
> installed, skip steps 3-6 below, and go directly to step 7 -- `make test` works the
> same way once you're inside that shell as it does in a local venv.

3. Install [uv] (faster installs than plain pip):

```shell
make uv
```

4. Create a virtual environment and activate it:

```shell
make venv
. .venv/bin/activate
```

The activation script must be sourced (`.` or `source`), not executed:
running `./.venv/bin/activate` would only affect a subshell.

5. Install all dependencies and the package itself in editable mode:

```shell
make install
```

6. (Optional) Install the [pre-commit] hooks:

```shell
make hooks
```

This is strongly recommended to maintain code quality and prevent technical debt,
particularly regarding documentation, [PEP8] compliance, spelling, and type-hinting.
If this feels too rigid for your current workflow, at a minimum,
make regular use of the `Makefile`'s `format`, `lint`, `codespell`, and `typecheck` targets.
[PEP8] checks are enforced in the GitHub CI.

7. Make sure you can run the unit tests:

```shell
make test
```

## Updating dependencies

<div align="justify">

`requirements.txt` contains all transitive dependencies pinned to specific versions. It
is automatically generated with `uv pip compile`, based on the dependencies specified in
`pyproject.toml`. This process ensures reproducibility, allowing the application to run
consistently across different environments.

Use `pyproject.toml` to define high-level dependencies with flexible version constraints
(e.g., `~=1.2`, `>=1.0`, `<2.0`, ...).

Every repository's `Makefile` is self-documenting -- run `make help` (or bare `make`) to
see its exact current targets and descriptions. The typical names are:

```shell
make reqs           # re-compile requirements.txt
make reqs-upgrade   # upgrade all dependencies to their latest compatible versions
```

</div>

> [!IMPORTANT]
> Do not modify `requirements.txt` manually.

> [!NOTE]
> After changing `requirements.txt`, rebuild the docker image (`make docker-build`)
> to use it locally.
> If the project uses Apache Beam, keep the Beam SDK image in the `Dockerfile`
> at the same version as the `apache-beam` pin in `requirements.txt`.

## Git Workflow

<div align="justify">

There are two main Git workflows commonly used in software development: [Git Flow] and
[GitHub Flow]. We encourage using **GitHub Flow** whenever possible, as it's a
lightweight workflow that supports rapid iteration, continuous delivery, and simpler
branching. It works especially well for teams that deploy frequently and want to keep
`main` always production-ready. However, if a project involves a long release cycle and
a long release process, or needs an unstable shared branch like `develop` for ongoing
integration, then **Git Flow** may be more appropriate. You can read a summary of both
workflows in [GITHUB-FLOW.md] and [GIT-FLOW.md].

</div>

## How to work on a feature branch

<div align="justify">

To work on a new feature or fix, create a branch from `main` (or `develop`, depending
on the workflow the repository follows).

- Branch names should be descriptive and concise, all lowercase and with words separated
  by hyphens. Optionally, prefix with the **JIRA** ticket, e.g.
  `PIPELINE-2020-name-of-the-branch`.
- Write clear commit messages. See [How to Write a Git Commit Message].
- Maintain a clean commit history in your feature branch. Use [interactive rebase]
  (`git rebase -i`) to squash, reorder, or edit commits.[^1]
- If you're not using [pre-commit] hooks, run the `Makefile`'s quality-check targets
  (`format`, `lint`, `codespell`, `typecheck`) as much as possible before pushing.
- Add unit tests for each piece of code: avoid connecting to external services during
  tests (mock as needed), and keep tests fast.
- When opening a pull request:
  - Target the correct base branch, depending on the repository's [Git Workflow].
  - Keep it focused and limited in scope to simplify review.
  - Link the related **JIRA** ticket in the description.

[^1]: When performing a rebase, it's acceptable to `push --force` to your own feature
      branch, but **never** on shared branches. Protect `main` and/or `develop` from
      force pushes via GitHub settings.

</div>

## How to deploy

<div align="justify">

A Google Cloud Build that publishes a Docker image is triggered in either of these
cases:

- A commit is merged into `main` (or `develop`, for repositories using Git Flow).
- A new tag is created.

The triggers are defined with Terraform in the repository's `cloudbuild/` directory.

</div>

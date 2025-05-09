<h1 align="center" style="border-bottom: none;">  python-app-template </h1>

<p align="center">
  <a href="https://github.com/GlobalFishingWatch/python-app-template/actions/workflows/main.yaml" >
    <img src="https://github.com/GlobalFishingWatch/python-app-template/actions/workflows/main.yaml/badge.svg"/>
  </a>
  <a href="https://codecov.io/gh/GlobalFishingWatch/python-app-template" >
    <img src="https://codecov.io/gh/GlobalFishingWatch/python-app-template/graph/badge.svg?token=uZTb6EphP8"/>
  </a>
  <a>
    <img alt="Python versions" src="https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue">
  </a>
  <a>
    <img alt="Last release" src="https://img.shields.io/github/v/release/GlobalFishingWatch/python-app-template">
  </a>
</p>

A template for python applications.

**Features**:
* :white_check_mark: Standard Python project structure & packaging.
* :white_check_mark: Dockerization.
* :white_check_mark: Dependency management with [pip-tools].
* :white_check_mark: Tools for quality checks: documentation, [PEP8], typehints, codespell.
* :white_check_mark: (Optional) pre-commit hooks to enforce automatic quality checks.
* :white_check_mark: Continuous Integration (CI) workflows (GitHub Actions).
* :white_check_mark: Continuous Deployment (CI) workflows (Google Cloud Build).
* :white_check_mark: Makefile with shortcuts to increase development speed.
* :white_check_mark: README badges with project information.
* :white_check_mark: Development workflow documentation.


[Apache Beam]: https://beam.apache.org
[codecov]: https://about.codecov.io
[docker compose]: https://docs.docker.com/compose/install/linux/
[docker official instructions]: https://docs.docker.com/engine/install/
[git-flow]: https://nvie.com/posts/a-successful-git-branching-model/
[Google BigQuery]: https://cloud.google.com/bigquery
[Google Dataflow]: https://cloud.google.com/products/dataflow?hl=en
[How to Write a Git Commit Message]: https://cbea.ms/git-commit/
[PEP8]: https://peps.python.org/pep-0008/
[pip-tools]: https://pip-tools.readthedocs.io/en/stable/
[pytest]: https://docs.pytest.org/en/stable/
[Semantic Versioning]: https://semver.org
[used by pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/config.html

[examples]: examples/

[.coveragerc]: .coveragerc
[.flake8]: .flake8
[.gitignore]: .gitignore
[activate_venv.sh]: activate-venv.sh
[cloudbuild.yaml]: cloudbuild.yaml
[codecov.yml]: codecov.yml
[docker-compose.yml]: docker-compose.yml
[Dockerfile]: Dockerfile
[LICENSE]: LICENSE
[Makefile]: Makefile
[pre-commit hooks]: .pre-commit-config.yaml
[pyproject.toml]: pyproject.toml
[pytest.ini]: pytest.ini
[requirements.txt]: requirements.txt
[README.md]: README.md
[setup.py]: setup.py

## Introduction

<div align="justify">

The following table provides a short description of each file in the repository:

| File                    | Description                                                                     |
| ------------------------| -----------------------------------------------------------------               |
|[.coveragerc]          	| Configuration for coverage reports [used by pytest-cov].                        |
|[.flake8]   					    | Configuration for [PEP8] checker.				                                        |
|[.gitignore]  					  | List of files and directories to be ignored by git.                             |
|[activate_venv.sh]       | Simple shortcut to enter virtual environment.                                   |
|[cloudbuild.yaml]        | Configuration to build and publish docker images in Google Cloud.               |
|[codecov.yml]            | Configuration for [codecov] GitHub integration.                                 |
|[docker-compose.yml]     | Configuration for [docker compose].                                             |
|[Dockerfile]          		| Instructions for building the Docker image.                                     |
|[LICENSE]             		| The software license.                                                           |
|[Makefile]               | A set of commands to simplify development.                                      |
|[pre-commit hooks]       | Configuration to automate software quality checks.                              |
|[pyproject.toml]         | Modern Python packaging configuration file.                                     |
|[pytest.ini]             | Configuration for [pytest].                                                     |
|[requirements.txt]       | Full set of dependencies pinned to specific versions.                           |
|[README.md]              | This file.					                                                            |
|[setup.py]             	| Legacy Python packaging config file, kept for compatibility with [Apache Beam]. |

## Development

Install Docker Engine using the [docker official instructions] (avoid snap packages)
and the [docker compose] plugin. No other dependencies are required.

### Preparing the environment

1. First, clone the repository.
```shell
git clone https://github.com/GlobalFishingWatch/python-app-template.git
```

2. Make sure you can build the docker image:
```shell
make docker-build
```

3. In order to be able to connect to BigQuery, authenticate and configure the project:
```shell
make docker-gcp
```

4. Create virtual environment and activate it:
```shell
make venv
./.venv/bin/activate
```

5. Install dependencies and the python package:
```shell
make install
```

6. (Optional) Install pre-commit hooks:
```shell
make hooks
```
This step is highly recommended to maintain the quality of the code
and avoid accumulating technical debt, specifically in terms of documentation, [PEP8], spelling, type-hinting.
If this is too rigid for your current workflow,
at least try to frequently use the provided commands in the [Makefile]:
`[format, lint, codespell, typecheck]`.

[PEP8] checks will be enforced in the GitHub CI.

7. Make sure you can run unit tests:
```shell
make test
```
</div>


> [!NOTE]
> Alternatively,
  you can perform all the development inside a docker container
  without the need of installing dependencies in a virtual environment.
  You can use `make docker-shell` to enter a docker container.

### Updating dependencies

<div align="justify">

The [requirements.txt] contains all transitive dependencies pinned to specific versions.
This file is compiled automatically with [pip-tools], based on [pyproject.toml].

Use [pyproject.toml] to specify high-level dependencies with some restrictions.
Do not modify [requirements.txt] manually.

To re-compile dependencies, just run
```shell
make reqs
```

If you want to upgrade all dependencies to latest available versions
(compatible with restrictions declared), just run:
```shell
make reqs-upgrade
```
</div>

> [!NOTE]
> Remember that if you change the requirements, you need to rebuild the docker image in order to use it locally.

### How to deploy

A Google Cloud build that publishes a Docker image will be triggered in the following cases:  
- Pushing a commit to the `main` or `develop` branches (this includes merges).  
- Creating a tag.
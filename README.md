<h1 align="center" style="border-bottom: none;">  python-app-template </h1>

<p align="center">
  <a href="https://github.com/GlobalFishingWatch/python-app-template/actions/workflows/main.yaml" >
    <img src="https://github.com/GlobalFishingWatch/python-app-template/actions/workflows/main.yaml/badge.svg"/>
  </a>
  <a href="https://codecov.io/gh/GlobalFishingWatch/python-app-template" >
    <img src="https://codecov.io/gh/GlobalFishingWatch/python-app-template/graph/badge.svg?token=uZTb6EphP8"/>
  </a>
  <a>
    <img alt="Python versions" src="https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue">
  </a>
  <a>
    <img alt="Last release" src="https://img.shields.io/github/v/release/GlobalFishingWatch/python-app-template">
  </a>
</p>

A template for Python applications.

**Features**:
* :white_check_mark: Standard Python project structure & packaging.
* :white_check_mark: Dependency management with [pip-tools].
* :white_check_mark: Tools for quality checks: documentation, [PEP8], typehints, codespell.
* :white_check_mark: **[Optional]** pre-commit hooks to enforce automatic quality checks.
* :white_check_mark: Dockerization with focus in image size optimization.
* :white_check_mark: Continuous Integration (CI) workflows (GitHub Actions).
* :white_check_mark: Continuous Deployment (CI) workflows (Google Cloud Build).
* :white_check_mark: Makefile with shortcuts to increase development speed.
* :white_check_mark: README badges with project information.
* :white_check_mark: Development workflow documentation.
* :white_check_mark: Support for [Apache Beam] integrated pipelines.


[Apache Beam]: https://beam.apache.org
[codecov]: https://about.codecov.io
[docker compose]: https://docs.docker.com/compose/install/linux/
[docker official instructions]: https://docs.docker.com/engine/install/
[git-flow]: https://nvie.com/posts/a-successful-git-branching-model/
[Google BigQuery]: https://cloud.google.com/bigquery
[Google Dataflow]: https://cloud.google.com/products/dataflow?hl=en
[How to Write a Git Commit Message]: https://cbea.ms/git-commit/
[interactive rebase]: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
[Markdown alerts]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts
[mermaid diagram]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams
[PEP8]: https://peps.python.org/pep-0008/
[pip-tools]: https://pip-tools.readthedocs.io/en/stable/
[pre-commit]: https://pre-commit.com
[pytest]: https://docs.pytest.org/en/stable/
[Semantic Versioning]: https://semver.org
[used by pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/config.html

[cli.py]: src/python_app_template/cli.py
[examples]: examples/

[.coveragerc]: .coveragerc
[.flake8]: .flake8
[.gitignore]: .gitignore
[activate_venv.sh]: activate-venv.sh
[cloudbuild.yaml]: cloudbuild.yaml
[codecov.yml]: codecov.yml
[docker-compose.yml]: docker-compose.yml
[Dockerfile]: Dockerfile
[GIT-WORKFLOW.md]: GIT-WORKFLOW.md
[LICENSE]: LICENSE
[Makefile]: Makefile
[MANIFEST.in]: MANIFEST.in
[pre-commit hooks]: .pre-commit-config.yaml
[pyproject.toml]: pyproject.toml
[pytest.ini]: pytest.ini
[requirements.txt]: requirements.txt
[requirements-test.txt]: requirements-test.txt
[README.md]: README.md
[setup.py]: setup.py

## Introduction

<div align="justify">

_Write here the motivation for this application._
_When applicable, cite relevant articles for the curious reader._

In this case,
the motivation for this repository is the need of a robust and documented
repository template for Python applications,
which are used at least in all the GFW data pipelines.

Some goals of this template are:
* Reduce the overhead of creating a new dockerized python application.
* Reduce the work needed to be done when moving prototypes to production.
* Define standards for development accross our data pipelines.

## Usage 

_Write here the relevant documentation on how to use this application.
Ideally, split it into sections_.

_Assume in this section you have published a package in PYPI or docker image in the registry._

_You can use [Markdown alerts] to highlight stuff._

</div>

Example:
> [!CAUTION]
  Using HTML sections in the README break the rendering of [Markdown alerts] alerts.
  Make sure you put them outside `<div></div>` sections for example.

<div  align="justify">

In this case, it can be useful to show a short description of each file in the root of the repository template:
| File                    | Description                                                                     |
| ------------------------| -----------------------------------------------------------------               |
|[.flake8]                | Configuration for [PEP8] checker.                                               |
|[.gitignore]             | List of files and directories to be ignored by git.                             |
|[activate_venv.sh]       | Simple shortcut to enter virtual environment.                                   |
|[cloudbuild.yaml]        | Configuration to build and publish docker images in Google Cloud.               |
|[codecov.yml]            | Configuration for [codecov] GitHub integration.                                 |
|[docker-compose.yml]     | Configuration for [docker compose].                                             |
|[Dockerfile]             | Instructions for building the Docker image.                                     |
|[GIT-WORKFLOW.md]        | Git workflow definition for this repository.                                    |
|[LICENSE]                | The software license.                                                           |
|[Makefile]               | Set of commands to simplify development.                                        |
|[MANIFEST.in]            | Set of patterns to include or exclude files from installed package.             |
|[pre-commit hooks]       | Configuration to automate software quality checks.                              |
|[pyproject.toml]         | Modern Python packaging configuration file.                                     |
|[requirements.txt]       | Full set of compiled production dependencies (pinned to specific versions).     |
|[requirements-test.txt]  | High level test dependencies needed to test the installed package.              |
|[README.md]              | This file.                                                                      |
|[setup.py]               | Legacy Python packaging config file, kept for compatibility with [Apache Beam]. |

### Using the CLI

_Write here instructions on how to use the CLI of the application._


### Config file example

_Expose an input config file example._

### Output schema.

_Discuss anything relevant about the about schema. Put a link to the schema definition._

### Data persistence pattern

_Expose what is the data persistence pattern for this application._

## Implementation details

_In here you can describe implementation details, more targeted to developers._

### Most relevant modules [Optional]

_Here you can describe the most relevant modules of your app._

Example:
<div align="center">

| Module | Description |
| --- | --- |
| [cli.py]     | Defines the application CLI. |

</div>

### Flow chart [Optional]

_Here you can show a [mermaid diagram] explaining the implementation._

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

6. (Optional) Install [pre-commit] hooks:
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

### Making changes

Create a branch and a Pull Request (PR) following the workflow defined in [GIT-WORKFLOW.md].

**When working on a branch, try to follow this guidelines:**
- Write clear commit messages. See [How to Write a Git Commit Message].
- Use [interactive rebase] to maintain the commit history of your branch clean.
- If you are not using [pre-commit] hooks,
  use as much as you can the provided commands in [Makefile] to maintain quality: `[format, lint, codespell, typecheck]`. 
- Add unit tests for each piece of code.
  * Don't connect to external services when running unit tests. Use mocks when needed.
  * Make sure unit tests run as fast as possible. 

**When submitting a PR, please ensure it meets the following criteria:**
- The PR targets the correct base branch (this depdends on which git workflow you are using).
- The title and body provide a clear and concise explanation of **what** the PR does and **why** it's necessary.
- The body contains a link the related JIRA ticket. This allows the integration with the ticket with the PR. 

### Updating dependencies

<div align="justify">

The [requirements.txt] file contains all transitive dependencies pinned to specific versions.
It is automatically generated using [pip-tools],
based on the dependencies specified in [pyproject.toml].
This process ensures reproducibility,
allowing the application to run consistently across different environments.

Use [pyproject.toml] to define high-level dependencies with flexible version constraints
(e.g., ~=1.2, >=1.0, <2.0, ...).
Do not modify [requirements.txt] manually.

To re-compile dependencies, just run
```shell
make reqs
```

If you want to upgrade all dependencies to latest compatible versions, just run:
```shell
make reqs-upgrade
```
</div>

> [!NOTE]
> Remember that if you change the [requirements.txt],
you need to rebuild the docker image (`make docker-build`) in order to use it locally.

### How to deploy

A Google Cloud build that publishes a Docker image will be triggered in the following cases:  
- Pushing a commit to the `main` or `develop` branches (this includes merges).  
- Creating a tag.


## References [Optional]

_Provide useful references for the explanations contained in this README._

Example:
<a id="1">[1]</a> Welch H., Clavelle T., White T. D., Cimino M. A., Van Osdel J., Hochberg T., et al. (2022). Hot spots of unseen fishing vessels. Sci. Adv. 8 (44), eabq2109. doi: 10.1126/sciadv.abq2109

<a id="1">[2]</a> J. H. Ford, B. Bergseth, C. Wilcox, Chasing the fish oil—Do bunker vessels hold the key to fisheries crime networks? Front. Mar. Sci. 5, 267 (2018).
<h1 align="center" style="border-bottom: none;">  python-app-template </h1>

<p align="center">
  <a href="https://github.com/GlobalFishingWatch/python-app-template/actions/workflows/main.yaml" >
    <img src="https://github.com/GlobalFishingWatch/python-app-template/actions/workflows/main.yaml/badge.svg"/>
  </a>
  <a href="https://codecov.io/gh/GlobalFishingWatch/python-app-template" >
    <img src="https://codecov.io/gh/GlobalFishingWatch/python-app-template/graph/badge.svg?token=uZTb6EphP8"/>
  </a>
  <a>
    <img alt="Python versions" src="https://img.shields.io/badge/python-3.12%20%7C%203.13-blue">
  </a>
  <a>
    <img alt="Last release" src="https://img.shields.io/github/v/release/GlobalFishingWatch/python-app-template">
  </a>
</p>

A template for Python applications.

**Features**:
* :white_check_mark: Standard Python project structure & packaging.
* :white_check_mark: Dependency management with [uv].
* :white_check_mark: Tools for quality checks: documentation, [PEP8], typehints, codespell.
* :white_check_mark: **[Optional]** pre-commit hooks to enforce automatic quality checks.
* :white_check_mark: Dockerization with focus in image size optimization.
* :white_check_mark: Continuous Integration (CI) workflows (GitHub Actions).
* :white_check_mark: Continuous Deployment (CD) workflows (Google Cloud Build).
* :white_check_mark: Makefile with shortcuts to increase development speed.
* :white_check_mark: README badges with project information.
* :white_check_mark: Development workflow documentation.
* :white_check_mark: Support for [Apache Beam] integrated pipelines.


[Apache Beam]: https://beam.apache.org
[branch protection rules]: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
[codecov]: https://about.codecov.io
[docker compose]: https://docs.docker.com/compose/install/linux/
[Google BigQuery]: https://cloud.google.com/bigquery
[Google Dataflow]: https://cloud.google.com/products/dataflow?hl=en
[Markdown alerts]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts
[mermaid diagram]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams
[PEP8]: https://peps.python.org/pep-0008/
[uv]: https://docs.astral.sh/uv/
[pre-commit]: https://pre-commit.com
[pytest]: https://docs.pytest.org/en/stable/
[used by pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/config.html

[cli/main.py]: src/python_app_template/cli/main.py
[cli/commands/]: src/python_app_template/cli/commands/
[pipelines/]: src/python_app_template/pipelines/
[config/]: config/
[config/hello/sample.yaml]: config/hello/sample.yaml
[gfw-common]: https://github.com/GlobalFishingWatch/gfw-common


[.github/]: .github/
[cloudbuild/]: cloudbuild/
[docs/]: docs/
[notebooks/]: notebooks/
[src/python_app_template/]: src/python_app_template
[src/python_app_template/assets/]: src/python_app_template/assets/
[tests/]: tests/

[.dockerignore]: .dockerignore
[.flake8]: .flake8
[.gitignore]: .gitignore
[.pre-commit-config.yaml]: .pre-commit-config.yaml
[activate-venv.sh]: activate-venv.sh
[codecov.yml]: codecov.yml
[CONTRIBUTING.md]: CONTRIBUTING.md
[contributing guide]: https://github.com/GlobalFishingWatch/python-app-template/blob/main/CONTRIBUTING.md
[docker-compose.yml]: docker-compose.yml
[Dockerfile]: Dockerfile
[Git Workflow]: https://github.com/GlobalFishingWatch/python-app-template/blob/main/CONTRIBUTING.md#git-workflow
[init_project.py]: init_project.py
[LICENSE]: LICENSE
[Makefile]: Makefile
[MANIFEST.in]: MANIFEST.in
[pyproject.toml]: pyproject.toml
[README.md]: README.md
[requirements.txt]: requirements.txt
[requirements-test.txt]: requirements-test.txt
[setup.py]: setup.py


## Introduction

<div align="justify">

_Write the motivation for this application here._
_When applicable, include citations for relevant articles or resources for further reading._

The motivation for this repository is to provide a robust,
well-documented template for Python applications,
including but not limited to GFW data pipelines.

Goals of this template include:
* Reducing the overhead of creating a new Dockerized Python application.
* Minimizing the effort required to transition prototypes to production.
* Establishing consistent development standards across projects.

## Usage

_Write the relevant documentation on how to use this application here.
Ideally, organize it into sections_.

_Assume in this section that a package has been published in PYPI
or a Docker image to the registry._

_Use [Markdown alerts] to highlight important information._

</div>

Example:
> [!CAUTION]
  Using HTML sections breaks the rendering of [Markdown alerts] alerts.
  To avoid this, place them outside `<div></div>` sections, for example.

### Minimum Requirements

This template can be used at various stages of development:
**Proof of Concept**, **Prototype**, and **Production**.  
Each stage has its own minimum quality requirements
and incrementally builds upon the requirements of the previous stages.


1. 💡 **Proof of Concept**  
   - Update the project's name with `python init_project.py my-project-name`.
   - Declare required dependencies in [pyproject.toml].
     Use the `dev` extra for development-only dependencies,
     and the `test` dependency group for test dependencies.
   - Store data files (e.g., `.txt`, `.json`, `.csv`) in the `src/my_project_name/assets/` directory.
   - Add the following sections to the `README.md`:  
     - **Introduction**  
     - **Usage**

2. 🛠️ **Prototype**  
   - Set up [branch protection rules] for `main` branch (and `develop` if exists).
     - ☑️ Restrict deletions.
     - ☑️ Require a pull request before merging.
       - ☑️ Require approvals.
       - ☑️ Require conversation resolution before merging.
     - ☑️ Require status checks to pass. Add GitHub actions to checks.
       - ☑️ Require branches to be up to date before merging.
     - ☑️ Block force pushes.
     - ☑️ Allowed merge methods: only Merge.
   - Select a [Git Workflow] to maintain consistent branching and collaboration practices.
   - Create the Google Cloud Build triggers that publish the Docker image upon merges and tags:
     run `terraform init` and `terraform apply` in [cloudbuild/].
   - Re-compile `requirements.txt` for Docker using:
     ```
     make reqs
     ```
   - Update the `README.md` to include:  
     - **Output Schema**

3. 🚀 **Production**  
   - Install and configure pre-commit hooks. See the [contributing guide].
   - Add unit tests to ensure code reliability.
   - Write thorough documentation:  
     - A complete `README.md`.
     - Docstrings for all **public** modules, classes, methods and functions.



### Repository Overview

_This section applies only to the template and provides an overview of the repository contents._

#### Directories

This is a brief summary of all the relevant directories of the repository.

<div  align="center">

| Directory                       | Description                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------- |
|[.github/]                       | Configuration for GitHub actions.                                               |
|[cloudbuild/]                    | Terraform config for the Cloud Build triggers.                                  |
|[config/]                        | Example configuration files for the CLI commands.                               |
|[docs/]                          | Markdown files with detailed documentation.                                     |
|[notebooks/]                     | All jupyter notebooks go here.                                                  |
|[src/python_app_template/]       | All source code go here.                                                        |
|[src/python_app_template/assets/]| All data files go here.                                                         |
|[tests/]                         | All tests go here.                                                              |

</div>

#### Files

This is a brief summary of all the relevant files of the repository.

<div  align="center">

| File                           | Description                                                                     |
| -------------------------------| ------------------------------------------------------------------------------- |
|[.dockerignore]                 | Lists files and folders that Docker should ignore when building an image.       |
|[.flake8]                       | Configuration for [PEP8] checker.                                               |
|[.gitignore]                    | List of files and directories to be ignored by git.                             |
|[.pre-commit-config.yaml]       | Configuration to automate software quality checks.                              |
|[activate-venv.sh]              | Simple shortcut to enter virtual environment.                                   |
|[codecov.yml]                   | Configuration for [codecov] GitHub integration.                                 |
|[CONTRIBUTING.md]               | Contributing guide shared by all projects created from this template.           |
|[docker-compose.yml]            | Configuration for [docker compose].                                             |
|[Dockerfile]                    | Instructions for building the Docker image.                                     |
|[init_project.py]               | Automates changing the project name across relevant files and directories.      |
|[LICENSE]                       | The software license.                                                           |
|[Makefile]                      | Set of commands to simplify development.                                        |
|[MANIFEST.in]                   | Set of patterns to include or exclude files from installed package.             |
|[pyproject.toml]                | Modern Python packaging configuration file.                                     |
|[requirements.txt]              | Full set of compiled production dependencies (pinned to specific versions).     |
|[requirements-test.txt]         | Compiled test dependencies, installed on top of the production image to test it.|
|[README.md]                     | This file.                                                                      |
|[setup.py]                      | Legacy Python packaging config file, kept for compatibility with [Apache Beam]. |

</div>

<div  align="justify">

### Using the CLI

_Write instructions on how to use the CLI of the application here.
The template ships an example `hello` command built on [gfw-common]'s CLI:
replace it with your own commands._

Run `python-app-template -h` for the list of commands,
or `python-app-template <command> -h` for a command's own options. For example:

```shell
python-app-template hello --name GFW --times 2 --labels environment=development
```

Every command also accepts a configuration file (`-c/--config-file`).
Command-line arguments take precedence over the configuration file,
and the configuration file over the command's defaults.

#### Config file example

_**Optional**_.
_Provide an example of an input configuration file._

Example ([config/hello/sample.yaml]):
```yaml
name: GFW
times: 2

# Labels for cost tracking (label values: lowercase letters, digits, '_' and '-').
labels:
  environment: development
```

## Output schema

_**Optional**_.
_Discuss any relevant details about the schema.
Provide a link to the schema definition._

## Data persistence pattern

_**Optional**_.
_Explain the data persistence pattern used in this application._

## How to Contribute

First, clone the repository:

```shell
git clone https://github.com/GlobalFishingWatch/python-app-template.git
cd python-app-template
```

Then, from the cloned repository, follow the [contributing guide]
(shared by all projects created from this template)
to prepare the development environment and learn the git workflow.

## Implementation details

_**Optional**_.
_This section is for describing implementation details, primarily for developers._

### Most relevant modules

_**Optional**_.
_Use this section to describe the most important modules of your application._

Example:
<div align="center">

| Module | Description |
| --- | --- |
| [cli/main.py] | Defines the application CLI and registers its commands. |
| [cli/commands/] | One module per command: its name, description and options. Delegates to its pipeline. |
| [pipelines/] | One package per command: its configuration (`config.py`) and its logic (`run()` in `main.py`). |

</div>

### Flow chart

_**Optional**_.
_Use this section to display a [mermaid diagram] that explains the implementation._

## References

_**Optional**_.
_Provide any relevant references to support the explanations in this README.
Here we provide some examples._


<a id="1">[1]</a> Welch H., Clavelle T., White T. D., Cimino M. A., Van Osdel J., Hochberg T., et al. (2022). Hot spots of unseen fishing vessels. Sci. Adv. 8 (44), eabq2109. doi: 10.1126/sciadv.abq2109

<a id="1">[2]</a> J. H. Ford, B. Bergseth, C. Wilcox, Chasing the fish oil—Do bunker vessels hold the key to fisheries crime networks? Front. Mar. Sci. 5, 267 (2018).

# Justfile - Thin wrapper for local development
# Adjusts PYTHON and PIP variables for venv, then calls Make recipes
# Use: `just install`, `just test`, `just reqs`, etc.

set shell := ["bash", "-c"]


VENV_NAME := ".venv"
PYTHON := VENV_NAME / "bin" / "python"
PIP := "uv pip"

[private]
default:
	just --list

# Create virtual environment
venv:
    make venv

# Upgrade pip
upgrade-pip:
    make upgrade-pip PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Install only test dependencies
install-test: upgrade-pip
    make install-test PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Install the package in editable mode & all dependencies for local development
install: upgrade-pip
    make install PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Run all unit tests exporting coverage.xml report
test:
    make test PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Install and pre-commit hooks
hooks:
    make hooks PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Auto-format python source files according with PEP8
format:
    make format PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Lint python source files
lint:
    make lint PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Use Codespell to do spell checking
codespell:
    make codespell PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Perform type-checking
typecheck:
    make typecheck PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Use pip-audit to scan for known vulnerabilities
audit:
    make audit PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Run all pre-commit hooks
pre-commit:
    make pre-commit PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Run the standard set of checks performed in CI
all: lint codespell typecheck audit test

# Compile requirements.txt with pip-tools
reqs:
    make reqs PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Upgrade requirements.txt with pip-tools
reqs-upgrade:
    make reqs-upgrade PYTHON="{{ PYTHON }}" PIP="{{ PIP }}"

# Docker: Build docker images
docker-build:
    make docker-build

# Docker: Create the docker volume for GCP
docker-volume:
    make docker-volume

# Docker: Authenticate to google cloud and configure the project
docker-gcp:
    make docker-gcp

# Docker: Run tests using prod image, exporting coverage.xml report
docker-ci-test:
    make docker-ci-test

# Docker: Enter interactive dev container shell
docker-shell:
    make docker-shell

# Clean local caches and build artifacts
clean:
    make clean

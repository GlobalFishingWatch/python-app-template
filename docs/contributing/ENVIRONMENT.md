[docker compose]: https://docs.docker.com/compose/install/linux/
[docker official instructions]: https://docs.docker.com/engine/install/
[PEP8]: https://peps.python.org/pep-0008/
[pre-commit]: https://pre-commit.com

[Makefile]: Makefile

### Preparing the environment

Install Docker Engine using the [docker official instructions] (avoid snap packages)
and the [docker compose] plugin. No other system dependencies are required.

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
This step is strongly recommended to maintain code quality and prevent technical debt,
particularly regarding documentation, [PEP8] compliance, spelling, and type-hinting.
If this feels too rigid for your current workflow,
at a minimum, make regular use of the provided [Makefile] commands:
`format`, `lint`, `codespell`, and `typecheck`.

[PEP8] checks will be enforced in the GitHub CI.

7. Make sure you can run unit tests:
```shell
make test
```
</div>

> [!NOTE]
> Alternatively,
  you can handle all the development inside a docker container
  without installing dependencies in a virtual environment.
  Use `make docker-shell` to enter a docker container.
[pip-tools]: https://pip-tools.readthedocs.io/en/stable/

[pyproject.toml]: pyproject.toml
[requirements.txt]: requirements.txt
[requirements-test.txt]: requirements-test.txt

### Updating dependencies

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

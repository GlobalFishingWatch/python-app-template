"""Command-line interface of the application, built on gfw-common's CLI."""

import sys

from typing import Any

from gfw.common.cli import CLI, labels_option
from python_app_template.cli.commands import Hello
from python_app_template.version import __version__


NAME = "python-app-template"
DESCRIPTION = "A template for python (dockerized) applications."
EXAMPLES = (
    "python-app-template hello --name GFW --times 2 --labels environment=development",
    "python-app-template hello -c config/hello/sample.yaml",
)


def run(args: list[str]) -> Any:
    """Builds the CLI and executes the command given in ``args``."""
    cli = CLI(
        name=NAME,
        description=DESCRIPTION,
        subcommands=[Hello],
        options=[labels_option()],  # Common options for all subcommands.
        version=__version__,
        examples=EXAMPLES,
    )

    result, _ = cli.execute(args)
    return result


def main() -> None:
    """Entry point of the installed package."""
    run(sys.argv[1:])


if __name__ == "__main__":
    main()

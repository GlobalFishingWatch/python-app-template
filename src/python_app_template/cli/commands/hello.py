"""CLI command that greets someone. An example of how to define a command."""

from types import SimpleNamespace

from gfw.common.cli import Command, Option
from python_app_template.pipelines.hello.config import HelloConfig
from python_app_template.pipelines.hello.main import run


DESCRIPTION = """\
Greets someone a number of times.

You can provide a configuration file or command-line arguments.
The latter take precedence, so if you provide both, command-line arguments
will overwrite options in the config file provided.
"""

HELP_NAME = "Who to greet."
HELP_TIMES = "How many times to greet."


class Hello(Command):
    """Greets someone a number of times."""

    @property
    def name(self) -> str:
        """The command's name."""
        return "hello"

    @property
    def description(self) -> str:
        """The command's description."""
        return DESCRIPTION

    @property
    def options(self) -> list[Option]:
        """The command's options."""
        return [
            Option("--name", type=str, default="World", help=HELP_NAME),
            Option("--times", type=int, default=1, help=HELP_TIMES),
        ]

    def run(self, config: SimpleNamespace, **kwargs: object) -> list[str]:
        """Runs the command with the resolved configuration."""
        return run(HelloConfig.from_namespace(config), **kwargs)

"""Runs the hello command."""

import logging

from python_app_template.pipelines.hello.config import HelloConfig


logger = logging.getLogger(__name__)


def run(config: HelloConfig, **kwargs: object) -> list[str]:
    """Greets ``config.name``, ``config.times`` times.

    Args:
        config:
            The command's configuration.

        **kwargs:
            Extra arguments the CLI passes through. Unused here.

    Returns:
        The greetings.
    """
    greetings = [f"Hello, {config.name}!" for _ in range(config.times)]
    for greeting in greetings:
        logger.info(greeting)

    return greetings

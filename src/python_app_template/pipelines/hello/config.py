"""Configuration of the hello command."""

from dataclasses import dataclass

from gfw.common.config import PipelineConfig


ERROR_TIMES = "times must be at least 1. Got: {}."


@dataclass(frozen=True, kw_only=True)
class HelloConfig(PipelineConfig):
    """Configuration of the hello command.

    Inherits the settings every pipeline has, like its ``labels``,
    and how to create it from the CLI's namespace (``from_namespace``).

    Raises:
        ValueError:
            If ``times`` is lower than 1.
    """

    name: str = "World"
    """Who to greet."""

    times: int = 1
    """How many times to greet."""

    def __post_init__(self) -> None:
        """Validates the configuration."""
        super().__post_init__()
        if self.times < 1:
            raise ValueError(ERROR_TIMES.format(self.times))

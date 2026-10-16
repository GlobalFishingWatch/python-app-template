import pytest

from python_app_template.cli import main
from python_app_template.pipelines.hello.config import HelloConfig


LABELS = {"environment": "test"}


@pytest.fixture
def run(mocker):
    return mocker.patch("python_app_template.cli.commands.hello.run")


def test_defaults(run):
    main.run(["hello", "--labels", "environment=test"])

    run.assert_called_once_with(HelloConfig(labels=LABELS, name="World", times=1))


def test_command_line_options(run):
    main.run(["hello", "--name", "GFW", "--times", "3", "--labels", "environment=test"])

    run.assert_called_once_with(HelloConfig(labels=LABELS, name="GFW", times=3))


def test_command_line_overrides_config_file(run, tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("name: GFW\ntimes: 2\nlabels:\n  environment: test\n")

    main.run(["hello", "-c", str(config_file), "--times", "5"])

    run.assert_called_once_with(HelloConfig(labels=LABELS, name="GFW", times=5))

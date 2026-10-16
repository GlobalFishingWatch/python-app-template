import sys

from python_app_template.cli import main


LABELS = ["--labels", "environment=test"]


def test_run_executes_command():
    assert main.run(["hello", "--name", "GFW", *LABELS]) == ["Hello, GFW!"]


def test_main_reads_sys_argv(monkeypatch, mocker):
    monkeypatch.setattr(sys, "argv", ["python-app-template", "hello", *LABELS])
    run = mocker.patch("python_app_template.cli.commands.hello.run")

    main.main()

    run.assert_called_once()

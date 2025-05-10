from python_app_template import cli


def test_cli():
    cli.cli(["--arg1", 1234])


def test_main():
    cli.main()

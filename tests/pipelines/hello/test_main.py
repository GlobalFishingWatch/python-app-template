from python_app_template.pipelines.hello.config import HelloConfig
from python_app_template.pipelines.hello.main import run


def test_run_greets_times():
    config = HelloConfig(labels={"environment": "test"}, name="GFW", times=2)

    assert run(config) == ["Hello, GFW!", "Hello, GFW!"]

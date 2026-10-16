from types import SimpleNamespace

import pytest

from gfw.common.config import PipelineConfigError

from python_app_template.pipelines.hello.config import HelloConfig


LABELS = {"environment": "test"}


def test_from_namespace():
    config = HelloConfig.from_namespace(SimpleNamespace(labels=LABELS, name="GFW", times=2))

    assert config == HelloConfig(labels=LABELS, name="GFW", times=2)


def test_times_lower_than_one_raises():
    with pytest.raises(ValueError, match="times must be at least 1"):
        HelloConfig(labels=LABELS, times=0)


def test_empty_labels_raise():
    with pytest.raises(PipelineConfigError):
        HelloConfig(labels={})

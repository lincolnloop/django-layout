import logging
import typing as t

if t.TYPE_CHECKING:
    import pytest

from django.conf import settings


def test_root_logger_does_not_capture_info(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.WARNING, logger=""):
        logging.getLogger().info("root info message")
    assert "root info message" not in caplog.text


def test_root_logger_captures_warning(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.WARNING, logger=""):
        logging.getLogger().warning("root warning message")
    assert "root warning message" in caplog.text


def test_app_logger_captures_info(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO, logger=settings.PROJECT_NAME):
        logging.getLogger(settings.PROJECT_NAME).info("app info message")
    assert "app info message" in caplog.text


def test_app_logger_captures_warning(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO, logger=settings.PROJECT_NAME):
        logging.getLogger(settings.PROJECT_NAME).warning("app warning message")
    assert "app warning message" in caplog.text

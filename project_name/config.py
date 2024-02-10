import base64
import os
from pathlib import Path
from typing import Literal

from goodconf import Field, GoodConf

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

PROJECT_DIR = Path(__file__).parents[1].resolve()


class Config(GoodConf):
    """Configuration for {{ project_name }}"""

    DEBUG: bool = False
    ALLOWED_HOSTS: list[str] = Field(
        default=["*"],
        description="Hosts allowed to serve the site "
        "https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts",
    )
    DATABASE_URL: str = Field(
        default="sqlite:///./sqlite3.db",
        description="A string with the database URL as defined in "
        "https://github.com/jacobian/dj-database-url#url-schema",
    )
    DJANGO_ENV: Literal["development", "dev", "production"] = Field(
        default="production",
        description="Toggle deployment settings for local development or production",
    )
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Python logging level",
    )
    SECRET_KEY: str = Field(
        initial=lambda: base64.b64encode(os.urandom(60)).decode(),
        description="A long random string you keep secret "
        "https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key",
    )
    ENVIRONMENT: str = Field(
        "test",
        description="Deploy environment",
    )
    BASIC_AUTH_CREDENTIALS: str = Field(
        default="",
        description="Basic Auth credentials for the site in the format 'username:password'",
    )
    SENTRY_DSN: str = Field(
        default="",
        description="Sentry DSN to enable error logging",
    )
    SENTRY_TRACE_SAMPLE_RATE: float = Field(
        default=0.25,
        description="Sentry trace sample rate "
        "https://docs.sentry.io/product/sentry-basics/concepts/tracing/trace-view/",
    )

    class Config:
        default_files = ["{{ project_name }}.yml"]


config = Config()

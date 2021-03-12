import base64
import os
from typing import List

from goodconf import GoodConf, Field
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")


class AppConfig(GoodConf):
    """Configuration for {{ project_name }}"""

    DEBUG: bool
    ALLOWED_HOSTS: List[str] = Field(
        ["*"],
        initial=lambda: ["*"],
        description="Hosts allowed to serve the site "
        "https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts",
    )
    DATABASE_URL: str = Field(
        "sqlite:///PATH",
        initial=lambda: "sqlite:///PATH",
        description="A string with the database URL as defined in"
        "https://github.com/jacobian/dj-database-url#url-schema"
    )
    SECRET_KEY: str = Field(
        base64.b64encode(os.urandom(60)).decode(),
        initial=lambda: base64.b64encode(os.urandom(60)).decode(),
        description="A long random string you keep secret "
        "https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key",
    )
    ENVIRONMENT: str = Field(
        "test",
        initial=lambda: "test",
        description="Deploy environment",
    )

    class Config:
        default_files = ["{{ project_name }}.yml"]


config = AppConfig()


def generate_config():
    print(AppConfig.generate_yaml(DEBUG=True))

import base64
import os

from goodconf import GoodConf
from goodconf.values import Value
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

PROJECT_DIR = Path(__file__).parents[1].resolve()


class Config(GoodConf):
    """Configuration for Drexel Data Platform"""

    DEBUG = Value(default=False, help="Enable debugging.")
    ALLOWED_HOSTS = Value(
        default=["*"],
        help="Hosts allowed to serve the site "
        "https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts",
    )
    DATABASE_URL = Value(default="sqlite:///PATH")
    SECRET_KEY = Value(
        initial=lambda: base64.b64encode(os.urandom(60)).decode(),
        help="a long random string you keep secret "
        "https://docs.djangoproject.com/en/2.0/ref/settings/#secret-key",
    )

    SENTRY_DSN = Value(default="", help="DSN for https://sentry.io")
    SENTRY_TRACES_SAMPLE_RATE = Value(
        default=0.25,
        help="https://docs.sentry.io/platforms/python/#monitor-performance",
    )
    ENVIRONMENT = Value(default="test", help="Deploy environment")


config = Config(
    default_files=["{{ project_name }}.yml"],
)


def generate_config():
    print(Config.generate_yaml(DEBUG=True))

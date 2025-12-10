import base64

import pytest
import requests

pytestmark = pytest.mark.server_env({"BASIC_AUTH_CREDENTIALS": "george:vandelay"})


def test_returns_401_without_credentials(server: str) -> None:
    """Server returns 401 when basic auth is enabled and no credentials provided."""
    response = requests.get(server, timeout=1)
    assert response.status_code == 401


def test_returns_200_with_valid_credentials(server: str) -> None:
    """Server returns 200 when valid basic auth credentials are provided."""
    credentials = base64.b64encode(b"george:vandelay").decode("ascii")
    response = requests.get(
        server,
        headers={"Authorization": f"Basic {credentials}"},
        timeout=1,
    )
    assert response.status_code == 200

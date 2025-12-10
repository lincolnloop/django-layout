import os
import socket
import subprocess
import time
import typing as t

import pytest

if t.TYPE_CHECKING:
    from collections.abc import Iterator


def _wait_for_server(host: str, port: int, timeout: float = 10.0) -> None:
    """Wait for server to accept connections."""
    start = time.monotonic()
    while time.monotonic() - start < timeout:  # pragma: no branch
        try:
            with socket.create_connection((host, port), timeout=1):
                return
        except OSError:
            time.sleep(0.1)
    msg = f"Server at {host}:{port} did not start within {timeout}s"  # pragma: no cover
    raise TimeoutError(msg)  # pragma: no cover


@pytest.fixture(scope="module")
def server(
    request: pytest.FixtureRequest,
    worker_id: str,
) -> Iterator[str]:
    """Start a live server for testing.

    Returns the base URL of the server.

    Use the `server_env` marker at module level to pass additional environment
    variables:
        pytestmark = pytest.mark.server_env({"BASIC_AUTH_CREDENTIALS": "user:pass"})
    """
    host = "127.0.0.1"
    port = 8100 + (0 if worker_id == "master" else int(worker_id.replace("gw", "")))
    env = os.environ.copy()

    for marker in request.node.iter_markers("server_env"):
        env.update(marker.args[0])

    proc = subprocess.Popen(  # noqa: S603
        ["/app/.venv/bin/gunicorn", "{{ project_name }}.wsgi", "-b", f"{host}:{port}"],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        _wait_for_server(host, port)
        yield f"http://{host}:{port}"
    finally:
        proc.terminate()
        proc.wait(timeout=5)

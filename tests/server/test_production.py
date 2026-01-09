import pytest
import requests

pytestmark = pytest.mark.server_env({"DJANGO_ENV": "production"})


def test_redirects_to_https_without_proxy_header(server: str) -> None:
    """Server redirects to HTTPS when X-Forwarded-Proto header is missing."""
    response = requests.get(server, allow_redirects=False, timeout=1)
    assert response.status_code == 301
    assert response.headers["Location"].startswith("https://")


def test_serves_request_with_proxy_header(server: str) -> None:
    """Server serves request when X-Forwarded-Proto: https header is present."""
    response = requests.get(server, headers={"X-Forwarded-Proto": "https"}, timeout=1)
    assert response.status_code == 200


def test_hsts_header(server: str) -> None:
    """Server sends HSTS header with preload directive."""
    response = requests.get(server, headers={"X-Forwarded-Proto": "https"}, timeout=1)
    hsts = response.headers["Strict-Transport-Security"]
    assert "max-age=31536000" in hsts
    assert "preload" in hsts


def test_content_type_nosniff(server: str) -> None:
    """Server sends X-Content-Type-Options: nosniff header."""
    response = requests.get(server, headers={"X-Forwarded-Proto": "https"}, timeout=1)
    assert response.headers["X-Content-Type-Options"] == "nosniff"


def test_x_frame_options(server: str) -> None:
    """Server sends X-Frame-Options: DENY header."""
    response = requests.get(server, headers={"X-Forwarded-Proto": "https"}, timeout=1)
    assert response.headers["X-Frame-Options"] == "DENY"


def test_referrer_policy(server: str) -> None:
    """Server sends Referrer-Policy header."""
    response = requests.get(server, headers={"X-Forwarded-Proto": "https"}, timeout=1)
    assert response.headers["Referrer-Policy"] == "same-origin"


def test_content_security_policy(server: str) -> None:
    """Server sends Content-Security-Policy header."""
    response = requests.get(server, headers={"X-Forwarded-Proto": "https"}, timeout=1)
    csp = response.headers["Content-Security-Policy"]
    assert "default-src 'self'" in csp

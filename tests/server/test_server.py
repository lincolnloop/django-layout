import requests


def test_admin_login_page(server: str) -> None:
    """Admin login page returns 200."""
    response = requests.get(f"{server}/{{ project_name }}-admin/login/", timeout=1)
    assert response.status_code == 200


def test_static_css_bundle(server: str) -> None:
    """Static CSS bundle is served."""
    response = requests.get(f"{server}/static/bundles/main.css", timeout=1)
    assert response.status_code == 200

import typing as t

from django.urls import path
from pytest_django.asserts import assertTemplateUsed

if t.TYPE_CHECKING:
    from django.http import HttpRequest
    from django.test import Client
    from pytest_django.fixtures import SettingsWrapper


def error_view(request: HttpRequest) -> None:
    """View that raises a server error."""
    raise ValueError


# Test URLconf that extends the base project URLs
urlpatterns = [path("error/", error_view)]


def test_404_page(client: Client) -> None:
    response = client.get("/non-existent-page/")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


def test_500_page(client: Client, settings: SettingsWrapper) -> None:
    settings.ROOT_URLCONF = "tests.test_error_pages"
    client.raise_request_exception = False
    response = client.get("/error/")
    assert response.status_code == 500
    assertTemplateUsed(response, "500.html")

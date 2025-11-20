import typing as t

from pytest_django.asserts import assertTemplateUsed

if t.TYPE_CHECKING:
    from django.test import Client


def test_404_page(client: Client) -> None:
    response = client.get("/non-existent-page/")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")

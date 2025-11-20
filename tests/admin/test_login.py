import typing as t

from django.urls import reverse_lazy

if t.TYPE_CHECKING:
    from django.test import Client

index_url = reverse_lazy("admin:index")
login_url = reverse_lazy("admin:login")


def test_anonymous_request_redirects_to_login_page(client: Client) -> None:
    response = client.get(index_url)
    assert response.status_code == 302

    expected = f"{login_url}?next={index_url}"
    assert response["location"] == expected

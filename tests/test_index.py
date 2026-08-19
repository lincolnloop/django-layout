import re
import typing as t

if t.TYPE_CHECKING:
    from django.test import Client


def test_index_page(client: Client) -> None:
    response = client.get("/")
    assert response.status_code == 200


def test_index_page_inline_style_carries_csp_nonce(client: Client) -> None:
    """
    The inline <style> block relies on `{% csp_nonce_attr %}`, which prettier
    will happily split across lines. Django's tag regex is not DOTALL, so a
    split tag renders as literal text and the style block stops loading.
    """
    response = client.get("/")
    match = re.search(r'<style nonce="([^"]+)">', response.content.decode())
    assert match, "inline <style> is missing its CSP nonce"
    csp = response.headers["Content-Security-Policy"]
    assert f"'nonce-{match.group(1)}'" in csp

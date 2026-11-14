from django.template import Context, Template


def test_multiline_template_tag_renders() -> None:
    """Prettier's jinja-template parser formats wrapped tags across lines.

    Django's lexer leaves a {% %} containing a newline as literal text; the
    tag_re patch in project_name/__init__.py makes it parse as a tag.
    """
    template = Template("{%\n  if True\n%}hello{%\n  endif\n%}")

    assert template.render(Context()) == "hello"

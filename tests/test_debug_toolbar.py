"""Tests related to stories debug toolbar panel."""
import pytest
from bs4 import BeautifulSoup


@pytest.mark.parametrize(("url", "count"), [("/", 0), ("/story/", 1), ("/admin/", 2)])
def test_debug_toolbar_panel(client, url, count):
    """Stories panel shoud appear in debug toolbar."""
    response = client.get(url)
    content = response.content.decode("utf-8")
    query = BeautifulSoup(content, "html.parser")
    [button] = query.select("li#djdt-StoriesPanel")
    [link] = button.select("a.StoriesPanel")
    word = "story" if count == 1 else "stories"
    assert link["title"] == f"Context and execution path of {count} {word}"
    word = "call" if count == 1 else "calls"
    assert " ".join(link.text.split()) == f"Stories {count} {word}"

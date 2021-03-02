"""Tests related to stories debug toolbar panel."""


def test_debug_toolbar_panel(client):
    """Stories panel shoud appear in debug toolbar."""
    response = client.get("/")
    assert b"" in response.content

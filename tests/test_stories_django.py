"""Tests related to stories_django module."""
from django.apps import AppConfig

from stories_django import default_app_config
from stories_django.apps import StoriesDjangoConfig
from stories_django.debug_toolbar import StoriesPanel
from stories_django.exceptions import StoryDjangoError


def test_exception():
    """`StoryDjangoError` should be Exception subclass."""
    assert default_app_config == "stories_django.apps.StoriesDjangoConfig"
    assert issubclass(StoriesDjangoConfig, AppConfig)
    assert StoriesDjangoConfig.name == "stories_django"
    assert StoriesPanel.template == "debug_toolbar/panels/stories.html"
    assert issubclass(StoryDjangoError, Exception)

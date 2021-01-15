"""Stories library integration with Django Debug Toolbar."""
from stories.contrib.debug_toolbars.django import StoriesPanel


StoriesPanel.template = "debug_toolbar/panels/stories.html"

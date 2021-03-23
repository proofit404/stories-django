# Debug Toolbar

## Configuration

Make sure that `'debug_toolbar'` application is
[set up properly](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html).

Than in addition to the debug toolbar settings make following changes to the
project settings:

```pycon

>>> from debug_toolbar.settings import PANELS_DEFAULTS

>>> INSTALLED_APPS = [
...     ...,
...     "stories_django",
...     ...,
... ]

>>> DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + [
...     "stories_django.debug_toolbar.StoriesPanel",
... ]

```

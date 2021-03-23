from debug_toolbar.settings import PANELS_DEFAULTS


SECRET_KEY = "*"

DEBUG = True

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "debug_toolbar",
    "stories_django",
    "django_project",
]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

TEMPLATES = [
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True}
]

ROOT_URLCONF = "django_project.urls"

STATIC_URL = "/static/"

DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + ["stories_django.debug_toolbar.StoriesPanel"]

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": "django_project.settings.show_toolbar"}


def show_toolbar(request):
    return True

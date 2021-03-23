import debug_toolbar
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.urls import include
from django.urls import path
from django.urls import re_path

from django_project.views import AdminView
from django_project.views import IndexView
from django_project.views import StoryView


urlpatterns = [
    re_path(r"^static/(?P<path>.*)$", serve),
    path("__debug__/", include(debug_toolbar.urls)),
    path("", IndexView.as_view()),
    path("story/", StoryView.as_view()),
    path("admin/", AdminView.as_view()),
]

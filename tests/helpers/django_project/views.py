from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View

from django_project.services import Action
from django_project.services import Admin


class IndexView(TemplateView):
    """The view."""

    template_name = "index.html"


class StoryView(View):
    """The view."""

    def get(self, request):
        """Do stuff using story."""
        action = Action()
        action.do(foo=1, bar=2)
        return render(request, "index.html")


class AdminView(View):
    """The view."""

    def get(self, request):
        """Do stuff using story."""
        action = Action()
        action.do(foo=1, bar=2)
        admin = Admin()
        admin.do()
        return render(request, "index.html")

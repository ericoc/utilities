from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """Index page."""
    extra_context = {"TITLE": "Utility"}
    http_method_names = ("get",)
    template_name = "index.html"

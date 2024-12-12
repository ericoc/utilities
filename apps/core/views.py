from django.views.generic.base import TemplateView


class CoreIndexView(TemplateView):
    """Index page."""
    template_name = "core_index.html"

from django.conf import settings
from django.views.generic.base import TemplateView


class BaseView(TemplateView):
    """Base view."""
    http_method_names = ("get",)
    template_name = "index.html"
    title = "Utilities"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["debug"] = settings.DEBUG
        context["title"] = self.title
        return context


class IndexView(BaseView):
    """Index page."""

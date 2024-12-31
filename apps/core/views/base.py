from django.conf import settings
from django.views.generic.base import TemplateView


class BaseView(TemplateView):
    """Base view."""
    http_method_names = ("get",)
    # icon = None
    template_name = "utility.html"
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timezone"] = settings.TIME_ZONE
        context["title"] = self.title.replace("_", " ").title()
        context["website_title"] = settings.WEBSITE_TITLE
        return context

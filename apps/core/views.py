from django.conf import settings
from django.views.generic.base import TemplateView


class BaseView(TemplateView):
    """Base view."""
    http_method_names = ("get",)
    template_name = "utility.html"
    color = None
    page_length = 12
    thresholds = ()
    time_format = None
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["color"] = self.color
        context["debug"] = settings.DEBUG
        context["page_length"] = self.page_length
        context["thresholds"] = self.thresholds
        context["time_format"] = self.time_format
        context["timezone"] = settings.TIME_ZONE
        context["title"] = self.title
        context["website_title"] = settings.WEBSITE_TITLE
        return context


class IndexView(BaseView):
    """Index view."""
    template_name = "index.html"
    title = "Home"

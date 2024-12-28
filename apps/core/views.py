from django.conf import settings
from django.views.generic.base import TemplateView


class BaseView(TemplateView):
    """Base template view."""
    http_method_names = ("get",)
    template_name = "utility.html"
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timezone"] = settings.TIME_ZONE
        context["title"] = self.title
        context["website_title"] = settings.WEBSITE_TITLE
        return context


class IndexView(BaseView):
    """Main/index view."""
    template_name = "index.html"
    title = "Home"


class UtilityView(BaseView):
    """Base view for utility usage data."""
    color = None
    datatable_time_format = None
    template_name = "utility.html"
    thresholds = ()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["color"] = self.color
        context["datatable_time_format"] = self.datatable_time_format
        context["thresholds"] = self.thresholds
        return context

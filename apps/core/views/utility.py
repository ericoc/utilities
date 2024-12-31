from django.apps import apps

from .base import BaseView


class UtilityView(BaseView):
    """Base utility view."""
    color = None
    datatable_time_format = None
    thresholds = ()
    utility = None

    def setup(self, request, *args, **kwargs):
        self.title = apps.get_app_config(request.path.replace("/", "")).label
        return super().setup(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["color"] = self.color
        context["datatable_time_format"] = self.datatable_time_format
        # context["icon"] = self.icon
        context["thresholds"] = self.thresholds
        return context

from django.apps import apps
from django.conf import settings

from .base import BaseView


class UtilityView(BaseView):
    """Base utility view."""
    color = ""
    datatables_fmt = ""
    long_name = ""
    short_name = ""
    thresholds = ()
    utility = ""
    utility_settings = {}

    def setup(self, request, *args, **kwargs):
        self.utility = apps.get_app_config(request.path.replace("/", "")).label
        print(self.utility)
        self.utility_settings = settings.UTILITIES.get(self.utility, {})
        print(self.utility_settings)
        self.color = self.utility_settings.get("color", "")
        self.datatables_fmt = self.utility_settings.get("datatables_fmt", "")
        self.long_name = self.utility_settings.get("long", "")
        self.short_name = self.utility_settings.get("short", "")
        self.title = apps.get_app_config(request.path.replace("/", "")).label
        self.thresholds = self.utility_settings.get("thresholds", "")
        return super().setup(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["datatables_fmt"] = self.datatables_fmt
        context["long_name"] = self.long_name
        context["short_name"] = self.short_name
        context["thresholds"] = self.thresholds
        return context

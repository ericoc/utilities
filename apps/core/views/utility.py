from django.apps import apps

from .base import BaseView


class UtilityView(BaseView):
    """Base utility view."""
    label = ""
    utility = ""

    def setup(self, request, *args, **kwargs):
        self.label = apps.get_app_config(request.path.replace("/", "")).label
        self.utility = self.utilities.get(self.label, {})
        self.color = self.utility.get("color", self.color)
        self.title = self.utility.get("title", self.title)
        return super().setup(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["label"] = self.label.replace("_", "-")
        context["utility"] = self.utility
        return context

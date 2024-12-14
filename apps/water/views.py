from django.views.generic import TemplateView

from .models import WaterUsage


class WaterView(TemplateView):
    """Water usage view."""
    extra_context = {"TITLE": "Water"}
    http_method_names = ("get",)
    model = WaterUsage
    template_name = "water.html"

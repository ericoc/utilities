from django.views.generic import TemplateView

from .models import ElectricUsage


class ElectricView(TemplateView):
    """Electric usage view."""
    extra_context = {"TITLE": "Electric"}
    http_method_names = ("get",)
    model = ElectricUsage
    template_name = "electric.html"

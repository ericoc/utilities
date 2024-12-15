from django.views.generic import TemplateView

from .models import GasUsage


class GasView(TemplateView):
    """Natural gas usage view."""
    extra_context = {"TITLE": "(Natural) Gas"}
    http_method_names = ("get",)
    model = GasUsage
    template_name = "gas.html"

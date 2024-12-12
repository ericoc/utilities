from django.views.generic import TemplateView

from .models import WaterUsage


class WaterUsageBaseView(TemplateView):
    """Base water usage view."""
    http_method_names = ("get",)
    model = WaterUsage
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["TITLE"] = self.title
        return context


class WaterIndexView(WaterUsageBaseView):
    """Water usage index view."""
    template_name = "water_index.html"
    title = "Index"


class WaterTableView(WaterUsageBaseView):
    """Water usage table view."""
    template_name = "water_table.html"
    title = "Table"


class WaterChartView(WaterUsageBaseView):
    """Water usage chart view."""
    template_name = "water_chart.html"
    title = "Chart"

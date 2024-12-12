from django.views.generic import TemplateView

from .models import ElectricUsage


class ElectricUsageBaseView(TemplateView):
    """Base electric usage view."""
    http_method_names = ("get",)
    model = ElectricUsage
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["TITLE"] = self.title
        return context


class ElectricIndexView(ElectricUsageBaseView):
    """Electric usage index view."""
    template_name = "electric_index.html"
    title = "Index"


class ElectricTableView(ElectricUsageBaseView):
    """Electric usage table view."""
    template_name = "electric_table.html"
    title = "Table"


class ElectricChartView(ElectricUsageBaseView):
    """Electric usage chart view."""
    template_name = "electric_chart.html"
    title = "Chart"

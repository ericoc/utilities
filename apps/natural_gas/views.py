from apps.core.views import BaseView


class NaturalGasView(BaseView):
    """Natural gas usage view."""
    template_name = "natural_gas.html"
    title = "Natural Gas"
    unit = "Hundreds of Cubic Feet"
    unit_short = "CCF"

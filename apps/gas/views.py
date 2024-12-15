from apps.core.views import BaseView


class GasView(BaseView):
    """Natural gas usage view."""
    template_name = "gas.html"
    title = "(Natural) Gas"

from apps.core.views import BaseView


class ElectricView(BaseView):
    """Electric usage view."""
    template_name = "electric.html"
    title = "Electric"

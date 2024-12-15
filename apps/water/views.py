from apps.core.views import BaseView


class WaterView(BaseView):
    """Water usage view."""
    template_name = "water.html"
    title = "Water"

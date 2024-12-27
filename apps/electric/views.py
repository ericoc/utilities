from apps.core.views import BaseView


class ElectricView(BaseView):
    """Electric usage view."""
    color = "e4a11b"
    thresholds = (1, 0.75, 0.5)
    time_format = "DataTable.render.datetime('DDDD, tt')"
    title = "Electric"

from apps.core.views import BaseView


class NaturalGasView(BaseView):
    """Natural gas usage view."""
    color = "853cfd"
    thresholds = (50, 25, 10)
    time_format = "DataTable.render.datetime('MMMM y')"
    title = "Natural Gas"

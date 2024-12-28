from apps.core.views import UtilityView

from .models import NaturalGasUsage


class NaturalGasView(UtilityView):
    """Natural gas usage view."""
    color = "853cfd"
    datatable_time_format = "datetime('MMMM y')"
    model = NaturalGasUsage
    thresholds = (50, 25, 10)
    title = "Natural Gas"

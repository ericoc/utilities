from apps.core.views import UtilityView

from .models import ElectricUsage


class ElectricView(UtilityView):
    """Electric usage view."""
    color = "e4a11b"
    datatable_time_format = "datetime('DDDD, tt')"
    model = ElectricUsage
    thresholds = (1, 0.75, 0.5)
    title = "Electric"

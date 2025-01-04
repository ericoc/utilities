from apps.core.views.utility import UtilityView


class ElectricView(UtilityView):
    """Electric usage view."""
    color = "e4a11b"
    datatable_time_format = "datetime('DDDD, tt')"
    default_start = {"days": 366.5}
    thresholds = (1, 0.75, 0.5)

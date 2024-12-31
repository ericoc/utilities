from apps.core.views.utility import UtilityView


class ElectricView(UtilityView):
    """Electric usage view."""
    color = "e4a11b"
    datatable_time_format = "datetime('DDDD, tt')"
    # icon = "lightbulb"
    thresholds = (1, 0.75, 0.5)

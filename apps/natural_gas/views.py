from apps.core.views.utility import UtilityView


class NaturalGasView(UtilityView):
    """Natural gas usage view."""
    color = "#853cfd"
    datatable_time_format = "datetime('MMMM y')"
    thresholds = (50, 25, 10)

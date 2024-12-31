from apps.core.views.utility import UtilityView


class WaterView(UtilityView):
    """Water usage view."""
    color = "2caffe"
    datatable_time_format = "date('DDDD')"
    # icon = "droplet"
    thresholds = (100, 75, 50)

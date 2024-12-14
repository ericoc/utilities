from django.urls import path

from .views import WaterChartView, WaterTableView


urlpatterns = [
    path("", WaterTableView.as_view(), name="water_index"),
    path("chart/", WaterChartView.as_view(), name="water_chart"),
    path("table/", WaterTableView.as_view(), name="water_table"),
]

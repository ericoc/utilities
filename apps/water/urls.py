from django.urls import path

from .views import WaterIndexView, WaterChartView, WaterTableView


urlpatterns = [
    path("", WaterIndexView.as_view(), name="index"),
    path("chart/", WaterChartView.as_view(), name="chart"),
    path("table/", WaterTableView.as_view(), name="table"),
]

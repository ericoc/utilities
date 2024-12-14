from django.urls import path

from .views import ElectricChartView, ElectricTableView


urlpatterns = [
    path("", ElectricTableView.as_view(), name="electric_index"),
    path("chart/", ElectricChartView.as_view(), name="electric_chart"),
    path("table/", ElectricTableView.as_view(), name="electric_table"),
]

from django.urls import path

from .views import ElectricIndexView, ElectricChartView, ElectricTableView


urlpatterns = [
    path("", ElectricIndexView.as_view(), name="electric_index"),
    path("chart/", ElectricChartView.as_view(), name="electric_chart"),
    path("table/", ElectricTableView.as_view(), name="electric_table"),
]

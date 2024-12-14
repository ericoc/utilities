from django.urls import path

from .views import ElectricView, ElectricChartView, ElectricTableView


urlpatterns = [
    path("", ElectricView.as_view(), name="electric")
]

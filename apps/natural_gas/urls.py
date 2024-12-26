from django.urls import path

from .views import NaturalGasView


urlpatterns = [
    path("", NaturalGasView.as_view(), name="natural_gas")
]

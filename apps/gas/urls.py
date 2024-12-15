from django.urls import path

from .views import GasView


urlpatterns = [
    path("", GasView.as_view(), name="gas")
]

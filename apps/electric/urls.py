from django.urls import path

from .views import ElectricView

urlpatterns = [
    path("", ElectricView.as_view(), name="electric")
]

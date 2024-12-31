from django.urls import path

from .views import WaterView


urlpatterns = [path("", WaterView.as_view(), name="water")]

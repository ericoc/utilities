from django.urls import path

from .views import CoreIndexView


urlpatterns = [
    path("", CoreIndexView.as_view(), name="core_index"),
]

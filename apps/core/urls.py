from django.urls import path

from .views.index import IndexView
from .views.add import AddView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add/", AddView.as_view(), name="add")
]

from django.urls import path

from .views.add import AddView
from .views.home import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add/", AddView.as_view(), name="add")
]

from django.urls import path

from .views.home import HomeView


urlpatterns = [path("", HomeView.as_view(), name="home")]

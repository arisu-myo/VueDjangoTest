from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.Home_index.as_view(), name="home"),
    path("<path>", views.Home_index.as_view(), name="home")
]

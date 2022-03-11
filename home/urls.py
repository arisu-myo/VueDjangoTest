from django.urls import path, re_path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.Home_index.as_view(), name="home"),
    re_path("^(?!media).*$", views.Home_index.as_view(), name="home"),
]

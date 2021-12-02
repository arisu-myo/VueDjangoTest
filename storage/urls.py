from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path("upload/", views.UploadFIle.as_view(), name="upload")
]

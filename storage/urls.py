from django.urls import path
from . import views

app_name = "storage"

urlpatterns = [
    path("upload/", views.UploadFile.as_view(), name="upload"),
    path("list/", views.FileList.as_view(), name="file_list")
]

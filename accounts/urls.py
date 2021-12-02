from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.CreateUser.as_view(), name="create_user"),
    path("login/", views.LoginUserData.as_view(), name="user_login"),
    path("login/auto/", views.UserData.as_view(), name="user_autologin"),
    path("logout/", views.Logout.as_view(), name="user_logout"),
    path("password/chenge/", views.PasswordChenge.as_view(), name="password_chege"),
    path("data/chenge/", views.UserDataChange.as_view(), name="user_data_chenge"),
    path("image/chenge/", views.UserImageChange.as_view(), name="image_chenge")
]

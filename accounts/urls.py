from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.CreateUser.as_view(), name="create_user"),
    path("login/", views.LoginUserData.as_view(), name="user_login"),
    path("logout/", views.Logout.as_view(), "user_logout"),
    path("password/chenge/", views.PasswordChenge.as_view(), name="password_chege"),
]

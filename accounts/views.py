from django.http.response import Http404
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from . import serializer
from config.settings import BASE_DIR

import subprocess


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSignupSerializer
    permission_classes = (permissions.AllowAny,)


class LoginUserData(TokenObtainPairView):
    # queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = (serializer.UserLoginSerializer)


class UserData(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get(self, request):
        return Response(
            data={
                "name": request.user.username,
                "email": request.user.email,
                "user_icon": request.user.user_image_origin.url
            },
            status=status.HTTP_200_OK)


class PasswordChenge(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.UserPasswordChengeSerializer
    lookup_field = "passowrd"
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(password=self.request.user.password)
            return instance
        except User.DoesNotExist:
            raise Http404


class UserDataChange(generics.UpdateAPIView):
    premission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializer.UserDataChengeSerializer
    lookup_field = "email"
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user.email)
            return instance
        except User.DoesNotExist:
            raise Http404


class Logout(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get(self, request):

        subprocess.Popen(
            ["pipenv", "run", "python", "manage.py", "flushexpiredtokens"],
            cwd=BASE_DIR,
            shell=True
        )

        # User フィルターを追加する
        token = OutstandingToken.objects.all().filter(user=request.user)
        black_token = BlacklistedToken.objects.all()
        black_list = []

        for bt in black_token:
            black_list.append(bt.token)

        try:
            for t in token:

                if t in black_list:
                    pass
                else:
                    RefreshToken(t.token).blacklist()

        except Exception as error:
            return Response(data={
                "error": str(error)
            },
                status=status.HTTP_401_UNAUTHORIZED)

        return Response(data={"message": "delete jwt"}, status=status.HTTP_200_OK)


class UserImageChange(generics.UpdateAPIView):
    pass

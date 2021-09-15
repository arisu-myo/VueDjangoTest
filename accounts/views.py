from django.http.response import Http404
from rest_framework import permissions, status, generics

from rest_framework.response import Response
# from rest_framework import status

from .models import User
from . import serializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
# from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSignupSerializer
    permission_classes = (permissions.AllowAny,)


class LoginUserData(TokenObtainPairView):
    # queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = (serializer.UserLoginSerializer)


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


class Logout(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get(self, request):

        return Response(data={
            "message": "まだテストログアウトは実装できていません"
        },
            status=status.HTTP_200_OK)

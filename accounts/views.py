from django.http.response import Http404
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from . import serializer


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


class Logout(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get(self, request):

        # User フィルターを追加する
        # token = OutstandingToken.objects.filter(user=request.user.pk)
        token = OutstandingToken.objects.all().filter(user=request.user)

        # try:
        for t in token:
            RefreshToken(t.token).blacklist()
        # except Exception:
        #     return Response(
        #         data={"error": "JWT_token is invalid"},
        #         status=status.HTTP_401_UNAUTHORIZED
        #     )

        return Response(data={"message": "delete jwt"}, status=status.HTTP_200_OK)

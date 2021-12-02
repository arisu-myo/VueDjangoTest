# from django.contrib.auth.forms import PasswordChangeForm
# import base64
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
# from django.contrib.auth import forms
# from rest_framework.response import Response
# from rest_framework import status
from django.contrib.auth import authenticate, login
from config.settings import DEBUG


class UserSignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=False,
        style={"input_type": "password"})
    password2 = serializers.CharField(
        write_only=True,
        required=False,
        style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

    def create(self, validated_data):
        if validated_data["password1"] != validated_data["password2"]:
            raise serializers.ValidationError(
                {"error": "パスワード2つの値が一致しません"}
            )

        return User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password1"])


class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token["email"] = user.email

        # try:
        #     # DB改変までの暫定処置
        #     file_data = open(str(user.user_image_origin), "rb").read()
        #     b64_data = base64.b64encode(file_data).decode("utf-8")
        #     # print(b64_data)
        #     token["icon"] = b64_data
        # except Exception:
        #     token["icon"] = None

        token["icon"] = user.user_image_origin.url

        return token

    def validate(self, attrs):
        # implement your logic here
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['name'] = str(refresh["name"])
        data["email"] = str(refresh["email"])
        data["user_icon"] = str(refresh["icon"])

        if DEBUG:
            user = authenticate(
                email=attrs["email"],
                password=attrs["password"])

            print(user)

            if user is not None:
                login(self.context.get("request"), user)

        return data


class UserPasswordChengeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        style={"input_type": "password"}
    )

    new_password = serializers.CharField(
        write_only=True,
        required=False,
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ("password", "new_password")

    def update(self, instance, validated_data):
        if not check_password(validated_data["password"], instance.password):
            print("not password chenge")
            raise serializers.ValidationError("Validation failed.")

        if "new_password" in validated_data:
            # print(validated_data["new_password"])
            instance.set_password(validated_data["new_password"])

        else:
            instance.super().update(instance, validated_data)
        instance.save()
        return instance


class UserDataChengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

    def update(self, instance, validated_data):
        if str(validated_data["username"]) == "":
            validated_data["username"] = instance.username
            print(instance.username)

        if str(validated_data["email"]) == "":
            validated_data["email"] = instance.email
            print(instance.email)

        instance.username = validated_data["username"]
        instance.email = validated_data["email"]
        instance.save()
        return instance


class UserImageChengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_image_origin",)

    def update(self, instance, validated_data):
        # print(validated_data)
        instance.user_image_origin = validated_data["user_image_origin"]
        instance.save()
        return instance

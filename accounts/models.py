from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill
import uuid
import os


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("not email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class ImageChnge:
    def get_image_path(self, filename):
        """ユーザーの画像をリネームする"""
        prefix = f"{self.id}/"
        img_name = str(uuid.uuid4()).replace("-", "")
        extension = os.path.splitext(filename)[-1]

        return prefix + img_name + extension


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    username = models.CharField(
        _("ユーザーネーム"),
        max_length=50,
        null=True
    )

    email = models.EmailField(
        _("メールアドレス"),
        max_length=254,
        unique=True
    )

    user_image_origin = models.ImageField(
        _("ユーザーアイコン"),
        upload_to=ImageChnge.get_image_path,
        default="static/default_image/defa.png",
        blank=True, null=True
    )

    # user_image_s = ImageSpecField(
    #     source="user_image_origin",
    #     processors=[ResizeToFill(250, 250)],
    #     format="JPEG"
    # )

    # user_image_ss = ImageSpecField(
    #     source="user_image_origin",
    #     processors=[ResizeToFill(45, 45)],
    #     format="JPEG"
    # )

    date_joined = models.DateTimeField(
        _("登録日"),
        default=timezone.now
    )

    last_login = models.DateTimeField(
        _("最終ログイン日"),
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)  # account active
    is_admin = models.BooleanField(default=False)  # staff権限

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    # 以下よくわからんが使わなかったらerrorが発生するため使用する
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app [app_label]?"
        return True

    def pulish(self):
        self.last_login = timezone.now()
        self.save()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

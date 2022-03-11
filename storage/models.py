from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from django.utils import timezone
import uuid
import os

# Create your models here.


class file_path:
    def path_name(self, filename):

        prefix = f"{self.user_link.id}/"
        img_name = str(uuid.uuid4()).replace("-", "")
        extension = os.path.splitext(filename)[-1]

        return f"{prefix}{img_name}/{img_name}{extension}"


class Files(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user_link = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    file_name = models.CharField(
        _("ファイルタイトル"),
        max_length=50,
    )

    file_description = models.TextField(
        _("ファイル説明"),
        blank=True
    )

    file = models.FileField(
        # upload_to=file_path.path_name,
        upload_to=file_path.path_name
    )

    file_m3u8 = models.FileField(
        null=True, blank=True
    )

    public = models.BooleanField(
        default=False, help_text="すべてのユーザーに公開する。"
    )

    upload_data = models.DateTimeField(
        _("作成日"),
        default=timezone.now
    )

    def __str__(self):
        return self.file_name

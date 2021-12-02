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

        return prefix + img_name + extension


class Files(models.Model):

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
        upload_to=file_path.path_name
    )

    upload_data = models.DateTimeField(
        _("作成日"),
        default=timezone.now
    )

    def __str__(self):
        return self.file_name
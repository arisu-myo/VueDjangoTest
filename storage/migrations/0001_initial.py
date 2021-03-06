# Generated by Django 3.2 on 2021-12-08 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import storage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50, verbose_name='ファイルタイトル')),
                ('file_description', models.TextField(blank=True, verbose_name='ファイル説明')),
                ('file', models.FileField(upload_to=storage.models.file_path.path_name)),
                ('upload_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('user_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

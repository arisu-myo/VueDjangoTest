# Generated by Django 3.2 on 2022-01-29 09:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_files_file_m3u8'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

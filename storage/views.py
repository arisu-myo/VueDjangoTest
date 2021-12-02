from rest_framework import permissions, generics

from . import serializer
from .models import Files


class UploadFIle(generics.CreateAPIView):
    queryset = Files.objects.all()
    serializer_class = serializer.UploadSerializer
    permission_classes = (permissions.IsAuthenticated,)

# ffmpeg でm3u8とtsファイルの生成（ストリーミング用のファイル河口）
# それをHLS.ｊｓ？？？でストリーミングできるっぽい？？？？
# 結論意味わからん

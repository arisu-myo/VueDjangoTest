from rest_framework import permissions, generics, status
from rest_framework.response import Response
from . import serializer
from .models import Files


class UploadFile(generics.CreateAPIView):
    queryset = Files.objects.all()
    serializer_class = serializer.UploadSerializer
    permission_classes = (permissions.IsAuthenticated,)

# ffmpeg でm3u8とtsファイルの生成（ストリーミング用のファイル河口）
# それをHLS.ｊｓ？？？でストリーミングできるっぽい？？？？
# 結論意味わからん


class FileList(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Files.objects.all()

    def get(self, request):
        file_lists = self.queryset.filter(user_link=request.user)
        lists = {data.file_name: data.file_m3u8.url for data in file_lists}
        # for data in file_lists:
        #     print(data.file.url)
        # print(lists)
        return Response(data=lists, status=status.HTTP_200_OK)

import uuid
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
    permission_classes = (permissions.AllowAny,)
    queryset = Files.objects.all()

    def get(self, request):

        # 見本
        # if "id" in request.GET:
        #     id = request.GET["id"]

        # パラメーターがUUID以外の場合はエラー
        if "user" in request.GET:
            is_p = False
            try:
                uuid.UUID(str(request.GET["user"]))
            except Exception:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            is_p = True  # P＝パラメーターの略

        # userが無い場合　Userが無い場合はすべてここで拾う
        if str(request.user) == "AnonymousUser":

            # userのパラメーターが無い　又は　空白の場合
            if is_p:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            if request.GET["user"] == "":
                return Response(status=status.HTTP_401_UNAUTHORIZED)

            # リストが空な場合Noneを返す
            file_lists = self.queryset.filter(
                user_link=request.GET["user"],
                public=True
            )
            if file_lists is None:
                return Response(data=None, status=status.HTTP_200_OK)

            # AnonymousUserの正常終了位置
            lists = {data.file_name: data.pk for data in file_lists}
            return Response(data=lists, status=status.HTTP_200_OK)

        # パラメーター情報が有る場合
        elif not is_p:
            # 要求者が本人だった場合
            if str(request.user.pk) == str(request.GET["user"]):
                file_lists = self.queryset.filter(user_link=request.user)
                lists = {data.file_name: data.pk for data in file_lists}
                return Response(data=lists, status=status.HTTP_200_OK)
            # 要求者が本人以外だった場合
            else:
                file_lists = self.queryset.filter(
                    user_link=request.GET["user"],
                    public=True
                )
                lists = {data.file_name: data.pk for data in file_lists}
                return Response(data=lists, status=status.HTTP_200_OK)

        # パラメーター情報が無い場合
        elif is_p:
            file_lists = self.queryset.filter(user_link=request.user)
            lists = {data.file_name: data.pk for data in file_lists}
            return Response(data=lists, status=status.HTTP_200_OK)

        else:
            return Response(
                data={"error": "期待された値ではない"},
                status=status.HTTP_400_BAD_REQUEST)


class VideoURL(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Files.objects.all()

    def get(self, request):
        if "id" not in request.GET:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # userが指定されてしない場合
        if "user" not in request.GET:

            # ログインしていない場合
            if str(request.user) == "AnonymousUser":
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # ログインしてる場合は本人のアカウントで試す
            else:
                filter_obj = self.queryset.filter(
                    user_link=request.user,
                    pk=str(request.GET["id"]),
                )
                url = [data.file_m3u8.url for data in filter_obj]
                return Response(
                    data=url[0],
                    status=status.HTTP_200_OK
                )
        else:

            # ログインしてるユーザーがパラメータと同じ場合
            if str(request.user.pk) == request.GET["user"]:
                filter_obj = self.queryset.filter(
                    user_link=request.user,
                    pk=str(request.GET["id"])
                )

                url = [data.file_m3u8.url for data in filter_obj]
                return Response(
                    data=url[0],
                    status=status.HTTP_200_OK
                )

            # それ以外は条件自体は整っているはずなのでpublicで検索
            else:
                filter_obj = self.queryset.filter(
                    user_link=request.GET["user"],
                    pk=str(request.GET["id"]),
                    public=True
                )

                url = [data.file_m3u8.url for data in filter_obj]
                return Response(
                    data=url[0],
                    status=status.HTTP_200_OK,
                )

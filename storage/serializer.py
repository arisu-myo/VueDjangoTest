from rest_framework import serializers
from .models import Files
# from .hls import ChengeHls
import os


class UploadSerializer(serializers.ModelSerializer):

    # user_link = serializers.ReadOnlyField(source=)
    # user_link = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # user_link = serializers.PrimaryKeyRelatedField(
    # many=True, read_only=True)

    class Meta:
        model = Files
        fields = ("file_name", "file_description", "file")

    def create(self, validated_data):

        # check data

        white_list = [".mp4", ".avi"]

        extension = os.path.splitext(
            str(validated_data["file"].name))[-1]
        print(extension)

        if extension not in white_list:
            raise serializers.ValidationError({"error": "許可されていな拡張子"})

        # input datas
        request = self.context.get("request")
        files = Files()
        files.user_link = request.user
        files.file_name = validated_data["file_name"]
        files.file_description = validated_data["file_description"]
        files.file = validated_data["file"]
        files.save()

        return files

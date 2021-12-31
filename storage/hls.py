# from .models import Files

import ffmpeg
import os
import time
import subprocess
from config import settings
# import asyncio

# ffmpeg自体はフォルダーを作成できないので注意


def encode_m3u8(file):

    filename = f"media/{file.file.name}"
    new_filename = str(file.file.name).split(".")[0]

    command = [
        "ffmpeg", "-y", "-i", filename,
        "-c:v", "copy", "-c:a", "copy",
        "-f", "hls", "-hls_time", "5",
        "-hls_playlist_type", "vod",
        "-hls_segment_filename", f"media/{new_filename}%3d.ts",
        f"media/{new_filename}.m3u8"
    ]

    subprocess.run(command, cwd=settings.BASE_DIR)

    return f"{new_filename}.m3u8"


def main():
    start = time.time()

    os.mkdir("video")
    input_video = input("変換するファイルを選択してください>>")
    stream = ffmpeg.input(input_video)
    # 音が反響する要修正
    audio = stream.audio
    # ぐちゃぐちゃしてるのも修正
    # 並列化等色々使ってより速度を上げるように
    # stream = ffmpeg.hflip(stream)
    print(stream)
    stream.filter("fps", fps=100)
    stream = ffmpeg.output(
        stream, audio,
        "video/output.m3u8",
        # vcodec="libx264",
        hls_time=2,
        movflags="faststart",
        hls_list_size=0,
        hls_playlist_type="vod"
    )

    ffmpeg.run(stream)
    end = time.time()

    print(f"実行時間：{end - start}")


def as_mp4():

    start = time.time()
    input_video = input("MP4へ変換するファイルを選択してください>>>")
    video = ffmpeg.input(input_video)
    audio = video.audio
    stream = ffmpeg.output(
        video, audio,
        "114514.mp4",
        vcodec="libx264",
        movflags="faststart",

    )
    ffmpeg.run(stream)
    end = time.time()

    print(f"実行時間：{end - start}")


if __name__ == '__main__':
    main()

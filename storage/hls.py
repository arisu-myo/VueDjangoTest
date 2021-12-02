# from .models import Files

import ffmpeg
import os
import time

# ffmpeg自体はフォルダーを作成できないので注意


class ChengeHls:
    def __init__(self, filename,):
        pass

    def is_mp4(self, filename):
        ext = self.extension(filename)
        print(ext)
        if ext != ".mp4":
            pass

    def extension(self, filename):
        return str(os.path.splitext(filename)[-1])


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
    stream.filter("fps", fps=60)
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

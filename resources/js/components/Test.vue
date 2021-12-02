<template>
  <div>
    <div>
      <!-- <video
        id="video"
        controls
        autoplay
        playsinline
        width="80%"
        height=""
        @click="controlVideo"
      ></video> -->
      <div style="width: 80%">
        <video-player :options="videoOptions" />
      </div>
      <!-- <button @click="this.videoPlay">video play</button> -->
    </div>
  </div>
</template>

<style scoped>
/* -43.65% */
.vjs_video_3-dimensions {
  position: relative;
  width: 100%;
  height: 0;
  padding-top: 56.25%;
}
</style>

<script>
import Hls from "hls.js";
import VideoPlayer from "./videojs.vue";

export default {
  components: {
    VideoPlayer,
  },
  data: () => {
    return {
      hls: new Hls({
        manifestLoadingTimeOut: 3000, // マスターマニフェストのタイムアウト(ミリ秒)
        manifestLoadingMaxRetry: 10, // マスターマニフェストを何回リトライするか
        manifestLoadingMaxRetryTimeout: 3000, // タイムアウトしたあとリトライするまでの最大待機時間(ミリ秒)
        levelLoadingTimeOut: 3000, // レベルマニフェストのタイムアウト(ミリ秒)
        levelLoadingMaxRetry: 10, // レベルマニフェストを何回リトライするか
        levelLoadingMaxRetryTimeout: 3000, // タイムアウトしたあとリトライするまでの最大待機時間(ミリ秒)
        fragLoadingTimeOut: 3000, // 動画データのタイムアウト(ミリ秒)
        fragLoadingMaxRetry: 10, // 動画データを何回リトライするか
        fragLoadingMaxRetryTimeout: 3000, // 動画データがタイムアウトしたあとリトライするまでの最大待機時間(ミリ秒)
        liveBackBufferLength: 0, // 再生し終わったデータを保持する長さ(秒)
      }),
      videoflg1: true,
      videoOptions: {
        controls: true,
        responsive: true,
        autoplay: false,
        sources: [
          {
            src: "media/video/output.m3u8",
            type: "application/x-mpegURL",
          },
        ],
      },
    };
  },
  methods: {
    controlVideo() {
      if (this.videoflg1) {
        this.videoflg1 = false;
        this.videoPlay();
      } else {
        // this.hls.destroy();
      }
    },

    videoPlay: function () {
      const video = document.getElementById("video");
      const videoUrl = "media/video/output.m3u8";
      if (Hls.isSupported()) {
        let hls = this.hls;
        hls.loadSource(videoUrl);
        hls.attachMedia(video);
        // video.play();
        // this.hls.on(hls.Evants.MANIFEST_PARSED,func  video.play();
        hls.on(Hls.Events.MANIFEST_PARSED, function () {
          video.play();
        });
      } else if (video.canPlayType("application/vnd.apple.mpegurl")) {
        video.src = videoUrl;
        video.addEventListener("canplay", () => {
          video.play();
        });
      }
    },
  },
};
</script>
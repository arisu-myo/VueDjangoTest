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
      <button @click="chengeVideo">test</button>
      <div style="width: 80%">
        <video-player :options="videoOptions" />
      </div>
      <!-- <video controls width="80%">
        <source
          src="media/1599366a-e30c-42fd-b2e8-9b41a41186be/3d6a2eaafbf0463a89c8241532a4a648.mp4"
        />
      </video> -->
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
import axios from "axios";
import { mapState } from "vuex";

export default {
  components: {
    VideoPlayer,
  },
  data: () => {
    return {
      video_url: null,
      hls: new Hls({}),
      videoflg1: true,
      videoOptions: {
        controls: true,
        responsive: true,
        autoplay: false,
        sources: [
          {
            // withCredentials: false,
            type: "application/x-mpegURL",
            // src: "/media/6b2ce74c-2e54-44e6-bc65-de88ccec641f/f5754471f7eb4ef8acc0370c35daab10/f5754471f7eb4ef8ac_1RiW1Q7.m3u8",
            // src: "",
          },
        ],
      },
    };
  },
  computed: {
    // ...mapState({
    //   VideoURL: (state) => state.pege.VideoURL,
    // }),
    createURL() {
      axios.get("api/file/list").then((responce) => {
        console.log(Object.values(responce.data)[0]);
        this.props.sources[0].src = Object.values(responce.data)[0];
        // this.VideoPlayer.src = Object.values(responce.data)[0];
      });
    },
  },
  methods: {},
};
</script>
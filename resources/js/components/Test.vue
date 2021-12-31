<template>
  <div>
    <div>
      <button @click="chengeVideo">test</button>
      <div style="width: 80%">
        <video-player :options="videoOptions" />
      </div>
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
import VideoPlayer from "./videojs.vue";
import axios from "axios";
import { mapState } from "vuex";

export default {
  components: {
    VideoPlayer,
  },
  data: () => {
    return {
      videoOptions: {
        controls: true,
        responsive: true,
        autoplay: false,
        sources: [
          {
            type: "application/x-mpegURL",
            src: "/",
          },
        ],
      },
    };
  },
  mounted() {
    axios.get("api/file/list").then((responce) => {
      console.log(Object.values(responce.data)[0]);
      this.videoOptions.sources[0].src = Object.values(responce.data)[0];
    });
  },

  methods: {},
};
</script>
<template>
  <video ref="videoPlayer" class="video-js">
    <source :src="src" type="application/x-mpegURL" />
  </video>
</template>



<script>
import videojs from "video.js";
import axios from "axios";
export default {
  name: "VideoPlayer",
  props: {
    options: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      player: null,
      src: "",
    };
  },
  mounted: async function () {
    await axios.get("api/file/list").then((responce) => {
      // console.log(Object.values(responce.data)[1]);
      this.src = Object.values(responce.data)[1];
    });

    this.player = videojs(
      this.$refs.videoPlayer,
      this.options,
      function onPlayerReady() {
        console.log("onPlayerReady", this);
      }
    );

    // console.log("mounted");
  },
  beforeDestroy() {
    if (this.player) {
      this.player.dispose();
    }
  },
};
</script>
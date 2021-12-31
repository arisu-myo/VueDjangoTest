<template>
  <video ref="videoPlayer" class="video-js"></video>
</template>



<script>
import videojs from "video.js";

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
    };
  },
  created() {
    // axios.get("api/file/list").then((responce) => {
    //   console.log(Object.values(responce.data)[0]);
    //   this.player.src = Object.values(responce.data)[0];
    // });
  },
  mounted() {
    this.player = videojs(
      this.$refs.videoPlayer,
      this.options,
      function onPlayerReady() {
        console.log("onPlayerReady", this);
      }
    );
  },
  beforeDestroy() {
    if (this.player) {
      this.player.dispose();
    }
  },
};
</script>
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
    let vid = this.$route.query.vid;
    let user = this.$route.query.user;

    if (user != undefined) {
      await axios
        .get(`api/file/video/?id=${vid}&user=${user}`)
        .then((responce) => {
          console.log(responce.data);
          this.src = responce.data;
        });
    } else {
      await axios.get(`api/file/video/?id=${vid}`).then((responce) => {
        console.log(responce.data);
        this.src = responce.data;
      });
    }

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
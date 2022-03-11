<template>
  <div>
    <div>
      <!-- <button @click="chengeVideo">test</button> -->
      <div class="douga80">
        <video-player :options="videoOptions" />
      </div>
    </div>
  </div>
</template>
<style scoped>
/* -43.65% */

.douga80 {
  width: 100vw;
}

.vjs_video_3-dimensions {
  position: relative;
  width: 100%;
  height: 0vh;
  padding-top: 56.25%;
}
</style>

<script>
import VideoPlayer from "./videojs.vue";

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
      },
    };
  },
};
</script>
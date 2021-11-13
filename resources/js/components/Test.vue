<template>
  <div id="test">
    <croppa
      v-model="myCroppa"
      :width="350"
      :height="350"
      placeholder="画像を選択してください。"
      canvas-color="transparent"
      :prevent-white-space="true"
    >
    </croppa>
    <button @click="generateImage">画像作成</button>
    <br />
    <img class="output" :src="imgUrl" />
  </div>
</template>

<script>
import cookies from "vue-cookies";
import axios from "axios";
export default {
  name: "test",
  data() {
    return {
      msg: null,
      myCroppa: null,
      imgUrl: "",
    };
  },
  methods: {
    async generateImage() {
      this.myCroppa.generateBlob((blob) => {
        let url = window.URL.createObjectURL(blob);
        console.log(url);
      });
    },
  },
};
</script>
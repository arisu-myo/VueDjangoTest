<template>
  <div id="test">
    <button @click="testFunction()">test</button>
    <img v-bind:src="test_image" v-if="test_image" />
    <button @click="DownloadTest()">download</button>
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
      test_image: null,
    };
  },
  methods: {
    testFunction() {
      let img = "/static/user_image/e923752dec3d4d419f6cdc28900e4f72.jpg";
      axios
        .get(img, {
          responseType: "blob",
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
          let blob = new Blob([response.data]);
          this.test_image = window.URL.createObjectURL(blob);
          console.log(this.test_image);
        });
    },
    DownloadTest() {
      let link = document.createElement("a");
      link.href = this.test_image;
      link.download = "test.png";
      link.click();
    },
  },
};
</script>
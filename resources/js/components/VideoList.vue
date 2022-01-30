<template>
  <div>
    <h1>heloo</h1>

    <li :v-for="file_id in filelist">
      <router-link to="/video">{{ file_id }}</router-link>
    </li>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: () => {
    return {
      filelist: null,
    };
  },
  mounted() {
    axios.get("/api/file/list").then((response) => {
      this.filelist = response.data;
      console.log(response.data);
      // this.filelist = Object.values(response.data);
    });
  },
};
</script>
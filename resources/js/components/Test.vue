<template>
  <div id="test">
    <button @click="testFunction()">test</button>
  </div>
</template>

<script>
import cookies from "vue-cookies";
import axios from "axios";
export default {
  name: "test",
  data() {
    return { msg: null };
  },
  methods: {
    testFunction() {
      axios
        .get("http://127.0.0.1:8000/api/user/logout/", {
          headers: {
            Authorization: `JWT ${cookies.get("ajwt")}`,
          },
        })
        .then((response) => console.log(response))
        .catch((error) => console.log(error.response));
    },
  },
};
</script>
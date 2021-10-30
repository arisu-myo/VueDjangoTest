<template>
  <div class="Profile">
    <img class="rounded-circle" v-bind:src="user_image" v-if="user_image" />

    <div style="font-size: 50px" v-if="user_image">{{ User.name }}</div>
    <div style="font-size: 50px" v-if="user_image">{{ User.email }}</div>
  </div>
</template>

<style scoped>
img {
  width: 250px;
  height: 250px;
}
</style>

<script>
import axios from "axios";
import { mapGetters, mapState } from "vuex";

export default {
  name: "Profile",
  data() {
    return {
      msg: null,
      user_image: null,
    };
  },
  computed: {
    ...mapState({
      User: (state) => state.user.User,
      LoginStatus: (state) => state.LoginStatus,
    }),
  },
  created() {
    this.$store.dispatch("user/autologin");
  },
  methods: {},
  mounted() {},
  watch: {
    User: function (newVal, oldVal) {
      if (this.User != null) {
        axios
          .get(this.User.user_icon, {
            responseType: "blob",
          })
          .then((response) => {
            // console.log(response);
            let blob = new Blob([response.data]);
            this.user_image = window.URL.createObjectURL(blob);
            // console.log(this.user_image);
          });
      }
    },
    LoginStatus: function (newVal, oldVal) {
      if (this.LoginStatus === false) {
        this.$router.push("/");
      }
    },
  },
};
</script>


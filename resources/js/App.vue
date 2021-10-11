<template>
  <div id="app">
    <header>
      <div>
        <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
          <a class="navbar-brand" href="#">日記的なブログ</a>

          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <router-link class="nav-link" to="/test">test</router-link>
              </li>
            </ul>

            <ul class="navbar-nav ml-auto">
              <li v-show="!LoginStatus" class="nav-item">
                <router-link class="nav-link" to="/signup">signup</router-link>
              </li>
              <li v-show="!LoginStatus" class="nav-item">
                <router-link class="nav-link" to="/login">login</router-link>
              </li>

              <li v-if="User === null" class="navbar-text" style="margin 10px">
                ようこそ ゲスト 樣
              </li>
              <li v-else class="navbar-text" style="padding: 0.5rem">
                ようこそ {{ User.name }} 樣
              </li>
              <li v-if="User != null">
                <button class="btn btn-outline-success" @click="logout()">
                  ログアウト
                </button>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </header>

    <router-view />
  </div>
</template>

<script>
import { mapState } from "vuex";
import cookies from "vue-cookies";
export default {
  name: "App",
  data() {
    return {
      msg: null,
    };
  },
  created: function () {
    document.title = "ホーム";
    this.$store.dispatch("user/autologin");
  },
  computed: {
    ...mapState({
      LoginStatus: (state) => state.user.LoginStatus,
      User: (state) => state.user.User,
    }),
  },
  methods: {
    async logout() {
      await this.$store.dispatch("user/logout");
    },
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
  margin-bottom: 50px;
}
</style>

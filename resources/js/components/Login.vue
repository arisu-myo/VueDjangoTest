<template>
  <div id="Login">
    <div
      class="card mx-auto border-0"
      style="width: 80%; max-width: 500px; margin-top: 10%"
    >
      <div class="card-body">
        <h3>ログイン</h3>
      </div>

      <form action="#">
        <div class="" style="margin: 1rem 0">
          <input
            type="email"
            name="email"
            id="email"
            v-model="loginForm.email"
            placeholder="メールアドレス"
            autocomplete="email"
            style="width: 100%; height: 50px"
          />
        </div>
        <div>
          <input
            id="password"
            type="password"
            placeholder="パスワード"
            v-model="loginForm.password"
            autocomplete="current-password"
            style="width: 100%; height: 50px"
          />
        </div>
      </form>
      <div class="text-right">
        <button
          class="btn btn-sm btn-primary"
          style="height: 40px; width: 40%; margin-top: 5%"
          @click="UserLogin"
        >
          ログイン
        </button>
      </div>
      <div style="margin-top: 5%">
        <router-link class="" to="/signup">
          アカウント登録はこちらから
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>

<script>
import { mapState } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        email: null,
        password: null,
      },
    };
  },
  created: function () {
    document.title = "ログイン";
  },
  computed: {
    ...mapState({
      LoginStatus: (state) => state.user.LoginStatus,
    }),
  },
  methods: {
    async UserLogin() {
      //call actions(login)
      await this.$store.dispatch("user/login", this.loginForm);

      if (this.LoginStatus) {
        this.$router.push("/");
      }
    },
  },
};
</script>
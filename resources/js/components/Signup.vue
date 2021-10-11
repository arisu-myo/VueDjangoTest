<template>
  <div id="SignUp">
    <div
      class="card mx-auto border-0"
      style="width: 80%; max-width: 500px; margin-top: 10%"
    >
      <div class="card-body">
        <h3>サインアップ</h3>
        <form action="#">
          <div>
            <input
              type="text"
              name="username"
              id="username"
              v-model="signupForm.username"
              placeholder="ユーザーネーム"
              autocomplete="username"
              style="width: 100%; height: 50px; margin-bottom: 1rem 0"
            />
          </div>

          <div class="" style="margin: 1rem 0">
            <input
              type="email"
              name="email"
              id="email"
              v-model="signupForm.email"
              placeholder="メールアドレス"
              autocomplete="email"
              style="width: 100%; height: 50px"
            />
          </div>

          <div class="group">
            <div class="password_box">
              <div class="password_inner">
                <input
                  id="password1"
                  type="password"
                  placeholder="パスワード"
                  autocomplete="new-password"
                  v-model="signupForm.password1"
                />
              </div>
              <i
                id="icon1"
                class="fas fa-eye-slash"
                @click="InpTypeChenge(1)"
              ></i>
            </div>
          </div>

          <div class="group">
            <div class="password_box">
              <div class="password_inner">
                <input
                  id="password2"
                  type="password"
                  placeholder="パスワード（確認）"
                  autocomplete="new-password"
                  v-model="signupForm.password2"
                />
              </div>
              <i
                id="icon2"
                class="fas fa-eye-slash"
                @click="InpTypeChenge(2)"
              ></i>
            </div>
          </div>
          <p class="text-left">
            <input type="checkbox" @click="Buttonactives" />
            利用規約を確認しました。
          </p>
        </form>
        <!----->
        <div class="text-right">
          <button
            class="btn btn-sm btn-primary"
            style="height: 40px; width: 40%"
            @click="CreateUser"
          >
            登録
          </button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState } from "vuex";

export default {
  name: "SignUp",
  data() {
    return {
      msg: null,
      debug_print: null,
      error_log: null,
      button_active: false,

      signupForm: {
        email: null,
        username: null,
        password1: null,
        password2: null,
      },
    };
  },

  created: function () {
    document.title = "signup";
  },

  computed: {
    ...mapState({
      LoginStatus: (state) => state.user.LoginStatus,
    }),
  },

  methods: {
    InpTypeChenge(index_numbar) {
      let input_pass1 = document.getElementById("password1");
      let input_pass2 = document.getElementById("password2");
      let icon1 = document.getElementById("icon1");
      let icon2 = document.getElementById("icon2");

      if (index_numbar === 1) {
        if (input_pass1.type === "password") {
          input_pass1.type = "text";
          icon1.className = "fas fa-eye";
        } else {
          input_pass1.type = "password";
          icon1.className = "fas fa-eye-slash";
        }
      } else if (index_numbar === 2) {
        if (input_pass2.type === "password") {
          input_pass2.type = "text";
          icon2.className = "fas fa-eye";
        } else {
          input_pass2.type = "password";
          icon2.className = "fas fa-eye-slash";
        }
      }
    },

    async Buttonactives() {
      if (this.button_active === false) {
        this.button_active = true;
      } else {
        this.button_active = false;
      }
    },

    async CreateUser() {
      if (this.button_active === false) {
        alert("利用規約に同意してください。");
        return;
      }
      //call actions(signup)
      await this.$store.dispatch("user/signup", this.signupForm);

      if (this.LoginStatus) {
        this.$router.push("/login");
      }
    },
  },
};
</script>

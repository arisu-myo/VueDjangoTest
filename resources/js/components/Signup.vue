<template>
  <div id="SignUp">
    <div
      class="card mx-auto border-0"
      style="width: 80%; max-width: 500px; margin-top: 10%"
    >
      <div class="card-body">
        <h1>サインアップ</h1>
        <form action="#">
          <div>
            <input
              type="text"
              name="username"
              id="username"
              v-model="username"
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
              v-model="email"
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
                  v-model="password1"
                />
              </div>
              <i
                id="icon1"
                class="fas fa-eye-slash"
                v-on:click="InpTypeChenge(1)"
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
                  v-model="password2"
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

<style scoped>
.group {
  margin: 1.2rem 0;
}

.password_box {
  display: flex; /*アイコン、テキストボックスを調整する*/
  align-items: center; /*アイコン、テキストボックスを縦方向の中心に*/
  justify-content: center; /*アイコン、テキストボックスを横方向の中心に*/
  width: 100%;
  height: 50px;
  border-radius: 5px;
  border: 1px solid lightgray;
}

.password_inner {
  width: 100%;
  height: 100%;
  background-color: transparent; /*.password_boxの枠線お角一部被るため透明に*/
  position: relative;
}

#password1,
#password2 {
  position: absolute;
  z-index: 1; /*.password_stringよりも上に配置*/
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  border: none; /*枠線非表示*/
  outline: none; /*フォーカス時の枠線非表示*/
  padding: 0 10px;
  font-size: 16px;
  background-color: transparent; /*後ろの.password_stringを見せるため*/
  box-sizing: border-box; /*横幅の解釈をpadding, borderまでとする*/
}

.password_string {
  position: absolute;
  height: 100%;
  width: 120px; /*文字列分の長さ*/
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  padding-left: 20px; /*position: absolute;でのmarginは親要素はみ出す*/
  font-size: 20px;
  line-height: 50px; /*文字列を縦方向にmiddleに見せるため*/
  background-color: transparent;
  color: #000000;
  box-sizing: border-box; /*横幅の解釈をpadding, borderまでとする*/
  transition: all 0.2s;
  -webkit-transition: all 0.2s;
}

.fa-eye,
.fa-eye-slash {
  /*アイコンに一定のスペースを設ける*/
  height: 50%;
  width: 60px;
  padding: 5px 5px;
}
</style>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      msg: null,
      debug_print: null,
      username: null,
      email: null,
      password1: null,
      password2: null,
      error_log: null,
      button_active: false,
    };
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

    CreateUser() {
      if (this.button_active === false) {
        alert("利用規約に同意してください。");
        return;
      }

      let error_log = "";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios
        .post("http://127.0.0.1:8000/api/user/signup/", {
          email: this.email,
          username: this.username,
          password1: this.password1,
          password2: this.password2,
        })
        .then((response) => (this.debug_print = response))
        .catch((error) => (this.error_log = error.response.data));

      this.username = "";
      this.email = "";
      this.password1 = "";
      this.password2 = "";
    },
  },
};
</script>
<template>
  <div class="Profile">
    <div class="card col-md-5">
      <h2 class="card-header text-left">ユーザー情報</h2>
      <div class="card-body">
        <p class="text-left">画像</p>
        <img
          class="rounded-circle border border-success"
          v-bind:src="user_image"
          v-if="user_image"
        />
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">
          <p class="text-left">ユーザー名</p>
          <span id="user" v-if="user_image" style="font-size: 20px">
            {{ User.name }}
          </span>

          <button
            type=""
            class="btn btn-outline-primary"
            style="margin: 1em"
            @click="InputUser()"
          >
            {{ user_button }}
          </button>

          <input
            id="user_form"
            type="text"
            v-model="user_name"
            placeholder="ユーザーネーム"
            style="
              width: 200px;
              display: none;
              border: 1px solid #000;
              position: relative;
            "
          />
        </li>

        <li class="list-group-item">
          <p class="text-left">メールアドレス</p>
          <span id="email" v-if="user_image" style="font-size: 20px">
            {{ User.email }}
          </span>

          <button
            type=""
            class="btn btn-outline-primary"
            style="margin: 1em"
            @click="InputEmail()"
          >
            {{ email_button }}
          </button>

          <input
            id="email_form"
            v-model="email"
            type="email"
            placeholder="メールアドレス"
            style="
              width: 200px;
              display: none;
              border: 1px solid #000;
              position: relative;
            "
          />
        </li>
      </ul>
      <div class="text-right" v-show="button_flg">
        <br />
        <button class="btn btn-success">ぼたんだよぉ～</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
img {
  width: 100px;
  height: 100px;
}

.card {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 0;
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
      email: "",
      email_flg: false,
      email_button: "変更する",
      user_name: "",
      user_flg: false,
      user_button: "変更する",
      button_flg: false,
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
  methods: {
    async InputEmail() {
      let flg = this.email_flg;
      let email_tag = document.getElementById("email");
      let email_from = document.getElementById("email_form");
      if (flg === false) {
        email_tag.style.display = "none";
        email_from.style.display = "";

        this.email_button = "戻る";
        this.email_flg = true;
      } else {
        email_tag.style.display = "";
        email_from.style.display = "none";

        this.email_button = `変更する`;
        this.email_flg = false;
      }
    },
    async InputUser() {
      let flg = this.user_flg;
      let user_tag = document.getElementById("user");
      let user_from = document.getElementById("user_form");

      if (flg === false) {
        user_tag.style.display = "none";
        user_from.style.display = "";

        this.user_button = "戻る";
        this.user_flg = true;
      } else {
        user_tag.style.display = "";
        user_from.style.display = "none";

        this.user_button = "変更する";
        this.user_flg = false;
      }
    },
  },
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

    email: function (val) {
      if (this.email != "") {
        this.button_flg = true;
      } else if (this.user_name === "") {
        this.button_flg = false;
      }
    },
    user_name: function (val) {
      if (this.user_name != "") {
        this.button_flg = true;
      } else if (this.email === "") {
        this.button_flg = false;
      }
    },
  },
};
</script>


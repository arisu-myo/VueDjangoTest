<template>
  <div class="Profile">
    <div id="overlay" style="display: none">
      <div id="content">
        <croppa
          v-model="myCroppa"
          :width="250"
          :height="250"
          placeholder="画像を選択してください。"
          canvas-color="transparent"
          :prevent-white-space="true"
        >
        </croppa>
        <div>
          <button @click="generateImage">画像作成</button>
          <button @click="modalDisplay(0)">close</button>
        </div>
      </div>
    </div>
    <div class="card col-md-5">
      <h2 class="card-header text-left">ユーザー情報</h2>
      <div class="card-body">
        <p class="text-left">画像</p>

        <div class="profileImg">
          <img
            class="rounded-circle border border-success"
            v-bind:src="user_image"
            v-if="user_image"
          />
          <!-- テキスト -->
          <div class="profileImg__text" @click="modalDisplay(1)">
            <!-- <p>変更</p> -->
            <span class="material-icons-outlined" style="font-size: 50px">
              camera_enhance
            </span>
          </div>
        </div>
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
            v-model="username"
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
        <button @click="ChengeData" class="btn btn-success">変更</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
img {
  width: 100%;
  height: 100%;
}

.card {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 0;
}

#overlay {
  /*　要素を重ねた時の順番　*/
  z-index: 1;

  /*　画面全体を覆う設定　*/
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);

  /*　画面の中央に要素を表示させる設定　*/
  display: flex;
  align-items: center;
  justify-content: center;
}

#content {
  z-index: 10;
  max-width: 400px;
  width: 80%;
  padding: 1em;
  background-color: #fff;
}
</style>

<style lang="scss" scoped>
.profileImg {
  width: 40%;
  height: 40%;
  text-align: center;
  margin: 10px auto;

  position: relative;
  &:hover .profileImg__text {
    opacity: 1;
  }
  &__text {
    border-radius: 50%;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    color: #fff;
    background-color: rgba(0, 0, 0, 0.6);
    transition: 0.3s ease-in-out;
    opacity: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    // p {
    //   line-height: 1.8;
    // }
  }
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
      username: "",
      user_flg: false,
      user_button: "変更する",
      button_flg: false,
      myCroppa: null,
      imgUrl: "",
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

        this.email = "";
        this.button_flg = false;
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

        this.username = "";
        this.button_flg = false;
      }
    },
    async ChengeData() {
      const data = {
        username: this.username,
        email: this.email,
      };

      this.$store.dispatch("user/ChengeData", data);
    },
    async modalDisplay(index) {
      let modal = document.getElementById("overlay");

      if (index === 1) {
        modal.style.display = "";
      } else {
        modal.style.display = "none";
      }
    },
    async generateImage() {
      this.myCroppa.generateBlob((blob) => {
        let url = window.URL.createObjectURL(blob);
        console.log(url);
      });
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
    username: function (val) {
      if (this.user_name != "") {
        this.button_flg = true;
      } else if (this.email === "") {
        this.button_flg = false;
      }
    },
  },
};
</script>


<template>
  <!-- 3/9 総括　スマホ画面用のCSSを仕掛ける？？ -->
  <!-- そのために大規模回収が必須 -->
  <div>
    <div class="boxs">
      <div class="item1">
        <!-- <h3 class="h3-1">&nbsp;</h3> -->
        <hr class="hr-0" />
        <h3 class="h3-1">UpLoad</h3>
        <hr class="hr-0" />
        <h3 class="h3-1">Video</h3>
        <hr class="hr-0" />
        <h3 class="h3-1">Picture</h3>
        <hr class="hr-0" />
        <h3 class="h3-1">Texts</h3>
        <hr class="hr-0" />
      </div>

      <div class="item2">
        <div v-if="douga_file != null">
          <p>※印が入っている所は必須事項です</p>
          <video class="douga" :src="douga_file" controls></video><br />

          <div>
            <label class="rh_text">ファイル名※：</label><br />
            <input
              class="input__upload"
              type="text"
              v-model="file_title"
            /><br />
          </div>

          <label class="text-left">説明：</label><br />
          <input class="input__upload" type="text" v-model="file_ds" /><br />

          <label>他の人に共有をする※：</label>
          <input type="checkbox" />
        </div>

        <label>アップロードしたいファイルを選択してください</label><br />
        <input type="file" accept="video/mp4,video/x-m4v" @change="setFile" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.input__upload {
  width: 25vw;
  height: 40px;
  margin: 0.3em;
}

.rh_text {
  padding-right: 15vw;
}

.hr-0 {
  padding: 0em;
  margin: 0em;
  background-color: black;
}

.h3-1 {
  padding-top: 1em;
  padding-bottom: 1em;
  padding-left: 0.6em;
  padding-right: 0.6em;
  margin-bottom: 0px;
  display: block;
}

.h3-1:hover {
  background-color: blue;
}

.boxs {
  width: 100%;
  height: 100vh; /*vhだと親要素に関係なく画面での比率になるっぽい？*/
  display: flex;
  flex-wrap: wrap;
}

@media screen and (max-width: 727px) {
  .boxs {
    width: 100%;
    height: 20vh;
    display: flex;
    flex-wrap: wrap;
  }
}
/* @media only screen and (max-device-width: 1200px) {
  スマホの場合のみ
} */

.item1 {
  display: block;
  flex-grow: 1;
  flex-shrink: 1;
  background-color: #3584bb;
}
.item2 {
  display: block;
  flex-grow: 4;
  flex-shrink: 4;
}

.douga {
  margin-top: 0.5em;
  width: 30vw;
}
@media screen and (max-width: 727px) {
  .douga {
    margin-top: 0.5em;
    width: 100vw;
  }
}
</style>


<script>
import { mapState } from "vuex";
export default {
  data: () => {
    return {
      douga_file: null,
      file_title: "",
      file_ds: "",
      public_flg: false,
    };
  },
  computed: {
    ...mapState({
      User: (state) => state.user.User,
      LoginStatus: (state) => state.user.LoginStatus,
    }),
  },
  created() {
    if (this.LoginStatus === false) {
      this.$router.push("/login");
    }
  },
  methods: {
    setFile(event) {
      const file = event.target.files[0];
      if (!file || !file.type.match("video/*")) {
        alert("現在はMP4形式の動画しかアップロードできません");
        return;
      }
      let url = window.URL.createObjectURL(file);
      console.log(url);

      this.douga_file = url;
      this.file_title = file.name;
    },
  },
  watch: {
    LoginStatus: function (newVal, oldVal) {
      this.$store.dispatch("user/autologin");
      if (this.LoginStatus === false) {
        this.$router.push("/");
      }
    },
  },
};
</script>
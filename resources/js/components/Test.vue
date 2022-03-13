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
          <h4 class="h4-text">動画（プレビュー）</h4>
          <video class="douga" :src="douga_file" controls></video><br />

          <div>
            <h4 class="h4-text">ファイル名(必須):</h4>

            <input
              class="upload_file_name"
              type="text"
              v-model="file_title"
            /><br />
          </div>

          <div>
            <h4 class="h4-text">説明(任意):</h4>

            <textarea
              maxlength="200"
              class="upload_ds"
              v-model="file_ds"
            /><br />
          </div>

          <div>
            <h4 class="h4-text">他者への表示：</h4>
            <label>共有を許可する</label>
            <input v-model="public_flg" type="checkbox" />
          </div>

          <button class="btn btn-success uploadbtn" @click="fileUpload()">
            アップロード
          </button>
        </div>

        <div v-if="douga_file == null">
          <label>アップロードしたいファイルを選択してください</label><br />
          <input type="file" accept="video/mp4,video/x-m4v" @change="setFile" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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
  スマホの場合のみ?
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
  width: 50vw;
}
.upload_file_name {
  width: 40vw;
  height: 40px;
  margin: 0.3em;
}
.upload_ds {
  width: 40vw;
  height: 120px;
}
.h4-text {
  margin: 1em 9em 1em 9em;
  padding: 0em 0em 0em 0.5em;
  text-align: left;
  border-left: 7px solid #3584bb;
}
.uploadbtn {
  margin: 2em 0em 1em 0em;
  padding: 1em 2em 1em 2em;
}

@media screen and (max-width: 727px) {
  .douga {
    margin-top: 0.5em;
    width: 100vw;
  }
  .upload_file_name {
    width: 80vw;
    height: 40px;
    margin: 0.3em;
  }
  .upload_ds {
    width: 80vw;
    height: 120px;
  }
  .h4-text {
    margin: 1em 0em 1em 1em;
    padding: 0em 0em 0em 0.5em;
    text-align: left;
    border-left: 7px solid #3584bb;
  }
}
</style>


<script>
import axios from "axios";
import { mapState } from "vuex";
export default {
  data: () => {
    return {
      douga_file: null,
      douga_data: null,
      file_title: "",
      file_ds: "",
      public_flg: false,
      test: null,
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
      this.douga_data = file;
      this.file_title = file.name;
    },
    fileUpload() {
      const data = new FormData();
      data.append("file", this.douga_data, "image.mp4");
      data.append("file_name", this.file_title);
      data.append("file_description", this.file_ds);
      data.append("public", this.public_flg);
      this.test = data;
      this.$store.dispatch("pege/FileUpLoad", data);
    },
  },
  beforeMount() {
    let videotag = document.getElementsByTagName("video");
    videotag.volume = 0.3;
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
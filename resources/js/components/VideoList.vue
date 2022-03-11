<template>
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
        <div>
          <h1>●●●●●●●さんの動画一覧</h1>
          <div v-if="userid != ''">
            <li v-for="(fileid, name) in filelist" :key="fileid">
              <router-link
                :to="{
                  path: '/video',
                  query: { vid: fileid, user: userid },
                }"
                >{{ name }}</router-link
              >
            </li>
          </div>
          <div v-if="userid === ''">
            <li v-for="(fileid, name) in filelist" :key="fileid">
              <router-link
                :to="{
                  path: '/video',
                  query: { vid: fileid },
                }"
                >{{ name }}</router-link
              >
            </li>
          </div>
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
</style>

<script>
import axios from "axios";
export default {
  data: () => {
    return {
      filelist: null,
      userid: "",
    };
  },
  mounted() {
    let user = this.$route.query.user;
    if (user === undefined) {
      user = "";
      console.log(user);
    } else {
      this.userid = user;
      user = `?user=${user}`;
    }

    axios
      .get(`/api/file/list/${user}`)
      .then((response) => {
        this.filelist = response.data;
        // console.log(response.data);
        // this.filelist = Object.values(response.data);
      })
      .catch((error) => {
        let response = error.response;
        if (response.status == 401) {
          alert("ログインしていません");
        }
        if (response.status == 400) {
          alert("不明なエラーが発生しました");
        }
      });
  },
};
</script>
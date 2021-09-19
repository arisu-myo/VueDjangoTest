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
                <a class="nav-link" href="#">home</a>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/signup">signup</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/login">login</router-link>
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
export default {
  name: "App",
  data() {
    return {
      msg: null,
    };
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

import Vue from "vue"
import App from "./App"
import store from "./store"
import router from "./router"
import VueCookies from "vue-cookies"
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
// import { VueLoading } from "vue-loading-template"

//croppa(画像切り取り用)
import Croppa from "vue-croppa"
import "vue-croppa/dist/vue-croppa.css"

//bootstrap
import 'bootstrap/dist/css/bootstrap.css' // add
import 'bootstrap-vue/dist/bootstrap-vue.css' // add

//vue-videojs-async
import { VueVideojs } from "vue-videojs-async"
import "vue-videojs-async/dist/vue-videojs-async.css"

Vue.component(
    "base-component",
    require("./App.vue").default
)

Vue.config.productionTip = true
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueCookies)
Vue.use(Croppa)
// Vue.use(VueLoading)
Vue.use(VueVideojs)

new Vue({
    el: "#app",
    router,
    store,
    components: { App },
    template: "<App />"
})

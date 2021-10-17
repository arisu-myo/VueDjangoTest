import Vue from "vue"
import App from "./App"
import store from "./store"
import router from "./router"
import VueCookies from "vue-cookies"
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
// import { VueLoading } from "vue-loading-template"

import 'bootstrap/dist/css/bootstrap.css' // add
import 'bootstrap-vue/dist/bootstrap-vue.css' // add



Vue.component(
    "base-component",
    require("./App.vue").default
)

Vue.config.productionTip = true
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueCookies)
// Vue.use(VueLoading)

new Vue({
    el: "#app",
    router,
    store,
    components: { App },
    template: "<App />"
})

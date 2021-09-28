import Vue from "vue"
import App from "./App"
import store from "./store"
import router from "./router"
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css' // add
import 'bootstrap-vue/dist/bootstrap-vue.css' // add

Vue.component(
    "base-component",
    require("./App.vue").default
)

Vue.config.productionTip = true
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

new Vue({
    el: "#app",
    router,
    store,
    components: { App },
    template: "<App />"
})

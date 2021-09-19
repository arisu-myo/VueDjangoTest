import Vue from "vue"
import App from "./App"
import store from "./store"
import router from "./router"
import BootstrapVue from "bootstrap-vue"
import 'bootstrap/dist/css/bootstrap.css' // add
import 'bootstrap-vue/dist/bootstrap-vue.css' // add


Vue.config.productionTip = false
Vue.use(BootstrapVue)



Vue.component(
    "base-component",
    require("./App.vue").default
)


new Vue({
    el: "#app",
    router,
    store,
    components: { App },
    template: "<App/>"
})
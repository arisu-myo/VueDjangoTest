import Vue from "vue"
import App from "./App"
import router from "./router"

Vue.component(
    "base-component",
    require("./App.vue").default
)

Vue.config.productionTip = false

new Vue({
    el: "#app",
    router,
    components: { App },
    template: "<App/>"
})
import Vue from "vue"
import Router from "vue-router"

import Home from "../components/Home"
Vue.use(Router)

export default new Router({
    routrs: [
        {
            path: "/home",
            name: "home",
            component: Home
        },
    ]
})
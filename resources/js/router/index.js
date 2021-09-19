import Vue from "vue"
import Router from "vue-router"

import Home from "../components/Home"
import SignUp from "../components/Signup"
Vue.use(Router)

export default new Router({
    routes: [
        {
            path: "/home",
            name: "home",
            component: Home
        },
        {
            path: "/signup",
            name: "signup",
            component: SignUp
        }
    ]
})
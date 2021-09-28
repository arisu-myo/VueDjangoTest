import Vue from "vue"
import Router from "vue-router"

import Home from "../components/Home"
import SignUp from "../components/Signup"
import Login from "../components/Login"
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
        },
        {
            path: "/login",
            name: "login",
            component: Login
        },
    ]
})
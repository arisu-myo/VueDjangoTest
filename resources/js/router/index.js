import Vue from "vue"
import Router from "vue-router"

import Home from "../components/Home"
import SignUp from "../components/Signup"
import Login from "../components/Login"
import Test from "../components/Test"
import NotFound from "../error/NotFound"
Vue.use(Router)

export default new Router({
    mode: 'history',
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
        {
            path: "/test",
            name: "test",
            component: Test
        },
        {
            path: "*",
            name: "not found",
            component: NotFound
        },

    ]
})
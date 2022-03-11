//vue base
import Vue from "vue"
import Router from "vue-router"

// vue components
import Home from "../components/Home"
import SignUp from "../components/Signup"
import Login from "../components/Login"
import Test from "../components/Test"
import Loading from "../components/loading"
import Profile from "../components/Profile"
import VideoView from "../components/Video"
import VideoList from "../components/VideoList"


// not found
import NotFound from "../error/NotFound"

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: "/",
            name: "home",
            component: Home
        },
        {
            path: "/signup",
            name: "登録",
            component: SignUp
        },
        {
            path: "/login",
            name: "ログイン",
            component: Login
        },
        {
            path: "/test",
            name: "テストページ",
            component: Test
        },
        {
            path: "/loading",
            name: "loading",
            component: Loading
        },
        {
            path: "/profile",
            name: "プロフィール",
            component: Profile,
        },
        {
            path: "/video",
            name: "Video",
            component: VideoView
        },
        {
            path: "/video/list",
            name: "Userの動画",
            component: VideoList
        },
        {
            path: "*",
            name: "not found",
            component: NotFound
        },

    ]
})
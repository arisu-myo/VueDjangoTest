const { default: axios } = require("axios");
import cookies from "vue-cookies";


const state = {
    User: null,
    LoginStatus: null,
    LoginErrorMessage: null,
    SignUpErrorMessage: null,
};

const getters = {
    // getUser: function (state) {
    //     return state.User.user_icon

    // }
};

const mutations = {
    setUser(state, user) {
        state.User = user;
    },
    setLoginStatus(state, status) {
        state.LoginStatus = status;
    },
    setLoginErrorMessage(state, message) {
        state.LoginErrorMessage = message;
    },
    setSignUpErrorMessage(state, message) {
        state.SignUpErrorMessage = message;
    },
}

const actions = {
    //signup
    async signup(context, data) {
        context.commit("setLoginStatus", null);
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        let response
        await axios
            .post("api/user/signup/", data)
            .then((response_data) => (response = response_data))
            .catch((error) => (response = error.response));

        if (response.status === 201) {
            context.commit("setLoginStatus", true);
            context.commit("setUser", response.data);
            return false
        }

        context.commit("setLoginStatus", false);
        context.commit("setSignUpErrorMessage", response.data);
    },
    //login
    async login(context, data) {
        context.commit("setLoginStatus", null);
        let response
        await axios
            .post("api/user/login/", data)
            .then((response_data) => (response = response_data))
            .catch((error) => (response = error.response))

        if (response.status === 200) {
            context.commit("setLoginStatus", true);
            context.commit("setUser", response.data);
            cookies.set("jwt", response.data.access);
            // console.log(response.data)
            return false
        }

        context.commit("setLoginStatus", false);
        context.commit("setLoginErrorMessage", response.data);
    },
    //logout
    async logout(context) {
        let tag1 = document.getElementById("app")
        tag1.style.pointerEvents = "none"

        context.dispatch("pege/LoadStatus", true, { root: true })

        let response
        await axios
            .get("api/user/logout/", {
                headers: {
                    Authorization: `JWT ${cookies.get("jwt")}`,
                },
            })
            .then((response_data) => (response = response_data))
            .catch((error) => (response = error.response));

        if (response.status === 200) {
            context.commit("setLoginStatus", null);
            context.commit("setUser", null)
            cookies.remove("jwt")
        } else {
            context.commit("setLoginStatus", null);
            context.commit("setUser", null)
            cookies.remove("jwt")
        }

        context.dispatch("pege/LoadStatus", false, { root: true })
        tag1.style.removeProperty("pointer-events");
    },
    //auto login
    async autologin(context) {
        if (!cookies.isKey("jwt")) {
            return false
        }

        await axios
            .get("api/user/login/auto/", {
                headers: {
                    Authorization: `JWT ${cookies.get("jwt")}`
                }
            })
            .then(res => {
                if (res.status === 200) {
                    context.commit("setLoginStatus", true)
                    context.commit("setUser", res.data)
                }
            })
            .catch(error => {
                context.commit("setLoginStatus", false)
                context.commit("setLoginErrorMessage", error.response.data)
                console.log(error.response.data)
            })
    },
    //UserChengeData
    async ChengeData(context, data) {

        if (state.User === null) {
            return false
        }

        if (data.name === "") {
            data.username = state.User.username
        } else if (data.email === "") {
            data.email = state.User.email
        }

        let response
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        await axios
            .put("api/user/data/chenge/", data, {
                headers: {
                    Authorization: `JWT ${cookies.get("jwt")}`
                },
            })
            .then((response_data) => (response = response_data))
            .catch((error) => (response = error.response));

        if (response.status === 200) {
            window.location.href = "/profile"
        }
    },
    async ImageChenge(context, data) {
        if (state.User === null) {
            return false
        }

        console.log(data.type)
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        await axios
            .put("api/user/image/chenge/", data, {
                headers: {
                    "content-type": "multipart/form-data",
                    Authorization: `JWT ${cookies.get("jwt")}`

                }
            })
            .then((res) => {
                let responce = res
                if (responce.status === 200) {
                    window.location.href = "/profile"
                }
            })
            .catch((error) => console.log(error.response))
    },
    async passChenge(context, data) {
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        await axios
            .put("api/user/password/chenge/", data, {
                headers: {
                    Authorization: `JWT ${cookies.get("jwt")}`
                }
            })
            .then(res => {
                if (res.status === 200) {
                    alert("パスワードの変更に成功しました。")

                }
            })
            .catch(error => {
                alert("パスワードの変更に失敗しました。")
            })
        await axios
            .get("api/user/logout/", {
                headers: {
                    Authorization: `JWT ${cookies.get("jwt")}`,
                },
            })
            .then(res => {
                if (res.status === 200) {
                    cookies.remove("jwt")
                }
            })
            .catch(error => {
                console.log(error)
                cookies.remove("jwt")
            })
    }
}

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
};
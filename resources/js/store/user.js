const { default: axios } = require("axios");
import cookies from "vue-cookies";


const state = {
    User: null,
    LoginStatus: null,
    LoginErrorMessage: null,
    SignUpErrorMessage: null,
};

const getters = {
    username: state => (state.user ? state.username : "")
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



    },
    //auto login
    async autologin(context) {
        if (!cookies.isKey("jwt")) {
            return false
        }

        let response
        await axios
            .get("api/user/login/auto/", {
                headers: {
                    Authorization: `JWT ${cookies.get("jwt")}`
                },
            })
            .then((response_data) => (response = response_data))
            .catch((error) => (response = error.response))

        if (response.status = 200) {
            context.commit("setLoginStatus", true);
            context.commit("setUser", response.data);
            return false
        }

        context.commit("setLoginStatus", false);
        context.commit("setLoginErrorMessage", response.data);

    }
}

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
};
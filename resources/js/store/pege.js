import axios from "axios";
import cookies from "vue-cookies";

const state = {
    Loading: true,

};


const mutations = {
    setLoading(state, loading) {
        state.Loading = loading;
    },
}

const actions = {
    async LoadStatus(context, loading) {
        context.commit("setLoading", loading);
    },
    async FileUpLoad(content, data) {
        axios.defaults.xsrfCookieName = "csrftoken";
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

        await axios
            .post("api/file/upload/", data, {
                headers: {
                    "content-type": "multipart/form-data",
                    Authorization: `JWT ${cookies.get("jwt")}`
                }
            })
            .then((res) => {
                window.location.href = "/test"
            })
            .catch((error) => console.log(error.response))
    }

}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
};
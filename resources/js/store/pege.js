const state = {
    Loading: true,
    VideoURL: ""
};


const mutations = {
    setLoading(state, loading) {
        state.Loading = loading;
    },
    setVideoURL(state, url) {
        state.VideoURL = url
    }
}

const actions = {
    async LoadStatus(context, loading) {
        context.commit("setLoading", loading);
    },
    async ChengeURL(context, url) {
        context.commit("setVideoURL", url);
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
};
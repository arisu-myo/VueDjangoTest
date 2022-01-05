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

}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
};
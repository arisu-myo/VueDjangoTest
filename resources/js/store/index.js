import Vue from "vue";
import Vuex from "vuex";

import user from "./user";
import pege from "./pege";

Vue.use(Vuex);

const store = new Vuex.Store({
    modules: {
        user,
        pege,
    }
});

export default store
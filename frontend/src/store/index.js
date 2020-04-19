import Vuex from "vuex"
import Vue from "vue"

import collections from './collections'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    collections
  }
})

import Vuex from "vuex"
import Vue from "vue"

import collections from './collections'
import items from './items'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    collections,
    items,
  }
})

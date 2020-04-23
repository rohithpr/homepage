import v0Client from '../api/api'

const state = {
  collections: []
}

const getters = {
  allCollections: state => state.collections
}

const actions = {
  fetchCollections: async ({ commit }) => {
    commit('clearCollections')
    let next = '/collection/'
    do {
      let { data } = await v0Client.get(next)
      commit('addToCollections', data.data)
      next = data.links.next
    } while (next)
  }
}

const mutations = {
  clearCollections: (state) => {
    state.collections = []
  },
  addToCollections: (state, collections) => {
    collections = transformRawCollection(collections)
    state.collections = [...state.collections, ...collections]
  }
}

const transformRawCollection = (collections) => {
  return collections.map((collection) => {
    return {
      ...collection.attributes,
      id: collection.id,
      items: collection.relationships.item_set.data.map(item => item.id)
    }
  })
}

export default {
  state,
  getters,
  actions,
  mutations
}

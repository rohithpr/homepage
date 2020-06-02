import v0Client from '../api/api'

const state = {
  collections: [],
  columns: {}
}

const getters = {
  getCollectionsInColumn: state => columnNumber => {
    return state.columns[columnNumber] || []
  }
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
    state.columns = {}
  },
  addToCollections: (state, collections) => {
    collections = transformRawCollection(collections)
    state.collections = [...state.collections, ...collections]
    state.columns = {...state.columns}
    collections.forEach(collection => {
      let column = collection.column
      state.columns[column] = [...state.columns[column] || [], collection]
    })
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
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}

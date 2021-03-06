import v0Client from '../api/api'

const state = {
  items: {}
}

const getters = {
  allItems: state => state.items,
  getItemsByIds: state => itemIds => {
    // TODO: Sort by row number before returning
    return itemIds.map(itemId => {
      return state.items[itemId]
    }).filter(item => item)
  }
}

const actions = {
  fetchItems: async ({ commit }) => {
    commit('clearItems')
    let next = '/item/'
    do {
      let { data } = await v0Client.get(next)
      commit('addToItems', data.data)
      next = data.links.next
    } while (next)
  },
}

const mutations = {
  addToItems: (state, items) => {
    items = transformRawItems(items)
    state.items = {
      ...state.items
    }
    items.forEach(item => {
      state.items[item.id] = item
    })
  },
  clearItems: (state) => {
    state.items = {}
  },
}

const transformRawItems = (items) => {
  return items.map((item) => {
    return {
      ...item.attributes,
      id: item.id
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

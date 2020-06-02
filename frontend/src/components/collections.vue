<template>
  <div class="collections">
    <div class="container-fluid">
      <div class="row">
        <div v-for="columnNumber in [0, 1, 2, 3, 4, 5]" :key="columnNumber" class="col-md-2">
          <CollectionColumn :columnNumber="columnNumber" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import { mapActions } from 'vuex'
import CollectionColumn from './collectionColumn'

export default {
  name: 'Collections',
  components: {
    CollectionColumn,
  },
  methods: {
    ...mapActions('collections', ['fetchCollections']),
    ...mapActions('items', ['fetchItems']),
  },
  mounted () {
    this.fetchCollections(),
    this.fetchItems()
  }
}
</script>

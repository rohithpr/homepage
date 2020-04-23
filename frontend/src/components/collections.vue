<template>
  <div class="collections">
    <div class="container-fluid">
      <div class="row">
        <div v-for="(column, index) in collectionColumns" :key="index" class="col-md-2">
          <CollectionColumn :column="column" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex'
import CollectionColumn from './collectionColumn'

export default {
  name: 'Collections',
  components: {
    CollectionColumn,
  },
  methods: mapActions(['fetchCollections', 'fetchItems']),
  computed: {
    ...mapGetters(['allCollections']),
    collectionColumns () {
      const columnWise = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
      this.allCollections.forEach((collection) => {
        // console.log(collection)
        columnWise[collection.column] = [...columnWise[collection.column], collection]
      })
      return columnWise
    }
  },
  mounted () {
    this.fetchCollections(),
    this.fetchItems()
  }
}
</script>

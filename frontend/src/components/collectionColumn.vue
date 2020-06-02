<template>
  <div class="collectionColumn">
    <div v-for="collection in column" :key="collection.id">
      <Collection :collection="collection" />
    </div>
  </div>
</template>

<script>
import Collection from './collection'
import { mapState, mapGetters } from 'vuex'

export default {
  name: 'CollectionColumn',
  components: {
    Collection
  },
  props: {
    columnNumber: {
      type: Number,
      default: 0
    }
  },
  computed: {
    ...mapState('collections', ['collections']),
    ...mapGetters('collections', ['getCollectionsInColumn']),
    column () {
      // TODO: Why does removing this `if` result in the computed not being updated
      // when state changes?
      if (this.collections.length) {
        return this.getCollectionsInColumn(this.columnNumber)
      }
      return []
    }
  }
}
</script>

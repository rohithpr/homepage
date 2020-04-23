<template>
  <div class="collectionColumn">
    <div v-for="collection in column" :key="collection.id">
      <Collection :collection="collection" />
    </div>
  </div>
</template>

<script>
import Collection from './collection'

export default {
  name: 'CollectionColumn',
  components: {
    Collection
  },
  props: {
    column: {
      type: Array,
      default: () => { return [] }
    }
  }
}
</script>

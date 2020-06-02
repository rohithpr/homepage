<template>
  <div class="collection">
    <div class="collection-key">{{ collection.key }}</div>
    <div class="collection-items">
      <!-- TODO: create a new component to house different kinds of items -->
      <div class="collection-item" v-for="item in collectionItems" :key="item.id">
        <span v-if="item.kind === 'bookmark'">
          <a target="_blank" :href="item.value" >
            <div>{{ item.key }}</div>
          </a>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Collection',
  props: {
    collection: {
      type: Object,
      default: () => { return {} }
    }
  },
  computed: {
    ...mapGetters('items', ['getItemsByIds']),
    collectionItems () {
      return this.getItemsByIds(this.collection.items)
    }
  }
}
</script>

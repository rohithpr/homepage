<template>
  <div class="collections">
    <v-container :fluid=true>
      <v-row>
        <!-- TODO: Make the number of columns customisable -->
        <v-col
          v-for="columnNumber in [0, 1, 2, 3, 4, 5]"
          :key="columnNumber"
          cols="12"
          sm="6"
          md="3"
          lg="2"
        >
          <CollectionColumn :columnNumber="columnNumber" />
        </v-col>
      </v-row>
    </v-container>
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

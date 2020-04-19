<template>
  <div class="collections">
    <div v-for="collection in allCollections" :key="collection.id" >
      {{ collection }}
    </div>
  </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Collections',
  methods: mapActions(['fetchCollections']),
  computed: mapGetters(['allCollections']),
  mounted () {
    this.fetchCollections()
  }
}
</script>

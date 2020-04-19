<template>
  <div>
    hello world
  </div>
</template>

<script>

import { mapActions } from 'vuex'

export default {
  name: 'Collections',
  methods: mapActions(['getCollections']),
  created () {
    console.log('created')
    this.getCollections()
  }
}
</script>

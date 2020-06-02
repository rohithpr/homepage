<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    </v-app-bar>
    <v-content>
      <Collections />
    </v-content>
  </v-app>
</template>

<script>
import Collections from './components/collections'

export default {
  name: 'App',
  components: {
    Collections
  }
}
</script>

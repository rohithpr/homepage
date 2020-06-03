<template>
  <v-app>
    <v-app-bar
      app
      bottom
      clipped-left
      color="primary"
      dark
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <span class="display-1 ml-3 mr-5">Homepage&nbsp;<span class="font-weight-light">Username</span></span>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      app
      bottom
      clipped
      expand-on-hover
      right
      mini-variant
      color="grey lighten-4"
    >
      <v-list>
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>add</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="display-1">Add Collection</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
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
  },
  data: () => ({
    drawer: true
  }),
  methods: {
  }
}
</script>

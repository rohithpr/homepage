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
        <v-list-item
          link
          @click="addCollection"
        >
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
      <v-dialog
        v-model="collectionEditorActive"
        :max-width="dialogMaxWidth"
      >
        <CollectionEditor
          :collectionId=currentCollectionId
        />
      </v-dialog>
      <Collections />
    </v-content>
  </v-app>
</template>

<script>
import Collections from './components/collections'
import CollectionEditor from './components/collectionEditor'

export default {
  name: 'App',
  components: {
    Collections,
    CollectionEditor
  },
  data: () => ({
    drawer: true,
    dialogMaxWidth: "90rem",
    collectionEditorActive: false,
    currentCollectionId: null
  }),
  methods: {
    addCollection () {
      this.currentCollectionId = null
      this.collectionEditorActive = true
    }
  }
}
</script>

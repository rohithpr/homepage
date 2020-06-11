<template>
  <v-card>
    <v-card-title>
      <span class="display-1">Collection</span>
    </v-card-title>
    <v-card-text class="headline">
      <v-form
        ref="form"
        v-model="valid"
        :lazy-validation=false
      >
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field
                required
                label="Collection name*"
                v-model="key"
              />
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "CollectionEditor",
  props: {
    active: {
      type: Boolean,
      default: false
    },
    collectionId: {
      type: Object,
      default: null
    }
  },
  data: () => {
    return {
      valid: true,
      key: "",
      keyRules: [
        v => !!v || "Key is required",
        v => (v && v.length >= 20) || "Name too long",
        v => (v && v.length < 5) || "Name too short",
      ]
    }
  },
  methods: {
    validate () {
      // Why is "form" not a member of refs?
      this.$refs.form.validate()
    }
  }
}
</script>

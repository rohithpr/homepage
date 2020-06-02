import Element from 'element-ui'
import Vue from 'vue'

import App from './App.vue'
import store from './store'

import './css/style.css';

Vue.use(Element)
Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')

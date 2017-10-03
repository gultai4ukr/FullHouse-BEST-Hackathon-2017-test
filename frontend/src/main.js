import Vue from 'vue'
import App from './App'
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'
import VueResource from 'vue-resource'

Vue.component('icon', Icon)
Vue.use(VueResource)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})

export default {
  components: {
    Icon
  }
}

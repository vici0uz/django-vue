import '@babel/polyfill'
import 'mutationobserver-shim'
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import './plugins/bootstrap-vue'
import './plugins/axios'
import { ValidationProvider, extend } from 'vee-validate'
import { required } from 'vee-validate/dist/rules'

// import * as VeeValidate from 'vee-validate'
// import './plugins/'
// import App from './App'
import MiApp from './MiApp'
import router from './router'

import BootstrapVue from 'bootstrap-vue'
import vSelect from 'vue-select'

import 'bootstrap/dist/css/bootstrap.min.css'

import 'bootstrap-vue/dist/bootstrap-vue.css'

import 'vue-select/dist/vue-select.css'
import vuetify from './plugins/vuetify'

extend('required', {
  ...required,
  message: 'El campo es requerido'
})
Vue.use(BootstrapVue)
Vue.use('v-select', vSelect)
Vue.component('ValidationProvider', ValidationProvider)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,

  components: { MiApp,
    ValidationProvider,
    vSelect },

  vuetify,
  template: '<MiApp/>'
})

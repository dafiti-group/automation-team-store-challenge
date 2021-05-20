import Vue from 'vue'
import App from './App.vue'
import router from "./router";
import store from "./store";

import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

import axios from 'axios'

axios.defaults.baseURL = 'http://0.0.0.0:8000'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

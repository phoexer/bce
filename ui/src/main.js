import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store/";
import AsyncComputed from "vue-async-computed";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";

Vue.use(VueMaterial);

Vue.use(AsyncComputed);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

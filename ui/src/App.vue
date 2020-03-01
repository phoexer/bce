<template>
  <div class="container">
    <Header></Header>
    <div class="row">
      <div class="col-sm-12">
        <div v-if="alert.message" :class="`alert ${alert.type}`">
          {{ alert.message }}
        </div>
        <router-view></router-view>
      </div>
    </div>
    <hr />
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "@/views/Header.vue";
import Footer from "@/views/Footer.vue";

export default {
  name: "app",
  components: {
    Header,
    Footer
  },
  computed: {
    alert() {
      return this.$store.state.alert;
    }
  },
  watch: {
    $route(to) {
      if (to.name != "home") {
        this.$store.dispatch("alert/clear");
      }
    }
  }
};
</script>

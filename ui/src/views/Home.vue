<!--<template>-->
<!--<div class="home">-->
<!--<img alt="Vue logo" src="../assets/logo.png">-->
<!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--</div>-->
<!--</template>-->

<!--<script>-->
<!--// @ is an alias to /src-->
<!--import HelloWorld from '@/components/HelloWorld.vue'-->

<!--export default {-->
<!--name: 'home',-->
<!--components: {-->
<!--HelloWorld-->
<!--}-->
<!--}-->
<!--</script>-->

<template>
  <div>
    <h3>Welcome To BCE App</h3>
    <h4>Summary</h4>
    <p>This is my solution to the BriteCore Engineering code challenge.</p>
    <p>
      For details you can check out the github page for
      <a href="https://github.com/phoexer/bce" target="_blank"
        >this project here</a
      >
    </p>
    <p>You can find instructions and documentation there.</p>
  </div>
</template>

<script>
export default {
  computed: {
    user() {
      return this.$store.state.authentication.user;
    }
    // users() {
    //     return this.$store.state.users.all;
    // }
  }
  // created() {
  //     this.$store.dispatch('users/getAll');
  // }
};
</script>

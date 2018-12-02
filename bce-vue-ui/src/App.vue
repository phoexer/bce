<template>
    <div class="container">
        <Header></Header>
        <div class="row">
            <div class="col-sm-12">
                <div v-if="alert.message" :class="`alert ${alert.type}`">
                    {{alert.message}}
                </div>
                <router-view></router-view>
            </div>
        </div>
        <hr />
        <Footer></Footer>
    </div>
</template>

<script>
    import Header from '@/views/Header.vue';
    import Footer from '@/views/Footer.vue';

    export default {
        name: 'app',
        components: {
            Header,
            Footer,
        },
        computed: {
            alert() {
                return this.$store.state.alert
            }
        },
        watch: {
            $route(to, from) {
                // clear alert on location change
                //console.log(to);
                // console.log(from.toString());
                if (to.name != 'home'){
                    // Clear alerts only when not going home
                    this.$store.dispatch('alert/clear');
                }
            }
        }
    };
</script>

<!--<template>-->
    <!--<div id="app">-->
        <!--<div id="nav">-->
            <!--<router-link to="/">Home</router-link>-->
            <!--|-->
            <!--<router-link to="/about">About</router-link>-->
        <!--</div>-->
        <!--<router-view/>-->
    <!--</div>-->
<!--</template>-->


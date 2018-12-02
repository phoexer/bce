import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Login from './components/Login.vue'
import Risk from './components/Risk.vue'
import RiskType from './components/RiskType.vue'


Vue.use(Router);

export const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/risks',
            name: 'risks',
            component: Risk
        },
        {
            path: '/risk-types',
            name: 'risk-types',
            component: RiskType
        },

        {
            path: '/about',
            name: 'about',
            component: About
        },
        {
            path: '/login',
            component: Login
        },
        // otherwise redirect to home
        {
            path: '*',
            redirect: '/'
        }
    ]
});

router.beforeEach((to, from, next) => {
    // redirect to login page if not logged in and trying to access a restricted page
    const publicPages = ['/login'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    if (authRequired && !loggedIn) {
        return next('/login');
    }

    next();
});

export default router;


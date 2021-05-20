import Vue from 'vue'
import Router from 'vue-router'

import store from '../store'

import Home from "../pages/Home.vue";
import Product from "../pages/Product.vue";
import SignUp from "../pages/SignUp.vue";
import Login from "../pages/Login.vue";

import Dashboard from "../pages/dashboard/Dashboard.vue";
import MyAccount from "../pages/dashboard/MyAccount.vue";

Vue.use(Router);

const routes = [
    {
        path: '/',
        component: Home,
        name: 'home',
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/product/:id',
        component: Product,
        name: 'product',
        props: true
    },
    {
        path: '/signup',
        component: SignUp,
        name: 'SignUp'
    },
    {
        path: '/login',
        component: Login,
        name: 'Login'
    },
    {
        path: '/dashboard',
        component: Dashboard,
        name: 'Dashboard',
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/my-account',
        component: MyAccount,
        name: 'MyAccount',
        meta: {
            requireLogin: true
        }
    },
]

const router = new Router({
  mode: 'history', // https://router.vuejs.org/api/#mode
  routes
})

router.beforeEach((to, from, next) => {
    function authCheck() {
      if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }

    if (!store.state.isAuthenticated) {
        store.commit('INITIALIZE_STORE')

        store.dispatch('checkUser', () => {

        authCheck();
        });

        return;
    }

    authCheck();
})

export default router

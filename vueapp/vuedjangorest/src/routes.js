import Vue from 'vue'
import VueRouter from 'vue-router'
import Shoes from './views/Shoes'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
        path:'/',
        name:'shoes',
        component: Shoes,
        },

    ]
})
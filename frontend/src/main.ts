import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'

import Home from './components/contentComponents/Home.vue'
import Login from './components/contentComponents/Login.vue'
import Register from './components/contentComponents/Register.vue'
import Radio from './components/contentComponents/Radio.vue'
import Player from './components/contentComponents/Player.vue'

const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/login',
        component: Login
    },
    {
        path: '/register',
        component: Register
    },
    {
        path: '/radio',
        component: Radio
    },
    {
        path: '/player/:mountpoint',
        component: Player,
        props: (route: { params: { mountpoint: any } }) => ({mountpoint: route.params.mountpoint})
    }
  ]
  
const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')

import { createApp, provide } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { createStore } from 'vuex';
import './style.css'
import App from './App.vue'

import Home from './components/contentComponents/Home.vue'
import Login from './components/contentComponents/Login.vue'
import Register from './components/contentComponents/Register.vue'
import Radio from './components/contentComponents/Radio.vue'
import Player from './components/contentComponents/Player.vue'
import Content from './components/containerComponents/Content.vue'

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
    },
    {
        path: '/content',
        name: 'Content',
        component: Content
    }
  ]
  
const router = createRouter({
  history: createWebHistory(),
  routes
})

const store = createStore({
    state() {
        return {
            isLoggedIn: false
        }
    },
    mutations: {
        setLoggedIn(state, value) {
            state.isLoggedIn = value
        }
    }
})

export function setupStore(app) {
    app.use(store)
}

const app = createApp(App)
setupStore(app)

provide('store', store)

app.use(router)
app.mount('#app')

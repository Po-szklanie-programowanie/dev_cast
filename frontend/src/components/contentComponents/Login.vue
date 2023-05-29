<template>
    <form @submit.prevent="login">
        <h2>Login</h2>
        <label>
            email
            <input v-model="username" type="text" required>
        </label>
        <label>
            password
            <input v-model="password" type="password" required>
        </label>
        <button type="submit">
            Login
        </button>
    </form>
</template>

<script lang="ts">
import axios from 'axios';
import qs from 'qs';
import { inject } from 'vue';

export default {
    name: "Login",
    data() {
        return {
            username: '',
            password: '',
            error: '',
        }
    },
    setup() {
        const store = inject('store') as any
        const setStateLoginTrue = () => {
            store.commit('setLoggedIn', true)
        }
        return {
            setStateLoginTrue
        }
    },
    methods: {
        async apiRespond() {
            try {
                const form = qs.stringify({
                grant_type: '',
                username: this.username,
                password: this.password,
                scope: '',
                client_id: '',
                client_secret: ''
                });

                const response = await axios.post(
                    'http://localhost:2137/token/', form, {
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        }
                    })
                
                const accessToken = response.data.access_token
                const tokenType = response.data.token_type
                localStorage.setItem('token', accessToken)
                localStorage.setItem('token_type', tokenType)

            } catch(error) {
                alert("błąd logowania: zły login lub hasło")
                detail: this.error
            }
        },
        async login() {
            this.apiRespond()
            this.setStateLoginTrue()
            this.$router.replace('/radio')
        }
    },
}
</script>

<style scoped>

</style>
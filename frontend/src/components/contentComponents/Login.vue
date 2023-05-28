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

export default {
    name: "Login",
    data() {
        return {
            username: '',
            password: '',
            error: '',
        }
    },
    methods: {
        async login() {
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
                this.$router.replace('/radio')
            } catch(error) {
                alert("chuj")
                detail: this.error
            }
        }
    }
}
</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}
</style>
<template>
    <form @submit.prevent="register">
        <label>
            email:
            <input v-model="email" type="text" required>
        </label>
        <label>
            password:
            <input v-model="password" type="password" required>
        </label>
        <button type="submit">
            Register
        </button>
    </form>
</template>

<script lang="ts">
import axios from 'axios';

export default {
    name: "Register",
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        register() {
            try {
                axios.post('http://localhost:2137/users/', {
                    email: this.email,
                    hashed_password: this.password
                })
                alert("Zarejestrowano")
                this.$router.replace('/login')
            } catch(error) {
                alert("błąd")
            }
        }
    }
}
</script>
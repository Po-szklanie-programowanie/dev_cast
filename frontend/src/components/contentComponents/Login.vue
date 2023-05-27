<template>
    <form @submit.prevent="login">
        <label>
            email
            <input v-model="form.email" type="text" required>
        </label>
        <label>
            password
            <input v-model="form.password" type="password" required>
        </label>
        <button type="submit">
            Login
        </button>
    </form>
</template>

<script lang="ts">
export default {
    name: "Login",
    data() {
        return {
            form: {
                email: '',
                password: ''
            }
        }
    },
    methods: {
        login() {
            console.log(this.form.email)
            console.log(this.form.password)
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
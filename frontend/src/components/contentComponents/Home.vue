<template>
    <button @click="redirectToPage('/login')">
        Login
    </button>
    <button @click="redirectToPage('/register')">
        Register
    </button>
</template>

<script lang="ts">
export default {
    name: "Home",
    mounted() {
        localStorage.removeItem('token')
        localStorage.removeItem('tokenType')
    },
    methods: {
        redirectToPage(path: string) {
            this.$router.push(path)
        }
    }
}
</script>
<style scoped>
</style>
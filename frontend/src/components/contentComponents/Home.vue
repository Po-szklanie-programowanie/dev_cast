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
    methods: {
        redirectToPage(path: string) {
            this.$router.push(path)
        }
    }
}
</script>
<style scoped>
</style>
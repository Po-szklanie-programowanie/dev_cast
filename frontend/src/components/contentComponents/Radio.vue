<template>
    <button @click="redirectToPage('/phonk')">
        Phonk
    </button>
    <button @click="redirectToPage('/lofi')">
        Lofi
    </button>
</template>

<script lang="ts">
    export default {
        methods: {
            redirectToPage(path: string) {
                this.$router.push(path)
            }
        }
    }
</script>
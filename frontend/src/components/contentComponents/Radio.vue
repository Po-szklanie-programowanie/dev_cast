<template>
    <button @click="redirectToPage('/player/phonk')">
        Phonk
    </button>
    <button @click="redirectToPage('/player/lofi')">
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
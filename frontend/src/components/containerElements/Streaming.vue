<script setup lang="ts">
defineProps<{genre: string, url: string}>()
</script>

<template>
    <div class="card">
        <h2>{{ genre }}</h2>
        <audio src="{{ url }}" controls></audio>
    </div>
</template>

<style scoped>

</style>
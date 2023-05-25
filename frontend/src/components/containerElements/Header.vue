<script setup lang="ts">
import BackButton from './BackButton.vue';

defineProps<{ title: string }>()

</script>

<template>
    <header class="header">
        <BackButton />
        <h1>{{ title }}</h1>
    </header>
</template>

<style>
</style>
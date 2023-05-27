<template>
    <main>
        <router-view></router-view>
    </main>
</template>

<script lang="ts">
export default {
    name: "Content"
}
</script>

<style>
main {
    display: flex;
    justify-content: space-around;
}
</style>
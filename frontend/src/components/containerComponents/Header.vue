<template>
    <header>
       <h1>{{ text }} </h1>
    </header>
</template>

<script lang="ts">
export default {
    props: {
        text: String
    }
}
</script>

<style scoped>
header {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

button {
    width: 5em;
    height: 50%;
    display: flex;
    align-content: center;
    justify-content: center;
}



</style>
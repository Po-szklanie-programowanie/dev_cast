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
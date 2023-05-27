<template>
    <footer>
        <h4>{{ text }}</h4>
    </footer>
</template>

<script lang="ts">
    export default {
        props: {
            text: String
        }
    }
</script>
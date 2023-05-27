<template>
    <div class="card">
        <h2>{{ mountpoint }}</h2>
        <audio ref="audioPlayer" autoplay controls>
            <source type="audio/mpeg" :src="'http://localhost:8000/'+mountpoint">
        </audio>
    </div>
</template>

<script lang="ts">
    export default {
        props: {
            mountpoint: String
        }
    }
</script>
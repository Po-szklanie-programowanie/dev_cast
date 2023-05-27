<template>
    <div>
        <h2>{{ mountpoint }}</h2>
        <audio ref="audioPlayer">
            <source type="audio/mpeg">
        </audio>
        <div class="audioControlParent">
            <div class="audioControlChild">
                <button @click="play">Play</button>
                <button ref="stopButton" @click="stop">Stop</button>
            </div>
            <div class="audioControlChild">
                <input @input="changeVolume" type="range" v-model="volume"
                min="0" max="100" :volume="volume / 100">
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import {ref} from 'vue'
    export default {
        data() {
            return {
                volume: ref(50),
            }
        },
        props: {
            mountpoint: String
        },
        mounted() {
            const audioPlayer: any = this.$refs.audioPlayer
            audioPlayer.src = `http://localhost:8000/${this.mountpoint}`
            
        },
        methods: {
            isMuted() {
                const audioPlayer: any = this.$refs.audioPlayer
                if(audioPlayer.muted) {
                    return true
                }
                else {
                    return false
                }
            },
            play() {
                const audioPlayer: any = this.$refs.audioPlayer
                if(audioPlayer.muted){
                    audioPlayer.muted = false
                }
                audioPlayer.play()
            },
            stop() {
                const audioPlayer: any = this.$refs.audioPlayer
                audioPlayer.muted = true
            },
            changeVolume(): void { 
                (this.$refs.audioPlayer as HTMLAudioElement).volume = this.volume / 100
            } 
        }
    }
</script>
<style scoped>
div.audioControlParent {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}
div.audioControlChild {
    display: flex;
    justify-content: space-around;
}
</style>
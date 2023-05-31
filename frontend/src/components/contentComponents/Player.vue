<template>
    <div v-if="isLoggedIn">
        <h2>{{ mountpoint }}</h2>
        <img ref="gif" src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif?20151024034921" alt="" width="220" height="124">
        <audio ref="audioPlayer" autoplay>
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
    <div v-else>
        <h2>Nie zalogowałeś się !</h2>
    </div>
</template>

<script lang="ts">
import {ref, inject} from 'vue';
import { computed } from '@vue/reactivity';

export default {
    data() {
        return {
            volume: ref(50),
        }
    },
    setup() {
        const store = inject('store') as any
        const isLoggedIn = computed(() => store.state.isLoggedIn)

        return {
            isLoggedIn
        }
    },
    props: {
        mountpoint: String
    },
    mounted() {
        const audioPlayer: HTMLAudioElement = this.$refs.audioPlayer as HTMLAudioElement
        const gif: HTMLImageElement = this.$refs.gif as HTMLImageElement
        audioPlayer.src = `http://localhost:8000/${this.mountpoint}`
        audioPlayer.addEventListener('playing', ()=>{
            gif.src = "https://media.tenor.com/g5ZphcWaj1MAAAAM/dancing-duck-vibing-duck.gif"
        })
        
        
    },
    methods: {
        isMuted(): boolean {
            const audioPlayer: any = this.$refs.audioPlayer
            if(audioPlayer.muted) {
                return true
            }
            else {
                return false
            }
            },
            play(): void {
                const audioPlayer: any = this.$refs.audioPlayer
                if(audioPlayer.muted){
                    audioPlayer.muted = false
                }
            },
            stop(): void {
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
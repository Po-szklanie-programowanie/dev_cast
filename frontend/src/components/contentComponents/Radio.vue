<template>
    <div v-if="isLoggedIn">
        <button @click="redirectToPage('/player/phonk')">
            Phonk
        </button>
        <button @click="redirectToPage('/player/lofi')">
            Lofi
        </button>
    </div>
    <div v-else>
        <h2>Nie zalogowałeś się !</h2>
    </div>
</template>

<script lang="ts">
import { inject } from 'vue';
import { computed } from '@vue/reactivity';

export default {
    setup() {
        const store = inject('store') as any
        const isLoggedIn = computed(() => store.state.isLoggedIn)

        return {
            isLoggedIn
        }
    },
    methods: {
       redirectToPage(path: string) {
            this.$router.push(path)
        }
    }
}
</script>
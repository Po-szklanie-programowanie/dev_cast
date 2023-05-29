<template>
    <main>
        <router-view></router-view>
        <div v-if="isLoggedIn.value">
            <button @click="back">
                &lt;
            </button>
            <button @click="logout">
                Logout
            </button>
        </div>
    </main>
</template>

<script lang="ts">
import { inject } from 'vue';
import { computed } from '@vue/reactivity';

export default {
    name: "Content",
    setup() {
        const store = inject('store') as any
        const isLoggedIn = computed(() => store.state.isLoggedIn)

        const setStateLoginFalse = () => {
            store.commit('setLoggedIn', false)
        }
        return {
            isLoggedIn,
            setStateLoginFalse
        }
    },
    methods: {
        logout(): void {
            localStorage.removeItem('token')
            localStorage.removeItem('tokenType')
            this.setStateLoginFalse()
            this.$router.replace('/')
        },
        back(): void {
            this.$router.go(-1);
        }
    }
}
</script>

<style>
main {
    display: flex;
    justify-content: space-around;
    flex-direction: column;
}
</style>
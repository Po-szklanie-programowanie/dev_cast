<script lang="ts">

import Header from './components/containerComponents/Header.vue';
import Footer from './components/containerComponents/Footer.vue';
import Content from './components/containerComponents/Content.vue';



export default {
    components: {
      Header, Content, Footer
    }

}

</script>

<template>
    <Header text="/DevCast/"/>
    <Content />
    <Footer text="Dev Cast &copy; 2023 Jakub Goleń Szymon Bal"/>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

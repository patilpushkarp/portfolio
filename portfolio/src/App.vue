<template>
  <div class="app">
    <NavigationBar></NavigationBar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavigationBar from './components/commons/NavigationBar.vue';

export default {
  components: {
    NavigationBar
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap');

@font-face {
    font-family: "Roxborough";
    src: url('~@/assets/fonts/Roxborough CF.ttf');
}

html {
  height: 100vh;
  margin: 0;
  padding: 0;
}

body {
  min-height: 100vh;
}

#app {
  font-family: 'Montserrat', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  height: 100%;
}

h1 {
  font-family: 'Roxborough', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h2 {
  font-family: 'Comfortaa', cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

</style>

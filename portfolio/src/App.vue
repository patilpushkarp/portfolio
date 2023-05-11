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
@import url('https://fonts.googleapis.com/css2?family=Montserrat&family=Snippet&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Snippet&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat&family=Playfair+Display+SC:ital,wght@1,700&family=Snippet&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap');

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
  font-family: 'Cinzel', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h2 {
  font-family: 'Snippet', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h5 {
  font-family: 'Playfair Display SC', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: grey;
}

</style>

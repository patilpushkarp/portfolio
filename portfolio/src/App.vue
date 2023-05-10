<template>
  <div class="app">
    <NavigationBar></NavigationBar>
  </div>
</template>

<script>
import NavigationBar from './components/commons/NavigationBar.vue';

export default{
  components:{
    NavigationBar
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Montserrat', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

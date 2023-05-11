<template>
  <div class="home">
    <div class="jumbotron">
      <div class="name">
        <h1>Pushkar</h1>
        <br>
        <h1>Patil</h1>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  background-image: linear-gradient(to right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0.7),
      rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.7)), url("./../assets/lotus.jpeg");
  background-size: cover;
  background-position: center;
  height: 100vh;
}

.jumbotron {
  margin: 0;
}

.name {
  position: fixed;
  justify-content: center;
  align-items: left;
  display: flex;
  flex-direction: column;
  height: 100%;
  left: 10%;
}

h1 {
  color: white;
  text-align: left;
  font-size: 8rem;
}
</style>

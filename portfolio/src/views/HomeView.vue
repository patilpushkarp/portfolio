<template>
  <div class="home">
    <div class="jumbotron">
      <div class="name">
        <div class="main-name">
          <h1>Pushkar Patil</h1>
        </div>
        <div class="d-flex nav-buttons">
          <div class="nav-button-wrap">
            <button type="button" class="btn nav-button btn-lg">About</button>
          </div>
          <div class="nav-button-wrap">
            <button type="button" class="btn nav-button btn-lg">Blogs</button>
          </div>
          <div class="nav-button-wrap">
            <button type="button" class="btn nav-button btn-lg">Projects</button>
          </div>
          <div class="nav-button-wrap">
            <button type="button" class="btn nav-button btn-lg">Connect</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  background-color: black;
  background-size: cover;
  background-position: center;
  height: 100vh;
}

.jumbotron{
  height: 100%;
}

.name {
  position: fixed;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  margin: 5% 0;
}

h1 {
  font-family: 'Unbounded', cursive;
  color: white;
  text-align: center;
  font-size: 8rem;
}

.nav-buttons{
  height: 30%;
  width: 100%;
  padding: 10% 5%;
}

.nav-button-wrap{
  flex: 1;
  align-items: center;
}

.nav-button{
  border: 0;
  border-radius: 25px;
  color: orange;
}

.nav-button:hover {
  background-color: orange;
  box-shadow: 0 12px 16px 0 rgba(220, 95, 6, 0.24),0 17px 50px 0 rgba(220, 95, 6,0.19);
}
</style>

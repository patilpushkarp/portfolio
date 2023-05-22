<template>
  <div class="home">
    <div class="jumbotron">
      <div class="name">
        <div class="main-name fade-in">
          <h1>Pushkar Patil</h1>
        </div>
        <div class="d-flex nav-buttons">
          <div v-for="(button, index) in navButtons" :key="index" class="nav-button-wrap pop-up">
            <router-link :to="button.route">
              <button type="button" class="btn nav-button btn-lg">
                {{ button.label }}
              </button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      navButtons: [
        { label: 'About', route: '/about' },
        { label: 'Blogs', route: '/blogs' },
        { label: 'Projects', route: '/projects' },
        { label: 'Connect', route: '/connect' },
      ],
    };
  },
};
</script>

<style scoped>
.home {
  background-color: black;
  background-size: cover;
  background-position: center;
  height: 100vh;
}

.jumbotron {
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

.nav-buttons {
  height: 30%;
  width: 100%;
  padding: 10% 5%;
  display: flex;
  justify-content: center;
}

.nav-button-wrap {
  flex: 1;
  align-items: center;
  color: orange;
}

.nav-button-wrap:hover {
  background-color: orange;
  color: black;
}

.nav-button {
  border: 0;
  border-radius: 25px;
  color: orange;
}

.nav-button:hover {
  background-color: orange;
  color: black;
  box-shadow: 0 12px 16px 0 rgba(220, 95, 6, 0.24), 0 17px 50px 0 rgba(220, 95, 6, 0.19);
}

.btn {
  color: orange;
  background-color: transparent;
  border-radius: 30px;
  padding: 10px 20px;
  transition: all 0.3s;
}

.btn:hover {
  background-color: orange;
  color: black;
}

 /* Animations*/

.fade-in {
  opacity: 0;
  animation: fade-in-animation 1s forwards;
}

@keyframes fade-in-animation {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.pop-up {
  opacity: 0;
  animation: pop-up-animation 0.5s ease-in-out forwards;
}

@keyframes pop-up-animation {
  0% {
    transform: translateY(50%);
    opacity: 0;
  }
  50% {
    transform: translateY(-10%);
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

</style>

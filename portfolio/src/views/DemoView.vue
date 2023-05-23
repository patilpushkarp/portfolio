<template>
    <div class="container">
        <div class="centered-button">
            <button @click="toggleShowSection">Toggle Section</button>
        </div>
        <transition name="fade" appear>
            <h2>Some text</h2>
        </transition>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            showSection: false,
        };
    },
    methods: {
        toggleShowSection() {
            this.showSection = !this.showSection;
        },
    },
};
</script>
  
<style scoped>
.container {
    position: relative;
    height: 100vh;
}

.centered-button {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 1;
}

.fade-enter-from {
    opacity: 0;
}

.fade-enter-active {
    transition: opacity 3s;
}

.fade-enter-to {
    opacity: 1;
}

.fade-leave-from {
    opacity: 1;
}

.fade-leave-active {
    transition: opacity 3s;
}

.fade-leave-to {
    opacity: 0;
}
</style>
<template>
    <div class="navigation">
        <nav class="navbar">
            <div class="container">
                <router-link class="navbar-brand" to="/">
                    <img src="../../assets/logo.png" alt="Logo" width="50" height="50">
                </router-link>

                <div class="row">
                    <div class="col-6">
                        <audio ref="audioPlayer" :src="audioFile" loop></audio>
                        <button class="navbar-toggler" type="button" @click="toggleAudioMute">
                            <span class="navbar-menu" v-if="!isMuted"><font-awesome-icon :icon="['fas', 'play']" /></span>
                            <span class="navbar-menu" v-else><font-awesome-icon :icon="['fas', 'pause']" /></span>
                        </button>
                    </div>
                    <div class="col-6">
                        <button class="navbar-toggler" type="button" @click="toggleMenu">
                            <span class="navbar-menu"><font-awesome-icon :icon="['fas', 'bars']" /></span>
                        </button>
                    </div>
                </div>

                <div class="collapse navbar-collapse" :class="{ 'show': isMenuOpen }">

                    <button class="navbar-toggler navbar-close" type="button" @click="toggleMenu">
                        <font-awesome-icon :icon="['fas', 'xmark']"></font-awesome-icon>
                    </button>

                    <div class="nav-content">
                        <h5>Know More</h5>
                        <ul class="navbar-nav ml-auto">
                            <li class="nav-item">
                                <h2><router-link class="nav-link" to="/about" @click="toggleMenu">About me</router-link>
                                </h2>
                            </li>
                            <li class="nav-item">
                                <h2><router-link class="nav-link" to="/projects" @click="toggleMenu">Projects</router-link>
                                </h2>
                            </li>
                            <li class="nav-item">
                                <h2><router-link class="nav-link" to="/blogs" @click="toggleMenu">Blogs</router-link></h2>
                            </li>
                            <li class="nav-item">
                                <h2><router-link class="nav-link" to="/connect" @click="toggleMenu">Connect with
                                        me</router-link></h2>
                            </li>
                        </ul>
                    </div>
                </div>

            </div>
        </nav>
    </div>
</template>
  
<script>
import audioFile from '@/assets/audio/music.mp3'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';

library.add(fas);

export default {

    components: {
        FontAwesomeIcon,
    },

    data() {
        return {
            isMenuOpen: false,
            audioFile: audioFile,
            isFirstClick: true,
            isMuted: false
        };
    },

    mounted() {
        const audioPlayer = new Audio(this.audioFile);
        this.$refs.audioPlayer = audioPlayer;
        document.addEventListener('click', this.handleClick);
    },

    methods: {
        toggleMenu() {
            this.isMenuOpen = !this.isMenuOpen;
        },

        toggleAudioMute() {
            const audioPlayer = this.$refs.audioPlayer;
            audioPlayer.muted = !audioPlayer.muted;
            this.isMuted = !this.isMuted;
        },

        handleClick() {
            if (this.isFirstClick) {
                this.isFirstClick = false;

                const audioPlayer = this.$refs.audioPlayer;
                audioPlayer.play();
                this.isMuted = !this.isMuted;
            }
        }
    },
    beforeUnmount() {
        document.removeEventListener('click', this.handleClick);
    },
};
</script>
  
<style scoped>
.navigation {
    max-width: 100%;
}

.navbar {
    margin-bottom: 0px;
}

.navbar-toggler {
    border-width: 0;
    background-color: black;
}

.navbar-menu {
    color: white;
    font-size: 1.5rem;
}

.navbar-nav {
    flex-direction: column;
}

.nav-link {
    padding: 2.5rem 1rem;
    color: white;
}

.navbar {
    width: 100vw;
    position: relative;
}

.collapse.navbar-collapse.show {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 100;
    background-color: black;
}

.container {
    height: 100%;
}

.navbar-close {
    position: fixed;
    top: 10%;
    right: 10%;
    margin: 0;
    padding: 0;
    border: none;
    background-color: transparent;
    color: #ffffff;
    font-size: 3rem;
    width: 5%;
}

.nav-content {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.navigation {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: transparent;
    z-index: 9999;
}
</style>
  
<template>
    <div class="connect">

        <div class="row">
            <div class="col-7">
                <div class="opening">
                    <div ref="opening">
                        <transition name="fade" appear>
                            <div>
                                <h3>To say - </h3>
                                <h1><b><em>"Ram, Ram, Patil!"</em></b></h1>
                            </div>
                        </transition>
                    </div>
                </div>
            </div>
            <div class="col-5">
                <div class="connectors">
                    <div ref="connectors">
                        <transition name="slide" appear>
                            <div>
                                <div class="connector-button">
                                    <a target="_blank" href="https://www.linkedin.com/in/patilpushkarp/"
                                        class="connector-link">LindedIn</a>
                                </div>
                                <div class="connector-button">
                                    <a href="mailto:patilpushkarp@live.com" class="connector-link">Email</a>
                                </div>
                            </div>
                        </transition>
                    </div>
                </div>
            </div>
        </div>

        <FooterBar></FooterBar>

    </div>
</template>

<script>
import FooterBar from '@/components/commons/FooterBar.vue';

export default {
    components: {
        FooterBar,
    }
}
</script>

<style scoped>
.connect {
    background-color: black;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100vh;
    color: white;
}

.opening {
    margin: 15% 15%;
    text-align: left;
    justify-content: center;
    display: flex;
    flex-direction: column;
    height: 70%;
}

.opening h3 {
    font-family: 'Comfortaa', cursive;
    font-size: 2rem;
}

.opening h1 {
    font-size: 4rem;
    color: cyan;
}

.row {
    height: 100%;
}

.connectors {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
}

.connector-button {
    padding: 10% 5%;
}

.connector-link {
    color: orange;
    text-decoration: none;
    font-size: 1.5rem;
    padding: 2% 5%;
    border-radius: 30px;
}

.connector-link:hover {
    background-color: orange;
    color: black;
    box-shadow: 0 12px 16px 0 rgba(220, 95, 6, 0.24), 0 17px 50px 0 rgba(220, 95, 6, 0.19);
}

/* Animations */

.fade-enter-from {
    opacity: 0;
    transform: translateY(20px);
}

.fade-enter-active {
    transition: opacity 4s, transform 1s;
}

.fade-enter-to {
    opacity: 1;
    transform: translateY(0);
}

.slide-enter-active {
    transition: transform 2s;
}

.slide-enter-from {
    transform: translateX(100%);
}
</style>
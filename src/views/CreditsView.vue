<template>
    <div class="credits">
        <div class="music-credits">
            <div class="card">
                <div class="card-header">
                    <b>MUSIC</b>
                </div>
                <div class="card-body">
                    <p>Zack Hemsey - "The Way (Instrumental)"</p>
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
    },
}
</script>

<style scoped>
.credits {
    background-color: black;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100vh;
    color: white;
}

.music-credits {
    height: 60%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: black;
}

.card {
    width: 60%;
}
</style>
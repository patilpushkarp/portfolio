<template>
    <footer>
        <div class="d-flex">
            <div class="flex-fill">
                Pushkar Patil
            </div>
            <div class="flex-fill">
                All rights reserved
            </div>
            <div class="flex-fill">
                <router-link to="/credits" class="credits-link">Credits</router-link>
            </div>
        </div>
    </footer>
</template>

<style scoped>
footer {
    padding: 5%;
    background-color: black;
    color: white;
}

.credits-link{
    text-decoration: none;
    color: white;
}
</style>
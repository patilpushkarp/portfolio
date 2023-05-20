<template>
    <div class="blogs-viewer">

        <div class="blogs-page-heading">
            <h1>Blogs 🗒</h1>
        </div>

        <div v-for="blog in blogsData" :key="blog.id" class="container">
            <div class="card">
                <div class="card-body">
                    <div class="row">
                        <div class="col-4 blog-image-space">
                            <img :src="blog.blogImage" class="blog-image"  alt="Blog Image"/>
                        </div>
                        <div class="col-8 blog-heading">
                            <h2><router-link :to="{ name: 'blog', params: { id: blog.id }}" class="blog-link">{{ blog.blogName }}</router-link></h2>
                        </div>
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
    },
    data() {
        return {
            blogsData: []
        };
    },
    async mounted() {
        await this.fetchData();

    },
    methods: {
        async fetchData() {
            try {
                const response = await fetch("http://127.0.0.1:8000/blogs");
                const data = await response.json();
                this.blogsData = data;
            } catch (error) {
                console.error(error);
            }
        },
    }
}
</script>

<style scoped>
.blogs-viewer {
    background-color: black;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100vh;
    color: white;
}


.blogs-page-heading {
    height: 100%;
    justify-content: center;
    align-items: center;
    display: flex;
}

h1 {
    font-size: 7rem;
    color: orange;
}

.card {
    border-radius: 30px;
    color: mediumvioletred;
    height: 40vh;
}

.card-body {
    display: flex;
    align-items: center;
}

.container {
    padding-bottom: 5%;
}

.blog-heading {
    text-align: left;
    padding: 5% 7% 5% 3%;
    text-align: justify;
}

.blog-image-space{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
}

.blog-image{
    width: 80%;
}

.blog-link{
    text-decoration: none;
    color: mediumvioletred;
}

</style>
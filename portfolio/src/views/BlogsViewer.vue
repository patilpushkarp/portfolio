<template>
    <div class="blogs-viewer">

        <div class="blogs-page-heading">
            <div ref="blogHead">
                <transition name="fade" appear>
                    <h1>Blogs 🗒</h1>
                </transition>
            </div>
        </div>

        <div v-for="blog in blogsData" :key="blog.id" class="container" :data-section-id="blog.id" ref="blogs">
            <transition name="slide">
                <div class="card" v-if="showSection(blog.id)">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-4 blog-image-space">
                                <img :src="blog.blogImage" class="blog-image" alt="Blog Image" />
                            </div>
                            <div class="col-8 blog-heading">
                                <h2><router-link :to="{ name: 'blog', params: { id: blog.id } }" class="blog-link">{{
                                    blog.blogName }}</router-link></h2>
                            </div>
                        </div>
                    </div>
                </div>
            </transition>
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
            blogsData: [],
            observedSections: [],
        };
    },
    async mounted() {
        await this.fetchData();
        this.initializeSections();
        this.observeIntersections();
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

        initializeSections() {
            this.blogsData.forEach((blog) => {
                this.observedSections.push({ id: blog.id, visible: false });
            });
        },

        observeIntersections() {
            const options = {
                root: null,
                rootMargin: '0px',
                threshold: 0,
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    const sectionId = parseInt(entry.target.dataset.sectionId);
                    const index = this.observedSections.findIndex((item) => item.id === sectionId);

                    if (entry.isIntersecting) {
                        if (index === -1) {
                            this.observedSections.push({ id: sectionId, visible: true });
                        } else {
                            this.observedSections[index].visible = true;
                        }
                    }
                });
            }, options);

            this.$refs.blogs.forEach((section) => {
                observer.observe(section);
            });
        },

        showSection(sectionId) {
            const index = this.observedSections.findIndex((item) => item.id === sectionId);
            return index !== -1 && this.observedSections[index].visible;
        },
    },
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
    height: 101%;
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

.blog-image-space {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
}

.blog-image {
    width: 80%;
}

.blog-link {
    text-decoration: none;
    color: mediumvioletred;
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
    transform: translateX(-100%);
}
</style>
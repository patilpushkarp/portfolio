<template>
    <div class="projects-viewer">

        <div class="projects-page-heading">
            <div ref="projectHead">
                <transition name="fade" appear>
                    <h1>Projects 💻</h1>
                </transition>
            </div>
        </div>

        <div v-for="project in projectsData" :key="project.id" class="container" :data-section-id="project.id"
            ref="projects">
            <transition name="slide">
                <div class="card" v-if="showSection(project.id)">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-5">
                                <div class="project-image-space">
                                    <img :src="getGoogleDriveImageURL(project.projectImage)" class="project-image"
                                        alt="Project Image" />
                                </div>
                            </div>
                            <div class="col-md-7">
                                <div class="project-heading">
                                    <h2><a target="_blank" class="project-link" :href="project.projectURL">{{
                                        project.projectName }}</a></h2>
                                </div>
                                <div class="project-summary">
                                    <p>{{ project.projectSummary }}</p>
                                </div>
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
import config from '@/config.js';
import FooterBar from '@/components/commons/FooterBar.vue';

export default {
    components: {
        FooterBar,
    },
    data() {
        return {
            projectsData: [],
            observedSections: [],
            backendUrl: config[process.env.NODE_ENV].backendUrl,
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
                const response = await fetch(`${this.backendUrl}/projects`);
                const data = await response.json();
                this.projectsData = data;
            } catch (error) {
                console.error(error);
            }
        },

        initializeSections() {
            this.projectsData.forEach((project) => {
                this.observedSections.push({ id: project.id, visible: false });
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

            this.$refs.projects.forEach((section) => {
                observer.observe(section);
            });
        },

        showSection(sectionId) {
            const index = this.observedSections.findIndex((item) => item.id === sectionId);
            return index !== -1 && this.observedSections[index].visible;
        },

        getGoogleDriveImageURL(imageId) {
            return `https://drive.google.com/uc?export=view&id=${imageId}`;
        },
    }
}
</script>

<style scoped>
.projects-viewer {
    background-color: black;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100vh;
    color: white;
}


.projects-page-heading {
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
    height: 85vh;
}

.card-body {
    display: flex;
    align-items: center;
}

.container {
    padding-bottom: 5%;
}

.project-image-space {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.project-heading {
    text-align: left;
    padding: 5% 7% 5% 3%;
    color: mediumvioletred;
}

.project-summary {
    text-align: left;
    padding: 5% 7% 5% 3%;
    color: black;
}

.project-image {
    width: 80%;
}

.project-link {
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
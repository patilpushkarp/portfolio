<template>
    <div class="projects-viewer">

        <div class="projects-page-heading">
            <h1>Projects 💻</h1>
        </div>

        <div v-for="project in projectsData" :key="project.id" class="container">
            <div class="card">
                <div class="card-body">
                    <div class="row">
                        <div class="col-5">
                            <div class="project-image-space">
                                <img :src="getGoogleDriveImageURL(project.projectImage)" class="project-image" alt="Project Image" />
                            </div>
                        </div>
                        <div class="col-7">
                            <div class="project-heading">
                                <h2><a target="_blank" class="project-link" :href="project.projectURL">{{ project.projectName }}</a></h2>
                            </div>
                            <div class="project-summary">
                                <p>{{ project.projectSummary }}</p>
                            </div>
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
            projectsData: []
        };
    },
    async mounted() {
        await this.fetchData();

    },
    methods: {
        async fetchData() {
            try {
                const response = await fetch("http://127.0.0.1:8000/projects");
                const data = await response.json();
                this.projectsData = data;
            } catch (error) {
                console.error(error);
            }
        },
        getGoogleDriveImageURL(imageId) {
            // const folderId = "1O5k910kLy5szvvZGkJNRTEvuuDznPcqA";
            // return `https://drive.google.com/file/d/${imageId}/view`;
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

.project-link{
    text-decoration: none;
    color: mediumvioletred;
}
</style>
<template>
    <div class="blog">

        <div class="blog-heading">
            <div class="blog-heading-area">
                <h1>{{ textHeading }}</h1>
                <p>{{ summary }}</p>
            </div>
        </div>

        <div class="container">
            <div class="card">
                <div class="card-body">
                    <div class="blog-body">
                        <div v-for="text in texts" :key="text.source" class="markdown-text">
                            <div v-if="text.cell_type === 'markdown'" v-html="convertMarkdownToHtml(text)"></div>
                            <div v-else :id="text.metadata.tags[0]"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <FooterBar></FooterBar>
    </div>
</template>
  
<script>
import config from '@/config.js';
import { marked } from "marked";
import * as Plotly from 'plotly.js-dist';

import FooterBar from '@/components/commons/FooterBar.vue';

export default {
    components: {
        FooterBar,
    },
    data() {
        return {
            texts: [],
            textHeading: "",
            summary: "",
            backendUrl: config[process.env.NODE_ENV].backendUrl,
        };
    },
    async mounted() {
        this.id = this.$route.params.id;
        await this.fetchData();
        this.getHeading();
        this.getSummary();
        this.renderCharts();
    },
    methods: {
        async fetchData() {
            try {
                const response = await fetch(`${this.backendUrl}/blog/${this.id}`);
                const data = await response.json();
                this.texts = data;
            } catch (error) {
                console.error(error);
            }
        },

        getHeading() {
            const objectWithHeading = this.texts.find((item) => {
                const metadataWithTagHeading = item.metadata.tags.find((metadataTagItem) => metadataTagItem.includes("heading"));
                return metadataWithTagHeading !== undefined;
            });

            this.textHeading = objectWithHeading ? objectWithHeading.source : null;
            this.textHeading = this.textHeading.replace("#", "").trim();

            this.texts = this.texts.filter(item => !item.metadata || !item.metadata.tags || !item.metadata.tags.includes("heading"));
        },

        getSummary() {
            const objectWithSummary = this.texts.find((item) => {
                const metadataWithTagSummary = item.metadata.tags.find((metadataTagItem) => metadataTagItem.includes("summary"));
                return metadataWithTagSummary !== undefined;
            });

            this.summary = objectWithSummary ? objectWithSummary.source : null;

            this.texts = this.texts.filter(item => !item.metadata || !item.metadata.tags || !item.metadata.tags.includes("summary"));
        },

        convertMarkdownToHtml(textObject) {
            if (textObject.cell_type === "code"){
                return "";
            }
            
            const markdown = textObject.source
            if (!markdown) {
                return "";
            }
            const renderer = new marked.Renderer();
            renderer.heading = function (text, level) {
                return `<h${level} class="custom-heading">${text}</h${level}>`;
            };

            marked.setOptions({ renderer });

            return marked(markdown);
        },

        renderCharts() {
            this.texts.forEach(item => {
                if (item.outputs) {
                    const chartData = item.outputs[0].data["application/vnd.plotly.v1+json"].data
                    const chartLayout = item.outputs[0].data["application/vnd.plotly.v1+json"].layout

                    const chartElementId = item.metadata.tags[0];
                    Plotly.newPlot(chartElementId, chartData, chartLayout);

                }
            });
        },
    },
};
</script>
  
<style scoped>
.blog {
    background-color: black;
    overflow-y: auto;
    overflow-x: hidden;
    height: 100vh;
    color: white;
}

h1 {
    font-size: 4rem;
}

.blog-heading {
    height: 100%;
    display: flex;
    /* flex-direction: column; */
    align-items: end;
}

.blog-heading-area {
    margin: 5%;
    padding: 5%;
    width: 70%;
    text-align: left;

}

.blog-heading-area p {
    font-size: 1rem;
}

.card {
    border-radius: 30px;
}

.blog-body {
    padding: 9% 10%;
    text-align: left;
}

.markdown-text {
    color: black;
    padding: 1% 0;
}

.custom-heading {
    color: orange;
}
</style>
  
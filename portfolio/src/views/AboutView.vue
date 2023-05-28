<template>
  <div class="about">

    <!-- Greetings -->
    <div class="greeting">
      <span ref="greeting">
        <transition name="fade" appear>
          <h1 style="color: orange;" v-show="greetingSection">Namaskar</h1>
        </transition>
        <transition name="pranam" appear>
          <h1 v-show="greetingSection">🙏🏼</h1>
        </transition>
      </span>
    </div>

    <!-- Introductory line -->
    <div class="jumbotron">
      <div class="container intro-line" ref="intro">
        <transition name="fade" appear>
          <h2 v-show="introSection">I am a tech enthusiast and business graduate, currently exploring and experimenting
            with
            diverse career avenues.</h2>
        </transition>
      </div>
    </div>

    <!-- Introductio -->
    <div class="intro">
      <div class="jumbotron">
        <div ref="about">
          <transition name="fade" appear>
            <h1 v-show="aboutSection">ABOUT</h1>
          </transition>
        </div>
      </div>

      <div class="row">
        <div class="col-6">
          <div class="paragraph">
            <div ref="aboutPara1">
              <transition name="slide" appear>
                <p v-show="aboutPara1Section">Driven by a lifelong pursuit of excellence, I have consistently demonstrated
                  a passion for achievement
                  since my early years. As a distinguished rank holder in school, a championship skater, and a top
                  performer
                  in competitive exams, I have thrived on challenges and continuously pushed myself to surpass
                  expectations.
                  Additionally, my artistic talents have positioned me as a reliable go-to person for creative endeavors.
                </p>
              </transition>
            </div>
          </div>
        </div>
        <div class="col-6">
          <!-- No content here -->
        </div>
      </div>
      <div class="row">
        <div class="col-6">

          <!-- No content here -->
        </div>
        <div class="col-6">
          <div class="paragraph">
            <div ref="aboutPara2">
              <transition name="slide" appear>
                <p v-show="aboutPara2Section">During my collegiate journey in engineering, I encountered a pivotal moment
                  of self-reflection.
                  Navigating
                  through the demands of academia and societal pressures, I momentarily lost sight of my true passions and
                  purpose. However, the onset of the global pandemic served as a catalyst for profound personal growth. It
                  rekindled a long-held dream within me—a desire to establish my own technology-driven business.</p>
              </transition>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-6">
          <div class="paragraph">
            <div ref="aboutPara3">
              <transition name="slide" appear>
                <p v-show="aboutPara3Section">Motivated by this newfound clarity, I embarked on a deliberate path of
                  self-discovery and skill
                  development. With unwavering dedication, I have been actively acquiring the knowledge and expertise
                  necessary to transform my entrepreneurial vision into a tangible and successful reality. Eager to
                  contribute
                  to the technology landscape, I am now poised to leverage my diverse background and multifaceted skill
                  set to
                  make a lasting impact in the business world.</p>
              </transition>
            </div>
          </div>
        </div>
        <div class="col-6">
          <!-- No content here -->
        </div>
      </div>
    </div>

    <!-- Experience -->
    <div class="experience">
      <div class="jumbotron">
        <div ref="experience">
          <transition name="fade" appear>
            <h1 v-show="experienceSection">EXPERIENCE</h1>
          </transition>
        </div>
      </div>

      <div class="container">
        <div class="card">
          <div class="card-header">
            <div ref="summary">
              <transition name="fade" appear>
                <div class="summary" v-show="summarySection">
                  Experienced Technology Consultant with 3+ years of expertise in digital transformation for e-commerce,
                  research operations, and pharmacovigilance in the Retail and Life Sciences & Healthcare industries.
                  Skilled in Product Development, Analytics, Cloud Transformation, and Automation within an Agile
                  framework.
                  Proactive self-starter who has successfully implemented five initiatives to improve team efficiencies
                  and
                  reduce development time.
                </div>
              </transition>
            </div>
          </div>

          <div class="card-body experience-details">
            <div ref="company">
              <transition name="fade" appear>
                <div class="row" v-show="companySection">
                  <div class="col-8">
                    <div class="company">
                      Deloitte India Consulting Pvt. Ltd.
                    </div>
                  </div>
                  <div class="col-4">
                    <div class="tenure">
                      Aug 2018 - Jan 2022
                    </div>
                  </div>
                </div>
              </transition>
            </div>

            <div ref="role">
              <transition name="slide" appear>
                <div class="role" v-show="roleSection">
                  <em>Consultant / Engineer 1</em>
                </div>
              </transition>
            </div>

            <hr>

            <div ref="productDev">
              <transition name="slide" appear>
                <div class="row" v-show="productDevSection">
                  <div class="col-5">
                    <div class="description-heading">
                      <b>Product Development</b>
                    </div>
                  </div>

                  <div class="col-7">
                    <div class="description">
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">Engaged in ConvergeHealth Safety's ETL pipeline creation saving
                          processing
                          time by 66% and
                          reducing
                          cost
                          by 50%</li>
                        <li class="list-group-item">Constructed a Python library for ETL of Pharmacovigilance Documents in
                          Converge to reduce
                          development
                          time
                          by 80%</li>
                        <li class="list-group-item">Assisted in Data Science Software Architecture creation, reducing
                          cloud
                          infra costs by 50% and
                          improving
                          revenue by 3x</li>
                        <li class="list-group-item">Volunteered in creation of application for visualization and
                          understanding
                          of the relationship
                          between
                          attributes of DBs</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </transition>
            </div>

            <hr>

            <div ref="cloudTransform">
              <transition name="slide" appear>
                <div class="row" v-show="cloudTransformSection">
                  <div class="col-5">
                    <div class="description-heading">
                      <b>Analytics</b>
                    </div>
                  </div>

                  <div class="col-7">
                    <div class="description">
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">Saved $20 million of client by mining and wrangling medical insurance
                          big
                          data in AWS cloud for Value-Based Contracts</li>
                        <li class="list-group-item">Created dashboard for leading automobile company for visualizing and
                          analyzing vendors improving the tracking & ordering</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </transition>
            </div>

            <hr>

            <div ref="analytics">
              <transition name="slide" appear>
                <div class="row" v-show="analyticsSection">
                  <div class="col-5">
                    <div class="description-heading">
                      <b>Cloud Transformation</b>
                    </div>
                  </div>

                  <div class="col-7">
                    <div class="description">
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">Engaged ETL pipeline creation for migration to AWS cloud enabling data
                          analytics ecosystem for drug discovery & exploration</li>
                        <li class="list-group-item">Analyzed AWS services for cloud migration compared to self-developed
                          applications hosted on the cloud for LHSC use cases</li>
                        <li class="list-group-item">Created microservices for performing EDA and Causal Inference for top
                          pharmaceutical client reducing their research time.</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </transition>
            </div>

            <hr>

            <div ref="automation">
              <transition name="slide" appear>
                <div class="row" v-show="automationSection">
                  <div class="col-5">
                    <div class="description-heading">
                      <b>Automation</b>
                    </div>
                  </div>

                  <div class="col-7">
                    <div class="description">
                      <ul class="list-group list-group-flush">
                        <li class="list-group-item">Created an automatic testing Web Application to reduce testing and
                          report
                          generation time by 75% for each dataset</li>
                        <li class="list-group-item">Optimised performance of application to parse US addresses, improving
                          run
                          time by 99% & resource utilization by 50%</li>
                        <li class="list-group-item">Automated semi-structure file conversions processes to improve the
                          compatibility of ETL application to more file formats</li>
                        <li class="list-group-item">Implemented scripts to automate image & file mappings for leading
                          retailer
                          saving 1 labor hour / day for 15 members</li>
                        <li class="list-group-item">Created microservices for Big Data migration QA application to detect
                          duplicate and corrupted entries across multiple DBs</li>
                        <li class="list-group-item">Assisted in the integration of machine learning models to improve the
                          capability & user experience of proprietary viz SaaS</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </transition>
            </div>

          </div>
        </div>


      </div>
    </div>

    <!-- Education -->
    <div class="education">
      <div class="jumbotron">
        <div ref="studies">
          <transition name="fade" appear>
            <h1 v-show="studiesSection">Studies</h1>
          </transition>
        </div>
      </div>

      <div class="studies-details">
        <div class="container">
          <div class="card">
            <div class="card-body education-details">

              <div ref="school1">
                <transition name="slide" appear>
                  <div class="row" v-show="school1Section">
                    <div class="col-3">
                      Masters in Business Administration
                    </div>
                    <div class="col-7">
                      Indian Institute of Management, Udaipur
                    </div>
                    <div class="col-2">
                      3.42 / 4.00
                    </div>
                  </div>
                </transition>
              </div>

              <hr>

              <div ref="school2">
                <transition name="slide" appear>
                  <div class="row" v-show="school2Section">
                    <div class="col-3">
                      Bachelor of Technology
                    </div>
                    <div class="col-7">
                      Veermata Jijabai Technological Institute, Mumbai
                    </div>
                    <div class="col-2">
                      7.86 / 10.00
                    </div>
                  </div>
                </transition>
              </div>

              <hr>

              <div ref="school3">
                <transition name="slide" appear>
                  <div class="row" v-show="school3Section">
                    <div class="col-3">
                      12th
                    </div>
                    <div class="col-7">
                      Nowrosjee Wadia College, Pune
                    </div>
                    <div class="col-2">
                      82.5%
                    </div>
                  </div>
                </transition>
              </div>

              <hr>

              <div ref="school4">
                <transition name="slide" appear>
                  <div class="row" v-show="school4Section">
                    <div class="col-3">
                      10th
                    </div>
                    <div class="col-7">
                      Global Indian International School, Pune
                    </div>
                    <div class="col-2">
                      92.4%
                    </div>
                  </div>
                </transition>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Skills and Tools-->
    <div class="skills">
      <div class="jumbotron">
        <div ref="skills">
          <transition name="fade" appear>
            <h1 v-show="skillsSection">SKILLS & TOOLS</h1>
          </transition>
        </div>
      </div>

      <div class="container">
        <div class="card">
          <div class="card-header skills-wrapper">

            <div ref="skillsList">
              <transition name="fade" appear>
                <div class="row" v-show="skillsListSection">
                  <div class="col-4">
                    <div class="skills-head">
                      <b>Skills</b>
                    </div>
                  </div>
                  <div class="col-8">
                    <div class="skills-list">
                      <div class="row">
                        <div class="col-6">
                          <ul class="list-group list-group-flush">
                            <li class="list-group-item">Data Analytics</li>
                            <li class="list-group-item">Machine Learning</li>
                            <li class="list-group-item">Web Development</li>
                            <li class="list-group-item">Product Development</li>
                          </ul>
                        </div>
                        <div class="col-6">
                          <ul class="list-group list-group-flush">
                            <li class="list-group-item">Causal Inference</li>
                            <li class="list-group-item">Natural Language Processing</li>
                            <li class="list-group-item">Software Development Life Cycle</li>
                            <li class="list-group-item">Deep Learning</li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </transition>
            </div>

          </div>

          <div class="card-body tools-wrapper">

            <div ref="toolsList">
              <transition name="fade" appear>
                <div class="row" v-show="toolsListSection">
                  <div class="col-4">
                    <div class="tools">
                      <b>Tools</b>
                    </div>
                  </div>
                  <div class="col-8">
                    <div class="tools-list">
                      <div class="row">
                        <div class="col-6">
                          <ul class="list-group list-group-flush">
                            <li class="list-group-item">Data Analytics</li>
                            <li class="list-group-item">Machine Learning</li>
                            <li class="list-group-item">Web Development</li>
                            <li class="list-group-item">Product Development</li>
                          </ul>
                        </div>
                        <div class="col-6">
                          <ul class="list-group list-group-flush">
                            <li class="list-group-item">Causal Inference</li>
                            <li class="list-group-item">Natural Language Processing</li>
                            <li class="list-group-item">Software Development Life Cycle</li>
                            <li class="list-group-item">Deep Learning</li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </transition>
            </div>

          </div>

        </div>
      </div>
    </div>

    <div ref="connect">
      <transition name="slideup" appear>
        <div class=connect v-show="connectSection">
          <div class="container">
            <div class="card">
              <div class="card-header">
                <div class="row">
                  <div class="col-5 connect-header">
                    Fancy a chat?
                  </div>
                  <div class="col-7">
                    <div class="connect-paragraph">
                      Looking to connect with like-minded professionals who are passionate about leveraging technology
                      to
                      drive transformative change? As an experienced Technology Consultant with a knack for delivering
                      innovative solutions, I invite you to connect with me. Together, we can explore opportunities to
                      collaborate, exchange insights, and create a positive impact in the realms of e-commerce, research
                      operations, and pharmacovigilance. Let's join forces to drive industry advancements, optimize
                      processes, and propel our careers to new heights. Connect with me today and let's make a
                      difference
                      together!
                    </div>
                    <div class="connect-button-wrapper">
                      <router-link to="/connect">
                        <button type="button" class="btn btn-xlarge connect-button">Connect</button>
                      </router-link>
                    </div>
                  </div>
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
import FooterBar from '@/components/commons/FooterBar.vue';

export default {
  components: {
    FooterBar,
  },
  data() {
    return {
      greetingSection: false,
      introSection: false,
      aboutSection: false,
      aboutPara1Section: false,
      aboutPara2Section: false,
      aboutPara3Section: false,
      experienceSection: false,
      summarySection: false,
      companySection: false,
      roleSection: false,
      productDevSection: false,
      analyticsSection: false,
      cloudTransformSection: false,
      automationSection: false,
      studiesSection: false,
      school1Section: false,
      school2Section: false,
      school3Section: false,
      school4Section: false,
      skillsSection: false,
      skillsListSection: false,
      toolsListSection: false,
      connectSection: false,
      greetingObserver: null,
      introObserver: null,
      aboutObserver: null,
      aboutPara1Observer: null,
      aboutPara2Observer: null,
      aboutPara3Observer: null,
      experienceObserver: null,
      summaryObserver: null,
      companyObserver: null,
      roleObserver: null,
      productDevObserver: null,
      analyticsObserver: null,
      cloudTransformObserver: null,
      automationObserver: null,
      studiesObserver: null,
      school1Observer: null,
      school2Observer: null,
      school3Observer: null,
      school4Observer: null,
      skillsObserver: null,
      skillsListObserver: null,
      toolsListObserver: null,
      connectObserver: null,
    };
  },
  mounted() {
    this.observeIntersection(this.$refs.greeting, "greeting");
    this.observeIntersection(this.$refs.intro, "intro");
    this.observeIntersection(this.$refs.about, "about");
    this.observeIntersection(this.$refs.aboutPara1, "aboutPara1");
    this.observeIntersection(this.$refs.aboutPara2, "aboutPara2");
    this.observeIntersection(this.$refs.aboutPara3, "aboutPara3");
    this.observeIntersection(this.$refs.experience, "experience");
    this.observeIntersection(this.$refs.summary, "summary");
    this.observeIntersection(this.$refs.company, "company");
    this.observeIntersection(this.$refs.role, "role");
    this.observeIntersection(this.$refs.productDev, "productDev");
    this.observeIntersection(this.$refs.analytics, "analytics");
    this.observeIntersection(this.$refs.cloudTransform, "cloudTransform");
    this.observeIntersection(this.$refs.automation, "automation");
    this.observeIntersection(this.$refs.studies, "studies");
    this.observeIntersection(this.$refs.school1, "school1");
    this.observeIntersection(this.$refs.school2, "school2");
    this.observeIntersection(this.$refs.school3, "school3");
    this.observeIntersection(this.$refs.school4, "school4");
    this.observeIntersection(this.$refs.skills, "skills");
    this.observeIntersection(this.$refs.skillsList, "skillsList");
    this.observeIntersection(this.$refs.toolsList, "toolsList");
    this.observeIntersection(this.$refs.connect, "connect");
  },
  methods: {
    observeIntersection(section, showProperty) {
      const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0,
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            this[`${showProperty}Section`] = true;
          }
        });
      }, options);

      observer.observe(section);
      this.setObserver(showProperty, observer);
    },

    setObserver(showProperty, observer) {
      this[`${showProperty}Observer`] = observer;
    },

    disconnectObserver(observer) {
      if (observer) {
        observer.disconnect();
      }
    },
  },
  beforeUnmount() {
    this.disconnectObserver(this.greetingObserver);
    this.disconnectObserver(this.introObserver);
    this.disconnectObserver(this.aboutObserver);
    this.disconnectObserver(this.aboutPara1Observer);
    this.disconnectObserver(this.aboutPara2Observer);
    this.disconnectObserver(this.aboutPara3Observer);
    this.disconnectObserver(this.experienceObserver);
    this.disconnectObserver(this.summaryObserver);
    this.disconnectObserver(this.companyObserver);
    this.disconnectObserver(this.roleObserver);
    this.disconnectObserver(this.productDevObserver);
    this.disconnectObserver(this.analyticsObserver);
    this.disconnectObserver(this.automationObserver);
    this.disconnectObserver(this.studiesObserver);
    this.disconnectObserver(this.school1Observer);
    this.disconnectObserver(this.school2Observer);
    this.disconnectObserver(this.school3Observer);
    this.disconnectObserver(this.school4Observer);
    this.disconnectObserver(this.skillsObserver);
    this.disconnectObserver(this.skillsListObserver);
    this.disconnectObserver(this.toolsListObserver);
    this.disconnectObserver(this.connectObserver);
  },
}
</script>

<style scoped>
span {
  display: flex;
  flex-direction: row;
}

.about {
  background-color: black;
  overflow-y: auto;
  overflow-x: hidden;
  height: 100vh;
  color: white;
}

.greeting {
  height: 100%;
  justify-content: center;
  align-items: center;
  display: flex;
}

h1 {
  font-size: 7rem;
  color: cyan;
  padding: 0 5%;
}

.jumbotron {
  height: 100vh;
  justify-content: center;
  align-items: center;
  display: flex;
  padding: 0 10%;
}

.intro-line h2 {
  font-size: 4rem;
  text-align: left;
}

.intro .paragraph {
  padding: 0 10%;
  text-align: left;
  height: 40vh;
}

.card {
  border-radius: 30px;
}

.card-header {
  padding: 2% 3%;
  justify-content: center;
  align-content: center;
  font-size: large;
  color: black;
}

.company {
  color: mediumvioletred;
  text-align: left;
  height: 100%;
  font-size: 2rem;
}

.tenure {
  text-align: right;
  color: mediumvioletred;
  height: 100%;
}

.experience-details {
  color: black;
  text-align: left;
}

.summary {
  color: black;
  font-family: 'Roxborough', serif;
  font-size: 2rem;
  text-align: left;
  padding: 5% 5%;
}

.experience-details {
  padding: 5%;
}

.role {
  padding: 5% 0;
  text-align: left;
  font-size: 1.5rem;
  font-family: 'Comfortaa', cursive;
}

.description-heading .skills .tools {
  font-family: 'Comfortaa', cursive;
  padding: 5% 0%;
}

.education {
  color: black;
}

.education-details {
  padding: 5%;
}

.skills-head {
  color: black;
}

.tools {
  color: black;
}

.skills-wrapper {
  padding: 5%;
}

.tools-wrapper {
  padding: 5%;
}

.list-group-item {
  background-color: transparent;
}

.connect {
  color: black;
  padding: 20% 0;
}

.connect-header {
  font-family: 'Roxborough', serif;
  font-size: 2rem;
  padding: 3% 0;
}

.connect-paragraph {
  font-size: 1rem;
  text-align: justify;
  padding: 5% 5%;
}

.connect-button-wrapper {
  padding: 3%;
}

.connect-button {
  background-color: transparent;
  color: black;
  border-color: black;
  border-radius: 50px;
  font-size: 1.5rem;
  padding: 2%;
  width: 30%;
}

.connect-button:hover {
  background-color: black;
  color: white;
  box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
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

.pranam-enter-active {
  animation: slide-scale 2s ease-out;
}

.slide-enter-active {
  transition: transform 2s;
}

.slide-enter-from {
  transform: translateX(-100%);
}

.slideup-enter-active {
  transition: transform 2s;
}

.slideup-enter-from {
  transform: translatey(-30%);
}

@keyframes slide-scale {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-50%);
  }
}
</style>

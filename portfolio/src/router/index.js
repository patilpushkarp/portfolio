import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ConnectView from '../views/ConnectView.vue'
import BlogView from '../views/BlogView.vue'
import BlogsViewer from '../views/BlogsViewer.vue'
import ProjectsViewer from '../views/ProjectsViewer.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/connect',
    name: 'connect',
    component: ConnectView
  },
  {
    path: '/blog/:id',
    name: 'blog',
    component: BlogView
  },
  {
    path: '/blogs',
    name: 'blogs',
    component: BlogsViewer
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsViewer
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

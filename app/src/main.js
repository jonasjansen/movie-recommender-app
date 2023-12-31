import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import GenreRecommender from './components/GenreRecommender.vue';
import RatingRecommender from './components/RatingRecommender.vue';


const routes = [
    { path: '/', component: Home },
    { path: '/genre', component: GenreRecommender },
    { path: '/rating', component: RatingRecommender },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

createApp(App).use(router).mount('#app');

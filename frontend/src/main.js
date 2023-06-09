import './assets/css/pico.css';
import './assets/css/main.css';

import { createApp } from 'vue';

import { createPinia } from 'pinia';

import Axios from 'axios';
import App from './App.vue';
import router from './router';

Axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? '/mlc/api/v1/' : 'http://127.0.0.1:5000/mlc/api/v1/';

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount('#app');

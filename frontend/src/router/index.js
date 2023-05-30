import { createRouter, createWebHistory } from 'vue-router';
// import ViewHomePage from '../views/ViewHomePage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/ViewHomePage.vue'),
    },
    {
      path: '/calculate',
      name: 'calculate',
      component: () => import('@/views/ViewCalculate.vue'),
    },

/*    {
      path: '/',
      name: 'home',
      component: ViewHomePage,
    },*/
  ],
});

export default router;

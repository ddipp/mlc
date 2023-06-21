import { createRouter, createWebHistory } from 'vue-router';

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
    {
      path: '/path',
      name: 'path',
      component: () => import('@/views/ViewPath.vue'),
    },
  ],
});

export default router;

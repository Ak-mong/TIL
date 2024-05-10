import { createRouter, createWebHistory } from 'vue-router'
import ProductListView from '../views/ProductListView.vue'
import CartView from '@/views/CartView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ProductListView
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView
    },
    {
      path:'/:product_id',
      name: 'product-detail',
      component : ProductDetailView,
    }
  ],
})

export default router
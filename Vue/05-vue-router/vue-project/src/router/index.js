import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserHome from '@/components/UserHome.vue'
import LoginView from '@/views/LoginView.vue'

const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path:'/user/:id',
      // name : 'user',
      component : UserView,
      beforeEnter: (to,from) =>{
        console.log(to)
        console.log(from)
      },
      children : [
        {path:'',name:'user', component: UserHome},
        // UserProfile은 UserView의 <RouterView> 내부에 렌더링
        {path:'profile', name:'user-profile', component: UserProfile},
        // UserPosts는 UserView의 <RouterView> 내부에 렌더링
        {path:'posts', name:'user-posts', component: UserPosts},
      ]
    },
    {
      path:'/login',
      name:'login',
      component: LoginView,
      beforeEnter: (to,from) =>{
        if (isAuthenticated === true){
          console.log('이미 로그인 상태입니다.')
          return {name:'home'}
        }
      }
    }
  ]
})

// 전역 가드
router.beforeEach((to,from) =>{

  // 로그인이 되어 있지 않고 + 이동하는 곳이 login이 아니라면
  // if (!isAuthenticated && to.name !== 'login'){
  //   console.log('로그인이 필요합니다.')
  //   return {name: 'login' }
  // }
  // console.log(to)
  // console.log(from)
})
export default router

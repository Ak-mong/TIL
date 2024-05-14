import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue' // 주석이었던 것
import LogInView from '@/views/LogInView.vue' // 주석이었던 것

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    // 주석이었던 것
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    // 주석이었던 것
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})
import { useCounterStore } from '@/stores/counter' // store 추가
router.beforeEach((to, from)=>{
  const store = useCounterStore() // router 안에서 정의되야 한다.
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if (to.name === 'ArticleView' && store.isLogin === false){
    window.alert('로그인이 필요해요!!')
    return {name: 'LogInView'}
  }
  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)){
    window.alert('이미 로그인 했습니다.')
    return {name:'ArticleView'}
  }
})
export default router

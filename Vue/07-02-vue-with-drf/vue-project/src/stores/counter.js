import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router' // 라우터 추가

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null) // 토큰 추가
  const router = useRouter()
  const isLogin = computed(()=>{
    if (token.value === null){
      return false
    }else{
      return true
    }
  })
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers:{ // 필요한 요청마다 넣어줘야 한다.
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
  const signUp = function(payload){
    // 1. 사용자 입력 데이터를 받아
    // const username = payload.username
    // const password = payload.password
    // const password2 = payload.password2
    const {username, password1, password2} = payload // 구조 분해 할당 활용

    // 2. axios로 장고에 요청을 보냄
    axios({
      method:'post',
      url:`${API_URL}/accounts/signup/`,
      data: {
        // username : username,
        // password: password,
        // password2:password2
        username, password1, password2 // 줄이기
      }
      })
      .then((response)=>{
        console.log('회원가입 성공!')
        console.log(response.data)
        logIn({username, password1})
      })
      .catch((error)=>{
        console.log(error)
      })
  }
  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // console.log('로그인 성공!')
        // console.log(response)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        router.push({ name : 'ArticleView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })

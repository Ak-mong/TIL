<template>
  <div>
    <RouterLink :to="{name: 'user-profile'}"> Profile</RouterLink>
    <RouterLink :to="{name: 'user-posts'}">Posts </RouterLink>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 User 페이지</h2>
    <h2>{{ userId }}번 User 페이지</h2> <!-- 이 방법을 권장함 , 변수관리와 가독성을 위함-->
    <button @click="goHome">홈으로!</button>
    <button @click="routeUpdate">100번 유저 페이지로!</button>
    <hr>
    <RouterView/>
  </div>
</template>

<script setup>
import { useRoute, useRouter, onBeforeRouteLeave,onBeforeRouteUpdate } from 'vue-router';
import {ref} from 'vue'
const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = function (){
  // router.push({name: 'home' })
  router.replace({name: 'home' })
}
onBeforeRouteLeave((to,from ) =>{
  const answer = window.confirm('정말 떠나실 건가요?')
  if ( answer === false){
    return false
  }
})
const routeUpdate = function(){
  router.push({name:'user',params:{id:100}})
}
onBeforeRouteUpdate((to,from)=>{
  console.log(to)
  // userId.value = to.params.id
})
</script>

<style  scoped>

</style>
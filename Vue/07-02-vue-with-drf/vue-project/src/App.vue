<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView'}">Articles</RouterLink>
      <!--  주석이었던 것 -->
      <RouterLink :to="{ name: 'SignUpView'}">회원가입</RouterLink>
      <RouterLink :to="{ name: 'LogInView'}">로그인</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>

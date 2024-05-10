
<template>
<!-- 3. 화면에 그려준다 -->
  <!-- {{ product }} -->
  <div v-if="product.id">
    <h1>상품 명: {{ product.title }}</h1>
    <img :src="product.image" alt="상품 이미지" width="150">
    <p>가격 : {{ product.price }}</p>
    <p>카테고리 : {{ product.category }}</p>
    <button @click="cartStore.addCart(product)">장바구니에 추가</button>
  </div>
  <p v-else>Loading 중...</p>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router'; 
import {useCartStore} from  '@/stores/counter'
import axios from 'axios';
const cartStore = useCartStore()
// 1. product Id 를 URL params 로 부터 가져온다.
  const route = useRoute()
  console.log(route)
  // console.log(route.params.product_id)
  const productId = route.params.product_id

// 2. product Id 를 이용해서 데이터를 가져온다.
/* 2-1 store 부터 접속하면  
  - 상품 디테일 페이지부터 접근하면 사용자가 데이터를 받을 수 없다

   2-2 axios로 상세 데이터를 호출하기
    2.2.1 API가 제공해주는 경우 OK
    2.2.2 API가 제공해주지 않는 경우
      - App.vue 등 상위 컴포넌트에서 호출
      -> 대신, 데이터가 있다면 재호출을 하지 않도록 구현
*/
// 상품 상세 정보 : datail에서만 사용함
const product = ref({})
axios({
  method: 'get',
  url : `https://fakestoreapi.com/products/${productId}`
})
.then((response)=>{
  product.value = response.data
})
.catch((error)=>{
  console.log(error)
})
</script>

<style scoped>
</style>
<template>
  <div>
    {{ myMsg }}
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName"/>
    <button @click="$emit('someEvent')">버튼1</button>
    <button @click="buttonClick">버튼2</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

// 내려받은 props를 선언

// 문자열 형태
// defineProps(['myMsg'])

// 객체 형태
// defineProps({
//   myMsg:String,
// })
const props = defineProps({
  //myMsg: [String, Object], // 여러가지 타입일 수 있는것을 배열로서 넣을 수 있다
  myMsg : {
    type : String,
    required : true
  },
  dynamicProps : String
})

console.log(props) // {myMsg: 'message'}
console.log(props.myMsg) // message

const emit = defineEmits(['myFocus', 'emitArgs','updateName'])

const buttonClick = function (){
  emit('myFocus')
}

const emitArgs = function(){
  emit('emitArgs', 1, 2, 3)
}

const updateName = function (){
  emit('updateName')
}

</script>

<style lang="scss" scoped>

</style>
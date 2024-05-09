
<template>
  <div>
    <!-- <p>state: {{ store.count }}</p>
    <p>newNumber: {{ newNumber }}</p>
    <p>getter: {{ store.doubleCount }}</p>
    <button @click="store.increment()">+++</button> -->
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoList/>
    <TodoForm/>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import TodoForm from './components/TodoForm.vue';
import TodoList from './components/TodoList.vue';
const store = useCounterStore()

// state 참조 및 변경
// console.log(store.count)
// const newNumber = store.count + 1

// getters
// console.log(store.doubleCount)

// actions 호출
// store.increment()


</script>
<style scoped>
</style>

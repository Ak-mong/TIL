import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    { id: id++ , text:'할 일 1', isDone:false},
    { id: id++ , text:'할 일 2', isDone:false},
  ])
  
  // create
  const addTodo = function (todoText){
    todos.value.push({
      id:id++,
      text:todoText,
      isDone:false
    })
  }

  // delete
    const deleteTodo = function(todoId){
    // console.log('delete')
    // todos 상태에서 인자로 전달된 todo(삭제 대상)을 찾아서 
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    // 찾은 인덱스를 활용하여 todos에서 삭제 후 새로운 todos로 교체
    todos.value.splice(index,1)
  }
  
  // update
  const updateTodo = function(todoId){
    // 전달 받은 todoid (수정 대상)을 활용
    // todos 배열을 순회하면서 id가 일치하면 isDone을 반대로 바꾸고
    // 변경된 새로운 배열을 반환

    // console.log('update')
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId){
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  // counting
  const doneTodosCount = computed(()=>{
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })
  return {todos, addTodo, deleteTodo, updateTodo, doneTodosCount}
  
  /*
  const count = ref(2)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment } 
  */
}, {persist: true})

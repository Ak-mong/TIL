<template>
  <div>
    <p> {{ myProp.id }}</p>
    <p> {{ myProp.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  myProp: Object,
})
</script>

<style lang="scss" scoped>

</style>

<script setup lang="ts">
import { defineProps, ref } from "vue";

const props = defineProps({
  src: {
    type: String,
  },
});
const img = 'kedro-retro-june-2021/'+props.src;
</script>

<template>
  <div class="relative max-w-60 overflow-hidden rounded-lg shadow-lg">
    <img class="object-cover w-30 h-15" :src="img"/>
    <div class="absolute top-0 left-0 px-6 py-4"></div>
  </div>
</template>
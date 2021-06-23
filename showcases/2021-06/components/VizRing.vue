
<script setup lang="ts">
import { defineProps, ref } from "vue";

const props = defineProps({
  src: {
    type: String,
  },
  color: {
    type: String,
  },
});
const img = 'kedro-retro-june-2021/'+props.src;
const attrs = [
  "relative",
  "max-w-60",
  "overflow-hidden",
  "rounded-lg",
  "text-center",
  "m-auto",
  "ring",
  "ring-1",
  "ring-offset-5",
  "ring-offset-dark-900",
];

const css = attrs.concat([props.color]).join(" ");
</script>

<template>
  <div :class="css">
    <img class="object-cover w-full h-50 m-auto" :src="img" />
  </div>
</template>
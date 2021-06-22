<script setup lang="ts">
import { defineProps, ref } from "vue";

const props = defineProps({
  name: {
    type: String,
  },
});
const img = "kedro-retro-june-2021/" + props.name.toString().replace(' ', '_').toLowerCase() + ".png";
</script>

<template>
  <span abs class="m-1 abs-tr" style="pointer-events: none">
    <div class="inline">
      <p class="text-m mr-3" >
        {{ name }}
        <img class="ml-2 w-8 h-8 rounded-full border border-yellow-100 inline" :src="img" 
        hover="border border-yellow-500"/>
      </p>
    </div>
  </span>
</template>
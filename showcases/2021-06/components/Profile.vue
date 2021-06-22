<script setup lang="ts">
import { defineProps, ref } from 'vue'

const props = defineProps({
  name: {
    type: String,
  },
  role: {
    type: String
  },
  github: {
    type: String
  },
  country: {
    type: String
  }
})
const gh = "https://github.com/"+props.github
const img = "kedro-retro-june-2021/"+props.name.toString().replace('\s+', '_').toLowerCase()+".png";
</script>

<template>
<div class="justify-center">
<div class="w-24 shadow-lg">
    <div class="bg-dark-500 rounded-lg flex flex-col">
    <span class="relative left-14 -top-1">
    <a :href="gh" target="_blank"
    class="icon-btn !border-none">
    <carbon-logo-github/>
    </a>
    </span>
        <div class="-mt-5">
        <img 
            class="w-12 h-12 rounded-full mx-auto border border-yellow-500 -m-1" 
            :src="img" 
            :alt=props.name
            hover="animate-spin"
        >
            <span>
              <p class="text-center">
            <span class="text-1.0em ">{{name}}</span>
            <br>
            <span class="text-0.7em text-center">{{role}}</span>
            <br><span>{{country}}</span>
            </p>
            </span>
        </div>
    </div>
</div>
</div>
</template>
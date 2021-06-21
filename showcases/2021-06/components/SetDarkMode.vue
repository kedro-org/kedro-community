<script setup lang="ts">
import { isDark, toggleDark } from '@slidev/client/logic/dark'
const buttonClass = "bg-primary rounded border-b-2 border-green-900 text-white text-sm px-2 pt-1.5 pb-1 inline-block !outline-none hover:bg-opacity-85";
</script>

<template>
  <button
    class="w-17 bg-primary rounded border-b-1 border-white-900 text-white text-sm px-2 pt-1.5 pb-1 inline-block !outline-none hover:bg-opacity-85"
    @click="toggleDark"
  >
    <div class="flex text-xs">
      <carbon-checkmark-filled v-if="isDark" class="text-green-400"/>
      <carbon:sun class="text-red-400" v-else />
      <span class="mr-1 ml-2 text-gray-500">{{ isDark ? 'Dark' : 'Light' }}</span>
    </div>
  </button>
</template>
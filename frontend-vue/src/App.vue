<script setup lang="ts">
import ListTabs from "./components/ListTabs.vue";
</script>

<template>
  <nav class="flex h-[10vh] items-end">
    <ListTabs />
  </nav>
  <div class="h-[90vh]">
    <RouterView />
  </div>
</template>

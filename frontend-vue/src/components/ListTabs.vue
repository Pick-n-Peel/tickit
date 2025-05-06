<script setup lang="ts">
import { useQuery } from "@tanstack/vue-query";
import { ref } from "vue";
import NewListButton from "./NewListButton.vue";

const selectedListId = ref(0);

const { data: lists } = useQuery({
  queryKey: ["lists"],
  queryFn: async () => {
    const response = await fetch("/api/list/");
    return response.json();
  },
});
</script>

<template>
  <div class="flex w-full justify-center items-center gap-2">
    <div role="tablist" class="w-fit tabs tabs-box">
      <a
        v-for="list in lists"
        :key="list.id"
        role="tab"
        class="tab"
        :class="{ 'tab-active': selectedListId === list.id }"
        @click="selectedListId = list.id"
        >{{ list.name }}
      </a>
    </div>
    <div class="tooltip" data-tip="Add New List">
      <NewListButton />
    </div>
  </div>
</template>

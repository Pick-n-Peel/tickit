<script setup lang="ts">
import { useQuery } from "@tanstack/vue-query";
import NewListButton from "./NewListButton.vue";
import { RouterLink } from "vue-router";

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
      <RouterLink
        v-for="list in lists"
        :key="list.id"
        :to="`/lists/${list.id}`"
        role="tab"
        class="tab"
        :class="{ 'tab-active': $route.params.listId === list.id.toString() }"
        >{{ list.name }}
      </RouterLink>
    </div>
    <div class="tooltip" data-tip="Add New List">
      <NewListButton />
    </div>
  </div>
</template>

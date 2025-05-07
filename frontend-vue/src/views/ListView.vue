<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { Trash } from "lucide-vue-next";
import { useMutation, useQueryClient } from "@tanstack/vue-query";
import fetchJson from "../data/fetch";

const router = useRouter();
const route = useRoute();
const queryClient = useQueryClient();
const listId = ref(route.params.listId);

watch(route, (newRoute) => {
  listId.value = newRoute.params.listId.toString();
});

const deleteList = useMutation({
  mutationFn: async () => {
    await fetchJson(`/api/list/${listId.value}/`, {
      method: "DELETE",
    });
  },
  onSettled: () => {
    queryClient.invalidateQueries({ queryKey: ["lists"] });
    router.push("/");
  },
});

const onDeleteClicked = () => {
  deleteList.mutateAsync();
};
</script>

<template>
  <div class="flex flex-col size-full justify-center items-center gap-2">
    <p class="font-bold text-base-content/50">List ID: {{ listId }}</p>
    <button class="btn btn-outline btn-error" @click="onDeleteClicked">
      <Trash class="size-4 mr-2" /> Delete
    </button>
  </div>
</template>

<script setup lang="ts">
import { useMutation, useQueryClient } from "@tanstack/vue-query";
import { Plus } from "lucide-vue-next";
import { ref, useTemplateRef } from "vue";
import fetchData from "../data/fetch";

const queryClient = useQueryClient();
const newListName = ref("");

const dialogRef = useTemplateRef("add_list_dialog");
const inputRef = useTemplateRef("new_list_name");

const createList = useMutation({
  mutationFn: async (listName: string) => {
    await fetchData("/api/list/", {
      method: "POST",
      body: JSON.stringify({ name: listName }),
    });
  },
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["lists"] });
  },
});

const onSubmit = () => {
  createList.mutateAsync(newListName.value);
  newListName.value = "";
  dialogRef.value?.close();
};

function onOpenDialog() {
  dialogRef.value?.showModal();
  dialogRef.value?.addEventListener("transitionend", () => {
    inputRef.value?.focus();
  });
}
</script>

<template>
  <button
    type="button"
    class="btn btn-ghost btn-success rounded-full size-8 p-0"
    @click="onOpenDialog"
  >
    <Plus class="size-4" />
  </button>
  <dialog id="add_list_dialog" ref="add_list_dialog" class="modal">
    <div class="modal-box">
      <h3>Create New List</h3>
      <input
        ref="new_list_name"
        placeholder="Enter Name"
        class="input mt-4 w-full"
        v-model="newListName"
      />
      <div class="modal-action">
        <button class="btn btn-success" @click="onSubmit">Done</button>
      </div>
    </div>
    <form method="dialog" class="modal-backdrop">
      <button>close</button>
    </form>
  </dialog>
</template>

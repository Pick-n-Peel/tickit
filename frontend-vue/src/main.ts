import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { VueQueryPlugin } from "@tanstack/vue-query";
import { createRouter, createWebHistory } from "vue-router";
import ListView from "./views/ListView.vue";
import DefaultView from "./views/DefaultView.vue";

const routes = [
  { path: "/", component: DefaultView },
  { path: "/lists/:listId", component: ListView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.use(router);
app.use(VueQueryPlugin);

app.mount("#app");

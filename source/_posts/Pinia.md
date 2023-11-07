---
title: Pinia
top_img: 'linear-gradient(45deg, rgba(204, 0, 102, 0.6), rgba(190, 60, 160, 0.6),
  rgba(100, 40, 100, 0.6), rgba(128, 0, 128, 0.6))'
tags:
  - StateManagement
  - vue
description: 🍍
abbrlink: 74dce755
date: 2023-10-13 14:15:15
updated: 2023-10-13 16:16:32
---


## 快速上手

- 安装

```bash
npm install pinia
```

- 入口文件中引入,将`pinia`挂载到`Vue`应用中

```ts
// main.ts

import { createApp } from "vue";
import App from "./App.vue";
import { createPinia } from "pinia";
const pinia = createPinia();


const app = createApp(App);
app.use(pinia);
app.mount("#app");
```

- 创建store

```ts
/src/store/user.ts


import { defineStore } from 'pinia'


// 第一个参数是应用程序中 store 的唯一 id
export const useUsersStore = defineStore('users', {
    state: () => {
        return {
            name: "Jhon",
            age: 25,
        };
    },
    //leii
    getters: {
        getAddAge: (state) => {
            return state.age + 100;
        },
    },
})

```

- 使用store

利用`pinia`的`storeToRefs`函数，将`state`中的数据变为了响应式的。

```ts
/src/App.vue
<script setup lang="ts">
import { useUsersStore } from "../src/store/user";
const store = useUsersStore();
const { name, age, sex } = storeToRefs(store);
</script>

```

- 批量更改数据

```ts
// 较少字段的修改方式
<button @click="patchStore">批量修改数据</button>
// 批量修改数据
const patchStore = () => {
  store.$patch({
    name: "张三",
    age: 23,
  });
};

```

```ts
store.$patch((state) => {
  state.items.push({ name: 'shoes', quantity: 1 })
  state.hasChanged = true
})
```


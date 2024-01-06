---
title: Vue
abbrlink: f8e09374
date: 2023-10-18 16:03:21
updated:
tags:
  - vue
description: 🐖
top_img: "linear-gradient(35deg, rgba(150, 60, 140, 0.6), rgba(0, 0, 255, 0.3), rgba(128, 0, 128, 0.6), rgba(204, 0, 102, 0.6), rgba(100, 40, 100, 0.6))"
---

## 渐进式 JavaScript 框架

## 使用过程中遇到的问题

### 属性带不带冒号

冒号实际上是`v-bind:attribute`的缩写

`v-bind`能够动态的绑定一个或多个 attribute，也可以是组件的 prop

### 模板引用

使用时需要加`value`

```js
xxxx.value.validate;
```

### 插槽的使用（slot）

示例：

> FancyList.vue

```vue
<script setup>
  import { ref } from 'vue'

  const props = defineProps(['api-url', 'per-page'])

  const items = ref([])

  // mock remote data fetching
  setTimeout(() => {
    items.value = [
      { body: 'Scoped Slots Guide', username: 'Evan You', likes: 20 },
      { body: 'Vue Tutorial', username: 'Natalia Tepluhina', likes: 10 }
    ]
  }, 1000)
</script>

<template>
  <ul>
    <li v-if="!items.length">
      Loading...
    </li>
    <li v-for="item in items">
      <slot name="item" v-bind="item"/>
    </li>
  </ul>
</template>

<style scoped>
  ul {
    list-style-type: none;
    padding: 5px;
    background: linear-gradient(315deg, #42d392 25%, #647eff);
  }
  li {
    padding: 5px 20px;
    margin: 10px;
    background: #fff;
  }
</style>
```

> 

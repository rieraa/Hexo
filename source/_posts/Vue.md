---
title: Vue
tags:
  - vue
description: 🐖
top_img: "linear-gradient(35deg, rgba(150, 60, 140, 0.6), rgba(0, 0, 255, 0.3), rgba(128, 0, 128, 0.6), rgba(204, 0, 102, 0.6), rgba(100, 40, 100, 0.6))"
abbrlink: f8e09374
date: 2023-10-18 16:03:21
updated:
---

## 渐进式 JavaScript 框架

## 生命周期！！

![image-20230906162803200](https://cn.vuejs.org/assets/lifecycle.16e4c08e.png)

## 使用过程中遇到的问题

### 属性带不带冒号

冒号实际上是`v-bind:attribute`的缩写

`v-bind`能够动态的绑定一个或多个 attribute，也可以是组件的 prop

### 模板引用

使用时需要加`value`

```js
xxxx.value.validate
```


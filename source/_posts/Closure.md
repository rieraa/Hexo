---
title: Closure(函数闭包)
abbrlink: 87bab44d
date: 2023-11-05 22:48:29
categories: JavaScript 深入学习
tags:
  - closure
---

## 什么是闭包

有权访问另一个函数作用域中的变量的函数，就是闭包。

这是一种闭包

```js
function animal() {
  const name = "dog";
  function getName() {
    console.log(name);
  }
  getName();
}
animal();
```

这也是一种闭包

```js
const name = "cat";
function getName() {
  console.log(name);
}
```

name 定义在全局作用域中，getName 在内部输出找不到自己定义的值，因此向外寻找，输出 getName，是一个隐性的闭包。

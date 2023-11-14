---
title: ES6使用手册
abbrlink: 93bcf3e9
date: 2023-10-11 21:49:55
tags:
  - javaScript
categories: JavaScript 基础
description: 😶‍🌫️
top_img: "linear-gradient(-45deg, #001f3f, #31578f, #820224)"
---

## 我用到的 es6

1. 模板字面量：通过``标识字符串
2.

## 1.let 和 const

## 2.模板字符串

### 1.模板字符串

```js
//字符串拼接 bad
const foo = "this is a" + content;

//模板字符串 good
const foo = `this is a ${content}`;
```

### 2.标签模板优化书写方式

```js
let url = oneLine`
	www.taobao.com/example/index.html
	?foo=${foo}
	&bar=${bar}
`;

console.log(url); // www.taobao.com/example/index.html?foo=foo&bar=bar
```

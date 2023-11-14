---
title: JS模块的导入导出
abbrlink: 3e90cfd3
date: 2023-11-12 19:22:50
top_img: "linear-gradient(45deg, rgba(0, 128, 128, 0.6), rgba(128, 0, 128, 0.6), rgba(204, 0, 102, 0.6), rgba(100, 40, 100, 0.6), rgba(190, 60, 160, 0.6))"
tags:
  - ES Moudle
  - CommonJS
description: ☹️
---

## JS 模块的导入导出

导入导出模块？ 要不要加{}？ 如何导出模块？路径中需不需要写文件后缀？

### commonjs

`nodejs ` 借鉴了 `Commonjs` 的 Module ，实现了良好的模块化管理

**特点**

- 在 `commonjs` 中每一个 js 文件都是一个单独的模块，我们可以称之为 module；

- 该模块中，包含 CommonJS 规范的核心变量: exports、module.exports、require；

### Es Module

export 与 export default 的区别

- export 与 export default 均可用于导出常量、函数、文件、模块等
- 可以在其它文件或模块中通过 import+(常量 | 函数 | 文件 | 模块)名的方式，将其导入，以便能够对其进行使用
- export default 后面不能跟 const 或 let 的关键词
- export、import 可以有多个，export default 仅有一个。
- 通过 export 方式导出，在导入时要加 { }，export default 则不需要
- export`具名`导出 xxx ，export default`匿名`。区别在于导入的时候，export 需要`一样`的名称才能匹配，后者无论取什么名都可以。
- 模块化管理中一个文件就是一个模块，export 可以导出多个方法和变量，export default 只能导出当前模块，一个 js 文件中只支持出现一个

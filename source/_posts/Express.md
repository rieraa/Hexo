---
title: Express
abbrlink: d7c881ac
date: 2023-10-10 22:21:09
tags:
  - node
description: 🥶
---

## 基本使用

这里直接使用`app.get`来处理请求

```js
var express = require("source/_posts/Express");
var app = express();

// respond with "hello world" when a GET request is made to the homepage
app.get("/", function (req, res) {
  res.send("hello world");
});
```

## 项目实例

`usersController.js`

> 暴露函数

```js
module.exports.register = (req, res, next) => {
  console.log(req.body);
};
```

`UserRoutes.js`

> 中间件 处理其中一类的请求

```js
const { register } = require("../controllers/usersController");

/* 
路由对象在Express.js中通常被视为一种特殊类型的中间件。当你将路由对象挂载到特定的路径上时，它可以拦截和处理该路径下的请求，类似于其他中间件。路由对象允许你组织和处理特定路径下的请求，因此在这种意义上它可以被认为是中间件的一种。
*/
const router = require("source/_posts/Express").Router;

// 设置请求路径及回调函数
router.post("/register", register);

module.exports = router;
```

`index.js`

> 中间件 处理其中一类的请求 挂载 userRoutes 到/api/auth 路径下

```js
const express = require("source/_posts/Express");
const cors = require("cors");
// 与mongodb进行交互
const mongoose = require("mongoose");

const userRoutes = require("./routes/UserRoutes");
const app = express();
require("dotenv").config();

// *中间件
app.use(cors());
app.use(express.json());

// *挂载userRoutes到api/auth路径下
app.use("api/auth", userRoutes);

mongoose
  .connect(process.env.MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("DB Connection Success");
  })
  .catch((error) => {
    console.error("Error occured", error.message);
  });

const server = app.listen(process.env.PORT, () => {
  console.log(`Server Started on Port ${process.env.PORT}`);
});
```

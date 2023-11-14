---
title: Promise
abbrlink: 54b11a0c
date: 2023-10-11 21:56:48
tags:
  - javaScript
description: 🤠
top_img: "linear-gradient(20deg, #001f3f, #1f3b69, #820224)"
---

# Promise

## Promise 的基本使用

```javascript
const p = new Promise((resolve, reject) => {});
```

- Promise 接受一个函数作为参数

- 在参数函数中有两个参数

  - resolve: 成功函数

  - reject: 失败函数

### 1) Promise 的状态

第一种状态:` pending`

第二种状态: `fulfilled`

第三种状态: `rejected`

### 2) Promise 状态的改变

```javascript
const p = new Promise((resolve, reject) => {
  // resolve(): 调用函数, 使当前Promise对象的状态改成fulfilled
  resolve();
});
console.dir(p); // fulfilled
```

```javascript
const p = new Promise((resolve, reject) => {
  // resolve(): 调用函数, 使当前Promise对象的状态改成fulfilled
  // reject(): 调用函数, 使当前Promise对象的状态改成rejected
  // resolve();
  reject();
});
console.dir(p);
```

- resolve(): 调用函数, 使当前 Promise 对象的状态改成`fulfilled`
- reject(): 调用函数,使当前 Promise 对象状态改成`rejected`

### 3) Promise 的结果

```javascript
const p = new Promise((resolve, reject) => {
  // 通过调用 resolve,传递参数,改变 当前Promise对象的结果
  resolve("成功的结果");
  // resolve();
  // reject("失败的结果")
});
console.dir(p);
```

## Promise 的方法

### 1) then 方法

```javascript
const p = new Promise((resolve, reject) => {
  // 通过调用 resolve,传递参数,改变 当前Promise对象的结果
  // resolve(123);
  reject("失败的结果");
});

//then方法函数
// - 参数
// 两个参数都是函数
// 返回值: 是一个Promise对象
p.then(
  (value) => {
    //当Promise的状态使fulfilled时执行
    console.log("成功的回调", value);
  },
  (err) => {
    // 当Promise的状态时rejected时, 执行
    console.log("失败时调用", err);
  }
);
console.dir(p);
```

> 在 then 方法中,通过 return 将返回的 Promise 实例改为 fulfilled 状态

```javascript
// 如果Promise的状态不改变,then里的方法不会执行
const p = new Promise((resolve, reject) => {});
const t = p.then(
  (value) => {
    console.log("成功");
    // 使用return可以将t实例的状态改为fulfilled
    return 123;
  },
  (reason) => {
    console.log("失败");
  }
);
t.then(
  (value) => {
    console.log("成功2", value);
  },
  (reason) => {
    console.log("失败2");
  }
);
```

> 在 then 方法中,出现代码错误,将返回的 Promise 实例改为 rejected 状态

```javascript
// 如果Promise的状态改变,then里的方法不会执行
const p = new Promise((resolve, reject) => {

})
const t = p.then.((value) => {
	console.log("成功")
  // 使用return可以将t实例的状态改为fulfilled
  return 123
},(reason) => {
  // 如果这里代码出错,会将t实例的状态改为rejected
console.log("失败")
})
t.then.((value) => {
	console.log("成功2",value)
},(reason) => {
console.log("失败2")
})
```

### 2) catch 方法

> 示例

```javascript
const p = new Promise((resolve, reject) => {
	// reject()
  // console.log(a)
  throw new Error("出错了");
})

// 思考: catch中的参数函数在什么时候被执行
//  1. 当Promise的状态改为rejcted.被执行
//  2. 当Promise执行过程出现代码错误时,被执行
p.catch((reason => {
	console.log("失败", reason)
})
console.log(p);
```

## async 和 await

## 1) async 函数

1.  函数的返回值为 promise 对象
2.  promise 对象的结果由 async 函数执行的返回值决定

示例

```javascript
async function main(){
  // 1.如果返回值是一个非Promise类型的数据
  //  return 一个字符串 数字 布尔值等都是成功的Promise对象
  // 2. 如果返回的时一个Promise对象
  //  return new Promise((resolve, reject) => {
  //  resolve("OK") 返回的是成功Promise对象,状态值:[[PromiseState]]:"fulfilled"
  //  reject("Err") 返回的是失败Promise对象,状态值:[[PromiseState]]:"rejected"
  // 3. 抛出异常
  throw "oh No" // 状态值:[[PromiseState]]:"rejected",结果是抛出的值
})
}
let result = main();
console.log(result);
```

返回值是一个 Promise 对象

![img](https://cdn.nlark.com/yuque/0/2021/png/2934759/1615302593894-e1a59c34-08ff-4241-8eba-5512b1718bde.png)

## 2) await 表达式

1. await 右侧的表达式一般为 promise 对象, 但也可以是其它的值
2. 如果表达式是 promise 对象, await 返回的是 promise 成功的值
3. 如果表达式是其它值, 直接将此值作为 await 的返回值

注意

1. await 必须写在 async 函数中, 但 async 函数中可以没有 await
2. 如果 await 的 promise 失败了, 就会抛出异常, 需要通过 try...catch 捕获处理

## 3) async 和 await 结合

示例

```javascript
const fs = require("fs");
const util = require("util");
const mineReadFile = util.promisify(fs.readFile);// promisify转换为Promise形态的函数

async function main(){
  // 捕获处理
	try{
  	// 读取第一个文件的内容
    let data1 = await mineReadFile("./resource/1.html");
    let data2 = await mineReadFile("./resource/2.html");
    let data3 = await mineReadFile("./resource/3.html");
  }catch(e){
  	console.log(e):
  }
}
```

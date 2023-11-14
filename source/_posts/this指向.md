---
title: this指向
tags:
categories: JavaScript 深入学习
abbrlink: 74520f03
date: 2023-10-13 16:17:21
updated: 2023-11-13 22:28:36
top_img: 'linear-gradient(40deg, rgba(255, 0, 0, 0.6), rgba(0, 128, 0, 0.6), rgba(0, 0, 255, 0.6), rgba(255, 255, 0, 0.6), rgba(128, 0, 128, 0.6))'
description: 🎇
---



 

## 不同情况下的`this`指向

理解函数中的 `this` 关键字可能需要一些JavaScript中this的上下文的背景知识。在JavaScript中，`this` 的值是在函数被调用时确定的，并取决于函数的调用方式。

当你定义一个函数时，它并不与任何特定的对象绑定。然而，当函数被调用时，JavaScript会根据调用方式来确定 `this` 的值。有几种情况下 `this` 的值会有所不同：

1. **全局上下文：** 当函数在全局范围内被调用时，`this` 指向全局对象（在浏览器环境中通常是 `window`）。

    ```javascript
    function globalFunction() {
      console.log(this); // 在浏览器中可能指向 window 对象
    }
    
    globalFunction();
    ```

2. **作为对象方法：** 当函数作为对象的方法被调用时，`this` 指向调用该函数的对象。

    ```javascript
    const obj = {
      method() {
        console.log(this); // 指向 obj 对象
      }
    };
    
    obj.method();
    ```

3. **通过构造函数调用：** 当函数被用作构造函数（通过 `new` 关键字调用）时，`this` 指向新创建的对象实例。

    ```javascript
    function Constructor() {
      this.property = 'value';
      console.log(this); // 指向新创建的对象实例
    }
    
    const instance = new Constructor();
    ```

4. **使用 `call`、`apply` 或 `bind` 显式指定 `this`：** 这些方法允许你显式地指定函数在调用时的 `this` 值。

    ```javascript
    function explicitContext() {
      console.log(this);
    }
    
    const explicitObject = { name: 'Explicit' };
    
    explicitContext.call(explicitObject); // 使用 call 显式指定 this
    ```

现在，回到 `Array.from` 的 `thisArg` 参数。在使用 `Array.from` 时，你可以通过 `thisArg` 参数指定在映射函数执行时的 `this` 上下文。这对于确保在映射函数中访问特定的对象属性或方法非常有用，因为在默认情况下，函数内部的 `this` 可能会指向不同的上下文。

```javascript
const contextObject = {
  multiplier: 2,
  mapFunction(x) {
    return x * this.multiplier;
  }
};

const arrayLike = { 0: 1, 1: 2, 2: 3, length: 3 };

const newArray = Array.from(arrayLike, contextObject.mapFunction, contextObject);
// newArray is now [2, 4, 6]
```

在这个例子中，`contextObject.mapFunction` 是映射函数，通过将 `contextObject` 作为 `thisArg` 参数传递给 `Array.from`，确保映射函数中的 `this` 指向了 `contextObject`。这样，映射函数就可以访问 `contextObject` 的属性 `multiplier`。

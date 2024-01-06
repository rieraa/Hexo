---
title: Repair
abbrlink: "89483117"
date: 2023-10-11 13:58:25
updated: 2023-11-05 20:17:57
tags:
  - javaScript
  - 浏览器
categories: JavaScript 基础
description: 🔴
---

## 数据类型

- **数字（Number）**，整数或浮点数，例如： 42 或者 3.14159。
- **任意精度的整数 (BigInt)** ，可以安全地存储和操作大整数，甚至可以超过数字的安全整数限制。
- **字符串（String）**，字符串是一串表示文本值的字符序列，例如："Howdy" 。
- **布尔值（Boolean）**，有 2 个值分别是：true 和 false.
- **null**，一个表明 null 值的特殊关键字。JavaScript 是大小写敏感的，因此 null 与 Null、NULL 或变体完全不同。
- **undefined**，和 null 一样是一个特殊的关键字，undefined 表示变量未赋值时的属性。
- **代表（Symbol）**( 在 ECMAScript 6 中新添加的类型)。一种实例是唯一且不可改变的数据类型。
- **对象（Object）**，即引用类型。包括 Object Array、Function 等。

## 类型判断

### typeof

能判断所有**值类型，函数**。不可对 **null、对象、数组**进行精确判断，因为都返回 `object` 。

```js
console.log(typeof undefined); // undefined
console.log(typeof 2); // number
console.log(typeof true); // boolean
console.log(typeof "str"); // string
console.log(typeof Symbol("foo")); // symbol
console.log(typeof 2172141653n); // bigint
console.log(typeof function () {}); // function
// 不能判别
console.log(typeof []); // object
console.log(typeof {}); // object
console.log(typeof null); // object
```

typeof 可以判断 function

typeof 只能判断基础类型

### instanceof

`instanceof`能判断**对象**类型，不能判断基本数据类型，

判断不了 Error 基础数据类型。

```javascript
class People {}
class Student extends People {}

const vortesnail = new Student();

console.log(vortesnail instanceof People); // true
console.log(vortesnail instanceof Student); // true
```

其实现就是顺着**原型链**去找，如果能找到对应的 `Xxxxx.prototype` 即为 `true` 。比如这里的 `vortesnail` 作为实例，顺着原型链能找到 `Student.prototype` 及 `People.prototype` ，所以都为 `true` 。

### Object.toString

所有原始数据类型都是能判断的，还有 **Error 对象，Date 对象**等。

```js
Object.prototype.toString.call(2); // "[object Number]"
Object.prototype.toString.call(""); // "[object String]"
Object.prototype.toString.call(true); // "[object Boolean]"
Object.prototype.toString.call(undefined); // "[object Undefined]"
Object.prototype.toString.call(null); // "[object Null]"
Object.prototype.toString.call(Math); // "[object Math]"
Object.prototype.toString.call({}); // "[object Object]"
Object.prototype.toString.call([]); // "[object Array]"
Object.prototype.toString.call(function () {}); // "[object Function]"
```

## `==`与`===`的作用与区别（严格相等）

[值的比较](https://zh.javascript.info/comparison)

普通的相等性检查 `==` 存在一个问题，它不能区分出 `0` 和 `false`：

```js
console.log("🚀 ~ file: script.js:2 ~ 0==false:", 0 == false); // true
console.log("🚀 ~ file: script.js:2 ~ 0 === false:", 0 === false); // false
```

`''`和 false 也无法区分

```js
console.log("🚀 ~ file: script.js:4 ~ '' == false;:", "" == false); // true
```

原因是：比较不同类型的值时，处于相等判断符号 `==` 两侧的值会先被转化为数字，空字符串和 `false` 也是如此，转化后它们都为数字 0

## 数组

### [数组方法](https://juejin.cn/post/7204243582378115132?searchId=20230922095929303C6A71AD841475833B)

![image-20230922113430665](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309221134892.png)

**1、concat()**

concat(): 方法用于合并两个或多个数组。此方法不会更改现有数组，而是返回一个新数组。

> 语法: concat(value0, value1, /_ … ,_/ valueN)
>
> > `valueN`(可选): 数组和/或值，将被合并到一个新的数组中。如果省略了所有 `valueN` 参数，则 `concat` 会返回调用此方法的现存数组的一个浅拷贝
>
> 返回值：新的 Array 实例

**_代码示例(如下)_**

```js
const num1 = [1, 2, 3];
const num2 = [4, 5, 6];
const num3 = [7, 8, 9];

const numbers = num1.concat(num2, num3);
// [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**2、join()**
join(): 方法将一个数组（或一个类数组)的所有元素连接成一个字符串并返回这个字符串，用逗号或指定的分隔符字符串分隔。如果数组只有一个元素，那么将返回该元素而不使用分隔符。

> 语法: join(separator)
>
> > `separator`(可选): 指定一个字符串来分隔数组的每个元素。如果需要，将分隔符转换为字符串。如果省略，数组元素用逗号（`,`）分隔。如果 `separator` 是空字符串（`""`），则所有元素之间都没有任何字符
>
> 返回值：一个所有数组元素连接的字符串。如果 `arr.length` 为 0，**则返回空字符串**

**_代码示例(如下)_**

```js
复制代码const a = ["wjk", "shh", "zyh"];
a.join(); // 'wjk,shh,zyh'
a.join(", "); // 'wjk, shh, zyh'
a.join(" + "); // 'wjk + shh + zyh'
a.join(""); // 'wjkshhzyh'
```

**3、pop()**
pop(): 方法从数组中删除最后一个元素，并返回该元素的值。此方法会更改数组的长度。

> 语法: concat(value0, value1, /_ … ,_/ valueN)
>
> 返回值：从数组中删除的元素（当数组为空时返回 **undefined**）。

**_代码示例(如下)_**

```js
复制代码const a = ["wjk", "shh", "www", "kkk"];

const b = a.pop();

console.log(a); // ['wjk','shh','www']

console.log(b); // 'kkk'
```

**4、shift()**
shift(): 方法从数组中删除**第一个**元素，并返回该元素的值。此方法更改数组的长度。

> 语法: shift()
>
> 返回值：从数组中删除的元素 (如果数组为空则返回 **undefined**)。

**_代码示例(如下)_**

```javascript
复制代码let a = ["wjk", "zzh", "ws", "zsl"];

console.log("调用 shift 之前：" + a);
// "调用 shift 之前：wjk,zzh,ws,zsl"

var shifted = a.shift();

console.log("调用 shift 之后：" + a);
// "调用 shift 之后：[zzh,ws,zsl"

console.log("被删除的元素：" + shifted);
// "被删除的元素：wjk"
```

**5、unshift()**
unshift(): 方法将一个或多个元素添加到数组的**开头**，并返回该数组的**新长度**。

> 语法: unshift(element0, element1, /_ … ,_/ elementN)
>
> > `elementN`: 要添加到数组开头的元素。
>
> 返回值：返回调用方法对象的新 **length** 属性值。

**_代码示例(如下)_**

```js
ini复制代码arr = [3, 2, 1];

arr.unshift(4);
arr.unshift(5);
arr.unshift(6);

console.log(arr);
// [6, 5, 4, 3, 2, 1]
```

**6、push()**
push(): 方法将一个或多个元素添加到数组的末尾，并返回该数组的**新长度**。

> 语法: push(element0, element1, /_ … ,_/ elementN)
>
> > `elementN`: 被添加到数组末尾的元素。
>
> 返回值：当调用该方法的时候，新的 **length** 属性值将被返回。

**_代码示例(如下)_**

```ini
ini复制代码let a = ["wjk", "zyh"];
let b = a.push("ws", "zzh");

console.log(sports);
// ["wjk", "zyh", "ws", "zzh"]

console.log(b);
// 4
```

**7、reverse()**
reverse(): 方法将数组中元素的位置颠倒，并返回该数组，该方法会改变原数组。

> 语法: reverse()
>
> 返回值：颠倒后的数组。

**_代码示例(如下)_**

```js
const a = [1, 2, 3];

console.log(a); // [1, 2, 3]

a.reverse();

console.log(a); // [3, 2, 1]
```

**8、slice()**
slice(): 方法将数组部分的副本返回到新的数组对象中。这个对象是从 `start` 到 `end` 选择的（包括 `start`，不包括`end`）。**需要注意的是，此方法不会修改原始数组**。

> 语法: slice(start, end)
>
> > `start`(可选)： 是一个从 `0` 开始的索引，用于开始复制数组的一部分。如果未定义，`start` 的默认值为 `0`。如果 `start` 大于数组的索引范围， `slice()` 方法将返回一个空数组，此外，`start` 还可以使用负索引， `slice(-1)` 提取数组的最后一个元素。
> >
> > `end`(可选)：规定从何处结束选取，如果没有指定该参数，那么切分的数组包含从 start 到数组结束的所有元素。如果该参数为负数， 则它表示在原数组中的倒数第几个元素结束抽取。
>
> 返回值：一个含有被提取元素的新数组。

**_代码示例(如下)_**

```js
const a = ["www", "jjj", "kkk", "aaa", "bbb"];
let b = a.slice(1, 3);
let c = a.slice();
console.log(b); //['jjj', 'kkk']
console.log(c);
["www", "jjj", "kkk", "aaa", "bbb"];
```

**9、sort()**
sort(): 方法对数组的元素进行排序，并返回数组。

> 语法: sort((a, b) => { /_ … _/ } )
>
> > `compareFn`(可选)：用来指定按某种顺序进行排列的函数。如果省略，元素按照转换为的字符串的各个字符的 Unicode 位点进行排序。
> >
> > `a`：第一个用于比较的元素
> > `b`： 第二个用于比较的元素。
> >
> > 若 a 小于 b，即 a - b 小于零，则返回一个小于零的值，**数组将按照升序排列**。
> >
> > 若 a 等于 b，则返回 0。
> >
> > 若 a 大于 b, 即 a - b 大于零，则返回一个大于零的值，**数组将按照降序排列。**
> >
> > x const fs = require("fs");const util = require("util");const mineReadFile = util.promisify(fs.readFile);// promisify 转换为 Promise 形态的函数 ​async function main(){  // 捕获处理 try{ // 读取第一个文件的内容    let data1 = await mineReadFile("./resource/1.html");    let data2 = await mineReadFile("./resource/2.html");    let data3 = await mineReadFile("./resource/3.html"); }catch(e){ console.log(e): }}javascript
>
> 返回值：排序后的数组。

| `compareFn(a, b)` 返回值 | 排序顺序               |
| ------------------------ | ---------------------- |
| > 0                      | `a` 在 `b` 后          |
| < 0                      | `a` 在 `b` 前          |
| === 0                    | 保持 `a` 和 `b` 的顺序 |

**_代码示例(如下)_**

```js
//升序
const nums = [4, 2, 5, 1, 3];
nums.sort((a, b) => a - b);
console.log(nums);
// [1, 2, 3, 4, 5]

//降序
const nums = [4, 2, 5, 1, 3];
nums.sort((a, b) => b - a);
console.log(nums);
// [5, 4, 3, 2, 1]
```

**10、splice()**
splice(): 方法用于添加或删除数组中的元素。此方法会改变原数组。

> 语法: _array_.splice(_start_,_howmany_,_item1_,.....,_itemX_)
>
> > `start`：规定从何处添加/删除元素，该参数是开始插入和（或）删除的数组元素的下标，如果是负值，则表示从数组末位开始的第几位，必须是数字。
> >
> > `howmany`(可选)：整规定应该删除多少元素。必须是数字，但可以是 "0"，如果未规定此参数，则删除从 start 开始到原数组结尾的所有元素。
> >
> > `item1,..., itemX`(可选)：要添加进数组的元素，从`start` 位置开始。如果不指定，则 `splice()` 将只删除数组元素。
>
> 返回值：由被删除的元素组成的一个数组。如果只删除了一个元素，则返回只包含一个元素的数组。如果没有删除元素，则返回空数组。

**_代码示例(如下)_**

```lua
lua复制代码var a = ['wjk', 'shy', 'czh', 'ws'];
a.splice(2, 0, 'zsl', 'why');
consle.log(a) //'wjk', 'shy', 'zsl', 'why', 'czh', 'ws'
```

**11、toString()**
toString(): 方法返回一个字符串，表示指定的数组及其元素。

> 语法: toString()
>
> 返回值：一个表示数组所有元素的字符串。

**_代码示例(如下)_**

```JS
const array = [1, 2, 'a', 'b'];

console.log(array1.toString());
//"1,2,a,b"
```

**12、valueOf()**
valueOf(): 方法返回 Array 对象的原始值，不会改变原数组。

> 语法: array.valueOf()
>
> 返回值：返回的是一个对象，也是原对象本身。

**_代码示例(如下)_**

```js
let array = [1, 2, 3];
console.log(typeof array.valueOf()); //object
console.log(array.valueOf() === array); //true
```

**13、indexOf()**
indexOf(): 方法返回在数组中可以找到给定元素的第一个索引，如果不存在，则返回 -1。

> 语法: indexOf(item, fromIndex)
>
> > `item`: 要查找的元素。
> >
> > `fromIndex`(可选)：规定在数组中开始检索的位置。它的合法取值是 0 到 stringObject.length - 1，如果是负数就是倒数到位置开始
>
> 返回值：首个被找到的元素在数组中的索引位置; 若没有找到则返回 **-1**。

**_代码示例(如下)_**

```js
const array = [2, 9, 9];
array.indexOf(2); // 0
```

**14、lastIndexOf()**
lastIndexOf(): 方法返回指定元素在数组中的最后一个的索引，如果不存在则返回 -1。从数组的后面向前查找，从 `fromIndex` 处开始。

> 语法: lastIndexOf(searchElement, fromIndex)
>
> > `searchElement`: 被要查找的元素。
> >
> > `fromIndex`(可选)：规定在字符串中开始检索的位置。它的合法取值是 0 到 stringObject.length - 1。如省略该参数，则将从字符串的最后一个字符处开始检索。即使该值为负，数组仍然会被从后向前查找。如果该值为负时，其绝对值大于数组长度，则方法返回 -1，即数组不会被查找。
>
> 返回值：数组中该元素最后一次出现的索引，如未找到返回 `-1`。

**_代码示例(如下)_**

```javascript
const array = [2, 9, 9];
array.lastIndexOf(9); // 2
```

**15、forEach()**
forEach(): 方法对数组的每个元素执行一次给定的函数。

> 语法: arr.forEach(callbackFn(currentValue [, index [, array]])[, thisArg]);
>
> > `callbackFn`: 为数组中每个元素执行的，函数函数调用时带有以下参数：
> >
> > > `currentValue`：数组中正在处理的当前元素值。
> > >
> > > `index`(可选)：数组中正在处理的当前元素的索引。
> > >
> > > `array`(可选)：`forEach()` 方法正在操作的数组。
> > >
> > > `thisArg`(可选)：可选参数。当执行回调函数 `callbackFn` 时，用作 `this` 的值。
>
> 返回值：`undefined`。

**_代码示例(如下)_**

```javascript
const arr = ["red", "green", "blue"];
const result = arr.forEach(function (ele, index) {
  console.log(ele); // 数组元素  red   green  blue
  console.log(index); // 索引号
});
```

**16、map()**
map(): 方法创建一个新数组，这个新数组由原数组中的每个元素都调用一次提供的函数后的返回值组成。

> 语法: array.map(function(currentValue, index, arr), thisIndex)
>
> > `callbackFn`: 生成新数组元素的函数，使用三个参数：
> >
> > > `currentValue`: `callbackFn` 数组中正在处理的当前元素值。
> > >
> > > `index`: `callbackFn` 数组中正在处理的当前元素的索引。
> > >
> > > `array`: `map` 方法调用的数组。
> > >
> > > `thisArg`(可选)：可选参数。当执行回调函数 `callbackFn` 时，用作 `this` 的值。
>
> 返回值：一个新数组，每个元素都是回调函数的返回值。

**_代码示例(如下)_**

```JS
let array = [1, 2, 3, 4, 5];

let newArray = array.map((item) => {
    return item * item;
})

console.log(newArray)  // [1, 4, 9, 16, 25]
```

**17、filter()**
filter(): 方法创建给定数组一部分的浅拷贝，其包含通过所提供函数实现的测试的所有元素。

> 语法: Array.filter(function(currentValue, indedx, arr), thisValue)
>
> > `callbackFn`: 用来测试数组中每个元素的函数。返回 `true` 表示该元素通过测试，保留该元素，`false` 则不保留。它接受以下三个参数：
> >
> > > `currentValue`: `callbackFn` 数组中正在处理的当前元素值。
> > >
> > > `index`(可选): `callbackFn` 数组中正在处理的当前元素的索引。
> > >
> > > `array`(可选): `filter` 方法调用的数组。		
> > >
> > > `thisArg`(可选)：可选参数。当执行回调函数 `callbackFn` 时，用作 `this` 的值。
>
> 返回值：一个新的、由通过测试的元素组成的数组，如果没有任何数组元素通过测试，则返回空数组。

**_代码示例(如下)_**

```JS
let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let res = nums.filter((num) => {
    return num > 5;
});
console.log(res);  // [6, 7, 8, 9, 10]

//数组去重
let arr = [1, 2, 3, 2, 3, 4];
let arrFIlter1 = arr.filter((ele, index, arr) => {
    return arr.indexOf(ele) === index;
});
console.log(arrFIlter1);
```

**18、every()**
every(): 方法测试一个数组内的所有元素是否都能通过某个指定函数的测试。它返回一个布尔值。
`注意`：若收到一个空数组，此方法在任何情况下都会返回 `true`。

> 语法: Array.every(function(currentValue,index,arr), thisValue)
>
> > `callbackFn`: 用来测试数组中每个元素的函数。返回 `true` 表示该元素通过测试，保留该元素，`false` 则不保留。它接受以下三个参数：
> >
> > > `currentValue`: `callbackFn` 数组中正在处理的当前元素值。
> > >
> > > `index`(可选): `callbackFn` 数组中正在处理的当前元素的索引。
> > >
> > > `array`(可选): `every` 方法调用的数组。
> > >
> > > `thisArg`(可选)：可选参数。当执行回调函数 `callbackFn` 时，用作 `this` 的值。
>
> 返回值：如果回调函数的每一次返回都为`真值`，返回 **`true`**，否则返回 **`false`**。

**_代码示例(如下)_**

```javascript
[12, 54, 18, 130, 44].every((x) => x >= 10); // true

let arr = [];
let flag = arr.every((item, index) => {
  return item && item.age > 10;
});
console.log(flag); //输出的是true
```

**19、some()**
some(): 如果有一个元素满足条件，则表达式返回*true* , 剩余的元素不会再执行检测，如果没有满足条件的元素，则返回 false。

`注意`：如果用一个空数组进行测试，在任何情况下它返回的都是`false`。

> 语法: Array.every(function(currentValue,index,arr), thisValue)
>
> > `callbackFn`: 用来测试数组中每个元素的函数。返回 `true` 表示该元素通过测试，保留该元素，`false` 则不保留。它接受以下三个参数：
> >
> > > `currentValue`: `callbackFn` 数组中正在处理的当前元素值。
> > >
> > > `index`(可选): `callbackFn` 数组中正在处理的当前元素的索引。
> > >
> > > `array`(可选): `some` 方法调用的数组。
> > >
> > > `thisArg`(可选)：可选参数。当执行回调函数 `callbackFn` 时，用作 `this` 的值。
>
> 返回值：数组中有至少一个元素通过回调函数的测试就会返回 **`true`**；所有元素都没有通过回调函数的测试返回值才会为 false。

**_代码示例(如下)_**

```js
[2, 5, 8, 1, 11].some((x) => x > 10); // true
```

**20、reduce()**
reduce(): 方法对数组中的每个元素执行一个由您提供的 reduce 函数(升序执行)，将其结果汇总为单个返回值。

> 语法: Array.reduce(function(accumulator, currentValue, currentIndex, arr), initialValue);
>
> > `callbackFn`: 一个“reducer”函数，包含四个参数：
> >
> > > `accumulator`: 累计器。
> > >
> > > `currentValue`: 当前元素。
> > >
> > > `currentIndex`(可选): 当前元素的索引。
> > >
> > > `arr`(可选): 要处理的数组。
> > >
> > > `initialValue`(可选): 传递给函数的初始值，相当于 accumulator 的初始值。

> 返回值：使用“reducer”回调函数遍历整个数组后的结果。

**_代码示例(如下)_**

```javascript
//简单来说就是对一个array执行reduce()方法，
//就是把其中的function()挨个地作用于arr中的元素上，
//而且上一次的输出会作为下一次的一个输入
let arr = [1, 2, 3, 4, 5];
let s = arr.reduce((sum, curr) => sum + curr, 0);
console.log(s); //15
```

**21、reduceRight()**
reduceRight():reduceRight() 方法的功能和 reduce()功能是一样的，不同的是 reduceRight() 从数组的末尾向前将数组中的数组项做累加。

> 语法: Array.reduceRight(function(total, currentValue, currentIndex, arr), initialValue)
>
> > `callbackFn`: 一个回调函数，用于操作数组中的每个元素，它可接受四个参数：
> >
> > > `accumulator`: 累计器。
> > >
> > > `currentValue`: 当前元素。
> > >
> > > `currentIndex`(可选): 当前元素的索引。
> > >
> > > `arr`(可选): 要处理的数组。
> > >
> > > `initialValue`(可选): 传递给函数的初始值，相当于 accumulator 的初始值。
>
> 返回值：执行之后的返回值。

**_代码示例(如下)_**

```javascript
//简单来说就是对一个array执行reduce()方法，
//就是把其中的function()挨个地作用于arr中的元素上，
//而且上一次的输出会作为下一次的一个输入
let arr = [5, 4, 3, 2, 1];
let s = arr.reduce((sum, curr) => sum + curr, 0);
console.log(s); //15
```

### 数组去重

- `filter`

  ```js
  // filter过滤
  console.log(
    nums.filter((num, index, nums) => {
      return nums.indexOf(num) === index;
    })
  );
  ```

- `Set/Array.form`

  ```js
  //Set+Array.from
  console.log("Set/Array.from:", Array.from(new Set(nums)));
  ```

  有个小问题：无法去重引用类型数据

- 古老的方法

  ```js
  //古老的双重循环
  for (let i = 0, len = nums1.length; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      if (nums1[i] == nums1[j]) {
        nums1.splice(j, 1);
      }
    }
  }
  ```

- `indexOf`/`includes()` 改一下判断条件即可

  ```js
  let repeatArr = [];
  for (let i = 0, len = nums.length; i < len; i++) {
    // if (repeatArr.includes(!nums[i]))
    if (repeatArr.indexOf(nums[i]) == -1) {
      repeatArr.push(nums[i]);
    }
  }
  ```

- `reduce`

  ```js
  function reduceMethod(arr) {
    return arr.reduce((res, currentNum) => {
      if (!res.includes(currentNum)) {
        res.push(currentNum);
      }
      return res;
    }, []);
  }
  ```

- 对象数组去重

  ```js
  function objArryTo(arr) {
    const res = [];
    const mapList = new Map();
    arr.forEach((item) => {
      if (!mapList.has(item.id)) {
        res.push(item);
        mapList.set(item.id, "");
      }
    });
    return res;
  }
  ```

## 浏览器点击后发生的事件

事件：

先捕获事件 e.pre

事件行为冒泡 有 e.() xxx 阻止默认行为，错了 是这个 !! e.prebentPopop 冒泡的英文

没有接着了

## 浏览器事件

> `DOM`事件流（`event flow` ）存在三个阶段：事件捕获阶段、处于目标阶段、事件冒泡阶段。

### 事件冒泡

### 事件捕获

### 事件委托

> 利用`事件冒泡`，把子元素的事件都绑定到父元素上。如果子元素阻止了事件冒泡，那么委托就无法实现

```js
Let father document.queryselector('.father')
father.onclick function(e){
    console.Log(e.target.innerHTML)
}
```

###

###

一千个元素

只给一个父元素监听点击事件 。事件

ul onClick

li

li

ul

然后根据事件冒泡行为 e.target 来找到具体被点击的事件

## [箭头函数和 function 的区别](https://juejin.cn/post/7069943937577779214?searchId=20230921223051AC4414E999DF322A6BF5#heading-5)

> [什么是箭头函数](https://juejin.cn/post/6994378843620556808?searchId=2023092123201435FA64AB005AAD373F6D#heading-2)

- 箭头函数与普通函数相比，缺少了`caller，arguments，prototype`

- 声明方式不同

  - 声明一个普通函数需要使用关键字`function`来完成，并且使用`function`既可以声明成一个**具名函数**也可以声明成一个**匿名函数**
  - 声明一个箭头函数则只需要使用箭头就可以，无需使用关键字`function`，比普通函数声明更简洁。
  - 箭头函数只能声明成**匿名函数**，但可以通过表达式的方式让箭头函数具名

- this 的指向不同

  > 对于普通函数来说，内部的`this`指向函数运行时所在的对象，但是这一点对箭头函数不成立。它没有自己的`this`对象，内部的`this`就是定义时上层作用域中的`this`。也就是说，箭头函数内部的`this`指向是固定的，相比之下，普通函数的`this`指向是可变

  ```js
  var name = "out";
  var person = {
    name: "inner",
    say: function () {
      console.log("say:", this.name);
    },
    say2: () => {
      console.log("say2:", this.name);
    },
  };
  person.say(); // say: inner
  person.say2(); // say2: out
  ```

- 箭头函数的 this 永远不会变，call、apply、bind 也无法改变(`call、apply、bind`核心思想：借用方法)

- 箭头函数没有原型 prototype

- 箭头函数不能当成一个构造函数

- 🧑🏻‍🌾 没有 new.target

- 🧑🏻‍🌾 [箭头函数没有自己的 arguments](https://juejin.cn/post/6994378843620556808?searchId=2023092123201435FA64AB005AAD373F6D)

## [匿名函数](https://juejin.cn/post/6844903977880928270?searchId=20230921223236C828FB8773AC18382EB1#heading-4)

## 弹性布局

CSS：

flex 布局（弹性布局）

父元素： justify-content alig-item display-flex

子元素： flex:1 flex-grow 1 flex -shirk 1 flex-basix 0

数字 比例

## BFC

BFC：

高度塌陷

## 重排和重绘

（重排）回流： 几何尺寸改变改变

重绘：上色，像素点

### 不触发重排，动画实现有什么方式

使用：transform

will-change 属性

opacity 和 visibility：hidden

## 浏览器事件循环

宏任务和微任务

## React Hook

useEffect 的

返回值 组件销毁时触发这个函数

return 里面清除定时器，避免内存泄露

## 浏览器缓存

强缓存和协商缓存，强缓存

强缓存： 看 cache-control： max-age 相对时间 或者 expires 绝对时间。思考一下绝对时间受到客户端时间的影响，

也有种 Etag 不看时间，看哈希值

请求头对应值：if-modify-since 代表着时间

协商缓存： 304

## 类型转换

### 字符串转换

当我们需要一个字符串形式的值时，就会进行字符串转换。

比如，`alert(value)` 将 `value` 转换为字符串类型，然后显示这个值。

我们也可以显式地调用 `String(value)` 来将 `value` 转换为字符串类型：

```javascript
let value = true;
alert(typeof value); // boolean

value = String(value); // 现在，值是一个字符串形式的 "true"
alert(typeof value); // string
```

字符串转换最明显。`false` 变成 `"false"`，`null` 变成 `"null"` 等

### 数字型转换

| 值           | 变成……                                                                                                                                                                                           |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `undefined`  | `NaN`                                                                                                                                                                                            |
| `null`       | `0`                                                                                                                                                                                              |
| `true/false` | `1` / `0`                                                                                                                                                                                        |
| `string`     | 去掉首尾空白字符（空格、换行符 `\n`、制表符 `\t` 等）后的纯数字字符串中含有的数字。如果剩余字符串为空，则转换结果为 `0`。否则，将会从剩余字符串中“读取”数字。当类型转换出现 error 时返回 `NaN`。 |

### 容易出错的

- 对 `undefined` 进行数字型转换时，输出结果为 `NaN`，而非 `0`。
- 对 `"0"` 和只有空格的字符串（比如：`" "`）进行布尔型转换时，输出结果为 `true`。every

## JS 操作浏览器 DOM

- 使用 `document.querySelector` 获取一组符合 CSS 选择符的元素快照，类型为 NodeList（此对象是对于文档的实时运行的动态查询）

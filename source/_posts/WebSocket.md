---
title: WebSocket
abbrlink: c793072c
date: 2023-10-11 14:07:21
tags:
  - websocket
categories: 网络请求
description: 😚
top_img: "linear-gradient(35deg, rgba(0, 128, 0, 0.6), rgba(255, 255, 0, 0.6), rgba(0, 0, 255, 0.6), rgba(255, 0, 0, 0.6), rgba(128, 0, 128, 0.6))"
---

# Web SOCKET

## websocket 介绍

web socket 是一种全双工通讯的网络技术,属于应用层协议,基于 TCP 传输协议,并复用了 HTTP 的握手通道

是一种长连接,不需要频繁的链接断开

### websocket 数据帧格式

> 单位是 bit 如 FIN RSV 都占据 1bit opcode 占据 4bit

![image-20230906162803200](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309061628568.png)

- FIN 1BIT 标记数据是否发送到最后一位

  如果是消息的最后一个分片，则返回的是 1 否则返回 0

- OPCODE 4BIT

  ==9 10 用于心跳监测==

  ![image-20230906222522624](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309062225696.png)

- MASK(掩码)

  - 客户端发送消息到服务端 掩码为 1
  - 服务端发送消息到客户端 掩码为 0

- PAYLOAD（数据载荷长度）

  说明传输的数据的字节 根据 Payload length 的长度 判断后续字节的作用

  ![image-20230907103055654](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309071030759.png)

  `Buffer`字节数组

  - 大端序：高位放在低地址先读，按顺序读取

  - 小端序：

    ![image-20230907112108233](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309071121351.png)

    **输出为 256 1**

- Masking-Key

  0 或 4 字节(32 位)所有从客户端传送到服务端的数据帧，数据载荷都进行了掩
  码操作，Mask 为 1，且携带了 4 字节的 Masking-key。如果 Mask 为 0，则没有 Masking-key。
  载荷数的长度，不包括 mask key 的长度

## websocket 建立链接过程

![	](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309062208820.png)

**客户端请求头及请求相应状态**：

![image-20230906221244548](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309062212586.png)

**服务端响应**

![image-20230906221421998](https://oooooo.oss-cn-fuzhou.aliyuncs.com/readme/202309062214054.png)

其中请求中的`Sec-Websocket-Key`用于验证链接是否合法

状态码中的 101 代表协议切换

## 客户端发送消息到客户端

### 代码

> 客户端代码

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <input
      type="text"
      id="text" />
    <button onclick="send()">send</button>
    <script>
      let text = document.getElementById("text");
      // 在浏览器链接服务器
      let soket = new WebSocket("ws://localhost:8889");
      // 当链接打开或建立后，触发回调
      soket.onopen = function () {
        soket.send("hello server");
      };

      // 服务器端给客户端发送消息时 可以通过soket.onmessage接受 存储于event中
      soket.onmessage = function (event) {
        // soket.send(event.data);
        console.log(event.data);
      };
      function send() {
        let value = text.value;
        text.value = "";
        soket.send(value);
      }
    </script>
  </body>
</html>
```

> 服务端代码

```js
const { Server } = require("ws");
const wsServer = new Server({ port: 8889 });
//wsServer 服务器
//socket 套接字 类似于打电话的手机

//"connection"监听客户端过来的链接
wsServer.on("connection", (socket) => {
  //“message"监听当前链接的客户端发来的消息
  socket.on("message", (message) => {
    console.log(message.toLocaleString());
    socket.send(message);
  });
});
```

### 流程

1. `let soket = new WebSocket("ws://localhost:8889") `浏览器链接服务器
2. `        soket.send("hello server");`客户端向服务器发消息 "hello server”
3. `socket.on("message"`)服务端监听到消息并触发回调，向客户端发送消息
4. `soket.onmessage`客户端监听到服务端的相应，触发回调打印

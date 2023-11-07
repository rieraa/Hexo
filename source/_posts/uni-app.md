---
title: uni-app
tags:
  - vue3
  - vite
  - mini_program
top_img: 'linear-gradient(30deg, rgba(190, 60, 160, 0.6), rgba(128, 0, 128, 0.6), rgba(204, 0, 102, 0.6), rgba(100, 40, 100, 0)'
description: "😷"
abbrlink: e19785da
date: 2023-10-15 21:37:31
sticky:
updated:
---



## pages.json 页面配置

`pages.json` 文件用来对 uni-app 进行全局配置，决定页面文件的路径、窗口样式、原生的导航栏、底部的原生tabbar 等。



## 配置字段

| 属性                                                         | 类型         | 必填 | 描述                                    | 平台兼容                 |
| :----------------------------------------------------------- | :----------- | :--- | :-------------------------------------- | :----------------------- |
| [globalStyle](https://uniapp.dcloud.net.cn/collocation/pages#globalstyle) | Object       | 否   | 设置默认页面的窗口表现                  |                          |
| [pages](https://uniapp.dcloud.net.cn/collocation/pages#pages) | Object Array | 是   | 设置页面路径及窗口表现                  |                          |
| [easycom](https://uniapp.dcloud.net.cn/collocation/pages#easycom) | Object       | 否   | 组件自动引入规则                        | 2.5.5+                   |
| [tabBar](https://uniapp.dcloud.net.cn/collocation/pages#tabbar) | Object       | 否   | 设置底部 tab 的表现                     |                          |
| [condition](https://uniapp.dcloud.net.cn/collocation/pages#condition) | Object       | 否   | 启动模式配置                            |                          |
| [subPackages](https://uniapp.dcloud.net.cn/collocation/pages#subPackages) | Object Array | 否   | 分包加载配置                            | H5、uni-app x 不支持     |
| [preloadRule](https://uniapp.dcloud.net.cn/collocation/pages#preloadrule) | Object       | 否   | 分包预下载规则                          | 微信小程序               |
| [workers](https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html) | String       | 否   | `Worker` 代码放置的目录                 | 微信小程序               |
| [leftWindow](https://uniapp.dcloud.net.cn/collocation/pages#leftwindow) | Object       | 否   | 大屏左侧窗口                            | H5                       |
| [topWindow](https://uniapp.dcloud.net.cn/collocation/pages#topwindow) | Object       | 否   | 大屏顶部窗口                            | H5                       |
| [rightWindow](https://uniapp.dcloud.net.cn/collocation/pages#rightwindow) | Object       | 否   | 大屏右侧窗口                            | H5                       |
| [uniIdRouter](https://uniapp.dcloud.net.cn/uniCloud/uni-id-summary#uni-id-router) | Object       | 否   | 自动跳转相关配置，新增于HBuilderX 3.5.0 | uni-app x 不支持         |
| entryPagePath                                                | String       | 否   | 默认启动首页，新增于HBuilderX 3.7.0     | 微信小程序、支付宝小程序 |

## 页面路由

## 事件总线

```
<template>
 <!-- #ifdef APP -->
 <scroll-view style="flex: 1">
   <!-- #endif -->
   <view>
     <button @click="on">开始监听</button>
     <button @click="once">监听一次</button>
     <button @click="off">取消监听</button>
     <button @click="emit">触发监听</button>
     <button @click="clear">清空消息</button>
     <view class="box">
       <view>收到的消息：</view>
       <view>
         <view v-for="(item, index) in log" :key="index">{{ item }}</view>
       </view>
     </view>
   </view>
   <!-- #ifdef APP -->
 </scroll-view>
 <!-- #endif -->
</template>

<script lang="uts">
export default {
 data() {
   return {
     log: [] as string[],
   }
 },
 methods: {
   fn(res: string) {
     this.log.push(res)
   },
   on() {
     uni.$on('test', this.fn)
   },
   once() {
     uni.$once('test', this.fn)
   },
   off() {
     uni.$off('test', this.fn)
   },
   emit() {
     uni.$emit('test', 'msg:' + Date.now())
   },
   clear() {
     this.log.length = 0
   },
 },
}
</script>

<style>
.box {
 padding: 10px;
}
</style>


```


# L4D2 一键连接跳转 API

一个专为 **求生之路2 (Left 4 Dead 2)** AstrBot 插件设计的 Steam 一键连接跳转服务，支持国内访问优化。

## 项目特点

- 支持 `/connect?server=IP:PORT` 和 `/connect/IP:PORT` 两种调用方式
- 使用 `steam://rungameid/550//+connect` 高成功率协议
- 自动跳转 + 醒目手动点击按钮，兼顾国内浏览器
- 部署简单，免费（Vercel）

## 快速部署流程（推荐）

### 1. Fork 本仓库
点击 GitHub 页面右上角的 **Fork**，将本项目 Fork 到你的账号下。

### 2. 在 Vercel 上部署
1. 打开 [Vercel](https://vercel.com) 并登录（推荐使用 GitHub 账号）
2. 点击 **New Project** → **Import Git Repository**
3. 选择你 Fork 的仓库，点击 **Deploy**

部署完成后，Vercel 会给你一个 `xxx.vercel.app` 的域名。

### 3.（强烈推荐）绑定自己的域名
在 Vercel 项目设置 → **Domains** 中添加你的域名（如 `hazel.wiki`），并完成 DNS 解析（CNAME）。

---

## 在 AstrBot 插件中的配置

在 `l4d2-with-astrbot` 插件配置中填写：

```json
"connectBaseUrl": "https://你的域名/connect"
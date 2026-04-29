# 🚀 L4D2 Connect API (Vercel Optimized)

一个专为 **求生之路2 (Left 4 Dead 2)** 社区设计的 Steam 一键连接跳转服务。

### 🌟 为什么需要它？
在 QQ、微信或手机浏览器中，直接点击 `steam://` 协议链接往往会被直接拦截或无响应。本 API 通过搭建一个极简的中间过渡页，引导浏览器正确识别协议，从而实现**一键拉起游戏并加入房间，彻底告别控制台手动输入 IP**。

---

## 🛠️ 快速部署 (免服务器)

### 1. 准备仓库
点击本页面右上角的 **Fork** 按钮，将本项目克隆到你自己的 GitHub 账号下。

### 2. Vercel 一键部署
1. 登录 [Vercel](https://vercel.com)（推荐直接使用 GitHub 账号授权登录）。
2. 在控制台点击 **Add New...** -> **Project**。
3. 在列表中找到你刚刚 Fork 的仓库，点击 **Import**。
4. 无需修改任何环境参数，直接点击 **Deploy**。等待十几秒后，Vercel 将为你分配一个默认的 `*.vercel.app` 域名。

### 3. 🌐 绑定自定义域名 (国内直连核心步骤)
由于 Vercel 的默认域名在国内大面积被墙，强烈建议绑定你自己的域名（如 `.cn`、`.com`、`.wiki` 等）。

**如果你使用的是 Cloudflare 托管域名，整个过程支持全自动一键绑定：**
1. 进入 Vercel 部署成功的项目主页，点击顶部导航栏的 **Settings** -> 左侧菜单的 **Domains**。
2. 输入你想要使用的子域名（例如 `link.你的域名.com`），点击 **Add**。
3. Vercel 会自动检测到你的域名托管在 Cloudflare，并弹出一键自动配置的提示（Quick Setup / Login to Cloudflare）。
4. **只需点击授权一键绑定**，Vercel 就会全自动跑完所有流程，帮你把底层的 DNS 记录全部配好！
5. 等待页面上的状态变成绿色的 `Valid Configuration`，即可在国内秒速直连。

---

## 📖 API 调用说明

部署完成后，你可以在群机器人（如 AstrBot 插件）或其他前端页面中配置以下地址：

| 调用方式 | 示例链接 | 说明 |
| :--- | :--- | :--- |
| **Query 参数** | `https://你的域名/connect?server=1.2.3.4:27015` | 标准调用方式，适配大多数插件 |
| **路径参数** | `https://你的域名/connect/1.2.3.4:27015` | 更简洁美观的链接格式 |

### 底层协议方案
本项目默认采用 `steam://rungameid/550//+connect%20{ip:port}` 唤醒协议。
*优势：相比传统的单纯 `steam://connect`，该长协议在 Steam 后台挂起、但游戏本体尚未启动的情况下，成功拉起游戏并自动加载进入服务器的成功率极高，减少了客户端装死不响应的概率。*

---

## ⚙️ 配合 AstrBot 插件使用

如果你使用的是 `l4d2-with-astrbot` 机器人插件，请打开插件目录下的 `config.json`，按如下格式填入你刚才绑定的域名：

```json
{
    "connectBaseUrl": "https://你的自定义域名/connect?server=",
    "group_configs": [
        // ... 你的其他群组和服务器配置
    ]
}
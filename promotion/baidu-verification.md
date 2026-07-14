# 百度搜索资源平台验证指南

> 目标：让百度搜索引擎收录你的网站（40篇文章 + 主页），用户搜"北京开锁"能找到你

---

## 第一步：打开百度搜索资源平台

1. 浏览器打开：**https://ziyuan.baidu.com/**
2. 用你的百度账号登录（没有就注册一个，用手机号即可）

---

## 第二步：添加站点

1. 登录后，点击左侧菜单 **"用户中心" → "站点管理"**
2. 点击 **"添加网站"**
3. 输入网站地址：`https://wzengyun.github.io/bjjingxunkaisuo/`
4. 选择验证方式：**推荐选"HTML标签验证"**

---

## 第三步：获取验证代码

选择"HTML标签验证"后，百度会给你一段代码，格式类似：

```html
<meta name="baidu-site-verification" content="codeva-XXXXXXX" />
```

**把这行代码完整复制，发给我**，我帮你加到网站里。

> 💡 如果你看到的是"文件验证"（需要上传一个 `baidu_verify_XXX.html` 文件），也可以把文件名告诉我，我帮你创建。

---

## 第四步：我帮你加入验证代码（我来做）

收到你的验证代码后，我会：
1. 把代码加到 `index.html` 和 `articles.html` 的 `<head>` 里
2. 推送到 GitHub 上线
3. 告诉你可以回去点"验证"了

---

## 第五步：验证通过后提交 Sitemap

1. 回到百度搜索资源平台
2. 左侧菜单 → **"普通收录" → "sitemap"**
3. 填入：`https://wzengyun.github.io/bjjingxunkaisuo/sitemap.xml`
4. 点击提交

这样百度就知道你有42个页面需要收录了。

---

## 第六步（可选）：手动提交URL加速收录

在 **"普通收录" → "URL提交"** 中，把以下URL批量粘贴提交：

```
https://wzengyun.github.io/bjjingxunkaisuo/
https://wzengyun.github.io/bjjingxunkaisuo/articles.html
https://wzengyun.github.io/bjjingxunkaisuo/posts/chaoyang.html
https://wzengyun.github.io/bjjingxunkaisuo/posts/haidian.html
https://wzengyun.github.io/bjjingxunkaisuo/posts/shaoyaoju.html
https://wzengyun.github.io/bjjingxunkaisuo/posts/yayuncun.html
```
（全部42个URL见 sitemap.xml）

---

## 同时做：Google Search Console

1. 打开 **https://search.google.com/search-console**
2. 用 Google 账号登录
3. 添加资源 → 网址前缀：`https://wzengyun.github.io/bjjingxunkaisuo/`
4. 选 HTML标签验证 → **把验证代码发给我**
5. 验证通过后 → 提交 sitemap

---

## ⏰ 时间线预期

| 步骤 | 耗时 | 效果 |
|------|------|------|
| 验证站点 | 5分钟 | 站点被百度认领 |
| 提交sitemap | 2分钟 | 百度开始抓取 |
| 等待收录 | 3-14天 | 文章陆续出现在百度搜索结果 |
| 持续优化 | 长期 | 排名逐步上升 |

> ⚠️ 百度收录新站通常需要3-14天，GitHub Pages的域名可能更慢一些。耐心等待，持续更新内容有助于加速。

---

## 常见问题

**Q: 验证一直失败怎么办？**
A: 确认代码已添加后等2分钟再验证。GitHub Pages 有CDN缓存，可能需要几分钟生效。

**Q: 多久能在百度搜到我的网站？**
A: 通常3-14天。首页和文章标题页面会先被收录，长尾关键词排名会慢慢上升。

**Q: 需要花钱做百度推广吗？**
A: 先用免费的自然收录。如果1个月后收录效果不理想，再考虑百度竞价排名（按点击付费）。

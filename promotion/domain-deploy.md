# kaisuo.me 域名部署指南

## 域名信息
- 域名：kaisuo.me
- 注册商：阿里云（万网）
- 实名认证：审核中
- 用途：北京京迅开锁官网，绑定 GitHub Pages

---

## 第一步：配置 DNS 解析（实名认证通过后操作）

登录阿里云域名控制台：https://dc.console.aliyun.com/

1. 找到 `kaisuo.me` → 点击 **解析**
2. 添加以下记录：

### A 记录（主域名 kaisuo.me）

| 记录类型 | 主机记录 | 记录值 | TTL |
|----------|----------|--------|-----|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |

### CNAME 记录（www 子域名）

| 记录类型 | 主机记录 | 记录值 | TTL |
|----------|----------|--------|-----|
| CNAME | www | wzengyun.github.io. | 600 |

> 注意：CNAME 记录值末尾的 `.` 不要省略

---

## 第二步：确认 GitHub 仓库设置

代码已提交（CNAME 文件已创建），GitHub Pages 会自动识别。

检查方式：
1. 打开 https://github.com/wzengyun/bjjingxunkaisuo/settings/pages
2. 确认 Custom domain 显示 `kaisuo.me`
3. 勾选 **Enforce HTTPS**（等 DNS 生效后几分钟再勾）

---

## 第三步：验证部署

DNS 生效后（通常 10-30 分钟），访问：
- https://kaisuo.me
- https://kaisuo.me/articles.html
- https://kaisuo.me/posts/chaoyang.html

---

## 第四步：重新提交百度站长平台

域名生效后，用新域名重新添加站点：
1. 登录 https://ziyuan.baidu.com/
2. 站点管理 → 添加网站 → 输入 `https://kaisuo.me`
3. 选择 HTML 标签验证
4. 验证码告诉我，我加到网站里
5. 验证通过后提交 sitemap：`https://kaisuo.me/sitemap.xml`

> kaisuo.me 是独立主域，不会再遇到 github.io 的站点数量限制问题

---

## 网络问题备注

如果 GitHub HTTPS 推送被阻断（国内偶发），可通过 SSH 推送：
- SSH 密钥已生成：`C:\Users\wangy\.ssh\id_ed25519.pub`
- 需要将公钥添加到 GitHub：Settings → SSH and GPG keys → New SSH key
- 添加后用 `git push origin master` 即可（已配置 SSH remote）

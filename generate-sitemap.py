# -*- coding: utf-8 -*-
"""Generate sitemap.xml and articles.html with all 340+ articles"""
import csv
import os

# Read slug mapping
areas = []
with open(r"d:\Software\Workspace\Lock AD\promotion\area-slugs.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        areas.append(row)

# Existing old articles (keep them)
old_slugs = ["chaoyang","haidian","dongcheng","xicheng","fengtai","tongzhou","daxing","changping",
             "shijingshan","shunyi","fangshan","guomao","zhongguancun","wangjing","sanlitun",
             "wudaokou","huilongguan","yizhuang","shangdi","xierqi","tiantongyuan","qinghe",
             "shahe","beiqijia","dawanglu","shuangjing","panjiayuan","tuanjiehu","muxiyuan",
             "fangzhuang","jinsong","qingnianlu","jiuxianqiao","taiyanggong","shaoyaoju",
             "yayuncun","gongzhufen","weigongcun","hangtianqiao","liyuan"]

# ============ Generate sitemap.xml ============
sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    '    <url><loc>https://kaisuo.me/</loc><priority>1.0</priority><changefreq>weekly</changefreq></url>',
    '    <url><loc>https://kaisuo.me/articles.html</loc><priority>0.9</priority><changefreq>weekly</changefreq></url>']

# Add old articles
for slug in old_slugs:
    sitemap_lines.append(f'    <url><loc>https://kaisuo.me/posts/{slug}.html</loc><priority>0.8</priority><changefreq>monthly</changefreq></url>')

# Add new articles
for area in areas:
    sitemap_lines.append(f'    <url><loc>https://kaisuo.me/posts/{area["slug"]}.html</loc><priority>0.8</priority><changefreq>monthly</changefreq></url>')

sitemap_lines.append('</urlset>')

with open(r"d:\Software\Workspace\Lock AD\sitemap.xml", "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_lines))

print(f"Sitemap: {len(sitemap_lines)-3} URLs")

# ============ Generate articles.html ============
# Group by district
from collections import OrderedDict
by_district = OrderedDict()
for area in areas:
    d = area["district"]
    if d not in by_district:
        by_district[d] = []
    by_district[d].append(area)

district_order = ["东城区","西城区","朝阳区","丰台区","石景山区","海淀区","门头沟区","房山区",
                  "通州区","顺义区","昌平区","大兴区","怀柔区","平谷区","密云区","延庆区"]

# Old articles grouped
old_articles = [
    ("热门区域", [("朝阳区","chaoyang"),("海淀区","haidian"),("东城区","dongcheng"),("西城区","xicheng"),
                 ("丰台区","fengtai"),("通州区","tongzhou"),("大兴区","daxing"),("昌平区","changping"),
                 ("石景山","shijingshan"),("顺义区","shunyi"),("房山区","fangshan")]),
    ("热门商圈", [("国贸","guomao"),("中关村","zhongguancun"),("望京","wangjing"),("三里屯","sanlitun"),
                 ("五道口","wudaokou"),("回龙观","huilongguan"),("亦庄","yizhuang"),("上地","shangdi"),
                 ("西二旗","xierqi"),("天通苑","tiantongyuan"),("清河","qinghe"),("沙河","shahe"),
                 ("北七家","beiqijia"),("大望路","dawanglu"),("双井","shuangjing"),("潘家园","panjiayuan"),
                 ("团结湖","tuanjiehu"),("木樨园","muxiyuan"),("方庄","fangzhuang"),("劲松","jinsong"),
                 ("青年路","qingnianlu"),("酒仙桥","jiuxianqiao"),("太阳宫","taiyanggong"),
                 ("芍药居","shaoyaoju"),("亚运村","yayuncun"),("公主坟","gongzhufen"),
                 ("魏公村","weigongcun"),("航天桥","hangtianqiao"),("梨园","liyuan")]),
]

# Build articles HTML
html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>北京开锁服务区域 - 覆盖全北京16区340+街道乡镇 | 北京京迅开锁 15501023797</title>
    <meta name="description" content="北京京迅开锁服务覆盖全北京16个区340余个街道、镇、乡，24小时上门开锁换锁芯，电话15501023797。">
    <meta name="keywords" content="北京开锁,北京开锁公司,北京开锁电话,北京换锁芯,北京各区开锁,北京街道开锁">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://kaisuo.me/articles.html">
    <meta name="baidu-site-verification" content="codeva-syDQl346cg" />
    <style>
        *{margin:0;padding:0;box-sizing:border-box;}
        body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",Arial,sans-serif;color:#333;background:#f8f9fa;line-height:1.8;}
        .header{background:linear-gradient(135deg,#1a2a4a,#0d1b33);color:#fff;padding:40px 20px;text-align:center;}
        .header h1{font-size:28px;font-weight:800;margin-bottom:8px;}
        .header p{font-size:15px;color:rgba(255,255,255,0.8);}
        .header .phone{font-size:32px;font-weight:800;color:#d4a843;margin:12px 0;letter-spacing:2px;}
        .header .phone a{color:#d4a843;text-decoration:none;}
        .container{max-width:1000px;margin:0 auto;padding:30px 20px;}
        .call-banner{background:#fff;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.08);padding:24px;text-align:center;margin-bottom:30px;}
        .call-banner .phone{font-size:28px;font-weight:800;color:#1a2a4a;}
        .call-banner .phone a{color:#d4a843;text-decoration:none;}
        .call-banner .btn{display:inline-block;background:#d4a843;color:#fff;padding:12px 36px;border-radius:50px;font-size:16px;font-weight:700;margin-top:10px;text-decoration:none;}
        .section{background:#fff;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.06);padding:24px;margin-bottom:20px;}
        .section h2{font-size:20px;font-weight:700;color:#1a2a4a;margin-bottom:16px;padding-left:12px;border-left:4px solid #d4a843;}
        .area-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:8px;}
        .area-grid a{display:block;padding:8px 14px;background:#f8f9fa;border-radius:6px;font-size:14px;color:#555;text-decoration:none;transition:all 0.2s;}
        .area-grid a:hover{background:#1a2a4a;color:#fff;}
        .district-title{font-size:16px;font-weight:700;color:#1a2a4a;margin:16px 0 8px;}
        .breadcrumb{text-align:center;font-size:14px;color:#666;margin-bottom:20px;}
        .breadcrumb a{color:#d4a843;text-decoration:none;}
        .float-call{position:fixed;bottom:24px;right:20px;z-index:9999;width:56px;height:56px;border-radius:50%;background:#d4a843;color:#fff;box-shadow:0 6px 24px rgba(212,168,67,0.5);display:flex;align-items:center;justify-content:center;font-size:26px;text-decoration:none;animation:pulse 2s infinite;}
        @media(min-width:769px){.float-call{display:none;}}
        @keyframes pulse{0%{box-shadow:0 0 0 0 rgba(212,168,67,0.5);}70%{box-shadow:0 0 0 16px rgba(212,168,67,0);}100%{box-shadow:0 0 0 0 rgba(212,168,67,0);}}
        @media(max-width:768px){.area-grid{grid-template-columns:repeat(auto-fill,minmax(130px,1fr));}}
    </style>
</head>
<body>
    <div class="header">
        <h1>北京开锁服务区域</h1>
        <p>覆盖全北京16区 340+街道乡镇 · 24小时上门服务</p>
        <div class="phone"><a href="tel:15501023797">15501023797</a></div>
        <p>座机：010-83879827 · 公安备案 · 最快15分钟到达</p>
    </div>

    <div class="container">
        <div class="breadcrumb"><a href="index.html">北京京迅开锁</a> &raquo; 服务区域</div>

        <div class="call-banner">
            <div class="phone"><a href="tel:15501023797">15501023797</a> / 010-83879827</div>
            <div>全北京24小时开锁服务 · 公安备案 · 技术开锁 · 价格透明</div>
            <a href="tel:15501023797" class="btn">立即拨打</a>
        </div>
""")

# Old articles sections
for title, items in old_articles:
    html_parts.append(f'        <div class="section">\n            <h2>{title}</h2>\n            <div class="area-grid">')
    for name, slug in items:
        html_parts.append(f'                <a href="posts/{slug}.html">{name}开锁</a>')
    html_parts.append('            </div>\n        </div>')

# New articles by district
for district in district_order:
    if district not in by_district:
        continue
    items = by_district[district]
    html_parts.append(f'        <div class="section">\n            <h2>{district}开锁服务（{len(items)}个街道/乡镇）</h2>\n            <div class="area-grid">')
    for area in items:
        short = area["name"].replace("街道","").replace("回族乡","").replace("满族乡","").replace("满族蒙古族乡","").replace("乡","").replace("镇","")
        html_parts.append(f'                <a href="posts/{area["slug"]}.html">{short}开锁</a>')
    html_parts.append('            </div>\n        </div>')

html_parts.append("""
    </div>

    <a href="tel:15501023797" class="float-call">📞</a>
</body>
</html>""")

with open(r"d:\Software\Workspace\Lock AD\articles.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_parts))

print(f"articles.html generated with {sum(len(v) for v in by_district.values())} area links")

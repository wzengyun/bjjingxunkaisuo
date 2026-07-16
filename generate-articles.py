# -*- coding: utf-8 -*-
"""
批量生成北京全部街道/乡镇开锁SEO文章
共340个街道/镇/乡，每篇针对一个区域的长尾关键词
"""
import os
from pypinyin import lazy_pinyin

# ============ 数据：北京16区全部街道/乡镇 ============
areas = [
    # 东城区 17街道
    ("东城区","东华门街道"),("东城区","景山街道"),("东城区","交道口街道"),("东城区","安定门街道"),
    ("东城区","北新桥街道"),("东城区","东四街道"),("东城区","朝阳门街道"),("东城区","建国门街道"),
    ("东城区","东直门街道"),("东城区","和平里街道"),("东城区","前门街道"),("东城区","崇文门外街道"),
    ("东城区","东花市街道"),("东城区","龙潭街道"),("东城区","体育馆路街道"),("东城区","天坛街道"),
    ("东城区","永定门外街道"),
    # 西城区 15街道
    ("西城区","西长安街街道"),("西城区","新街口街道"),("西城区","月坛街道"),("西城区","展览路街道"),
    ("西城区","德胜街道"),("西城区","金融街街道"),("西城区","什刹海街道"),("西城区","大栅栏街道"),
    ("西城区","天桥街道"),("西城区","椿树街道"),("西城区","陶然亭街道"),("西城区","广安门内街道"),
    ("西城区","牛街街道"),("西城区","白纸坊街道"),("西城区","广安门外街道"),
    # 朝阳区 24街道+18乡+1民族乡
    ("朝阳区","建外街道"),("朝阳区","朝外街道"),("朝阳区","呼家楼街道"),("朝阳区","三里屯街道"),
    ("朝阳区","左家庄街道"),("朝阳区","香河园街道"),("朝阳区","和平街街道"),("朝阳区","安贞街道"),
    ("朝阳区","亚运村街道"),("朝阳区","小关街道"),("朝阳区","酒仙桥街道"),("朝阳区","麦子店街道"),
    ("朝阳区","团结湖街道"),("朝阳区","六里屯街道"),("朝阳区","八里庄街道"),("朝阳区","双井街道"),
    ("朝阳区","劲松街道"),("朝阳区","潘家园街道"),("朝阳区","垡头街道"),("朝阳区","大屯街道"),
    ("朝阳区","望京街道"),("朝阳区","奥运村街道"),("朝阳区","东湖街道"),("朝阳区","首都机场街道"),
    ("朝阳区","南磨房乡"),("朝阳区","高碑店乡"),("朝阳区","将台乡"),("朝阳区","太阳宫乡"),
    ("朝阳区","小红门乡"),("朝阳区","十八里店乡"),("朝阳区","平房乡"),("朝阳区","东风乡"),
    ("朝阳区","来广营乡"),("朝阳区","三间房乡"),("朝阳区","管庄乡"),("朝阳区","金盏乡"),
    ("朝阳区","孙河乡"),("朝阳区","崔各庄乡"),("朝阳区","东坝乡"),("朝阳区","黑庄户乡"),
    ("朝阳区","豆各庄乡"),("朝阳区","王四营乡"),("朝阳区","常营回族乡"),
    # 丰台区 24街道+2镇
    ("丰台区","右安门街道"),("丰台区","太平桥街道"),("丰台区","西罗园街道"),("丰台区","大红门街道"),
    ("丰台区","南苑街道"),("丰台区","东高地街道"),("丰台区","东铁匠营街道"),("丰台区","六里桥街道"),
    ("丰台区","丰台街道"),("丰台区","新村街道"),("丰台区","长辛店街道"),("丰台区","云岗街道"),
    ("丰台区","方庄街道"),("丰台区","宛平街道"),("丰台区","马家堡街道"),("丰台区","和义街道"),
    ("丰台区","卢沟桥街道"),("丰台区","花乡街道"),("丰台区","成寿寺街道"),("丰台区","石榴庄街道"),
    ("丰台区","玉泉营街道"),("丰台区","看丹街道"),("丰台区","五里店街道"),("丰台区","青塔街道"),
    ("丰台区","北宫镇"),("丰台区","王佐镇"),
    # 石景山区 9街道
    ("石景山区","八宝山街道"),("石景山区","老山街道"),("石景山区","八角街道"),("石景山区","古城街道"),
    ("石景山区","苹果园街道"),("石景山区","金顶街街道"),("石景山区","广宁街道"),("石景山区","五里坨街道"),
    ("石景山区","鲁谷街道"),
    # 海淀区 22街道+7镇
    ("海淀区","万寿路街道"),("海淀区","永定路街道"),("海淀区","羊坊店街道"),("海淀区","甘家口街道"),
    ("海淀区","八里庄街道"),("海淀区","紫竹院街道"),("海淀区","北下关街道"),("海淀区","北太平庄街道"),
    ("海淀区","学院路街道"),("海淀区","中关村街道"),("海淀区","海淀街道"),("海淀区","青龙桥街道"),
    ("海淀区","清华园街道"),("海淀区","燕园街道"),("海淀区","香山街道"),("海淀区","清河街道"),
    ("海淀区","花园路街道"),("海淀区","西三旗街道"),("海淀区","马连洼街道"),("海淀区","田村路街道"),
    ("海淀区","上地街道"),("海淀区","曙光街道"),
    ("海淀区","海淀镇"),("海淀区","东升镇"),("海淀区","温泉镇"),("海淀区","四季青镇"),
    ("海淀区","西北旺镇"),("海淀区","苏家坨镇"),("海淀区","上庄镇"),
    # 门头沟区 4街道+9镇
    ("门头沟区","大峪街道"),("门头沟区","城子街道"),("门头沟区","东辛房街道"),("门头沟区","大台街道"),
    ("门头沟区","王平镇"),("门头沟区","永定镇"),("门头沟区","龙泉镇"),("门头沟区","潭柘寺镇"),
    ("门头沟区","军庄镇"),("门头沟区","雁翅镇"),("门头沟区","斋堂镇"),("门头沟区","清水镇"),
    ("门头沟区","妙峰山镇"),
    # 房山区 8街道+13镇+6乡
    ("房山区","城关街道"),("房山区","新镇街道"),("房山区","向阳街道"),("房山区","东风街道"),
    ("房山区","迎风街道"),("房山区","星城街道"),("房山区","拱辰街道"),("房山区","西潞街道"),
    ("房山区","良乡镇"),("房山区","周口店镇"),("房山区","琉璃河镇"),("房山区","阎村镇"),
    ("房山区","窦店镇"),("房山区","石楼镇"),("房山区","长阳镇"),("房山区","河北镇"),
    ("房山区","长沟镇"),("房山区","大石窝镇"),("房山区","张坊镇"),("房山区","青龙湖镇"),
    ("房山区","韩村河镇"),
    ("房山区","霞云岭乡"),("房山区","南窖乡"),("房山区","佛子庄乡"),("房山区","大安山乡"),
    ("房山区","史家营乡"),("房山区","蒲洼乡"),
    # 通州区 11街道+10镇+1民族乡
    ("通州区","中仓街道"),("通州区","新华街道"),("通州区","北苑街道"),("通州区","玉桥街道"),
    ("通州区","潞源街道"),("通州区","通运街道"),("通州区","文景街道"),("通州区","九棵树街道"),
    ("通州区","临河里街道"),("通州区","杨庄街道"),("通州区","潞邑街道"),
    ("通州区","宋庄镇"),("通州区","张家湾镇"),("通州区","漷县镇"),("通州区","马驹桥镇"),
    ("通州区","西集镇"),("通州区","台湖镇"),("通州区","永乐店镇"),("通州区","潞城镇"),
    ("通州区","永顺镇"),("通州区","梨园镇"),("通州区","于家务回族乡"),
    # 顺义区 6街道+19镇
    ("顺义区","胜利街道"),("顺义区","光明街道"),("顺义区","石园街道"),("顺义区","空港街道"),
    ("顺义区","双丰街道"),("顺义区","旺泉街道"),
    ("顺义区","仁和镇"),("顺义区","后沙峪镇"),("顺义区","天竺镇"),("顺义区","杨镇"),
    ("顺义区","牛栏山镇"),("顺义区","南法信镇"),("顺义区","马坡镇"),("顺义区","高丽营镇"),
    ("顺义区","李桥镇"),("顺义区","李遂镇"),("顺义区","大孙各庄镇"),("顺义区","张镇"),
    ("顺义区","龙湾屯镇"),("顺义区","木林镇"),("顺义区","北小营镇"),("顺义区","北石槽镇"),
    ("顺义区","赵全营镇"),
    # 昌平区 8街道+14镇
    ("昌平区","城北街道"),("昌平区","城南街道"),("昌平区","天通苑北街道"),("昌平区","天通苑南街道"),
    ("昌平区","霍营街道"),("昌平区","回龙观街道"),("昌平区","龙泽园街道"),("昌平区","史各庄街道"),
    ("昌平区","南口镇"),("昌平区","马池口镇"),("昌平区","沙河镇"),("昌平区","东小口镇"),
    ("昌平区","阳坊镇"),("昌平区","小汤山镇"),("昌平区","南邵镇"),("昌平区","崔村镇"),
    ("昌平区","百善镇"),("昌平区","北七家镇"),("昌平区","兴寿镇"),("昌平区","流村镇"),
    ("昌平区","十三陵镇"),("昌平区","延寿镇"),
    # 大兴区 8街道+14镇
    ("大兴区","兴丰街道"),("大兴区","林校路街道"),("大兴区","清源街道"),("大兴区","观音寺街道"),
    ("大兴区","天宫院街道"),("大兴区","高米店街道"),("大兴区","荣华街道"),("大兴区","博兴街道"),
    ("大兴区","亦庄镇"),("大兴区","黄村镇"),("大兴区","旧宫镇"),("大兴区","西红门镇"),
    ("大兴区","瀛海镇"),("大兴区","青云店镇"),("大兴区","采育镇"),("大兴区","安定镇"),
    ("大兴区","礼贤镇"),("大兴区","榆垡镇"),("大兴区","庞各庄镇"),("大兴区","北臧村镇"),
    ("大兴区","魏善庄镇"),("大兴区","长子营镇"),
    # 怀柔区 2街道+12镇+2民族乡
    ("怀柔区","泉河街道"),("怀柔区","龙山街道"),
    ("怀柔区","怀柔镇"),("怀柔区","雁栖镇"),("怀柔区","庙城镇"),("怀柔区","北房镇"),
    ("怀柔区","杨宋镇"),("怀柔区","桥梓镇"),("怀柔区","怀北镇"),("怀柔区","汤河口镇"),
    ("怀柔区","渤海镇"),("怀柔区","九渡河镇"),("怀柔区","琉璃庙镇"),("怀柔区","宝山镇"),
    ("怀柔区","长哨营满族乡"),("怀柔区","喇叭沟门满族乡"),
    # 平谷区 2街道+14镇+2乡
    ("平谷区","滨河街道"),("平谷区","兴谷街道"),
    ("平谷区","平谷镇"),("平谷区","峪口镇"),("平谷区","马坊镇"),("平谷区","金海湖镇"),
    ("平谷区","东高村镇"),("平谷区","山东庄镇"),("平谷区","南独乐河镇"),("平谷区","大华山镇"),
    ("平谷区","夏各庄镇"),("平谷区","马昌营镇"),("平谷区","王辛庄镇"),("平谷区","大兴庄镇"),
    ("平谷区","刘家店镇"),("平谷区","镇罗营镇"),
    ("平谷区","黄松峪乡"),("平谷区","熊儿寨乡"),
    # 密云区 2街道+17镇+1民族乡
    ("密云区","鼓楼街道"),("密云区","果园街道"),
    ("密云区","密云镇"),("密云区","溪翁庄镇"),("密云区","西田各庄镇"),("密云区","十里堡镇"),
    ("密云区","河南寨镇"),("密云区","巨各庄镇"),("密云区","穆家峪镇"),("密云区","太师屯镇"),
    ("密云区","高岭镇"),("密云区","不老屯镇"),("密云区","冯家峪镇"),("密云区","古北口镇"),
    ("密云区","大城子镇"),("密云区","东邵渠镇"),("密云区","北庄镇"),("密云区","新城子镇"),
    ("密云区","石城镇"),("密云区","檀营满族蒙古族乡"),
    # 延庆区 3街道+11镇+4乡
    ("延庆区","百泉街道"),("延庆区","香水园街道"),("延庆区","儒林街道"),
    ("延庆区","延庆镇"),("延庆区","康庄镇"),("延庆区","八达岭镇"),("延庆区","永宁镇"),
    ("延庆区","旧县镇"),("延庆区","张山营镇"),("延庆区","四海镇"),("延庆区","千家店镇"),
    ("延庆区","沈家营镇"),("延庆区","大榆树镇"),("延庆区","井庄镇"),
    ("延庆区","大庄科乡"),("延庆区","刘斌堡乡"),("延庆区","香营乡"),("延庆区","珍珠泉乡"),
]

def to_slug(name):
    """将中文名转为拼音URL slug，去掉'街道'/'镇'/'乡'后缀"""
    clean = name.replace("街道","").replace("回族乡","").replace("满族乡","").replace("满族蒙古族乡","").replace("乡","").replace("镇","")
    return "".join(lazy_pinyin(clean))

# 区域名次级关键词
area_keywords = {
    "街道": ["小区","写字楼","商场","学校","医院","地铁站"],
    "镇": ["小区","村庄","工业园","学校","医院"],
    "乡": ["小区","村庄","学校"],
}

def get_area_type(name):
    if "街道" in name: return "街道"
    if "镇" in name: return "镇"
    return "乡"

def get_nearby_areas(district, current_name, count=5):
    """获取同区的其他区域名作为相关推荐"""
    same_district = [n for d,n in areas if d==district and n!=current_name]
    return same_district[:count]

def generate_html(district, name, slug):
    """生成单篇SEO文章HTML"""
    area_type = get_area_type(name)
    short_name = name.replace("街道","").replace("回族乡","").replace("满族乡","").replace("满族蒙古族乡","").replace("乡","").replace("镇","")
    nearby = get_nearby_areas(district, name)
    nearby_text = " · ".join(n[:4] for n in nearby) if nearby else district

    keywords = f"{name}开锁,{name}开锁电话,{name}开锁公司,{name}换锁芯,{name}配钥匙,{district}开锁,北京开锁,北京京迅开锁"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}开锁|{name}开锁公司 24小时上门 15501023797</title>
    <meta name="description" content="{name}开锁服务，24小时快速上门。{district}{name}开锁、换锁芯、配钥匙、汽车开锁、保险柜开锁，电话15501023797，{short_name}附近最快15分钟到达。">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://kaisuo.me/posts/{slug}.html">
    <meta name="baidu-site-verification" content="codeva-syDQl346cg" />
    <style>
        :root {{--primary:#1a2a4a;--accent:#d4a843;--bg:#f8f9fa;--white:#fff;--text:#333;--text-light:#666;--shadow:0 4px 20px rgba(0,0,0,0.08);}}
        *{{margin:0;padding:0;box-sizing:border-box;}}
        body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",Arial,sans-serif;color:var(--text);background:var(--bg);line-height:1.8;-webkit-font-smoothing:antialiased;}}
        .breadcrumb{{max-width:800px;margin:0 auto;padding:20px 20px 0;font-size:14px;color:var(--text-light);}}
        .breadcrumb a{{color:var(--accent);text-decoration:none;}}
        .breadcrumb a:hover{{text-decoration:underline;}}
        .article-container{{max-width:800px;margin:20px auto 60px;padding:40px;background:var(--white);border-radius:12px;box-shadow:var(--shadow);}}
        @media(max-width:768px){{.article-container{{margin:10px 10px 40px;padding:24px 18px;}}}}
        .article-header{{border-bottom:2px solid #f0f0f0;padding-bottom:20px;margin-bottom:24px;}}
        .article-header h1{{font-size:26px;font-weight:800;color:var(--primary);line-height:1.4;margin-bottom:12px;}}
        .article-meta{{font-size:13px;color:var(--text-light);display:flex;gap:16px;flex-wrap:wrap;}}
        .article-content h2{{font-size:20px;font-weight:700;color:var(--primary);margin:28px 0 12px;padding-left:12px;border-left:4px solid var(--accent);}}
        .article-content h3{{font-size:17px;font-weight:700;color:var(--primary);margin:24px 0 10px;}}
        .article-content p{{margin-bottom:14px;font-size:15px;color:var(--text);}}
        .article-content ul{{margin:10px 0 18px 20px;}}
        .article-content li{{margin-bottom:6px;font-size:15px;}}
        .call-card{{background:linear-gradient(135deg,var(--primary),#0d1b33);color:white;border-radius:10px;padding:24px;text-align:center;margin:30px 0;}}
        .call-card .label{{font-size:13px;color:rgba(255,255,255,0.7);}}
        .call-card .phone{{font-size:28px;font-weight:800;color:var(--accent);letter-spacing:2px;margin:8px 0;}}
        .call-card .btn{{display:inline-block;background:var(--accent);color:white;text-decoration:none;padding:12px 36px;border-radius:50px;font-size:16px;font-weight:700;margin-top:10px;transition:all 0.3s;}}
        .call-card .btn:hover{{background:#c49638;}}
        .service-footer{{background:#f0f4f8;border-radius:8px;padding:20px 24px;margin-top:30px;}}
        .service-footer h3{{font-size:16px;color:var(--primary);margin-bottom:10px;}}
        .service-footer ul{{columns:2;}}
        @media(max-width:480px){{.service-footer ul{{columns:1;}}}}
        .service-footer li{{font-size:14px;margin-bottom:4px;}}
        .related-areas{{margin-top:24px;padding:16px;background:#f8f9fa;border-radius:8px;}}
        .related-areas a{{display:inline-block;margin:4px 6px;padding:4px 12px;background:white;border:1px solid #e0e0e0;border-radius:20px;font-size:13px;color:var(--text-light);text-decoration:none;transition:all 0.2s;}}
        .related-areas a:hover{{border-color:var(--accent);color:var(--accent);}}
        .float-call{{position:fixed;bottom:24px;right:20px;z-index:9999;width:56px;height:56px;border-radius:50%;background:var(--accent);color:white;box-shadow:0 6px 24px rgba(212,168,67,0.5);display:flex;align-items:center;justify-content:center;font-size:26px;text-decoration:none;animation:pulse 2s infinite;}}
        @media(min-width:769px){{.float-call{{display:none;}}}}
        @keyframes pulse{{0%{{box-shadow:0 0 0 0 rgba(212,168,67,0.5);}}70%{{box-shadow:0 0 0 16px rgba(212,168,67,0);}}100%{{box-shadow:0 0 0 0 rgba(212,168,67,0);}}}}
    </style>
</head>
<body>
    <div class="breadcrumb">
        <a href="../index.html">🏠 北京京迅开锁</a> &raquo; <a href="../articles.html">服务区域</a> &raquo; <span>{name}开锁</span>
    </div>

    <article class="article-container">
        <div class="article-header">
            <h1>{name}开锁 — 24小时上门开锁换锁芯</h1>
            <div class="article-meta">
                <span>📞 15501023797 / 010-83879827</span>
                <span>📍 {district}·{name}</span>
                <span>🕐 24小时服务</span>
            </div>
        </div>

        <div class="call-card">
            <div class="label">📞 {name}开锁服务热线</div>
            <div class="phone">15501023797</div>
            <div>座机：010-83879827 · 北京京迅开锁 · 公安备案 · 最快15分钟上门</div>
            <a href="tel:15501023797" class="btn">📞 立即拨打电话</a>
        </div>

        <div class="article-content">
            <h2>{name}开锁 — {district}快速上门服务</h2>
            <p>北京京迅开锁在<strong>{district}{name}</strong>提供专业开锁服务。{short_name}{area_type}的居民和商户，无论您是钥匙忘在家里、锁芯损坏、还是需要更换智能锁，我们都能快速到达现场为您解决。</p>
            <p>我们在{district}设有服务网点，覆盖{name}及周边{nearby_text}等区域，24小时随叫随到，最快15分钟上门服务。</p>

            <h3>{name}开锁服务范围</h3>
            <p>{name}各小区、写字楼、商铺、学校、医院等场所，均可提供上门开锁服务。服务覆盖{short_name}全部区域及周边地带。</p>

            <h3>{name}开锁服务项目</h3>
            <ul>
                <li>住宅开锁 — 防盗门、室内门、推拉门等各类门锁开启</li>
                <li>写字楼开锁 — 办公室门锁、玻璃门锁、文件柜锁</li>
                <li>汽车开锁 — 全品牌车型钥匙锁车内应急开锁</li>
                <li>保险柜开锁 — 机械/电子/指纹保险柜无损开启</li>
                <li>换锁芯 — A级/B级/C级锁芯更换升级</li>
                <li>配钥匙 — 门钥匙、车钥匙、保险柜钥匙配制</li>
                <li>智能锁安装 — 指纹锁、人脸识别锁、密码锁安装维修</li>
            </ul>

            <h2>为什么选择北京京迅开锁？</h2>
            <ul>
                <li><strong>公安备案：</strong>已在公安机关完成特种行业备案，正规经营，身份可查</li>
                <li><strong>快速上门：</strong>{district}各{area_type}均设服务点，{name}最快15分钟到达</li>
                <li><strong>技术开锁：</strong>专业工具无损开锁，不破坏原有锁具，减少损失</li>
                <li><strong>价格透明：</strong>上门前明确报价，无隐形消费，无坐地起价</li>
                <li><strong>售后保障：</strong>换锁芯、智能锁安装享售后保修服务</li>
                <li><strong>全天服务：</strong>24小时电话畅通，深夜、节假日照常上门</li>
            </ul>

            <h2>{name}开锁常见问题</h2>
            <h3>钥匙忘在家里怎么办？</h3>
            <p>别着急，拨打<strong>15501023797</strong>，我们技术人员携带专业工具快速到达{name}，技术开锁不破坏门锁，开门后您原有的钥匙仍可正常使用。</p>
            <h3>锁芯坏了能修吗？</h3>
            <p>锁芯损坏建议直接更换新的锁芯，我们提供A/B/C级锁芯更换服务，{name}上门更换，现场完成，换完即用。</p>
            <h3>深夜能上门开锁吗？</h3>
            <p>可以！我们是24小时服务，无论多晚，只要您在{name}需要开锁，拨打15501023797，我们随时出发。</p>
        </div>

        <div class="related-areas">
            <h3 style="font-size:15px;color:var(--primary);margin-bottom:8px;">📍 {district}其他区域开锁服务</h3>
            {''.join(f'<a href="{to_slug(n)}.html">{n.replace("街道","").replace("回族乡","").replace("满族乡","").replace("满族蒙古族乡","").replace("乡","").replace("镇","")}开锁</a>' for n in nearby)}
        </div>

        <div class="service-footer">
            <h3>🔧 北京京迅开锁 — 全北京服务项目</h3>
            <ul>
                <li>🔐 住宅开锁（防盗门/室内门）</li>
                <li>🚗 汽车开锁（全品牌车型）</li>
                <li>🗄️ 保险柜开锁（机械/电子/指纹）</li>
                <li>🔧 换锁芯（A/B/C级锁芯）</li>
                <li>🔑 配钥匙（门钥匙/车钥匙）</li>
                <li>🤖 智能锁安装（指纹/人脸/密码）</li>
            </ul>
        </div>
    </article>

    <a href="tel:15501023797" class="float-call">📞</a>
</body>
</html>"""
    return html

# ============ 主程序 ============
output_dir = r"d:\Software\Workspace\Lock AD\posts"
os.makedirs(output_dir, exist_ok=True)

generated = []
slug_counts = {}

for district, name in areas:
    slug = to_slug(name)
    # 处理重名slug
    if slug in slug_counts:
        slug_counts[slug] += 1
        slug = f"{slug}{slug_counts[slug]}"
    else:
        slug_counts[slug] = 1

    html = generate_html(district, name, slug)
    filepath = os.path.join(output_dir, f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    generated.append((district, name, slug))

print(f"Done! Generated {len(generated)} articles")

# 生成 sitemap 条目
sitemap_entries = []
for district, name, slug in generated:
    sitemap_entries.append(f'    <url><loc>https://kaisuo.me/posts/{slug}.html</loc><priority>0.8</priority><changefreq>monthly</changefreq></url>')

# 保存 sitemap URL 列表
with open(r"d:\Software\Workspace\Lock AD\promotion\all-sitemap-urls.txt", "w", encoding="utf-8") as f:
    f.write("https://kaisuo.me/\n")
    f.write("https://kaisuo.me/articles.html\n")
    for district, name, slug in generated:
        f.write(f"https://kaisuo.me/posts/{slug}.html\n")

# 保存 slug 映射
with open(r"d:\Software\Workspace\Lock AD\promotion\area-slugs.csv", "w", encoding="utf-8") as f:
    f.write("district,name,slug,url\n")
    for district, name, slug in generated:
        f.write(f"{district},{name},{slug},https://kaisuo.me/posts/{slug}.html\n")

# 按区统计
from collections import Counter
district_counts = Counter(d for d,n,s in generated)
print("\nDistrict counts:")
for d, c in sorted(district_counts.items()):
    print(f"  {d}: {c}")

print(f"\nAll URLs saved to promotion/all-sitemap-urls.txt")
print(f"Slug mapping saved to promotion/area-slugs.csv")

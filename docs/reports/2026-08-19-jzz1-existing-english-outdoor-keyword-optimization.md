# JZZ1 现有英文户外关键词优化记录

日期：2026-08-19

适用站点：`https://www.jzz1.com/`

## 1. 本轮范围

本轮只优化网站当前已有的英文产品路线和关键词，不新增西班牙语页面、葡萄牙语页面、城市页或新的产品能力。URL、语言结构、询盘方式和视觉布局保持不变。

## 2. 页面关键词分工

| 页面 | 主关键词方向 | 已有辅助方向 | 页面职责 |
| --- | --- | --- | --- |
| `products/railings.html` | `aluminum railing supplier` | `aluminum balcony railings supplier`、`balcony railing systems`、`stair railings`、`aluminum railings for apartment projects` | 阳台、楼梯、露台、甲板和项目护栏总入口 |
| `products/aluminum-garden-fences.html` | `aluminum garden fence supplier` | `aluminum garden fences`、`aluminum fence panels`、`villa`、`residential`、`perimeter`、`matching gate` | 花园围栏、庭院围栏和边界围栏 |
| `products/aluminum-garden-gates.html` | `aluminum garden gate supplier` | `pedestrian gates`、`matching fence systems`、`drawing-based openings`、`hardware` | 花园行人门和围栏配套门 |
| `products/outdoor-aluminum-gates.html` | `outdoor aluminum gates supplier` | `aluminum driveway gates`、`villa entrance gates`、`perimeter gates`、`custom aluminum gates by drawing` | 车道门、别墅入口门和项目外围门 |
| `products/outdoor-aluminum-systems.html` | `outdoor aluminum systems supplier` | `railings`、`garden fences`、`garden gates`、`project gate systems` | 户外围护系统总入口和产品分流页 |

## 3. 已实施内容

- 更新五个现有英文户外页面的 Title 和 Meta Description。
- 同步更新 Open Graph 标题和描述。
- 在首段中自然补足 supplier、project、drawing-based quotation、driveway、villa entrance、pedestrian 等已有采购意图词。
- 将护栏页的关键词说明改为自然的供应商采购路线文案，减少关键词清单感。
- 将户外大门页的搜索意图列表改为自然的 sourcing route 文案，明确车道门与花园行人门的页面边界。
- 在户外系统总页增加通往 `outdoor-aluminum-gates.html` 的已有产品内链。
- 更新五个页面在 `sitemap.xml` 中的 `lastmod` 为 `2026-08-19`。

## 4. 明确未做事项

- 未新增西班牙语或葡萄牙语页面。
- 未新增 `hreflang`，因为当前站点没有对应语言版本。
- 未新增城市页或 Google 地图落地页。
- 未加入自动门、电动门、泳池围栏等未确认能力。
- 未修改现有 URL、图片目录、主导航或询盘后端。

## 5. 验证结果

已通过：

```bash
xmllint --noout sitemap.xml
bash scripts/privacy-scan.sh
bash scripts/verify-outdoor-systems.sh
git diff --check
```

专项脚本覆盖修改页的唯一 H1、robots、canonical、Product/Breadcrumb/FAQ 结构化数据、询盘入口、图片、站内路由和 sitemap；仓库根目录实际存在 `robots.txt` 和 `sitemap.xml`，且 XML 校验及隐私扫描均通过。

浏览器验证应覆盖首页、五个修改页面的桌面端和 390px 移动端，重点确认标题、图片、询盘链接、控制台和横向溢出。

## 6. 回滚记录

本轮修改前已生成 Git bundle 备份，具体本机路径保存在私有运维索引中。公开仓库只记录本报告和最终提交，不记录本机私有绝对路径。

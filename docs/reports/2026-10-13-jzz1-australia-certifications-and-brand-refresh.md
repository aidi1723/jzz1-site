# JZZ1 国际认证（澳标 AS 2047 & 玻璃 AS/NZS 2208）部署、视觉升级与全站维护记录

日期：2026-10-13  
适用站点：`https://www.jzz1.com/` (Jinan Jingzao New Materials Co., Ltd. / JZZ1 佛山系统门窗出口制造工厂)  
负责模块：国际资质数字化、区域市场 SEO/GEO、首页视觉优化、新 Logo 升级与生产环境发布  

---

## 1. 任务背景与核心目标

根据用户需求与电脑桌面提供的真实认证凭据，完成以下核心目标：
1. **澳标门窗权威认证**：`AS 2047:2014`（Windows and external glazed doors in buildings）—— Intertek SAI Global StandardsMark Licence（编号：`SMK41678`），涵盖 MD75S 与 MD76A 两大系统；
2. **澳新建筑安全玻璃认证**：`AS/NZS 2208:1996`（含修正案 1）—— CSi PAS-Mark 认证（编号：`7632`，JAS-ANZ / IAF MLA 认可，已采用防扫码/防窜货安全保护版）；
3. **SEO / GEO 深度优化**：建立高权重独立市场门户，贯通大模型（AIO/LLMs）事实源，确保海外买家与 AI 搜索引擎精准抓取与采信；
4. **品牌与视觉全面焕新**：替换原有杂乱的半成品车间主图，上线极简顶奢现代海景别墅实景图；将全站 Logo 统一更换为香槟金几何“JZ”新标识及全套 Favicon。

---

## 2. 实施范围与产物清单

### 2.1 凭证资产数字化（防扫码与版权保护）
- 目标路径：`images/certificates/`
- 生成资产：
  - `as2047-standardsmark-licence-p1.webp` (174 KB) / `as2047-standardsmark-licence-p1-600.webp` (53 KB) + `.jpg`（SAI Global 证书首页）
  - `as2047-schedule-md75s-md76a-p2.webp` (147 KB) / `as2047-schedule-md75s-md76a-p2-600.webp` (45 KB) + `.jpg`（产品附表与测试尺寸）
  - `as-nzs-2208-safety-glazing-csi.webp` (75 KB) / `as-nzs-2208-safety-glazing-csi-600.webp` (44 KB) + `.jpg`（CSi 安全玻璃证书，防扫码版）

### 2.2 页面架构与视觉体系升级
- **`certificates.html`**：
  - 从纯文字列表重构为三卡片官方认证展厅，支持点击弹出 Lightbox 高清大图；
  - 嵌入 AS 2047 官方实测参数表（MD75S 极限风压 4000 Pa、水密 600 Pa；MD76A 极限风压 3000 Pa、水密 200 Pa）；
  - 增设“申请完整未脱敏测试报告与图纸”高意向转化按钮。
- **新建 `australia.html`**：
  - 专为澳大利亚与新西兰工程总包、门窗批发商打造的独立国家级采购门户；
  - 全面解析 NCC / BCA 建筑规范风压等级（N1–N5 非台风区、C1–C2 台风区）；
  - 丛林火灾防护等级（BAL-12.5 至 BAL-40）与 WERS 节能配置说明；
  - 远洋长途海运 5 重包装方案（钢带加固免熏蒸胶合板木箱）；
  - 澳洲专属快速询盘 RFQ 表单与右下角智能悬浮联系底栏。
- **`index.html`**：
  - 顶部主导航新增 `Australia` 与 `Certificates` 直达入口；
  - 首屏 Trust Pills 新增 `AS 2047 & AS/NZS 2208 Certified`；
  - Priority Markets 第一位提升为 Australia & New Zealand；
  - 替换 Hero 视觉图为顶奢海景独栋别墅实景图（大跨度断桥铝提升推拉门与落地固定玻璃幕墙）。
- **`products/windows.html`、`technical-standards.html`、`knowledge-base/`**：
  - 在产品列表、技术标准总表及澳洲采购指南中注入真实许可证编号与内链拓扑。

### 2.3 GEO / AIO 生成式搜索引擎与知识图谱升级
- **`llms.txt` & `llms-full.txt`**：写入发证机构（Intertek SAI Global、CSi）、许可证编号（SMK41678、7632）、物理实测压力值与海运防护规范；
- **`brand-facts.json`**：知识图谱中 `areaServed` 增加 Australia 与 New Zealand，定义 `hasCredential` 官方认证对象；
- **`sitemap.xml` & `sitemap.html`**：新增 `australia.html`（权重 0.9），更新各相关页面 `lastmod` 为 `2026-10-13`。

### 2.4 新 Logo 规范与品牌全案部署
- **设计原型**：香槟金几何线框“JZ”一体化字母交织设计，呈现高端铝挤压型材断面美感；
- **全套资产生成**：
  - `images/assets/logo.svg` / `images/logo.svg`：全站 Header 矢量主 Logo（深空灰微质感圆角底板 + 香槟金立体徽标）；
  - `images/assets/og-logo.svg` / `images/og-logo.svg`：1200×630 社交分享宽屏卡片，内嵌认证徽章；
  - `images/assets/logo-badge-512.png`：512×512 高清母版；
  - `images/assets/logo-mark-transparent.png`：透明背景免扣图母版；
  - `images/assets/apple-touch-icon.png` (180×180)、`favicon-48.png`、`favicon-32.png`、`favicon.ico`：全尺寸浏览器标签与系统图标；
- **样式统一**：在 `css/site.css` 与 `css/product.css` 中规范 `.brand img` 圆角与 `.brand strong` 字体字阶。

---

## 3. 安全备份机制

在正式部署推送前执行了双重完备备份：
1. **Git 远程与本地 Tag 备份**：
   - 标签：`backup-pre-australia-cert-20261013`
   - 指向上一稳定版本：`1185d22`
   - 已同步推至 GitHub 远端仓库。
2. **本地独立物理压缩包备份**：
   - 路径：`/Volumes/MacSSD/项目开发/网站/backups/jzz1-site-backup-pre-australia-cert-20261013.tar.gz` (65 MB 全站快照)。

---

## 4. 生产环境构建与发布记录

| 提交哈希 (Commit) | 说明 | GitHub Pages 工作流 ID | 线上分发状态 |
| :--- | :--- | :---: | :---: |
| `d7e92aa` | 澳标 AS 2047 / AS/NZS 2208 体系、落地页与 SEO/GEO 深度部署 | `38339094539` | **Success** (已分发) |
| `ba4fa24` | 首页 Hero 主图替换为顶奢现代极简海景别墅实景图 | `38340147663` | **Success** (已分发) |
| `419f8e8` | 全站 Logo、Favicon 及 OpenGraph 视觉换新为香槟金“JZ”徽标 | `38361763262` | **Success** (已分发) |

---

## 5. 线上验证与健康检查 (HTTP 200 OK)

线上各核心端点已完成抽样校验，均返回有效 200 OK 响应：
- `https://www.jzz1.com/` (39.9 KB, HTTP 200)
- `https://www.jzz1.com/australia.html` (28.3 KB, HTTP 200)
- `https://www.jzz1.com/certificates.html` (25.8 KB, HTTP 200)
- `https://www.jzz1.com/images/assets/logo.svg` (119 KB, HTTP 200)
- `https://www.jzz1.com/images/assets/og-logo.svg` (435 KB, HTTP 200)
- `https://www.jzz1.com/images/assets/favicon-32.png` (2.6 KB, HTTP 200)
- `https://www.jzz1.com/images/site-refresh/hero-project.webp` (187 KB, HTTP 200)
- `https://www.jzz1.com/images/certificates/as2047-standardsmark-licence-p1.webp` (178 KB, HTTP 200)
- `https://www.jzz1.com/llms-full.txt` (9.7 KB, HTTP 200)
- `https://www.jzz1.com/brand-facts.json` (3.2 KB, HTTP 200)
- `https://www.jzz1.com/sitemap.xml` (20.8 KB, HTTP 200)

---

## 6. 后续维护建议

1. **外链与社交平台分发**：可在 LinkedIn、Facebook 国际主页发布包含 `https://www.jzz1.com/australia.html` 的帖子，自动触发新 `og-logo.svg` 与澳标认证富文本卡片；
2. **Google Search Console 提交通知**：进入 GSC 后台对 `sitemap.xml` 执行重新抓取请求，加速 Google 对新页面 `/australia.html` 与更新后证书页面的收录；
3. **询盘日常监控**：确保 WhatsApp (+86 135 6267 6792) 与企业邮箱 (info@jzz1.com / export@jzz1.com) 接收畅通。

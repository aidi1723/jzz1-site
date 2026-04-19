# JZZ1 SEO / GEO 运营手册 2026

这份文件是 `www.jzz1.com` 的 SEO / GEO 实操手册，目标不是写理论，而是让团队每周都能按照同一套规则做页面、做内链、做校验、做复盘。

## 1. 当前站点策略

### 域名与索引规则

- 统一使用 `https://www.jzz1.com/` 作为 canonical 域名
- 不再把裸域或其他别名当成独立 SEO 目标
- 一个搜索意图只对应一个主页面
- 低价值、重复、仅导航用途页面，必要时使用 `noindex,follow`

### 当前有效的页面类型

- 核心产品页：`products/`
- 采购 Guide：`guides/`
- 技术问答 / 参数页：`knowledge-base/`
- 国家/市场页：`singapore.html`、`malaysia.html`、`indonesia.html`
- 信任/标准页：`technical-standards.html`、`certificates.html`
- Hub 页：首页、`guides/`、`knowledge-base/`、`sitemap.html`

### 当前主线

- 第一梯队市场优先：`Singapore`、`Malaysia`、`Indonesia`
- 用买家采购意图驱动，而不是只追求泛大词
- 用参数、FAQ、标准、场景化内容增加页面“可引用性”
- 让首页、产品页、市场页、Guide、Knowledge Base 形成闭环内链

### 当前产品覆盖

- 门窗主线：windows / doors / entrance doors / thermal break / sliding / casement
- 型材主线：aluminum profiles / custom extrusion / powder coated profiles / upvc profiles
- 户外围护：railings / balcony railings / sunrooms
- 扩展产品：curtain wall systems / outdoor aluminum gates
- 系统支撑：glass / gasket / hardware / OEM / custom tooling / packing labels

## 2. 权威数据与工具栈

### 官方绝对权威

#### Google Search Console

用途：

- 看收录
- 看查询词
- 看国家分布
- 看页面曝光 / 点击 / 平均排名

要求：

- 网站上线后必须绑定
- 每次新增页面后提交 `sitemap.xml`
- 每周复盘一次 `Queries`、`Pages`、`Countries`

#### Google Lighthouse / Lighthouse CI

用途：

- Core Web Vitals
- 技术 SEO 健康度
- 页面可访问性与性能基线

要求：

- 发布前至少手动跑一次关键页
- 如后续接 CI，可把 SEO 分数和 Performance 分数纳入上线门槛

### 行业标准工具

#### Ahrefs / SEMrush

用途：

- 竞品关键词
- 外链机会
- 国家级别词库补充

原则：

- 有采购条件就接入
- 没采购前，不把它们当唯一决策来源

#### Screaming Frog

用途：

- 全站技术巡检
- 死链、标题重复、重定向链、缺失 Meta

频率：

- 每月做一次技术审计

## 3. 页面设计规则

### 产品页模板

每个核心产品页应包含：

1. 明确采购对象和应用场景
2. 技术参数表
3. 可选配置或表面处理
4. FAQ 区块
5. FAQ Schema
6. 指向 Guide / 市场页 / 标准页的内链

补充原则：

- 如果关键词代表完整采购对象，例如 `curtain wall systems`、`outdoor aluminum gates`、`custom aluminum extrusion profiles`，优先做独立产品页。
- 如果关键词更像系统支撑项，例如 `glass`、`gasket`、`hardware`、`oem labels`，优先做 Knowledge Base 或 FAQ 支撑页，再回链到产品页。

### Guide 页模板

Guide 页优先承接以下类型的搜索意图：

- `product + scenario`
- `country + product + scenario`
- `problem + solution`
- `standard + scenario`

建议结构：

1. 主问题开场
2. 当地项目条件 / 采购约束
3. 推荐配置逻辑
4. 参数表或 RFQ checklist
5. FAQ
6. 指向产品页或联系页的 CTA

### Knowledge Base 页模板

Knowledge Base 更适合做：

- 技术型问答
- 采购检查清单
- 参数对照
- AI 搜索更容易引用的直接答案页

建议结构：

1. 先给直接答案
2. 6-10 个短问答
3. 参数表或对比表
4. 指向产品页 / 市场页的回链

## 4. 第一梯队市场规则

### Singapore

重点方向：

- acoustic
- Green Mark / BCA 类讨论
- condo / high-rise
- slim-frame / minimalist systems

### Malaysia

重点方向：

- hospitality
- hotel balcony doors
- tropical glazing
- mixed-use / commercial supply

### Indonesia

重点方向：

- tropical climate
- coastal durability
- apartment / hotel balcony doors
- mixed package RFQ

### 第二梯队

- `Philippines`
- `Vietnam`
- `Thailand`

### 第三梯队

- `Australia`
- `USA / Canada`
- `Europe`

第三梯队不是不做，而是先用标准页和长尾页承接，不作为 Q2 首页主线。

## 5. 内链规则

- 每个新 Guide 至少链接回 1 个产品页
- 每个产品页至少链接到 2 个对应 Guide 或市场页
- 市场页必须链接到：
  - 产品页
  - Guide
  - Knowledge Base
  - Technical Standards
- `sitemap.html` 和 `sitemap.xml` 是强制更新项，不是可选项
- Anchor text 保持自然，不要机械重复完全相同关键词

## 6. 结构化数据规则

### 产品页

- 可用 `Product` schema
- 有可见 FAQ 时再上 `FAQPage`
- Schema 内容必须和页面可见内容一致

### Guide / FAQ 页

- 有真实可见问答再上 `FAQPage`
- 不做虚假评分、虚假评论类结构化数据
- 优先做技术、参数、采购流程相关内容

### 系统支撑词规则

- `glass`、`gasket`、`hardware`、`tooling`、`OEM packing` 这类词，不要全部拆成独立产品页。
- 优先用：
  - `Knowledge Base` 做规格解释
  - `Guide` 做采购流程
  - `Product` 页做最终承接和询盘转化
- 这样更符合真实采购路径，也更容易避免低质量泛流量。

### 主词 + 配件词组合规则

- 高价值组合，优先遵循以下公式：
  - `主产品词 + 影响报价的规格词`
  - `主产品词 + 影响性能的部件词`
  - `主产品词 + 影响执行交付的 OEM / packing / tooling 词`
- 推荐示例：
  - `aluminum windows with low-e glass`
  - `thermal break aluminum windows with epdm gasket`
  - `aluminum doors with laminated glass and hardware`
  - `custom aluminum profiles with gasket groove`
  - `oem aluminum windows with project labels`
  - `custom tooling for aluminum window and door profiles`
- 不推荐：
  - 只有配件名、没有采购对象的词
  - 词虽然长，但不符合真实 RFQ 逻辑的词
  - 无法自然落入正文、FAQ、参数表的堆词组合

## 7. 每周运行节奏

### 周一

- 看 GSC 的 Queries / Pages / Countries
- 记录本周主推关键词
- 决定本周要改哪个产品页、加哪个 Guide、补哪个 Knowledge Base

### 周二

- 写页面 brief
- 确认主关键词、页面意图、内链来源页

### 周三

- 完成正文、FAQ、参数表、Meta、Schema

### 周四

- 补内链
- 更新 `sitemap.html` 和 `sitemap.xml`
- 过 Lighthouse / 技术检查

### 周五

- 发布
- 在 GSC 请求抓取
- 记录本周改了哪些页面
- 生成下一周候选关键词

详见：

- `seo/weekly-website-optimization-plan-2026-q2.md`
- `seo/weekly-tasks/2026-04-19-week-1-priority-market-sprint.md`

## 8. 发布前检查清单

每个页面上线前必须检查：

- Title 唯一
- Meta Description 唯一
- Canonical 正确
- 只有 1 个 H1
- Robots 设置正确
- 页面可从 Hub 或相关页被正常发现
- FAQ 可见内容和 FAQ Schema 一致
- 工程类页面有参数表或 checklist
- 已加入 `sitemap.html`
- 已加入 `sitemap.xml`

## 9. 本地校验命令

从发布仓库运行：

```bash
git status --short
xmllint --noout sitemap.xml
git diff --check
```

如果以后接 CI，可以额外加入：

```bash
lighthouse https://www.jzz1.com/ --only-categories=performance,seo,accessibility
```

## 10. 相关文件

- `seo/keyword-roadmap-2026-q2.md`
- `seo/product-weekly-longtail-matrix-2026-q2.md`
- `seo/priority-market-execution-roadmap-2026-q2.md`
- `seo/weekly-website-optimization-plan-2026-q2.md`

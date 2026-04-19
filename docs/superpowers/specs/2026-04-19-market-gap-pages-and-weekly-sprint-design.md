# 市场缺口页与 Week 2 执行批次设计

## 背景

第一梯队市场 `Singapore`、`Malaysia`、`Indonesia` 已经具备市场页、Guide、Knowledge Base 的基础结构，但仍有 3 类明显缺口：

- 新加坡还缺一个直接回答阳台门声学参数与 RFQ 输入的 `Knowledge Base` 页面
- 马来西亚还缺一个更偏商用采购和 mixed opening RFQ 的 `Guide`
- 印度尼西亚还缺一个更聚焦 apartment package 与 mixed window-door RFQ 的 `Guide`

同时，项目里已经有周度 SEO 执行体系，但还需要把这一批的落地动作写成可复用的周任务文件，便于后续按周推进。

## 目标

- 新增 3 个缺口页，分别承接新加坡、马来西亚、印度尼西亚的下一层采购型长尾词
- 把新页面接入市场页、产品页、Guides Hub、Knowledge Base Hub 与 sitemap
- 在项目中新增本周执行文件，形成“路线图 -> 周计划 -> 本周任务”的闭环

## 本批交付

### 页面

- `knowledge-base/singapore-balcony-door-acoustic-spec-checklist.html`
- `guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html`
- `guides/indonesia-apartment-window-package-rfq-guide.html`

### 文档

- `docs/superpowers/plans/2026-04-19-market-gap-pages-and-weekly-sprint.md`
- `seo/weekly-tasks/2026-04-19-week-2-market-gap-pages.md`

### 站内结构更新

- 市场页：`singapore.html`、`malaysia.html`、`indonesia.html`
- 产品页：`products/windows.html`、`products/doors.html`
- Guide / KB 页面：补强对应 related links
- Hub：`guides/index.html`、`knowledge-base/index.html`
- 发现入口：`sitemap.html`、`sitemap.xml`
- 规划文档：`seo/priority-market-execution-roadmap-2026-q2.md`、`seo/keyword-roadmap-2026-q2.md`、`seo/weekly-website-optimization-plan-2026-q2.md`

## 关键词与页面映射

### Singapore

- 主词：
  - `singapore balcony door acoustic spec checklist`
  - `singapore balcony door supplier`
  - `singapore minimalist sliding doors`
- 页面角色：
  - 用 `Knowledge Base` 形式承接 direct-answer 与 checklist 型搜索意图
  - 由 `singapore.html` 与 `guides/singapore-acoustic-sliding-doors-for-condo-projects.html` 导流

### Malaysia

- 主词：
  - `malaysia commercial windows supplier`
  - `malaysia balcony door supplier`
  - `malaysia hotel window and door supplier`
  - `malaysia tropical coastal windows`
- 页面角色：
  - 用 `Guide` 形式承接 commercial / hospitality / mixed-use 项目的 RFQ 场景
  - 由 `malaysia.html`、`products/windows.html`、`products/doors.html`、现有 Malaysia hotel guide 导流

### Indonesia

- 主词：
  - `indonesia aluminum windows for apartments`
  - `indonesia apartment window package`
  - `indonesia mixed window and door rfq`
- 页面角色：
  - 用 `Guide` 形式承接 apartment package、mixed package、window-plus-door 的项目意图
  - 由 `indonesia.html`、`products/windows.html`、现有 Indonesia tropical guide 导流

## 信息架构原则

- 每个新增页面都必须至少有 3 个站内入口，不做孤页
- `Guide` 页面负责承接场景型、采购型、项目型搜索意图
- `Knowledge Base` 页面负责承接 direct-answer、spec table、FAQ、checklist 型搜索意图
- 新页面必须同时进入 HTML sitemap 与 XML sitemap

## 成功标准

- 3 个新页面具备完整的 `title`、`description`、`canonical`、`robots`、结构化数据
- 新页面可以从市场页、产品页或 Hub 页直接进入
- `sitemap.xml` 校验通过
- 本周任务被记录进 `seo/weekly-tasks/`

## 风险与控制

- 风险：页面上线但站内入口不足，形成孤页
  - 控制：同步更新市场页、产品页、Hub、sitemap
- 风险：关键词太泛，偏离当前英文站 B2B/B2P 采购定位
  - 控制：只做带项目、RFQ、spec、supplier、package 意图的长尾词
- 风险：周度任务写了但不能执行
  - 控制：把“已完成、本周待上线后执行、下周建议动作”写成固定模板

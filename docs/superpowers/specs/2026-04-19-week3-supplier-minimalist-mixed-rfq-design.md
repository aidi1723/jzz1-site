# Week 3 Supplier / Minimalist / Mixed-RFQ 设计

## 背景

Week 1 和 Week 2 已经把第一梯队市场的基础页面和第二层缺口页补出来了。下一步不再是继续泛泛铺词，而是进入更接近成交前阶段的三类意图：

- `supplier-intent`
- `minimalist / slim-frame project intent`
- `mixed RFQ / package checklist intent`

这三类意图更贴近真实项目采购，也更适合把流量从市场页和产品页进一步导到更高转化概率的长尾页面。

## 目标

- 新增 3 个 Week 3 页面，分别承接新加坡、马来西亚、印度尼西亚的高价值长尾意图
- 把新页面接进现有市场页、产品页、Guide / Knowledge Base Hub、sitemap 和周任务体系
- 让路线图中的 Week 3 从“建议动作”变成“已执行批次”

## 本批页面

### Singapore

- `guides/singapore-minimalist-sliding-doors-for-condos.html`
- 目标词：
  - `singapore minimalist sliding doors`
  - `singapore balcony door supplier`
  - `singapore slim frame sliding doors`

页面角色：

- 用 `Guide` 承接 supplier-intent + slim-frame/minimalist 搜索意图
- 由 `singapore.html`、`products/sliding-aluminum-windows.html`、`guides/singapore-acoustic-sliding-doors-for-condo-projects.html` 导流

### Malaysia

- `knowledge-base/malaysia-tropical-coastal-window-spec-checklist.html`
- 目标词：
  - `malaysia tropical coastal windows`
  - `malaysia commercial windows supplier`
  - `malaysia hotel window and door supplier`

页面角色：

- 用 `Knowledge Base / checklist` 承接 tropical/coastal/spec-table/direct-answer 搜索意图
- 由 `malaysia.html`、`products/windows.html`、`guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html` 导流

### Indonesia

- `knowledge-base/indonesia-mixed-window-and-door-rfq-checklist.html`
- 目标词：
  - `indonesia mixed window and door rfq`
  - `indonesia mixed window and door rfq checklist`
  - `indonesia commercial window supplier`

页面角色：

- 用 `Knowledge Base / checklist` 承接 mixed package、window-plus-door、RFQ checklist 意图
- 由 `indonesia.html`、`products/windows.html`、`products/doors.html`、`guides/indonesia-apartment-window-package-rfq-guide.html` 导流

## 结构设计

- Singapore 页面偏 `Guide`
  - hero
  - buyer concerns
  - slim-frame supplier checklist
  - RFQ table
  - related pages
- Malaysia 页面偏 `Knowledge Base`
  - direct answer
  - tropical/coastal spec table
  - checklist
  - related pages
- Indonesia 页面偏 `Knowledge Base`
  - direct answer
  - mixed package split table
  - RFQ checklist
  - related pages

## 站内接线

### 市场页

- `singapore.html` 链到新加坡 minimalist sliding guide
- `malaysia.html` 链到马来西亚 tropical/coastal checklist
- `indonesia.html` 链到印尼 mixed RFQ checklist

### 产品页

- `products/sliding-aluminum-windows.html` 链到新加坡 minimalist sliding guide
- `products/windows.html` 链到马来西亚 tropical/coastal checklist 和印尼 mixed RFQ checklist
- `products/doors.html` 链到新加坡 minimalist sliding guide 和印尼 mixed RFQ checklist

### Cluster pages

- `guides/singapore-acoustic-sliding-doors-for-condo-projects.html`
- `guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html`
- `guides/indonesia-apartment-window-package-rfq-guide.html`
- `guides/indonesia-tropical-window-and-balcony-door-sourcing.html`
- `knowledge-base/malaysia-hotel-balcony-door-and-tropical-glazing-faq.html`

### Discovery

- `guides/index.html`
- `knowledge-base/index.html`
- `sitemap.html`
- `sitemap.xml`

## 文档与执行

本批还需要同步更新：

- `seo/priority-market-execution-roadmap-2026-q2.md`
- `seo/keyword-roadmap-2026-q2.md`
- `seo/weekly-website-optimization-plan-2026-q2.md`
- `seo/weekly-tasks/2026-04-19-week-3-supplier-minimalist-mixed-rfq.md`

## 成功标准

- 3 个新页面具备完整 `title`、`description`、`canonical`、`FAQ / Breadcrumb / Article` 结构化数据
- 3 个新页面都至少有 3 个以上站内入口
- `sitemap.xml` 校验通过
- Week 3 周任务文件写入仓库
- 路线图里 Week 3 由建议动作转为已执行内容

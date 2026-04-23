# JZZ1 核心页路由优化

日期：2026-04-23

适用站点：`https://www.jzz1.com/`

## 目标

把以下核心页的搜索意图切得更清楚，减少首页、产品页、OEM 页、Distributor 页、采购指南之间的主题重叠：

- 首页
- `products/windows.html`
- `oem-aluminum-window-supplier.html`
- `guides/aluminum-windows-for-distributors.html`
- `guides/how-to-buy-aluminum-windows-from-china.html`

本轮聚焦方向：

- 以东南亚项目采购为主线
- 保留 `supplier` 级商业词，但不再让每个页平均争抢
- 让内链先按“购买路径”分流，而不是按“站内栏目”分流

## 页面边界

| 页面 | 角色 | 主要承接 | 不再重点承接 |
| --- | --- | --- | --- |
| 首页 | 品牌总入口 | 品牌词、总能力词、优先市场入口、核心资源入口 | OEM 细节、完整采购教程、全部技术细节 |
| `products/windows.html` | 窗类产品枢纽 | `aluminum windows supplier`、系统选择、产品配置、项目询盘入口 | 完整 OEM 私牌叙事、完整采购教程叙事 |
| `oem-aluminum-window-supplier.html` | OEM 商业页 | `OEM aluminum window supplier`、`private label aluminum windows`、复购一致性 | 泛产品介绍、材料和系统大而全说明 |
| `guides/how-to-buy-aluminum-windows-from-china.html` | 采购指南 | `how to buy aluminum windows from china`、RFQ、MOQ、packing、delivery | 私牌流程、渠道 SKU 规划 |

## 这次已做的页面调整

### 首页

- 把高意图页面区改成“按 buying route 进入”。
- 新增 `Aluminum Windows` 产品入口卡片，让首页直接把泛产品词导向产品页。
- 保留 `How to Buy Aluminum Windows from China` 和 `OEM Aluminum Window Supplier` 作为两条不同意图路线。

### `products/windows.html`

- 强化“产品总页”定位，在首屏文案里明确这是产品与配置入口。
- 把通用支持表述从 OEM 导回到 drawing-based quotation 和 export project coordination。
- 新增 “Choose the right next step” 区块，把用户按产品页、OEM 页、采购指南、国家页分流。
- 调整场景页锚文本，降低与 OEM 页的混淆。

### `oem-aluminum-window-supplier.html`

- 首屏文案更聚焦 private label、repeat orders、branded packing。
- 新增 “Use this route when private label and repeat-order control matter most” 区块，突出 OEM 专属价值。
- 新增 “Choose the right next page” 区块，把一般产品型流量导回 `products/windows.html`，把采购教程流量导回 buying guide。

### `guides/how-to-buy-aluminum-windows-from-china.html`

- 保持教程页定位，不往 OEM 页和产品总页延展。
- 新增 “Choose the next page based on your buying stage” 区块，把读完教程的用户导向产品页、OEM 页、Distributor 页和国家页。
- 相关链接里的锚文本更具体，减少模糊导航词。

### `guides/aluminum-windows-for-distributors.html`

- 把主线进一步收紧到 `SKU planning / repeat-order supply / model coding / packing rules`。
- 降低 distributor 页对 `OEM / private label` 的直接覆盖，把这部分需求明确导向 `oem-aluminum-window-supplier.html`。
- 新增 “Use this route when SKU mix and repeat-order planning matter most” 和 “Choose the right next page” 两个分流区块。
- 调整 FAQ 和 Article schema，让搜索引擎更容易理解这是一页渠道规划内容，而不是 OEM 商业页的变体。

## 建议继续做的下一步

1. 在 `singapore.html`、`malaysia.html`、`indonesia.html` 里用同样的 route-based linking 方式接住从首页和 buying guide 过来的流量。
2. 下一轮处理 `products/doors.html`，把酒店阳台门、项目门、入口门的动线再拆开。
3. 用 GSC 验证以下 4 组词是否开始出现页面级分化：
   - 首页 vs `products/windows.html`
   - `products/windows.html` vs `oem-aluminum-window-supplier.html`
   - `products/windows.html` vs `guides/how-to-buy-aluminum-windows-from-china.html`
   - 国家页 vs 场景页

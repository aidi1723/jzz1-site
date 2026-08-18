# JZZ1 户外铝合金系统产品突出补充计划

日期：2026-08-18

适用站点：`https://www.jzz1.com/`

方案状态：方案 B 已于 2026-08-18 完成实施和本地验证，实施提交为 `801736b`。

## 1. 目标

在不破坏 JZZ1 现有门窗、型材、幕墙和阳光房产品结构的前提下，把以下产品提升为清晰、可发现、可询盘的户外产品组：

- 铝合金护栏
- 铝合金花园护栏
- 铝合金花园门

本轮不以堆叠关键词或增加大量同质页面为目标，而是建立一条完整购买路径：

```text
首页重点入口
  -> 户外铝合金系统总页
    -> 铝合金护栏
    -> 铝合金花园护栏
    -> 铝合金花园门
      -> 项目案例 / 工厂能力 / 联系询盘
```

## 2. 当前基线

截至 2026-08-18，网站已有：

- `products/railings.html`
- `products/aluminum-balcony-railings.html`
- `products/outdoor-aluminum-gates.html`
- 4 个阳台护栏相关 Guide
- 1 个护栏技术 FAQ

主要缺口：

- 首页护栏和户外门只是普通产品卡片，没有形成重点产品区。
- 花园护栏、铝合金围栏没有独立产品页。
- 花园门没有独立产品页，只在 Outdoor Aluminum Gates 页面中被顺带提及。
- 当前护栏产品页反复使用同一张图片，且图片不能充分展示完整护栏系统。
- Outdoor Aluminum Gates 页面使用的图片不是花园门产品实拍。
- 花园护栏、花园门缺少独立搜索意图、项目证据和专属询盘清单。

## 3. 方案选择

采用“一个户外产品总入口 + 三条独立产品线”的结构：

```text
Outdoor Aluminum Systems
├── Aluminum Railings
├── Aluminum Garden Fences
└── Aluminum Garden Gates
```

采用该结构的原因：

- 让首页可以突出一个完整产品组，而不是孤立地增加两张卡片。
- 保留已有护栏和户外门 URL，避免破坏已建立的索引和内链。
- 花园护栏和花园门分别对应独立采购意图，避免内容互相争抢。
- 可以自然表达围栏与门配套、统一颜色和统一项目交付。

## 4. 页面范围

### 4.1 新增户外系统总页

建议 URL：

```text
/products/outdoor-aluminum-systems.html
```

页面角色：

- 作为首页进入户外产品线后的总入口。
- 帮助买家在护栏、花园护栏和花园门之间选择。
- 表达三类产品可以独立采购，也可以作为统一户外围护方案采购。

建议 H1：

```text
Outdoor Aluminum Railings, Garden Fences, and Gates
```

建议首段：

```text
JZZ1 supplies aluminum railings, garden fences, and matching garden gates for villas,
residential developments, hospitality projects, and outdoor spaces. Systems can be
produced from drawings with coordinated dimensions, finishes, hardware, packing,
and project labels.
```

页面结构：

1. 首屏：产品组名称、应用范围、主场景图和询盘按钮。
2. 三条产品路线：Railings、Garden Fences、Garden Gates。
3. 配套系统：围栏与门的尺寸、颜色、样式和五金协调。
4. 户外表面处理：只描述可确认的工艺和颜色选择，不写未经证明的寿命。
5. 项目输入：图纸、总长度、高度、开口尺寸、安装方式、数量和目的地。
6. 项目证据：真实应用、细节、包装和发货图片。
7. 相关页面与询盘入口。

### 4.2 优化铝合金护栏总页

保留 URL：

```text
/products/railings.html
```

页面角色：

- 继续承接 `aluminum railings supplier` 等护栏总类搜索意图。
- 清晰分流至阳台、楼梯、露台和户外护栏应用。
- 不把花园围栏全部塞入该页，只提供明确的相关产品入口。

建议内容模块：

- Balcony railings
- Stair railings
- Terrace and villa railings
- Outdoor project railings
- Top mount / side mount / project-specific fixing
- Height, layout, finish and packing inputs
- 实景、整体、立柱、扶手、连接件和安装节点图库

应保留并加强：

- `/products/aluminum-balcony-railings.html`
- 护栏 Guide 与技术 FAQ
- 项目图纸询盘入口

### 4.3 新增花园护栏产品页

建议 URL：

```text
/products/aluminum-garden-fences.html
```

建议 H1：

```text
Aluminum Garden Fences
```

页面角色：

- 专门承接花园、庭院、别墅边界和隐私围栏需求。
- 展示围栏面板、立柱、固定方式、间距、颜色和配套门。
- 与建筑阳台护栏保持不同搜索意图和内容表达。

建议产品分类：

- Open-style aluminum garden fences
- Horizontal slat fences
- Vertical slat fences
- Privacy fence panels
- Villa and residential perimeter fences
- Fence and gate matching systems

页面结构：

1. 花园或庭院应用主图。
2. 款式分类与适用场景。
3. 围栏面板、立柱、间距和固定方式。
4. 颜色与表面处理。
5. 直线、转角、坡度和地面条件的图纸输入。
6. 与花园门配套的尺寸和样式说明。
7. 包装、标签和项目拆分。
8. FAQ 与快速询盘清单。

### 4.4 新增花园门产品页

建议 URL：

```text
/products/aluminum-garden-gates.html
```

建议 H1：

```text
Aluminum Garden Gates
```

页面角色：

- 承接花园门、庭院门、行人门和围栏配套门需求。
- 与宽泛的 Outdoor Aluminum Gates 页面形成父子关系，不复制相同内容。

建议产品分类：

- Single pedestrian garden gates
- Double-leaf garden gates
- Matching fence gates
- Slatted garden gates
- Panel and privacy garden gates
- Villa and residential access gates

只有在真实产品支持的情况下，才增加 sliding、automatic、motorized 等分类。

页面结构：

1. 花园门实景主图。
2. 单开、双开及配套围栏门分类。
3. 开口宽度、高度、净空和开启方向。
4. 框架、填充样式、合页、锁具和把手。
5. 与围栏配套的颜色、间距和视觉一致性。
6. 图纸确认、包装和出货流程。
7. FAQ 与门洞尺寸询盘清单。

### 4.5 保留并重定位户外门总页

保留 URL：

```text
/products/outdoor-aluminum-gates.html
```

该页继续承接：

- Villa entrance gates
- Driveway gates
- Perimeter gates
- Project entrance gates
- Custom outdoor aluminum gates

该页新增指向 `/products/aluminum-garden-gates.html` 的明确入口，但不与花园门页面重复标题、首段、FAQ 和产品分类。

## 5. 首页重点展示

在现有 Product Architecture 区块之后、Markets 区块之前新增完整宽度内容带：

```text
Outdoor aluminum systems

Aluminum railings, garden fences, and matching gates
for villas, residential projects, and outdoor spaces.

[Railings] [Garden Fences] [Garden Gates]
```

布局要求：

- 桌面端使用一张较大的真实场景图配三条清晰产品入口。
- 移动端按单列顺序展示，不使用横向滚动产品卡。
- 三张产品图必须对应真实产品，不能复用普通门窗或仓库图片。
- 保持现有暖矿物白、石色、石墨和香槟金视觉系统。
- 不增加新的营销式大 Hero，不改变首页现有主标题和核心市场定位。
- 不把户外产品区做成第二套导航或密集产品目录。

建议 CTA：

- `Explore Outdoor Systems`
- `View Garden Fences`
- `View Garden Gates`
- `Send Layout for Quote`

## 6. 导航与内链

不在顶部导航继续增加独立链接，避免导航重新变得拥挤。

推荐入口关系：

```text
Homepage
  -> Outdoor Aluminum Systems
  -> Railings
  -> Garden Fences
  -> Garden Gates

Outdoor Aluminum Systems
  <-> Railings
  <-> Garden Fences
  <-> Garden Gates

Garden Fences
  <-> Garden Gates
  -> Factory
  -> Projects
  -> Contact

Garden Gates
  <-> Outdoor Aluminum Gates
  <-> Garden Fences
  -> Factory
  -> Projects
  -> Contact
```

每个新产品页至少获得以下入口：

- 首页户外产品区
- 户外系统总页
- 相关产品页
- Projects 或 Guide / Knowledge Base 页面
- HTML sitemap
- XML sitemap

## 7. SEO 页面意图

### Aluminum Railings

主要意图：

- `aluminum railings supplier`
- `aluminum balcony railings`
- `aluminum stair railings`
- `outdoor aluminum railing systems`

### Aluminum Garden Fences

主要意图：

- `aluminum garden fence`
- `aluminum fence panels`
- `aluminum privacy fence`
- `aluminum villa fence`
- `garden fence supplier`

### Aluminum Garden Gates

主要意图：

- `aluminum garden gate`
- `aluminum pedestrian gate`
- `aluminum villa gate`
- `custom aluminum garden gates`
- `aluminum gate and fence system`

### Outdoor Aluminum Gates

继续承接：

- `outdoor aluminum gates supplier`
- `aluminum driveway gate manufacturer`
- `villa entrance aluminum gates`
- `custom outdoor aluminum gates`

每页只选择一个主意图，其他词作为相关内容自然出现，不做关键词清单式正文。

## 8. 页面 SEO 标准

每个新增或修改页面必须具备：

- 唯一 Title
- 唯一 Meta Description
- 绝对 Canonical URL
- 一个明确 H1
- `index,follow`
- Open Graph 与 Twitter 图片
- Product Schema
- BreadcrumbList Schema
- 可见 FAQ 与一致的 FAQPage Schema
- 真实产品图和描述性 Alt
- 相关产品、项目、工厂和联系页内链
- `sitemap.html` 和 `sitemap.xml` 收录

不发布虚假评分、评论、认证、承重、使用寿命、盐雾等级或自动门能力。

## 9. 素材交付清单

素材由用户补充。每条产品线建议提供 6–8 张真实图片。

### 每条产品线最低素材

- 1 张横向应用主图，建议不低于 1600px 宽。
- 1 张完整产品正面或侧面图。
- 2 张不同款式或配置图。
- 1 张立柱、扶手、填充或框架细节图。
- 1 张五金、连接件或安装节点图。
- 1 张颜色或表面处理图。
- 1 张包装或出货图，可选。

### 素材提交时需要同时说明

- 图片对应产品类别。
- 产品名称或内部型号。
- 应用场景。
- 材料和表面处理。
- 可确认的尺寸范围。
- 安装或固定方式。
- 是否可以公开展示。
- 是否为本公司真实产品或真实项目。

### 建议文件名

```text
aluminum-railing-balcony-installed-01.jpg
aluminum-railing-post-detail-01.jpg
aluminum-garden-fence-horizontal-slat-01.jpg
aluminum-garden-fence-post-detail-01.jpg
aluminum-garden-gate-single-leaf-01.jpg
aluminum-garden-gate-hinge-lock-detail-01.jpg
```

图片不得包含无法移除的竞争品牌水印、错误联系方式、短视频按钮或与网站不一致的文字覆盖层。

## 10. 询盘内容

### 护栏询盘字段

- Application
- Layout or drawing
- Total length
- Railing height
- Mounting method
- Finish and color
- Quantity
- Destination
- Packing and labels

### 花园护栏询盘字段

- Fence layout
- Total length
- Fence height
- Panel or slat style
- Post spacing
- Ground or fixing condition
- Finish and color
- Matching gate requirement
- Quantity and destination

### 花园门询盘字段

- Opening width and height
- Single or double leaf
- Opening direction
- Frame and infill style
- Hinge, lock and handle requirement
- Matching fence style
- Finish and color
- Quantity and destination

询盘入口继续使用可用的 WhatsApp、邮箱和 Contact 页面，不在本轮增加新的后端 API。

## 11. 项目案例页补强

在 `projects.html` 中把当前单一 Railings 展示扩展为清晰的户外应用分组：

- Balcony and terrace railings
- Garden and perimeter fences
- Garden and villa gates

只使用真实项目或真实产品图片。没有真实案例时，标注为产品参考，不描述为已完工项目。

## 12. 实施阶段

### 阶段 0：备份与素材审核

- 从正式仓库创建新的日期备份。
- 建立素材清单，删除重复、模糊和无关图片。
- 核对产品名称、能力边界和可公开参数。

### 阶段 1：产品架构与首页入口

- 新建 Outdoor Aluminum Systems 总页。
- 新增首页重点产品区。
- 建立三条产品路线和基础内链。

### 阶段 2：独立产品页

- 完成 Aluminum Garden Fences 页面。
- 完成 Aluminum Garden Gates 页面。
- 优化 Railings、Balcony Railings 和 Outdoor Aluminum Gates 页面。

### 阶段 3：项目、内容与 SEO 接线

- 补强 Projects 页面。
- 增加必要 Guide 或 FAQ 支撑内容，但不批量制造同质页面。
- 更新首页、产品页、相关页面、HTML sitemap 和 XML sitemap 的内链。

### 阶段 4：验证与发布

- 本地检查桌面和移动端。
- 验证 metadata、canonical、JSON-LD、图片 Alt 和内部链接。
- 运行 XML、隐私扫描和 diff 检查。
- 发布后核对线上页面、移动端、询盘入口和 sitemap。
- 写入维护日志和回滚路径。

## 13. 验收标准

### 内容与产品

- 首页存在一个明确的户外铝合金系统重点区。
- 户外产品总页能够分流到护栏、花园护栏和花园门。
- 花园护栏和花园门各有独立页面和唯一搜索意图。
- 每个重点产品页至少有 5 张真实且相关的图片。
- 页面内容不包含未经证明的产品能力和性能数据。

### 转化

- 每个重点产品页至少有 2 个有效询盘入口。
- 每个页面提供与产品匹配的询盘字段或快速询盘清单。
- WhatsApp、邮箱和 Contact 页面链接有效。

### SEO

- 每页只有一个 H1。
- Title、Description 和 Canonical 唯一且正确。
- Product、Breadcrumb 和 FAQ JSON-LD 与可见内容一致。
- 每个新产品页至少有 4 个有效站内入口。
- `sitemap.xml` 校验通过。

### UI 与质量

- 桌面和移动端无横向溢出或内容遮挡。
- 图片比例稳定，不因加载造成明显布局跳动。
- 产品区符合现有 JZZ1 视觉规范，不改变全站品牌基调。
- 页面没有失效链接、缺图、控制台错误或错误联系方式。

## 14. 备份、实施与维护路径

正式维护以当前 `origin/main` 检出目录为准。本机绝对路径、历史备份根目录和私有运维索引不写入公开仓库，维护人员应从不发布的本地运维索引获取。

实施前备份名称：

```text
jzz1-site-2026-08-18-before-outdoor-systems-optimization
```

仓库内公开安全维护入口：

```text
docs/JZZ1_MAINTENANCE_PATHS.zh-CN.md
```

## 15. 非目标

本轮不包含：

- 全站视觉重做。
- 更换现有域名、服务器或部署平台。
- 删除现有门窗、型材、幕墙和阳光房页面。
- 新建在线商城、价格系统或购物车。
- 新建询盘后端 API。
- 在没有真实素材和参数的情况下编造产品案例或性能数据。

## 16. 实施结果

1. 已完成素材分类、去重、裁切和响应式图片输出。
2. 已建立 Outdoor Aluminum Systems、Aluminum Garden Fences 和 Aluminum Garden Gates 三个新页面。
3. 已加强首页、护栏、阳台护栏、户外门和项目参考页的产品入口。
4. 已更新 HTML/XML sitemap，并加入专项验证脚本。
5. 已通过桌面端、390px 移动端、JSON-LD、XML、隐私扫描和 diff 检查。
6. 详细实施与回滚说明见 `docs/reports/2026-08-18-jzz1-outdoor-aluminum-systems-implementation.md`。

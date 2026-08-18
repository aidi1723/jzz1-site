# JZZ1 户外铝合金系统优化实施记录

日期：2026-08-18

适用站点：`https://www.jzz1.com/`

实施提交：`801736b`（`Add outdoor aluminum systems product routes`）

## 1. 实施目标

在不改变 JZZ1 现有门窗、型材、幕墙和阳光房业务结构的前提下，建立“户外铝合金系统”重点入口，并把铝合金护栏、花园护栏和花园门整理为清晰、可发现、可询盘的产品路线。

## 2. 页面与入口

本次新增页面：

- `products/outdoor-aluminum-systems.html`
- `products/aluminum-garden-fences.html`
- `products/aluminum-garden-gates.html`

本次加强的现有页面：

- `index.html`
- `products/railings.html`
- `products/aluminum-balcony-railings.html`
- `products/outdoor-aluminum-gates.html`
- `projects.html`
- `sitemap.html`
- `sitemap.xml`

首页新增户外铝合金系统重点区，但不改变原首页 Hero、核心市场定位和主导航结构。三个新页面均包含唯一 Title、Meta Description、Canonical、H1、Product Schema、BreadcrumbList、FAQPage、询盘入口和相关产品内链。

## 3. 素材处理

- 原始素材共 39 个文件，包含图片、视频和重复副本。
- 筛选为 16 个可复用素材角色，生成 48 个网站文件。
- 每个素材角色提供 `1200.jpg`、`1200.webp` 和 `640.webp` 三种输出。
- 排除重复图片和原始视频，不把短视频文件直接发布到站点。
- 对含外部品牌标识的素材进行了裁切，避免发布无关品牌信息。
- 未确认项目归属的安装图片统一表述为“产品或应用参考”，不宣称为 JZZ1 已完工项目。

网站素材统一存放于：

```text
images/outdoor-systems/
```

## 4. 内容与能力边界

- 不发布未经证明的承重、寿命、盐雾、质保或认证数据。
- 不把花园门描述为自动门、滑动门或电动门，除非后续有真实能力和资料支持。
- 围栏、护栏和花园门按图纸、尺寸、固定条件、表面处理、包装和目的地进行询盘引导。
- `Outdoor Aluminum Gates` 保留原有宽泛入口门、车道门和别墅门定位，新花园门页面承接行人门和围栏配套门意图。

## 5. UI 与响应式处理

- 沿用仓库 `DESIGN.md` 的暖矿物白、石墨黑、香槟金和真实产品图方向。
- 首页重点区使用现有页面节奏，不新增第二个营销式 Hero。
- 桌面端检查了首页和三个新产品页的首屏布局与图片加载。
- 移动端发现产品页长导航会把页面宽度撑到 907px，已在 `css/product.css` 中把移动导航改为独立横向浏览区域。
- 修复后在 390px 视口下，三个新产品页的 `scrollWidth` 均为 390px，没有横向页面溢出。

## 6. 验证结果

以下检查均通过：

```bash
bash scripts/verify-outdoor-systems.sh
xmllint --noout sitemap.xml
bash scripts/privacy-scan.sh
git diff --check
```

浏览器验证结果：

- 首页重点户外图片正常加载。
- 三个新产品页桌面端首屏布局正常。
- 390 x 844 移动视口无页面横向溢出。
- 三个新产品页控制台均为 0 errors、0 warnings。
- 页面图片引用有效；首屏图使用 eager loading，其余图库保留 lazy loading。

自动检查脚本位于：

```text
scripts/verify-outdoor-systems.sh
```

## 7. 回滚与维护

- 发布前完整备份位置记录在私有运维索引中，不写入公开仓库。
- 如需仅撤销网站实施提交，可在确认后对 `801736b` 执行 `git revert`。
- 如需完整文件级回滚，应使用私有运维索引中记录的 2026-08-18 发布前备份。
- 后续新增素材时，继续生成 640px 与 1200px WebP，并保留 1200px JPEG 兼容版本。

## 8. 后续观察

发布后应检查：

1. 首页、三个新产品页和 sitemap 的线上 HTTPS 状态码。
2. 手机浏览器中的导航滑动、按钮、图片和询盘链接。
3. Google Search Console 对三个新 URL 的发现、抓取与索引状态。
4. 花园护栏、花园门和护栏相关询盘是否开始出现更清晰的产品意图。


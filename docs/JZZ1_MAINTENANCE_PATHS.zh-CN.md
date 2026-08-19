# JZZ1 网站维护入口（公开仓库安全版）

## 文档用途

本文记录 `https://www.jzz1.com/` 的仓库内维护入口、发布检查和文档关系。出于隐私与安全原因，公开仓库不保存操作员用户名、本机绝对路径、设备名或私有备份目录。

本机精确路径、历史备份位置和工作区位置保存在不发布到网站的私有运维索引中。维护人员应先查阅该私有索引，再进入当前 `origin/main` 正式检出目录。

## 站点身份

- 网站域名：`https://www.jzz1.com/`
- 品牌：`JZZ1`
- 公司名称：`Jinan Jingzao New Materials Co., Ltd`
- Git 远程仓库：`https://github.com/aidi1723/jzz1-site.git`

## 仓库内主要入口

```text
DESIGN.md
index.html
css/site.css
css/product.css
products/
guides/
knowledge-base/
images/
projects.html
sitemap.html
sitemap.xml
scripts/privacy-scan.sh
docs/reports/
docs/superpowers/specs/
docs/superpowers/plans/
```

## 后续维护标准流程

1. 在正式检出目录检查分支、提交和工作区状态。
2. 修改前按私有运维索引建立带日期和任务名的回滚备份。
3. 阅读 `DESIGN.md`，保持现有视觉语言、导航、响应式布局和业务路径。
4. 检查唯一 Title、Meta Description、Canonical 和 H1。
5. 检查产品页、市场页、Guide、Knowledge Base、项目页和联系页内链。
6. 同步更新 `sitemap.html` 与 `sitemap.xml`。
7. 保持可见 FAQ 与 FAQPage JSON-LD 一致。
8. 不发布未经证明的认证、性能、承重、寿命、自动化能力或项目归属声明。

发布前运行：

```bash
xmllint --noout sitemap.xml
bash scripts/privacy-scan.sh
git diff --check
git status --short
```

发布后检查线上 HTTPS、页面状态码、移动端布局、询盘入口、图片和 sitemap，并在 `docs/reports/` 写入不含本机隐私信息的发布记录。

## 2026-08-19 现有英文户外关键词优化

本轮只优化现有英文页面和现有英文关键词，不新增西班牙语、葡萄牙语、城市页或未验证产品能力。公开实施记录：

```text
docs/reports/2026-08-19-jzz1-existing-english-outdoor-keyword-optimization.md
```

修改范围：

- `products/railings.html`
- `products/aluminum-garden-fences.html`
- `products/aluminum-garden-gates.html`
- `products/outdoor-aluminum-gates.html`
- `products/outdoor-aluminum-systems.html`
- `sitemap.xml`

关键词分工为：护栏供应商、花园围栏和围栏面板、花园行人门、车道门和别墅入口门、户外铝合金系统总入口。提交和线上发布完成后，应把最终提交号与部署工作流补入本索引。

## 户外铝合金系统实施记录

本轮护栏、花园护栏和花园门方案与实施记录位于：

```text
docs/superpowers/specs/2026-08-18-jzz1-outdoor-aluminum-systems-design.md
docs/reports/2026-08-18-jzz1-outdoor-aluminum-systems-implementation.md
```

实施采用一个 Outdoor Aluminum Systems 总入口，并保留现有护栏和户外门 URL。公开页面只使用经审核的真实素材，并把未确认归属的安装图标注为应用参考。发布前可运行 `bash scripts/verify-outdoor-systems.sh` 执行本轮专项检查。

# JZZ1 网站维护路径与存放目录

## 文档用途

本文用于记录 `https://www.jzz1.com/` 在本机的正式维护仓库、镜像目录、历史备份、设计资料和常用维护文档路径，避免后续维护时找错项目或重复搜索。

最后核对时间：`2026-08-18`（Asia/Shanghai）

## 站点身份

- 网站域名：`https://www.jzz1.com/`
- 品牌：`JZZ1`
- 公司名称：`Jinan Jingzao New Materials Co., Ltd`
- Git 远程仓库：`https://github.com/aidi1723/jzz1-site.git`

## 本机根目录

JZZ1 网站文件不在 `/Users/aidi/网站` 下，实际存放根目录为：

```text
/Users/aidi/ai启蒙电影/谷歌seo/.site-work
```

后续查找 JZZ1 网站时，应先进入该目录。

## 正式维护仓库

当前正式发布和后续改版使用的 Git 仓库：

```text
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704
```

2026-08-18 核对状态：

```text
branch: main
commit: f645a4a
commit message: Improve JZZ1 SEO RFQ conversion pages
origin/main: f645a4a
working tree: clean
```

正式仓库约 `113MB`，包含完整 HTML、CSS、图片、产品页、市场页、Guide、Knowledge Base、SEO 文档和 Git 历史。

以后修改网站，应以此目录为主，不要直接在历史备份中修改。

## 日常镜像目录

当前站点镜像目录：

```text
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-site
```

用途：

- 保存一份可直接浏览和比较的站点镜像。
- 可用于页面内容核对和发布前对照。
- 不是优先维护入口；正式修改应进入 `jzz1-release-20260704`。

2026-08-18 核对时，该目录的 `index.html` 与正式仓库及线上首页 SHA-256 一致：

```text
114f2b1996b2ccdae977dda38f6ec911bb9e4de6c1d42c529006eb34f5ab3573
```

## 历史回滚备份

2026-07-04 三阶段优化前的完整备份：

```text
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/backups/jzz1-site-2026-07-04-before-three-phase-optimization
```

用途：

- 用于对比 2026-07-04 优化前后的页面变化。
- 当前版本出现严重问题时，可作为历史回滚参考。
- 该目录不是当前线上版本，不应在其中继续开发。

该备份的 `index.html` SHA-256 为：

```text
57f0c9c77f6ad29c734e70464dea980e4242376922d124dce0899f5d94ed1fe7
```

## 设计资料目录

早期 JZZ1 设计系统和首页改版资料：

```text
/Users/aidi/Documents/Codex/2026-04-17-new-chat/jzz1-design-system
```

主要文件：

```text
DESIGN.md
homepage-redesign-brief.md
asset-shortlist.md
```

该目录只有设计规范和改版参考，不是完整网站备份。

正式仓库内也有当前站点的视觉规范：

```text
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/DESIGN.md
```

## 维护与运营记录

正式仓库中的主要维护资料：

```text
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/docs/reports/2026-04-23-jzz1-core-page-routing-update.md
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/seo/seo-geo-operations-playbook-2026.md
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/seo/weekly-website-optimization-plan-2026-q2.md
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/seo/keyword-roadmap-2026-q2.md
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/seo/priority-market-execution-roadmap-2026-q2.md
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/seo/weekly-tasks/
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/docs/superpowers/specs/
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/docs/superpowers/plans/
```

全局路径索引保存在：

```text
/Users/aidi/网站/ops/jzz1-maintenance-paths-zh.md
```

## 后续维护标准流程

1. 进入正式仓库并检查状态：

```bash
cd /Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704
git status --short
git log -5 --oneline --decorate
```

2. 修改前在 `.site-work/backups/` 下建立带日期和任务名称的新备份，命名格式：

```text
jzz1-site-YYYY-MM-DD-before-<task-name>
```

3. 阅读正式仓库中的 `DESIGN.md`，保持现有视觉语言、导航、响应式布局和业务路径。

4. 修改页面时同步检查：

- 唯一 `title`、Meta Description、Canonical 和 H1。
- 产品页、市场页、Guide、Knowledge Base 之间的内链。
- `sitemap.html` 和 `sitemap.xml`。
- FAQ 可见内容与 JSON-LD 是否一致。
- WhatsApp、邮箱和联系页入口。

5. 发布前从正式仓库运行：

```bash
git status --short
xmllint --noout sitemap.xml
git diff --check
bash scripts/privacy-scan.sh
```

6. 发布后核对线上页面，并记录本次提交、变更文件、验证结果和回滚目录。

## 路径辨识提醒

以下目录不是 JZZ1 网站：

```text
/Users/aidi/网站/菲律宾
```

该目录是 `CDCY Aluminum Warehouse` 项目，不能作为 `jzz1.com` 的维护仓库。以后看到门窗、铝型材或菲律宾项目内容时，应先核对域名和仓库路径，避免混淆。

## 当前结论

- 当前线上版本对应正式仓库 `jzz1-release-20260704`。
- `jzz1-site` 是当前镜像。
- `backups/jzz1-site-2026-07-04-before-three-phase-optimization` 是历史回滚备份。
- 后续 JZZ1 网站优化、产品突出和 SEO 调整都应从正式仓库开始，并在改动前创建新的日期备份。

## 2026-08-18 户外产品补充计划

铝合金护栏、花园护栏和花园门的产品突出补充计划保存在：

```text
/Users/aidi/网站/ops/jzz1-outdoor-aluminum-systems-supplement-plan-zh.md
/Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-release-20260704/docs/superpowers/specs/2026-08-18-jzz1-outdoor-aluminum-systems-design.md
```

方案采用“一个户外产品总入口 + 铝合金护栏 + 花园护栏 + 花园门三条独立产品线”。当前仅完成方案和内容规划，网站页面尚未实施修改。

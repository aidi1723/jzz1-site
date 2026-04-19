# JZZ1 每周网站 SEO 优化计划 2026 Q2

这份计划的目的，是把 SEO 工作从“想到哪做哪”变成每周可以重复执行的固定动作。

## 1. 每周最低产出

每周至少完成以下 6 项中的 5 项：

1. 更新 1 个核心页面
2. 新增或重写 1 个 Guide
3. 新增或重写 1 个 Knowledge Base / FAQ 页
4. 完成 1 次内链补强
5. 更新 `sitemap.html` 和 `sitemap.xml`
6. 在 GSC 提交索引并记录结果

## 2. 每周固定节奏

### 周一：数据复盘

- 打开 `Google Search Console`
- 看 `Queries`
- 看 `Pages`
- 看 `Countries`
- 记录本周要打的 5 个关键词

如果 GSC 数据还不够多，就优先看：

- 当前站内哪些页面是空缺
- 第一梯队市场哪些场景还没有专页

### 周二：确定本周页面

- 选 1 个主页面
- 选 1 个 Guide
- 选 1 个 Knowledge Base
- 确认每个页面的主关键词和内链来源

### 周三：内容制作

- 补 Title / Description / Canonical / H1
- 写首段直接回答
- 增加参数表、RFQ checklist 或 FAQ
- 补结构化数据

### 周四：站内结构优化

- 从首页、产品页、市场页、Hub 页补内链
- 更新 `sitemap.html`
- 更新 `sitemap.xml`
- 跑本地检查和 XML 校验

### 周五：发布与留档

- 发布页面
- 在 GSC 请求抓取
- 记录本周改了什么
- 生成下一周任务文件

## 3. 第一梯队市场周任务顺序

### Week 1

- 首页主线切换为 Singapore / Malaysia / Indonesia
- 核心页面补强
- 印尼专题簇上线

### Week 2

- 新加坡专题补强

### Week 3

- 马来西亚专题补强

### Week 4

- 印尼专题继续扩展

### Week 5+

- 回到产品线做长期滚动：
  - windows
  - doors
  - profiles
  - railings
  - sunrooms
  - upvc

## 4. 每周页面组合建议

### 组合 A：市场拉升

- 1 个市场页补强
- 1 个对应 Guide
- 1 个对应 Knowledge Base

适合：

- Singapore
- Malaysia
- Indonesia

### 组合 B：产品拉升

- 1 个产品页补强
- 1 个采购 Guide
- 1 个 FAQ / Checklist

适合：

- windows
- doors
- profiles

### 组合 C：技术信任拉升

- 1 个 standards / checklist 页
- 1 个场景型 Guide
- 1 次全站内链补强

适合：

- AS2047
- NFRC
- coastal / passive house / performance topics

## 5. 交付标准

每周任务只有满足下面条件，才算真正完成：

- 页面可正常访问
- Title / Description / Canonical 正确
- 页面被至少两个相关页面链接
- 已加入 `sitemap.html`
- 已加入 `sitemap.xml`
- XML 校验通过
- 本周任务写入周报文件

## 6. 工具使用顺序

### 必用

- `Google Search Console`
- `Google Lighthouse`

### 推荐

- `Screaming Frog`
- `Ahrefs` 或 `SEMrush`

### 本地检查

```bash
git status --short
xmllint --noout sitemap.xml
git diff --check
```

## 7. 周任务文件规范

每周新增一个文件到：

`seo/weekly-tasks/`

命名格式：

`YYYY-MM-DD-week-N-topic.md`

文件里必须写清楚：

- 本周目标
- 本周实际完成页面
- 本周未完成项
- 下周推荐动作

## 8. 相关文件

- `seo/priority-market-execution-roadmap-2026-q2.md`
- `seo/keyword-roadmap-2026-q2.md`
- `seo/product-weekly-longtail-matrix-2026-q2.md`

# Market Gap Pages And Weekly Sprint Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the next three market-gap SEO pages for Singapore, Malaysia, and Indonesia, then connect them through the existing market, product, hub, sitemap, and weekly execution system.

**Architecture:** Keep the existing static-site cluster model: market page -> product page -> guide / knowledge base -> sitemap / roadmap docs. Use one Singapore checklist page, one Malaysia RFQ guide, and one Indonesia apartment-package guide so each market gets a clearer long-tail entry instead of adding generic product prose.

**Tech Stack:** Static HTML, existing JZZ1 CSS, XML sitemap, Markdown SEO docs

---

## File Structure

- Create: `docs/superpowers/specs/2026-04-19-market-gap-pages-and-weekly-sprint-design.md`
- Create: `docs/superpowers/plans/2026-04-19-market-gap-pages-and-weekly-sprint.md`
- Create: `knowledge-base/singapore-balcony-door-acoustic-spec-checklist.html`
- Create: `guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html`
- Create: `guides/indonesia-apartment-window-package-rfq-guide.html`
- Create: `seo/weekly-tasks/2026-04-19-week-2-market-gap-pages.md`
- Modify: `guides/singapore-acoustic-sliding-doors-for-condo-projects.html`
- Modify: `guides/malaysia-hotel-balcony-doors-for-hospitality-projects.html`
- Modify: `guides/indonesia-tropical-window-and-balcony-door-sourcing.html`
- Modify: `products/windows.html`
- Modify: `products/doors.html`
- Modify: `singapore.html`
- Modify: `malaysia.html`
- Modify: `indonesia.html`
- Modify: `guides/index.html`
- Modify: `knowledge-base/index.html`
- Modify: `sitemap.html`
- Modify: `sitemap.xml`
- Modify: `seo/priority-market-execution-roadmap-2026-q2.md`
- Modify: `seo/keyword-roadmap-2026-q2.md`
- Modify: `seo/weekly-website-optimization-plan-2026-q2.md`

### Task 1: Write the new market-gap pages

**Files:**
- Create: `knowledge-base/singapore-balcony-door-acoustic-spec-checklist.html`
- Create: `guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html`
- Create: `guides/indonesia-apartment-window-package-rfq-guide.html`

- [ ] **Step 1: Create the Singapore checklist page**
- [ ] **Step 2: Create the Malaysia commercial RFQ guide**
- [ ] **Step 3: Create the Indonesia apartment-package RFQ guide**
- [ ] **Step 4: Confirm each page includes metadata, canonical, structured data, and related links**

### Task 2: Connect the pages to existing traffic routes

**Files:**
- Modify: `guides/singapore-acoustic-sliding-doors-for-condo-projects.html`
- Modify: `guides/malaysia-hotel-balcony-doors-for-hospitality-projects.html`
- Modify: `guides/indonesia-tropical-window-and-balcony-door-sourcing.html`
- Modify: `products/windows.html`
- Modify: `products/doors.html`
- Modify: `singapore.html`
- Modify: `malaysia.html`
- Modify: `indonesia.html`
- Modify: `guides/index.html`
- Modify: `knowledge-base/index.html`

- [ ] **Step 1: Add Singapore checklist links from Singapore market and acoustic-door pages**
- [ ] **Step 2: Add Malaysia RFQ guide links from Malaysia market, door page, and Malaysia hotel guide**
- [ ] **Step 3: Add Indonesia apartment guide links from Indonesia market, windows page, and Indonesia tropical guide**
- [ ] **Step 4: Add the new pages to the Guides and Knowledge Base hubs**

### Task 3: Register the URLs and update execution docs

**Files:**
- Modify: `sitemap.html`
- Modify: `sitemap.xml`
- Modify: `seo/priority-market-execution-roadmap-2026-q2.md`
- Modify: `seo/keyword-roadmap-2026-q2.md`
- Modify: `seo/weekly-website-optimization-plan-2026-q2.md`
- Create: `seo/weekly-tasks/2026-04-19-week-2-market-gap-pages.md`

- [ ] **Step 1: Add the three new URLs to both sitemaps with `2026-04-19` lastmod**
- [ ] **Step 2: Update the market roadmap so these pages move from “缺口” to “已执行”**
- [ ] **Step 3: Update the keyword roadmap to reflect started keywords and the remaining worthwhile gaps**
- [ ] **Step 4: Write the Week 2 task file with completed work, launch follow-ups, and next-week recommendations**

### Task 4: Verify and sync

**Files:**
- Modify: all changed files above

- [ ] **Step 1: Run mirror verification**

Run:

```bash
xmllint --noout /Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-site/sitemap.xml
```

Expected: no output

- [ ] **Step 2: Confirm the new URLs are linked from market pages, product pages, hub pages, and sitemaps**

Run:

```bash
rg -n "singapore-balcony-door-acoustic-spec-checklist|malaysia-commercial-window-and-balcony-door-rfq-guide|indonesia-apartment-window-package-rfq-guide" /Users/aidi/ai启蒙电影/谷歌seo/.site-work/jzz1-site
```

Expected: the new URLs appear in the intended pages instead of only on themselves

- [ ] **Step 3: Sync only intended files to the formal repo**
- [ ] **Step 4: Run formal verification, commit, and push**

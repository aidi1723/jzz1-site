# Week 3 Supplier Minimalist Mixed RFQ Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver the Week 3 SEO batch focused on supplier-intent, minimalist sliding-door intent, and mixed RFQ checklist intent across Singapore, Malaysia, and Indonesia.

**Architecture:** Extend the existing market cluster with one Singapore guide and two checklist-style knowledge-base pages. Then wire those URLs into the current market pages, product pages, guide/knowledge hubs, both sitemaps, and the Q2 roadmap docs so the batch behaves like a crawlable cluster rather than isolated content.

**Tech Stack:** Static HTML, existing JZZ1 CSS, XML sitemap, Markdown SEO docs

---

## File Structure

- Create: `docs/superpowers/specs/2026-04-19-week3-supplier-minimalist-mixed-rfq-design.md`
- Create: `docs/superpowers/plans/2026-04-19-week3-supplier-minimalist-mixed-rfq.md`
- Create: `guides/singapore-minimalist-sliding-doors-for-condos.html`
- Create: `knowledge-base/malaysia-tropical-coastal-window-spec-checklist.html`
- Create: `knowledge-base/indonesia-mixed-window-and-door-rfq-checklist.html`
- Create: `seo/weekly-tasks/2026-04-19-week-3-supplier-minimalist-mixed-rfq.md`
- Modify: `products/sliding-aluminum-windows.html`
- Modify: `products/windows.html`
- Modify: `products/doors.html`
- Modify: `singapore.html`
- Modify: `malaysia.html`
- Modify: `indonesia.html`
- Modify: `guides/singapore-acoustic-sliding-doors-for-condo-projects.html`
- Modify: `guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html`
- Modify: `guides/indonesia-apartment-window-package-rfq-guide.html`
- Modify: `guides/indonesia-tropical-window-and-balcony-door-sourcing.html`
- Modify: `knowledge-base/malaysia-hotel-balcony-door-and-tropical-glazing-faq.html`
- Modify: `guides/index.html`
- Modify: `knowledge-base/index.html`
- Modify: `sitemap.html`
- Modify: `sitemap.xml`
- Modify: `seo/priority-market-execution-roadmap-2026-q2.md`
- Modify: `seo/keyword-roadmap-2026-q2.md`
- Modify: `seo/weekly-website-optimization-plan-2026-q2.md`

### Task 1: Create the three Week 3 pages

**Files:**
- Create: `guides/singapore-minimalist-sliding-doors-for-condos.html`
- Create: `knowledge-base/malaysia-tropical-coastal-window-spec-checklist.html`
- Create: `knowledge-base/indonesia-mixed-window-and-door-rfq-checklist.html`

- [ ] **Step 1: Create the Singapore minimalist sliding guide**
- [ ] **Step 2: Create the Malaysia tropical/coastal window checklist**
- [ ] **Step 3: Create the Indonesia mixed RFQ checklist**
- [ ] **Step 4: Verify all three pages include metadata, canonical, schema, and related links**

### Task 2: Connect the pages into existing clusters

**Files:**
- Modify: `products/sliding-aluminum-windows.html`
- Modify: `products/windows.html`
- Modify: `products/doors.html`
- Modify: `singapore.html`
- Modify: `malaysia.html`
- Modify: `indonesia.html`
- Modify: `guides/singapore-acoustic-sliding-doors-for-condo-projects.html`
- Modify: `guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html`
- Modify: `guides/indonesia-apartment-window-package-rfq-guide.html`
- Modify: `guides/indonesia-tropical-window-and-balcony-door-sourcing.html`
- Modify: `knowledge-base/malaysia-hotel-balcony-door-and-tropical-glazing-faq.html`
- Modify: `guides/index.html`
- Modify: `knowledge-base/index.html`

- [ ] **Step 1: Add Singapore minimalist guide links from Singapore market, sliding-window product, and Singapore acoustic-door guide**
- [ ] **Step 2: Add Malaysia tropical/coastal checklist links from Malaysia market, windows product, commercial RFQ guide, and Malaysia FAQ**
- [ ] **Step 3: Add Indonesia mixed RFQ checklist links from Indonesia market, windows product, doors product, apartment RFQ guide, and Indonesia tropical guide**
- [ ] **Step 4: Add all three new pages to the guide and knowledge-base hubs**

### Task 3: Register URLs and execution docs

**Files:**
- Modify: `sitemap.html`
- Modify: `sitemap.xml`
- Modify: `seo/priority-market-execution-roadmap-2026-q2.md`
- Modify: `seo/keyword-roadmap-2026-q2.md`
- Modify: `seo/weekly-website-optimization-plan-2026-q2.md`
- Create: `seo/weekly-tasks/2026-04-19-week-3-supplier-minimalist-mixed-rfq.md`

- [ ] **Step 1: Add the three new URLs to both sitemaps with `2026-04-19` lastmod**
- [ ] **Step 2: Update the roadmap so Week 3 is reflected as executed**
- [ ] **Step 3: Update the keyword roadmap to move Week 3 keywords into started coverage**
- [ ] **Step 4: Write the Week 3 task file with completed work, post-launch checks, and next recommendations**

### Task 4: Verify and sync

**Files:**
- Modify: all changed files above

- [ ] **Step 1: Run mirror verification**

Run:

```bash
xmllint --noout <jzz1-site-worktree>/sitemap.xml
```

Expected: no output

- [ ] **Step 2: Confirm the three URLs are linked from market pages, product pages, hubs, and sitemaps**

Run:

```bash
rg -n "singapore-minimalist-sliding-doors-for-condos|malaysia-tropical-coastal-window-spec-checklist|indonesia-mixed-window-and-door-rfq-checklist" <jzz1-site-worktree>
```

Expected: the new URLs appear in multiple cluster pages instead of only themselves

- [ ] **Step 3: Sync only intended files to the formal repo**
- [ ] **Step 4: Run formal verification, commit, and push**

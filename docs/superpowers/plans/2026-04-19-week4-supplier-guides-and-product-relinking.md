# Week 4 Supplier Guides And Product Relinking Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 3 supplier-intent market guides and relink the core product and market hubs so Singapore, Malaysia, and Indonesia traffic can move deeper into RFQ-stage pages.

**Architecture:** Reuse the existing static Guide-page template and extend the existing internal-link graph. This batch stays content-first: new Guide pages, tighter product-page routing, updated market clusters, refreshed sitemap entries, and synced roadmap documents.

**Tech Stack:** Static HTML, existing CSS (`/css/product.css`, `/css/site.css`), XML sitemap, Markdown SEO documentation

---

### Task 1: Add Week 4 design and execution docs

**Files:**
- Create: `docs/superpowers/specs/2026-04-19-week4-supplier-guides-and-product-relinking-design.md`
- Create: `docs/superpowers/plans/2026-04-19-week4-supplier-guides-and-product-relinking.md`
- Create: `seo/weekly-tasks/2026-04-19-week-4-supplier-guides-and-product-relinking.md`

- [ ] Write the Week 4 design doc with target pages, keywords, relinking scope, and success criteria.
- [ ] Write this implementation plan with concrete file scope.
- [ ] Add the Week 4 weekly task record with completed work, post-launch checklist, conclusions, and next-step notes.

### Task 2: Create the 3 Week 4 supplier guides

**Files:**
- Create: `guides/singapore-condo-window-supplier-rfq-guide.html`
- Create: `guides/malaysia-hotel-window-and-door-supplier-guide.html`
- Create: `guides/indonesia-commercial-window-supplier-project-guide.html`

- [ ] Create the Singapore supplier guide with supplier-comparison, condo RFQ, and acoustic-window intent.
- [ ] Create the Malaysia supplier guide with hotel package, balcony-door supplier, and room-label logic.
- [ ] Create the Indonesia commercial supplier guide with project-city, window-package, and coastal/commercial RFQ logic.
- [ ] Ensure every new page includes metadata, FAQ schema, breadcrumbs, CTA, RFQ table or checklist, and related-page links.

### Task 3: Relink product hubs and market pages

**Files:**
- Modify: `products/windows.html`
- Modify: `products/doors.html`
- Modify: `products/sliding-aluminum-windows.html`
- Modify: `singapore.html`
- Modify: `malaysia.html`
- Modify: `indonesia.html`

- [ ] Add the new supplier guides into the windows, doors, and sliding-windows product hubs.
- [ ] Add the new supplier guides into each first-tier market page.
- [ ] Update search-intent copy where needed so the product and market hubs mention the new supplier keyword layer.

### Task 4: Relink existing guide clusters and discovery hubs

**Files:**
- Modify: `guides/singapore-aluminum-windows-for-condo-projects.html`
- Modify: `guides/singapore-minimalist-sliding-doors-for-condos.html`
- Modify: `guides/malaysia-commercial-window-and-balcony-door-rfq-guide.html`
- Modify: `guides/malaysia-hotel-balcony-doors-for-hospitality-projects.html`
- Modify: `guides/indonesia-apartment-window-package-rfq-guide.html`
- Modify: `guides/indonesia-tropical-window-and-balcony-door-sourcing.html`
- Modify: `guides/indonesia-curtain-wall-systems-for-commercial-facades.html`
- Modify: `guides/index.html`
- Modify: `sitemap.html`
- Modify: `sitemap.xml`

- [ ] Add related-page links from cluster pages into the new Week 4 URLs.
- [ ] Add the new pages into `guides/index.html`.
- [ ] Add the new pages into both HTML and XML sitemaps.

### Task 5: Update roadmap docs and verify

**Files:**
- Modify: `seo/priority-market-execution-roadmap-2026-q2.md`
- Modify: `seo/keyword-roadmap-2026-q2.md`
- Modify: `seo/weekly-website-optimization-plan-2026-q2.md`

- [ ] Update the market execution roadmap to show the Week 4 supplier-guide batch as executed.
- [ ] Update the keyword roadmap so new keywords move from backlog into active coverage.
- [ ] Update the weekly execution plan so Week 4 is defined as a supplier-guide and product-relinking sprint.
- [ ] Run `xmllint --noout sitemap.xml`.
- [ ] Run `git diff --check`.

### Task 6: Sync to formal repo and publish

**Files:**
- Modify in mirror first, then sync matching files into `<jzz1-publish-worktree>`

- [ ] Sync the Week 4 files from the mirror workspace into the formal publish repo.
- [ ] Run the same XML and diff checks in the formal repo.
- [ ] Stage only the Week 4 target files.
- [ ] Commit with a Week 4 SEO batch message.
- [ ] Push to `origin/main`.

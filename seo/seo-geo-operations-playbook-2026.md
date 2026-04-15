# JZZ1 SEO / GEO Operations Playbook 2026

This file records the working rules, page patterns, audit checklist, and publishing process that have already been used on `www.jzz1.com`. It is intended as an internal reference for future weekly SEO and GEO work.

## 1. Current Site Strategy

### Domain and indexing rules

- Only use `https://www.jzz1.com/` as the canonical domain.
- Do not optimize or promote the apex domain as a separate target.
- Keep one canonical URL per intent page.
- If a page is low-value, duplicate, or only for navigation support, use `noindex,follow` instead of letting it compete with core landing pages.

### Current page types already proven useful

- Core product pages: `products/`
- Buying-intent guides: `guides/`
- Technical FAQ pages: `knowledge-base/`
- Trust and compliance pages: `technical-standards.html`, `certificates.html`
- Country landing pages: `singapore.html`, `malaysia.html`, `philippines.html`, `vietnam.html`, `thailand.html`

### Current optimization direction

- Build around buyer-intent long-tail queries, not only broad category terms.
- Combine `product + scenario`, `country + scenario`, and `standard + scenario`.
- Add visible specification tables and FAQ blocks to increase factual density.
- Use internal links to connect homepage, product hubs, guides, standards pages, and sitemaps.
- Keep content practical, engineering-oriented, and RFQ-friendly.

## 2. Core SEO / GEO Rules

### SEO rules

- One page should target one primary search intent.
- Use natural keyword variants, not keyword stuffing.
- Every important page must have:
  - unique `<title>`
  - unique `meta description`
  - canonical pointing to `https://www.jzz1.com/...`
  - `robots` rule that matches intent
  - one clear `<h1>`
- Every new strategic page must be linked from at least:
  - one relevant product page or hub
  - one guide or standards hub
  - `sitemap.html`
  - `sitemap.xml`

### GEO rules

- Use a direct answer in the opening section when possible.
- Put concrete numbers on the page:
  - opening size
  - glazing options
  - profile depth
  - hardware type
  - wind load
  - thermal values
  - finishing options
- Prefer comparison tables and specification tables over vague claims.
- Add FAQ sections that match how buyers ask questions in Google, Gemini, Perplexity, and LinkedIn.
- Keep brand and company facts consistent across pages.
- Where appropriate, mention standards and testing logic such as `AS2047`, `NFRC`, `impact-rated`, `passive house`, `coastal powder coating`.

## 3. Page Templates

### A. Product page template

Each core product page should include:

1. Clear buyer-facing intro paragraph
2. Use-case bullets or application sectors
3. Technical parameter table
4. Optional configuration or finish list
5. Technical FAQ section
6. FAQ schema
7. Internal links to related guides and standards pages

Recommended parameter table fields:

- Product type
- Frame material / profile thickness
- Glass options
- Surface finish
- Hardware options
- Opening style
- Typical application
- Customization scope
- Export support

### B. Guide page template

This is the preferred structure for long-tail ranking pages:

1. Title targeting one intent
2. Short introduction that states the scenario and buyer need
3. Section for project requirements or local conditions
4. Section for recommended product / specification logic
5. Parameter table or RFQ checklist
6. FAQ section
7. CTA pointing back to the relevant product page or contact page

Working guide formulas:

- `product + scenario`
- `country + product + scenario`
- `standard + product + scenario`
- `problem + solution`

Examples already used on the site:

- `Thailand coastal powder coated profiles`
- `Singapore balcony railing systems`
- `Malaysia commercial sunroom enclosures`
- `AS2047 bifold doors for Australia housing projects`
- `NFRC commercial windows for US projects`

### C. Technical FAQ page template

Use `knowledge-base/` pages for queries that are:

- highly specific
- comparison-driven
- problem-solving
- good for AI citation

Recommended structure:

1. Short definition or direct answer
2. 6 to 10 focused Q&A entries
3. One or more simple comparison or parameter tables
4. Links back to related product pages
5. FAQ schema

## 4. Weekly Operating Rhythm

### Minimum weekly target

- Publish or materially update 5 long-tail opportunities every week.

### Preferred operating order

1. Refresh one product page with better copy, parameters, and FAQs
2. Publish 1 to 2 guide pages around that product
3. Publish or expand one technical FAQ page
4. Add links from related hubs
5. Update `sitemap.html` and `sitemap.xml`

### Product expansion rule

For each core product family, maintain a queue of at least 5 usable long-tail keywords:

- windows
- doors
- profiles
- railings
- sunrooms
- uPVC windows and doors
- uPVC profiles

Use the roadmap files together with this playbook:

- `seo/keyword-roadmap-2026-q2.md`
- `seo/product-weekly-longtail-matrix-2026-q2.md`

## 5. Market Priorities

### Australia

Focus terms:

- `AS2047`
- energy efficiency
- bifold doors
- thermal break windows
- housing projects

### USA / Canada

Focus terms:

- `NFRC`
- impact-rated / hurricane
- passive house
- commercial windows
- coastal sliding doors

### Southeast Asia

Focus by market:

- Singapore: acoustic, Green Mark, minimalist systems
- Malaysia: hospitality, commercial enclosures, project supply
- Thailand: coastal, heat control, corrosion resistance
- Philippines: typhoon resistance, high wind pressure
- Vietnam: industrial and high-end residential demand

## 6. Content Writing Rules

- Write for buyers, architects, contractors, developers, and distributors.
- Avoid generic statements like `high quality` without proof or detail.
- Prefer specific phrases like:
  - `double glazed option`
  - `powder coated finish for coastal conditions`
  - `thermal break frame`
  - `shop drawing support`
  - `custom size and glazing configuration`
- Keep tone practical and export-oriented.
- Do not promise ranking outcomes.
- Do not create multiple pages with nearly identical intent just to inflate page count.

## 7. Internal Linking Rules

- Every new guide should link to at least one product page.
- Product pages should link back to the most relevant long-tail guides.
- Standards pages should surface standards-driven guides.
- Country pages should link to locally relevant scenario pages.
- Keep anchor text natural. Do not repeat one exact keyword on every link.

## 8. Structured Data Rules

### Product pages

- Add `Product` schema where appropriate.
- Add FAQ schema when the page contains visible FAQ content.
- Keep schema aligned with visible page text.

### FAQ and guide pages

- Use FAQ schema only when the questions and answers are visible on the page.
- Avoid fake review or rating markup.
- Prefer technical, informational, and business-useful structured content.

## 9. Audit Checklist Before Publishing

For every new or updated SEO page, check:

- unique title
- unique meta description
- canonical uses `https://www.jzz1.com/...`
- correct robots rule
- one H1 only
- page is linked from a crawlable hub
- page is added to `sitemap.html`
- page is added to `sitemap.xml`
- no broken internal links
- visible FAQ content matches FAQ schema
- parameter table is present if the page is product or engineering focused

## 10. Local Validation Commands

Run these commands from the publish repository:

```bash
git status --short
xmllint --noout sitemap.xml
git diff --check
```

Use `git status -sb` to confirm whether local `HEAD` is ahead of or equal to `origin/main`.

## 11. Publishing Process

1. Finish content edits
2. Recheck links and metadata
3. Validate `sitemap.xml`
4. Confirm no whitespace or patch errors with `git diff --check`
5. Commit with a clear message
6. Push to `origin main`
7. Confirm the local branch and `origin/main` point to the same commit

## 12. What Has Worked Best So Far

- Expanding from generic product copy into technical and scenario pages
- Adding parameter tables directly on product pages
- Adding technical FAQ sections and FAQ schema
- Building country-specific and standards-specific guide clusters
- Keeping all important pages discoverable through HTML and XML sitemaps
- Using `www` canonical consistency across the whole site

## 13. Next Recommended Work

- Continue publishing standards + scenario landing pages
- Add more case-study style pages with real project constraints
- Expand `projects.html` with crawlable text and internal links
- Continue weekly long-tail batches for every core product family
- Review underperforming pages and either improve, consolidate, or `noindex` them

## 14. Notes

- Indexing is never guaranteed. The goal is to improve crawlability, clarity, topical depth, and citation probability.
- Ranking improvement usually comes from clusters, internal links, factual density, and consistent publishing rhythm rather than one isolated page.
- This file should be updated whenever the workflow or page pattern changes materially.

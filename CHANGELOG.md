# Changelog - JZZ1 Architectural Windows & Doors

All notable changes to the `jzz1.com` website will be documented in this file.

## [Unreleased]

## [2.2.0] - 2026-10-13

### Added
- **GEO Knowledge Graph Expansion**: Comprehensive expansion of `llms.txt` incorporating all 44 technical guides across 5 categorised tracks (Procurement & Sourcing, Engineering Comparisons, Ocean Packing, Typologies, and Regional Routes).
- **AI "Answer-Ready" Block**: Executive quote summary deployed to `australia.html` detailing AS 2047-2014 SMK41678, AS/NZS 2208 CSi 7632, MD75S (ULS 4000 Pa, Water 600 Pa), and MD76A (ULS 3000 Pa) for direct AI citation.
- **Visible & Structured FAQ Section**: 8-item technical/procurement FAQ cards and corresponding `FAQPage` JSON-LD on `australia.html` covering wind load ratings, direct export without local fabricator, customs clearance/Form 15, alloy distinctions (6063-T5 vs 6061-T6), and BAL bushfire ratings.
- **International `hreflang` Cluster**: Global localization header cluster (`en-au`, `en-sg`, `en-my`, `en-id`, `en-ph`, `en-th`, `en-vn`, `fr`, `es`, `it`, `x-default`) deployed across 11 regional landing pages and `index.html`.
- **Enriched Product Schema**: `Product` JSON-LD schema enriched across all 19 `products/*.html` files with official manufacturer entity (`Jinan Jingzao New Materials Co., Ltd.`), architectural materials, test certifications, and USD currency offers.
- **Enriched Article Schema**: Added `datePublished` and `dateModified` (2026-10-13) with full legal publisher/author metadata across all 43 technical guides.
- **Enhanced `brand-facts.json`**: Upgraded with machine-readable entity dictionary, Jinan headquarters coordinates, certification test schedules, MOQ (10 sets), lead times (7-25 days), and export packaging protocols.
- **Sitemap & Robots Audit**: Audited 100% indexable URL coverage in `sitemap.xml` (119 URLs) and synchronized all `<lastmod>` timestamps to `2026-10-13`. Confirmed open crawl directives in `robots.txt`.

## [2.1.0] - 2026-10-13

### Added
- Integrated Australian window and door standard `AS 2047:2014` (Intertek SAI Global StandardsMark Licence `SMK41678`) covering MD75S and MD76A systems.
- Integrated Australia & New Zealand safety glazing standard `AS/NZS 2208:1996` (CSi PAS-Mark Certificate `7632`, JAS-ANZ / IAF MLA certified, anti-scan protected).
- Created dedicated Australia & Oceania export hub `australia.html` detailing NCC/BCA wind zones (N1–N5, C1–C2), bushfire ratings (BAL-12.5 to BAL-40), and 5-layer ocean export crating.
- Re-architected `certificates.html` with interactive lightbox modals, testing data matrices, and unredacted compliance document request dispatch.
- Added Australia target entities to GEO/AIO knowledge infrastructure (`llms.txt`, `llms-full.txt`, `brand-facts.json`).

### Changed
- Replaced outdated hero image with high-end modern architectural villa facade featuring thermal break sliding glass walls.
- Revamped full brand visual identity with minimalist champagne-gold geometric "JZ" monogram across header, footer, OpenGraph cards (`og-logo.svg`), and multi-resolution favicons (`favicon-48.png`, `favicon-32.png`, `favicon.ico`, `apple-touch-icon.png`).
- Re-styled brand typography and UI badge components.

### Security
- Created backup tag `backup-pre-australia-cert-20261013` prior to production deployment.
- Deployed anti-scan watermark overlays on certificate visual assets.

## [2.0.0] - 2026-09-16

### Added
- Complete site aesthetics refresh and modern architectural layout.
- Zero-loss multi-channel inquiry dispatch with structured RFQ WhatsApp integration.
- SEO CTR enhancement and Perplexity / Google AI Overviews knowledge graph ingestion.

## [1.0.0] - 2026-05-14

### Added
- Initial release of JZZ1 architectural aluminum systems global export website.

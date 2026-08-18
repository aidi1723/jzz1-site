#!/usr/bin/env bash
set -euo pipefail

pages=(
  products/outdoor-aluminum-systems.html
  products/aluminum-garden-fences.html
  products/aluminum-garden-gates.html
)

routes=(
  /products/outdoor-aluminum-systems.html
  /products/aluminum-garden-fences.html
  /products/aluminum-garden-gates.html
)

images=(
  outdoor-systems-villa-terrace
  aluminum-railing-lakeside-deck
  aluminum-railing-villa-deck
  aluminum-railing-waterfront-deck
  aluminum-railing-modern-stair
  aluminum-railing-factory-finished
  aluminum-railing-profile-detail
  aluminum-garden-fence-villa-front
  aluminum-garden-fence-perimeter
  aluminum-garden-fence-lawn
  aluminum-garden-fence-post-detail
  aluminum-garden-gate-park
  aluminum-garden-gate-villa-front
  aluminum-garden-gate-panel-sample
  aluminum-garden-gate-components
  aluminum-garden-gate-stair-access
)

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

for page in "${pages[@]}"; do
  [[ -s "$page" ]] || fail "missing page $page"
  [[ "$(rg -o '<h1[ >]' "$page" | wc -l | tr -d ' ')" == "1" ]] || fail "$page must contain one H1"
  rg -q '<meta name="robots" content="index,follow"' "$page" || fail "$page robots"
  rg -q '<link rel="canonical" href="https://www.jzz1.com/' "$page" || fail "$page canonical"
  rg -q '"@type":"Product"' "$page" || fail "$page Product schema"
  rg -q '"@type":"BreadcrumbList"' "$page" || fail "$page breadcrumb schema"
  rg -q '"@type":"FAQPage"' "$page" || fail "$page FAQ schema"
  rg -q 'https://wa.me/8613562676792' "$page" || fail "$page WhatsApp CTA"
  rg -q 'mailto:info@jzz1.com' "$page" || fail "$page email CTA"
done

for route in "${routes[@]}"; do
  count="$(rg -l -F "$route" --glob '*.html' . | wc -l | tr -d ' ')"
  (( count >= 5 )) || fail "$route has only $count HTML entry points"
  rg -Fq "https://www.jzz1.com$route" sitemap.xml || fail "$route missing from sitemap.xml"
  rg -Fq "$route" sitemap.html || fail "$route missing from sitemap.html"
done

for name in "${images[@]}"; do
  for suffix in 1200.jpg 640.webp 1200.webp; do
    [[ -s "images/outdoor-systems/$name-$suffix" ]] || fail "missing image $name-$suffix"
  done
done

xmllint --noout sitemap.xml
bash scripts/privacy-scan.sh
printf 'PASS: outdoor aluminum systems verification\n'

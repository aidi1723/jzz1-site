#!/usr/bin/env python3
"""
Upgrade Product Schema for jzz1.com product pages
Adds: @id, manufacturer, additionalProperty (B2B attributes)
"""

import re
import json
from pathlib import Path

# Product-specific configurations
PRODUCT_CONFIG = {
    "windows.html": {
        "name": "Aluminum Windows",
        "description": "Custom aluminum windows with thermal break or non-thermal series for different climates and budgets. Configurable glass and hardware. OEM/ODM available.",
        "category": "Aluminum Windows",
        "properties": [
            {"name": "Profile System", "value": "Thermal break / Non-thermal aluminum"},
            {"name": "Glass Options", "value": "Single / Double / Triple glazing; Low-E; Laminated"},
            {"name": "Surface Finish", "value": "Powder coating (RAL colors) / Anodizing"},
            {"name": "MOQ", "value": "10 sets"},
            {"name": "Lead Time", "value": "7–25 days"},
            {"name": "OEM/ODM", "value": "Supported"}
        ]
    },
    "doors.html": {
        "name": "Aluminum Doors",
        "description": "Aluminum entry doors, sliding doors and folding door systems. Thermal break options, multi-point locks, and custom sizes for residential and commercial projects.",
        "category": "Aluminum Doors",
        "properties": [
            {"name": "Door Types", "value": "Entry / Sliding / Folding / Lift-and-slide"},
            {"name": "Profile System", "value": "Thermal break / Non-thermal aluminum"},
            {"name": "Locking System", "value": "Multi-point locks available"},
            {"name": "Glass Options", "value": "Double / Triple glazing; Low-E; Laminated"},
            {"name": "Surface Finish", "value": "Powder coating (RAL colors) / Anodizing"},
            {"name": "MOQ", "value": "10 sets"},
            {"name": "Lead Time", "value": "7–25 days"},
            {"name": "OEM/ODM", "value": "Supported"}
        ]
    },
    "profiles.html": {
        "name": "Aluminum Profiles",
        "description": "Custom aluminum extrusion profiles for windows, doors, curtain walls and industrial applications. Multiple alloys, finishes and fabrication services available.",
        "category": "Aluminum Profiles",
        "properties": [
            {"name": "Alloy Series", "value": "6063-T5 / 6063-T6 / 6061-T6"},
            {"name": "Profile Types", "value": "Window / Door / Curtain wall / Industrial"},
            {"name": "Surface Finish", "value": "Mill finish / Anodizing / Powder coating / Electrophoresis"},
            {"name": "Fabrication", "value": "Cutting / Drilling / CNC machining / Bending"},
            {"name": "MOQ", "value": "500 kg per profile"},
            {"name": "Lead Time", "value": "10–20 days"},
            {"name": "OEM/ODM", "value": "Supported"}
        ]
    },
    "railings.html": {
        "name": "Aluminum Railings & Balustrades",
        "description": "Aluminum railing and balustrade systems for balconies, stairs and terraces. Glass infill options, powder coated finishes, and modular installation design.",
        "category": "Aluminum Railings",
        "properties": [
            {"name": "Railing Types", "value": "Balcony / Stair / Terrace / Pool fence"},
            {"name": "Infill Options", "value": "Glass / Cable / Bar / Solid panel"},
            {"name": "Mounting Style", "value": "Top mount / Side mount / Face mount / Frameless glass"},
            {"name": "Surface Finish", "value": "Powder coating (RAL colors) / Anodizing"},
            {"name": "MOQ", "value": "20 meters"},
            {"name": "Lead Time", "value": "10–20 days"},
            {"name": "OEM/ODM", "value": "Supported"}
        ]
    },
    "sunrooms.html": {
        "name": "Aluminum Sunrooms & Conservatories",
        "description": "Modular aluminum sunroom and conservatory systems. Thermal break frames, polycarbonate or glass roofing, customizable dimensions for residential gardens and commercial spaces.",
        "category": "Aluminum Sunrooms",
        "properties": [
            {"name": "Structure Type", "value": "Freestanding / Lean-to / Gable / Victorian"},
            {"name": "Frame System", "value": "Thermal break aluminum"},
            {"name": "Roofing Options", "value": "Polycarbonate panels / Tempered glass / Laminated glass"},
            {"name": "Wall Options", "value": "Glass panels / Aluminum panels / Combination"},
            {"name": "Surface Finish", "value": "Powder coating (RAL colors) / Anodizing"},
            {"name": "MOQ", "value": "1 set (custom size)"},
            {"name": "Lead Time", "value": "15–30 days"},
            {"name": "OEM/ODM", "value": "Supported"}
        ]
    }
}

def create_product_schema(filename, config):
    """Generate enhanced Product schema JSON"""
    slug = filename.replace('.html', '')
    url = f"https://www.jzz1.com/products/{filename}"
    
    schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "@id": f"{url}#product",
        "name": config["name"],
        "description": config["description"],
        "url": url,
        "brand": {
            "@type": "Brand",
            "name": "JZZ1"
        },
        "manufacturer": {
            "@id": "https://www.jzz1.com/#org"
        },
        "category": config["category"],
        "additionalProperty": [
            {"@type": "PropertyValue", "name": prop["name"], "value": prop["value"]}
            for prop in config["properties"]
        ],
        "offers": {
            "@type": "Offer",
            "@id": f"{url}#offer",
            "url": url,
            "availability": "https://schema.org/InStock",
            "itemCondition": "https://schema.org/NewCondition",
            "seller": {
                "@id": "https://www.jzz1.com/#org"
            }
        }
    }
    return schema

def upgrade_file(filepath, config):
    """Upgrade a single product HTML file"""
    content = filepath.read_text(encoding='utf-8')
    
    # Generate new Product schema
    new_schema = create_product_schema(filepath.name, config)
    new_schema_json = json.dumps(new_schema, indent=2, ensure_ascii=False)
    
    # Pattern to find existing Product schema
    pattern = r'<script type="application/ld+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"Product"[^}]*\}(?:\s*,?\s*"[^"]*":\s*[^}]*\})*\s*</script>'
    
    # Replace old Product schema with new one
    new_script = f'<script type="application/ld+json">\n{new_schema_json}\n</script>'
    
    # Try to find and replace
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_script + content[match.end():]
        print(f"✓ Replaced Product schema in {filepath.name}")
    else:
        # If pattern didn't match, try simpler approach - find between specific comments or markers
        print(f"⚠ Pattern not found in {filepath.name}, trying alternative...")
        # Look for the Product script block more loosely
        alt_pattern = r'(<script type="application/ld+json">\s*\{[^}]*"@type":\s*"Product"[^<]*\}\s*</script>)'
        match = re.search(alt_pattern, content, re.DOTALL)
        if match:
            content = content[:match.start()] + new_script + content[match.end():]
            print(f"✓ Replaced Product schema in {filepath.name} (alt method)")
        else:
            print(f"✗ Could not find Product schema in {filepath.name}")
            return False
    
    # Write back
    filepath.write_text(content, encoding='utf-8')
    return True

def main():
    products_dir = Path("/Users/aidi/.openclaw/workspace/jzz1-site/products")
    
    success_count = 0
    for filename, config in PRODUCT_CONFIG.items():
        filepath = products_dir / filename
        if filepath.exists():
            if upgrade_file(filepath, config):
                success_count += 1
        else:
            print(f"✗ File not found: {filename}")
    
    print(f"\n{'='*50}")
    print(f"Upgraded {success_count}/{len(PRODUCT_CONFIG)} product pages")

if __name__ == "__main__":
    main()

# Bulgaria - Cities and Locations

> Complete database of Bulgarian cities, municipalities, and administrative-territorial units with EKATTE codes.

**Module:** `l10n_bg_city` | **Version:** 18.0.1.0.0 | **License:** LGPL-3 | **Category:** Localization

## Overview

Complete database of Bulgarian cities, municipalities, and administrative-territorial units with EKATTE codes.

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `base_address_extended`, `contacts` | — |

## New models

- `res.city.types`

## Extended models

- `res.city` (inherited)
- `res.country.state` (inherited)

## Views

- `views/res_city_view.xml`

## Seeded data

- `data/res.city.cityhall.csv`
- `data/res.city.csv`
- `data/res.city.municipality.csv`
- `data/res.country.state.csv`
- `data/res_city_types.xml`
- `data/res_country_data.xml`
- `data/src`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_city' or via CLI:
odoo -i l10n_bg_city -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

# Partner Multilang

> Automatic multilingual partner names with intelligent
            transliteration and language detection.

**Module:** `partner_multilang` | **Version:** 18.0.3.0.4 | **License:** LGPL-3 | **Category:** Localization

## Overview

Automatic multilingual partner names with intelligent
            transliteration and language detection.

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `contacts` | — |

**External Python packages:** `transliterate`, `unidecode`, `lingua`

## New models

- `raw`
- `res.company`
- `res.partner`
- `res.transliterate.mixin`

## Extended models

- `ir.binary` (inherited)
- `res.config.settings` (inherited)
- `res.country.state` (inherited)
- `res.lang` (inherited)

## Views

- `views/res_config_settings_view.xml`
- `views/res_lang_views.xml`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'partner_multilang' or via CLI:
odoo -i partner_multilang -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)
- Module tests: `tests/`

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

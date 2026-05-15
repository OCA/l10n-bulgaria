# Bulgaria - Report Theme Sections

> Professional report theme with modular section-based layout for Bulgarian business documents.

**Module:** `l10n_bg_report_theme` | **Version:** 18.0.5.0.4 | **License:** LGPL-3 | **Category:** ?

## Overview

Professional report theme with modular section-based layout for Bulgarian business documents.

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `web`, `sale`, `account`, `stock`, `purchase` | `l10n_bg_config` |

**External Python packages:** `webcolors`

## Extended models

- `base.document.layout` (inherited)
- `ir.actions.report` (inherited)
- `res.company` (inherited)

## Views

- `views/base_document_layout_views.xml`
- `views/ir_action_report_templates.xml`
- `views/purchase_order_templates.xml`
- `views/purchase_quotation_templates.xml`
- `views/report_invoice.xml`
- `views/report_templates.xml`
- `views/res_company_views.xml`

## Seeded data

- `data/report_layout.xml`
- `data/report_paperformat_data.xml`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_report_theme' or via CLI:
odoo -i l10n_bg_report_theme -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

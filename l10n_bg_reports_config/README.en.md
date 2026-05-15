# Bulgarian Accounting Reports Configuration

> Configuration module for Bulgarian Accounting Reports - Odoo 18.0 specific views and wizards

**Module:** `l10n_bg_reports_config` | **Version:** 18.0.9.0.2 | **License:** LGPL-3 | **Category:** Accounting/Localizations/Reporting

## Overview

Configuration module for Bulgarian Accounting Reports - Odoo 18.0 specific views and wizards

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `account` | `l10n_bg_reports_audit`, `l10n_bg_config`, `l10n_bg_ledger` |

## Extended models

- `l10n.bg.vat.ratio.history` (inherited)

## Views

- `views/account_account_tag_views.xml`
- `views/account_bg_partner.xml`
- `views/account_bg_products.xml`
- `views/account_bg_vat_line_purchase_reports.xml`
- `views/account_bg_vat_line_sale_reports.xml`
- `views/account_bg_vat_line_vies_reports.xml`
- `views/account_menuitem.xml`
- `views/account_move_views.xml`
- `views/product_view.xml`
- `views/res_company_history_intrastat.xml`
- `views/res_company_history_vat.xml`
- `views/res_company_views.xml`
- `views/res_config_view.xml`
- `views/res_partner.xml`

## Seeded data

- `data/account_account_tag_function.xml`
- `data/settings.xml`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_reports_config' or via CLI:
odoo -i l10n_bg_reports_config -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

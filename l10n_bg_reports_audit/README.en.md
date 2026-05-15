# Bulgarian Accounting Reports Base

> Technical base module for Bulgarian accounting reports - SQL queries and tag configurations

**Module:** `l10n_bg_reports_audit` | **Version:** 18.0.12.0.3 | **License:** LGPL-3 | **Category:** Accounting/Localizations/Reporting

## Overview

Technical base module for Bulgarian accounting reports - SQL queries and tag configurations

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `account` | `l10n_bg`, `l10n_bg_ledger`, `l10n_bg_config` |

## New models

- `account.account.tag`
- `display_name`
- `l10n.bg.export.file`
- `l10n.bg.intrastat.threshold`
- `l10n.bg.vat.ratio.history`
- `res.partner`

## Extended models

- `account.journal` (inherited)
- `account.move` (inherited)
- `account.move.line` (inherited)
- `ir.actions.report` (inherited)
- `product.template` (inherited)
- `res.company` (inherited)
- `res.config.settings` (inherited)
- `res.partner` (inherited)

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_reports_audit' or via CLI:
odoo -i l10n_bg_reports_audit -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

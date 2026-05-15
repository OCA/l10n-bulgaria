# Bulgaria localization Configuration

> This module allows you to install and configure all
        the localization modules related to Bulgaria.

**Module:** `l10n_bg_config` | **Version:** 18.0.8.0.5 | **License:** LGPL-3 | **Category:** Localization

## Overview

This module allows you to install and configure all
        the localization modules related to Bulgaria.

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `account`, `base_vat` | `l10n_bg`, `l10n_bg_ledger`, `l10n_bg_tariff_code` |

**External Python packages:** `xmltodict`

## New models

- `account.move`
- `l10n.bg.config.mixin`
- `res.partner`

## Extended models

- `account.account.tag` (inherited)
- `account.chart.template` (inherited)
- `ir.module.module` (inherited)
- `res.company` (inherited)
- `res.config.settings` (inherited)
- `res.country` (inherited)

## Views

- `views/account_account_tag_views.xml`
- `views/account_move_views.xml`
- `views/partner_view.xml`
- `views/res_company_views.xml`
- `views/res_config_view.xml`

## Seeded data

- `data/res_lang_data.xml`
- `data/template`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_config' or via CLI:
odoo -i l10n_bg_config -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)
- Module tests: `tests/`

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

# ErpNet.FP Fiscal Printer for odoo

> Integration with ERP.BG fiscal printers through ErpNet.FP server.
        Supports real-time fiscal receipt printing and status monitoring.

**Module:** `l10n_bg_erp_net_fp` | **Version:** 18.0.7.0.2 | **License:** LGPL-3 | **Category:** Point Of Sale

## Overview

Integration with ERP.BG fiscal printers through ErpNet.FP server.
        Supports real-time fiscal receipt printing and status monitoring.

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `bus`, `mail`, `point_of_sale`, `account` | — |

## New models

- `fiscal.printer.device`
- `fiscal.printer.response`
- `fiscal.printer.status`
- `request_id`

## Extended models

- `account.tax.group` (inherited)
- `fiscal.printer.device` (inherited)
- `pos.config` (inherited)
- `pos.order` (inherited)
- `pos.printer` (inherited)
- `pos.session` (inherited)
- `res.config.settings` (inherited)

## Views

- `views/account_tax_views.xml`
- `views/fiscal_printer_device_views.xml`
- `views/fiscal_printer_response_views.xml`
- `views/menu_items.xml`
- `views/pos_config_view.xml`
- `views/pos_order_view.xml`
- `views/pos_printer_views.xml`
- `views/pos_session_view.xml`
- `views/res_config_settings_views.xml`

## Wizards

- `wizard/fiscal_cash_operation_wizard.py`

## Controllers

- `controllers/main.py`

## Seeded data

- `data/fiscal_printer_device_cron.xml`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_erp_net_fp' or via CLI:
odoo -i l10n_bg_erp_net_fp -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

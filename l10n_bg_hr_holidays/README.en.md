# Bulgaria - HR Holidays

> Bulgarian localization for HR Holidays

**Module:** `l10n_bg_hr_holidays` | **Version:** 18.0.1.0.4 | **License:** LGPL-3 | **Category:** Human Resources/Time Off

## Overview

Bulgarian localization for HR Holidays

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `hr_contract`, `hr_holidays` | `l10n_bg` |

## New models

- `nssi.leave.reason`

## Extended models

- `hr.leave` (inherited)
- `hr.leave.type` (inherited)

## Views

- `views/hr_leave_type_views.xml`
- `views/hr_leave_views.xml`
- `views/l10n_bg_nssi_leave_reason.xml`

## Seeded data

- `data/hr_holidays_data.xml`
- `data/nssi.leave.reason.csv`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_hr_holidays' or via CLI:
odoo -i l10n_bg_hr_holidays -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

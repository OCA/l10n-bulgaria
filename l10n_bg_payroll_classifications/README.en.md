# Bulgarian HR Payroll Classifications

> Bulgarian localization for HR payroll with NKPD and Economic Activity classifications

**Module:** `l10n_bg_payroll_classifications` | **Version:** 18.0.5.0.2 | **License:** LGPL-3 | **Category:** Human Resources/Localization

## Overview

Bulgarian localization for HR payroll with NKPD and Economic Activity classifications

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `hr` | — |

## New models

- `bg.hr.payroll.economic.activity`
- `bg.hr.payroll.ncop.classification`

## Extended models

- `hr.job` (inherited)

## Views

- `views/bg_mod_economic_activity.xml`
- `views/bg_ncop_classification.xml`
- `views/hr_job_views.xml`
- `views/hr_menus.xml`

## Seeded data

- `data/bg_hr_payroll_economic_activity`
- `data/bg_hr_payroll_ncop_classification`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_payroll_classifications' or via CLI:
odoo -i l10n_bg_payroll_classifications -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

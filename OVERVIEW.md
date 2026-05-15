# l10n-bulgaria-oca — Bulgaria Localization (OCA Variants)

> LGPL-3 OCA-compatible mirrors of community modules. 25 modules.

## Scope vs main repo

Same scope as [`l10n-bulgaria`](https://github.com/rosenvladimirov/l10n-bulgaria) (CE) but adapted to OCA conventions (linting, structure, dependencies). Used when you want strict OCA compliance.

## When to pick OCA over CE

- OCA CI / pre-commit pipeline required
- Need only the subset that OCA carries (25 modules vs 36)
- Project policy mandates OCA-only addons

## Module catalog

### Foundation
- `l10n_bg_config` — central configuration backbone
- `partner_multilang` — JSONB multilingual partner names
- `l10n_bg_multilang` — multi-language support
- `l10n_bg_address_extended` — precise BG addresses
- `markdown_viewer_locale` — locale-aware Markdown viewer

### Geographic
- `l10n_bg_city` — ЕКАТТЕ database
- `l10n_bg_tax_offices` — NRA directorate registry

### Accounting & Reports
- `l10n_bg_reports_audit` — SQL views + NRA tag framework
- `l10n_bg_reports_config` — accounting reports UI
- `l10n_bg_report_theme` — section-based report layout
- `l10n_bg_invoice_copy` — ОРИГИНАЛ/КОПИЕ watermark
- `l10n_bg_report_stock` — accepted delivery documents
- `l10n_bg_account_reconcile_patch` — JSONB regexp fix

### Banking
- `l10n_bg_bank_wallet` — encrypted credential storage
- `l10n_bg_account_statement_import_mt940` — MT940 import

### NRA / Trade Registry / TARIC
- `l10n_bg_company_registry` — Trade Registry API
- `l10n_bg_tariff_code` — TARIC/HS/CN codes
- `taric_ai_classifier` — AI-powered TARIC classification

### HR
- `l10n_bg_hr_holidays` — 61 BG leave types
- `l10n_bg_payroll_classifications` — NKPD + KID classifications

### Fiscal Printers
- `l10n_bg_erp_net_fp` — ErpNet.FP integration

### MRP / Multilang
- `l10n_bg_mrp_multilang`
- `l10n_bg_project_multilang`

### Stock / Sale
- `l10n_bg_sale_order_delivery_note`
- `l10n_bg_stock_sale_line_description`

## Per-module docs

`<module>/README.md` (handwritten) or auto-generated `README.en.md` + `README.bg.md`.

## Sister repositories

- [`l10n-bulgaria`](https://github.com/rosenvladimirov/l10n-bulgaria) — primary CE source
- [`l10n-bulgaria-ee`](https://github.com/rosenvladimirov/l10n-bulgaria-ee) — Enterprise add-ons (OPL-1)
- [`l10n-bulgaria-expert`](https://github.com/rosenvladimirov/l10n-bulgaria-expert) — Specialized (OPL-1)
- [`l10n-bulgaria-enterprise`](https://github.com/rosenvladimirov/l10n-bulgaria-enterprise) — Odoo Enterprise (OPL-1)

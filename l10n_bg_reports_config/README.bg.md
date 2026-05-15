# Bulgarian Accounting Reports Configuration

> Конфигурация на счетоводните отчети

**Модул:** `l10n_bg_reports_config` | **Версия:** 18.0.9.0.2 | **Лиценз:** LGPL-3 | **Категория:** Accounting/Localizations/Reporting

## Описание

Конфигурация на счетоводните отчети

## Зависимости

| Odoo базови | Българска локализация |
|---|---|
| `account` | `l10n_bg_reports_audit`, `l10n_bg_config`, `l10n_bg_ledger` |

## Разширени модели

- `l10n.bg.vat.ratio.history` (extension)

## Изгледи (views)

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

## Заредени данни

- `data/account_account_tag_function.xml`
- `data/settings.xml`

## Инсталация

```bash
# Добавете пътя на репозиторията в Odoo addons_path,
# след това инсталирайте през UI Apps → търсене 'l10n_bg_reports_config' или през CLI:
odoo -i l10n_bg_reports_config -d <вашата_база> --stop-after-init
```

## Свързани

- Главно репозитори: [`l10n-bulgaria-oca`](../README.md)

---
*Генериран 2026-05-15 от `__manifest__.py` + source layout. Ръчно обогатяване за пълен handbook.*

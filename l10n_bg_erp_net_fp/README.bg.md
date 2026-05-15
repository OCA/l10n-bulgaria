# ErpNet.FP Fiscal Printer for odoo

> ErpNet.FP фискални принтери

**Модул:** `l10n_bg_erp_net_fp` | **Версия:** 18.0.7.0.2 | **Лиценз:** LGPL-3 | **Категория:** Point Of Sale

## Описание

ErpNet.FP фискални принтери

## Зависимости

| Odoo базови | Българска локализация |
|---|---|
| `bus`, `mail`, `point_of_sale`, `account` | — |

## Нови модели

- `fiscal.printer.device`
- `fiscal.printer.response`
- `fiscal.printer.status`
- `request_id`

## Разширени модели

- `account.tax.group` (extension)
- `fiscal.printer.device` (extension)
- `pos.config` (extension)
- `pos.order` (extension)
- `pos.printer` (extension)
- `pos.session` (extension)
- `res.config.settings` (extension)

## Изгледи (views)

- `views/account_tax_views.xml`
- `views/fiscal_printer_device_views.xml`
- `views/fiscal_printer_response_views.xml`
- `views/menu_items.xml`
- `views/pos_config_view.xml`
- `views/pos_order_view.xml`
- `views/pos_printer_views.xml`
- `views/pos_session_view.xml`
- `views/res_config_settings_views.xml`

## Помощници (wizards)

- `wizard/fiscal_cash_operation_wizard.py`

## Контролери

- `controllers/main.py`

## Заредени данни

- `data/fiscal_printer_device_cron.xml`

## Инсталация

```bash
# Добавете пътя на репозиторията в Odoo addons_path,
# след това инсталирайте през UI Apps → търсене 'l10n_bg_erp_net_fp' или през CLI:
odoo -i l10n_bg_erp_net_fp -d <вашата_база> --stop-after-init
```

## Свързани

- Главно репозитори: [`l10n-bulgaria-oca`](../README.md)

---
*Генериран 2026-05-15 от `__manifest__.py` + source layout. Ръчно обогатяване за пълен handbook.*

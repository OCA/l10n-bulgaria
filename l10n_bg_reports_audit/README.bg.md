# Bulgarian Accounting Reports Base

> База за счетоводните отчети — SQL views + НАП тагове

**Модул:** `l10n_bg_reports_audit` | **Версия:** 18.0.12.0.3 | **Лиценз:** LGPL-3 | **Категория:** Accounting/Localizations/Reporting

## Описание

База за счетоводните отчети — SQL views + НАП тагове

## Зависимости

| Odoo базови | Българска локализация |
|---|---|
| `account` | `l10n_bg`, `l10n_bg_ledger`, `l10n_bg_config` |

## Нови модели

- `account.account.tag`
- `display_name`
- `l10n.bg.export.file`
- `l10n.bg.intrastat.threshold`
- `l10n.bg.vat.ratio.history`
- `res.partner`

## Разширени модели

- `account.journal` (extension)
- `account.move` (extension)
- `account.move.line` (extension)
- `ir.actions.report` (extension)
- `product.template` (extension)
- `res.company` (extension)
- `res.config.settings` (extension)
- `res.partner` (extension)

## Инсталация

```bash
# Добавете пътя на репозиторията в Odoo addons_path,
# след това инсталирайте през UI Apps → търсене 'l10n_bg_reports_audit' или през CLI:
odoo -i l10n_bg_reports_audit -d <вашата_база> --stop-after-init
```

## Свързани

- Главно репозитори: [`l10n-bulgaria-oca`](../README.md)

---
*Генериран 2026-05-15 от `__manifest__.py` + source layout. Ръчно обогатяване за пълен handbook.*

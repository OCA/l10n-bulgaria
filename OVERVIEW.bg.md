# l10n-bulgaria-oca — Българска локализация (OCA варианти)

> LGPL-3 OCA-съвместими mirrors на community модулите. 25 модула.

## Обхват vs main repo

Същият обхват като [`l10n-bulgaria`](https://github.com/rosenvladimirov/l10n-bulgaria) (CE), но адаптиран към OCA конвенциите (линтинг, структура, зависимости). Използва се когато се изисква стриктно OCA съответствие.

## Кога да изберете OCA пред CE

- OCA CI / pre-commit pipeline нужен
- Нужна е само частта която OCA носи (25 vs 36 модула)
- Проектна политика изисква само OCA addons

## Каталог на модулите

### Основа
- `l10n_bg_config` — централна конфигурация
- `partner_multilang` — JSONB многоезични partner имена
- `l10n_bg_address_extended` — прецизни БГ адреси
- `markdown_viewer_locale` — преглед на локализирани Markdown

### Географски

### Счетоводство & Отчети
- `l10n_bg_invoice_copy` — ОРИГИНАЛ/КОПИЕ воден знак
- `l10n_bg_report_stock` — приемно-предавателни документи
- `l10n_bg_account_reconcile_patch` — JSONB regexp fix

### Банкови
- `l10n_bg_account_statement_import_mt940` — MT940 импорт

### НАП / Търговски регистър / TARIC
- `taric_ai_classifier` — AI TARIC класификатор

### Личен състав

### Фискални принтери
- `l10n_bg_erp_net_fp` — ErpNet.FP интеграция

### MRP / Многоезичност

### Stock / Sale
- `l10n_bg_stock_sale_line_description`

## Документация на модул

`<module>/README.md` (ръчно) или авто-генерирани `README.en.md` + `README.bg.md`.

## Свързани репозитори

- [`l10n-bulgaria`](https://github.com/rosenvladimirov/l10n-bulgaria) — основен CE източник
- [`l10n-bulgaria-ee`](https://github.com/rosenvladimirov/l10n-bulgaria-ee) — Enterprise (OPL-1)
- [`l10n-bulgaria-expert`](https://github.com/rosenvladimirov/l10n-bulgaria-expert) — Специализирани (OPL-1)
- [`l10n-bulgaria-enterprise`](https://github.com/rosenvladimirov/l10n-bulgaria-enterprise) — Odoo Enterprise (OPL-1)

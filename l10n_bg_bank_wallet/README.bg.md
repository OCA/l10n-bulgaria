# Bulgarian Banking Integration - Crypto Wallet

> Криптирано хранилище за банкови ключове и API токени

**Модул:** `l10n_bg_bank_wallet` | **Версия:** 18.0.1.0.2 | **Лиценз:** LGPL-3 | **Категория:** Localization

## Описание

Криптирано хранилище за банкови ключове и API токени

## Зависимости

| Odoo базови | Българска локализация |
|---|---|
| `web` | — |

**Python пакети:** `cryptography`

## Нови модели

- `crypto.wallet`
- `name`

## Разширени модели

- `res.users` (extension)

## Изгледи (views)

- `views/l10n_bg_crypto_wallet.xml`

## Инсталация

```bash
# Добавете пътя на репозиторията в Odoo addons_path,
# след това инсталирайте през UI Apps → търсене 'l10n_bg_bank_wallet' или през CLI:
odoo -i l10n_bg_bank_wallet -d <вашата_база> --stop-after-init
```

## Свързани

- Главно репозитори: [`l10n-bulgaria-oca`](../README.md)

---
*Генериран 2026-05-15 от `__manifest__.py` + source layout. Ръчно обогатяване за пълен handbook.*

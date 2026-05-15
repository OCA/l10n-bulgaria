# Bulgarian Banking Integration - Crypto Wallet

> Secure storage of cryptographic keys and passwords for banking integrations

**Module:** `l10n_bg_bank_wallet` | **Version:** 18.0.1.0.2 | **License:** LGPL-3 | **Category:** Localization

## Overview

Secure storage of cryptographic keys and passwords for banking integrations

## Dependencies

| Odoo core | Bulgarian-localization |
|---|---|
| `web` | — |

**External Python packages:** `cryptography`

## New models

- `crypto.wallet`
- `name`

## Extended models

- `res.users` (inherited)

## Views

- `views/l10n_bg_crypto_wallet.xml`

## Installation

```bash
# Add this repository's path to your Odoo addons_path,
# then install via UI Apps → search 'l10n_bg_bank_wallet' or via CLI:
odoo -i l10n_bg_bank_wallet -d <your_database> --stop-after-init
```

## See also

- Parent repository: [`l10n-bulgaria-oca`](../README.md)

---
*Generated 2026-05-15 from `__manifest__.py` + source layout. Hand-enrich for full handbook coverage.*

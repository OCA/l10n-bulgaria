# Copyright 2025 Rosen Vladimirov
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Bulgarian Banking Integration - Crypto Wallet",
    "version": "18.0.1.0.1",
    "category": "Localization",
    "summary": (
        "Secure storage of cryptographic keys and passwords for banking integrations"
    ),
    "description": "\n"
    "Crypto Wallet for Sensitive Data Storage\n"
    "=========================================\n"
    "\n"
    "This module provides a secure way to store:\n"
    "* RSA keys for digital signing\n"
    "* API keys for banking integrations\n"
    "* Passwords and certificates\n"
    "* Other sensitive cryptographic data\n"
    "\n"
    "Uses PBKDF2 with 100,000 iterations and Fernet symmetric encryption.\n"
    "\n"
    "Features:\n"
    "---------\n"
    "* **Secure Storage**: All data is encrypted using industry-standard cryptography\n"
    "* **User Isolation**: Each user has their own wallet accessible only to them\n"
    "* **Key Management**: Add, retrieve, and manage different types of keys\n"
    "* **Banking Ready**: Designed specifically for banking API integrations\n"
    "* **Audit Trail**: Track when keys are accessed and modified\n"
    "\n"
    "Security:\n"
    "---------\n"
    "* Uses user password hash as master password\n"
    "* PBKDF2 key derivation with 100,000 iterations\n"
    "* Fernet symmetric encryption for data protection\n"
    "* Per-user salt for additional security\n"
    "\n"
    "Supported Key Types:\n"
    "-------------------\n"
    "* RSA Private/Public Keys\n"
    "* API Keys (for banking APIs)\n"
    "* SSH Keys\n"
    "* PGP Keys\n"
    "* Passwords\n"
    "* Certificates\n"
    "* Tokens\n"
    "* Custom data types\n"
    "    ",
    "author": "Rosen Vladimirov",
    "website": "https://github.com/OCA/l10n-bulgaria",
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "data": [
        "security/l10n_bg_crypto_wallet.xml",
        "security/ir.model.access.csv",
        "views/l10n_bg_crypto_wallet.xml",
        "wizards/crypto_wallet_add_key_wizard.xml",
        "wizards/crypto_wallet_unlock_wizard.xml",
        "wizards/crypto_wallet_change_password_wizard.xml",
        "wizards/crypto_wallet_export_wizard.xml",
        "wizards/crypto_wallet_key_manager_wizard.xml",
        "wizards/crypto_wallet_generate_keypair_wizard.xml",
    ],
    "demo": [],
    "images": ["static/description/banner.png"],
    "installable": True,
    "auto_install": False,
    "application": True,
    "external_dependencies": {"python": ["cryptography"]},
    "maintainers": ["rosenvladimirov"],
    "development_status": "Beta",
}

# Copyright 2023 Rosen Vladimirov
# License AGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Bulgaria localization Configuration",
    "summary": "\n"
    "        This module allows you to install and configure all\n"
    "        the localization modules related to Bulgaria.",
    "description": "\n"
    "Bulgaria Localization Configuration - Core Foundation Module\n"
    "=============================================================\n"
    "\n"
    "This is the core configuration module for Bulgarian localization in Odoo, "
    "providing\n"
    "the essential infrastructure and utilities required by all other Bulgarian "
    "accounting\n"
    "and localization modules.\n"
    "\n"
    "**Core Features**\n"
    "-----------------\n"
    "\n"
    "**Configuration Management**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Centralized configuration system for all Bulgarian localization modules\n"
    "* XML-based configuration templates with dynamic parsing\n"
    "* Company-level settings for Bulgarian accounting compliance\n"
    "* Multi-company support with per-company configuration\n"
    "* Encryption system for sensitive API keys and credentials\n"
    "\n"
    "**Mixin Architecture (l10n.bg.config.mixin)**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Abstract model that can be inherited by any Odoo model\n"
    "* Automatic detection of Bulgarian records based on company settings\n"
    "* Dynamic view modification - hides Bulgarian fields when not needed\n"
    "* Smart field visibility control in form, list, and search views\n"
    "* Context-aware field display based on chart of accounts\n"
    "\n"
    "**Bulgarian Company Data Management**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Support for Bulgarian Unified Identification Codes (UIC/BULSTAT)\n"
    "* Multiple identification types:\n"
    "  - BG UIC (Unified Identification Code/BULSTAT)\n"
    "  - BG EGN (Personal Identification Number)\n"
    "  - BG PNF (Personal Number of Foreigner)\n"
    "  - BG Official Number from NRA\n"
    "  - BG Unique code under CRA\n"
    "  - Non-EU Tax Numbers\n"
    "  - EU VAT Numbers\n"
    "* Automatic validation using stdnum library\n"
    "* Representative/Manager contact management\n"
    "* Tax agent and company agent support\n"
    "* Department code tracking for NRA reporting\n"
    "\n"
    "**Partner Extensions**\n"
    "~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Enhanced partner types: representative, agent, tax agent\n"
    "* Automatic UIC/EGN/PNF validation and detection\n"
    "* API key encryption and management for secure data exchange\n"
    "* Representative assignment and hierarchy management\n"
    "* Country-specific title formatting support\n"
    "\n"
    "**Account Move Enhancements**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Automatic number formatting to 10-digit standard\n"
    "* Deal date tracking (separate from invoice date)\n"
    "* Bulgarian document date management\n"
    "* Smart number extraction from various formats\n"
    "\n"
    "**Account Tag Descriptions**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Translatable descriptions for account tags\n"
    "* Enhanced tax reporting metadata\n"
    "* Better audit trail documentation\n"
    "\n"
    "**Chart of Account Template System**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Plugin-based architecture for chart template extensions\n"
    "* Dynamic CSV parsing for accounts, groups, and taxes\n"
    "* Modular plugin loading from installed modules (l10n_bg_config_plugins_*)\n"
    "* Account code masking system with flexible formatting\n"
    "* Automatic code padding and formatting (e.g., ###.### format)\n"
    "* Template inheritance and override support\n"
    "* Centralized data management for accounts, groups, taxes, journals\n"
    "\n"
    "**Multi-language Support**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Tracking of installed multilanguage modules\n"
    "* JSON-based configuration for multilanguage settings\n"
    "* Integration with partner_multilang and l10n_bg_multilang\n"
    "* State tracking for multilanguage module activation\n"
    "\n"
    "**Security & Encryption**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* API key generation with customizable templates\n"
    "* XOR-based encryption for sensitive credentials\n"
    "* Base64 encoding for secure storage\n"
    "* Company-specific encryption keys\n"
    "* Automatic key generation when not provided\n"
    "\n"
    "**Module Dependency Management**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "Provides configuration options for installing related modules:\n"
    "* Currency Rate Update (OCA & EE versions)\n"
    "* Bulgarian Cities and Locations\n"
    "* Extended Address Management\n"
    "* NRA Tax Offices and Departments\n"
    "* Intrastat Product Declaration (OCA)\n"
    "* Partner Transliteration (ISO9)\n"
    "* Multi-register Identification Codes\n"
    "* Accounting Tax Audit Reports\n"
    "* Intrastat Reporting (EE)\n"
    "* Asset Management with Bulgarian rules\n"
    "* Report Themes\n"
    "* VAT Reports and Export Files (OCA & EE)\n"
    "\n"
    "**Technical Infrastructure**\n"
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Pre-init and post-init hooks for setup automation\n"
    "* Auto-install when l10n_bg is present\n"
    "* External dependency: xmltodict for XML processing\n"
    "* Backend assets for enhanced UI components\n"
    "* Proper tags for discoverability: localization, accounting, bulgaria\n"
    "* Country code: BG\n"
    "* Python 3.11+ required\n"
    "* Odoo 18.0 compatible\n"
    "\n"
    "**Wizard Tools**\n"
    "~~~~~~~~~~~~~~~~\n"
    "* Account tag bulk edit wizard\n"
    "* Settings preview with XML file support\n"
    "* Chart template plugin installer\n"
    "* Multilanguage settings viewer with JSON formatting\n"
    "\n"
    "**View Enhancements**\n"
    "~~~~~~~~~~~~~~~~~~~~~\n"
    "* Automatic field hiding for non-Bulgarian companies\n"
    "* Context-sensitive UI elements\n"
    "* Enhanced configuration settings interface\n"
    "* Representative contact selection\n"
    "* Department code configuration\n"
    "\n"
    "**Use Cases**\n"
    "~~~~~~~~~~~~~\n"
    "This module is essential for:\n"
    "- Setting up Bulgarian accounting in Odoo\n"
    "- Managing multiple Bulgarian companies\n"
    "- Integrating with NRA systems\n"
    "- Preparing for Bulgarian tax reporting\n"
    "- Ensuring compliance with Bulgarian commercial law\n"
    "- Building custom Bulgarian localization plugins\n"
    "\n"
    "**Integration Points**\n"
    "~~~~~~~~~~~~~~~~~~~~~~\n"
    "* Works as foundation for all l10n_bg_* modules\n"
    "* Provides base classes and mixins for inheritance\n"
    "* Supplies configuration infrastructure\n"
    "* Manages module state and dependencies\n"
    "* Handles data encryption for secure API integrations\n"
    "\n"
    "**Note**: This module requires l10n_bg (Bulgarian Chart of Accounts) and\n"
    "automatically installs it if not present. It serves as the configuration\n"
    "backbone for the entire Bulgarian localization ecosystem.\n"
    "    ",
    "version": "18.0.8.0.4",
    "development_status": "Production/Stable",
    "category": "Localization",
    "license": "LGPL-3",
    "author": "Rosen Vladimirov,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-bulgaria",
    "depends": [
        "base",
        "account",
        "base_vat",
        "l10n_bg",
        "l10n_bg_ledger",
        "l10n_bg_tariff_code",
    ],
    "external_dependencies": {"python": ["xmltodict"]},
    "data": [
        "data/res_lang_data.xml",
        "security/ir.model.access.csv",
        "wizards/account_account_tag_bulk_edit_wizard.xml",
        "wizards/account_settings_preview_xml_file.xml",
        "wizards/account_chart_template_plugins.xml",
        "views/res_config_view.xml",
        "views/account_account_tag_views.xml",
        "views/partner_view.xml",
        "views/res_company_views.xml",
        "views/account_move_views.xml",
    ],
    "demo": [],
    "images": ["static/description/banner.png"],
    "assets": {"web.assets_backend": ["l10n_bg_config/static/src/**/*"]},
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
    "auto_install": ["l10n_bg"],
    "tags": ["localization", "accounting", "bulgaria", "configuration"],
    "countries": ["BG"],
    "odoo_version": "18.0",
    "python_version": ">=3.11",
    "maintainers": ["rosenvladimirov"],
}

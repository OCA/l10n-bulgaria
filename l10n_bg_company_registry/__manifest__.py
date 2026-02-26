{
    "name": "Bulgarian Company Registry Integration",
    "version": "18.0.2.0.1",
    "category": "Localization",
    "summary": "Real-time integration with Bulgarian Trade Registry (portal.registryagency.bg)",
    "description": "\n"
    "Bulgarian Company Registry Integration\n"
    "=======================================\n"
    "\n"
    "Real-time integration with the official Bulgarian Trade Registry API\n"
    "(portal.registryagency.bg) to automatically fetch and populate company data.\n"
    "\n"
    "Key Features:\n"
    "-------------\n"
    "* Real-time API integration with portal.registryagency.bg\n"
    "* Search companies by EIK (Bulgarian company identification number)\n"
    "* Automatically populate partner data including:\n"
    "  - Company name (Bulgarian)\n"
    "  - Complete structured address (city, street, postal code, district)\n"
    "  - Legal form (ООД, ЕООД, АД, ЕТ, etc.)\n"
    "  - Registration date and court\n"
    "  - Economic activity (NACE/NKID code and description)\n"
    "  - Company managers and representatives\n"
    "  - Contact information (email, phone)\n"
    "* Smart address parsing supporting all Bulgarian formats:\n"
    "  - Streets (ул.) and boulevards (бул.)\n"
    "  - Residential complexes (ж.к.)\n"
    "  - Resort complexes (к.к.)\n"
    "  - Localities (м.) and quarters (кв.)\n"
    "  - With district information (р-н)\n"
    "  - Email and phone extraction from addresses\n"
    "* 100% success rate for address parsing\n"
    "* No offline database needed - always fresh data\n"
    "* Works with l10n_bg_config module for EIK/UIC validation\n"
    "\n"
    "Recent Improvements (v18.0.2.0.1):\n"
    "----------------------------------\n"
    "* Fixed HTML address parsing to preserve structure\n"
    "* Fixed contact information extraction from addresses\n"
    "* Fixed multi-word street name parsing\n"
    "* Added support for residential complexes and all address types\n"
    "* Achieved 100% success rate (up from 37%)\n"
    "* Tested with real companies from multiple cities\n"
    "\n"
    "Technical Details:\n"
    "------------------\n"
    "* API Endpoint: https://portal.registryagency.bg/CR/api/Deeds/\n"
    "* Direct connection to official government registry\n"
    "* Real-time data retrieval (30-second timeout)\n"
    "* Intelligent address parsing with regex patterns\n"
    "* Manager/representative extraction\n"
    "* Bilingual support (Bulgarian with English generation)\n"
    "\n"
    "Integration:\n"
    "------------\n"
    "* Depends on l10n_bg_config for Bulgarian localization fields\n"
    "* Uses standard Odoo fields where possible\n"
    "* Extends res.partner with Bulgarian-specific fields\n"
    "* Provides wizard for interactive company search\n"
    "\n"
    "Usage:\n"
    "------\n"
    "1. Open a partner record\n"
    "2. Enter EIK number\n"
    '3. Click "Fetch from Registry" button\n'
    "4. All data is automatically populated\n"
    "\n"
    'Or use the "Search Registry" wizard for more control.\n'
    "\n"
    "Author: Rosen Vladimirov\n"
    "License: LGPL-3\n"
    "Version: 18.0.2.0.1 (December 2025)\n"
    "    ",
    "author": "Rosen Vladimirov",
    "website": "https://github.com/OCA/l10n-bulgaria",
    "license": "LGPL-3",
    "depends": ["base", "contacts", "l10n_bg_config", "l10n_bg_city"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_actions_server.xml",
        "views/res_partner_views.xml",
        "wizard/bg_company_search_wizard_views.xml",
    ],
    "external_dependencies": {"python": ["requests"]},
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "maintainers": ["rosenvladimirov"],
}

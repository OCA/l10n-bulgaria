{
    "name": "Bulgarian Company Registry Integration",
    "version": "18.0.2.0.1",
    "category": "Localization",
    "summary": (
        "Real-time integration with Bulgarian Trade Registry "
        "(portal.registryagency.bg)"
    ),
    "author": "Odoo Community Association (OCA), Rosen Vladimirov",
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

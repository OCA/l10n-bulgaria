# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Account Reconcile Partner Regex SQL Fix",
    "description": (
        "\n        Fix partner name regexp_matches for translated jsonb names."
    ),
    "version": "18.0.1.0.0",
    "license": "OPL-1",
    "author": "Rosen Vladimirov",
    "website": "https://github.com/OCA/l10n-bulgaria",
    "depends": ["account_reconcile_model_oca"],
    "data": [],
    "demo": [],
    "post_load": "post_load_hook",
    "images": ["static/description/banner.png"],
    "maintainers": ["rosenvladimirov"],
}

#  Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Bulgarian HR Payroll Classifications",
    "version": "18.0.5.0.1",
    "category": "Human Resources/Localization",
    "summary": "Bulgarian localization for HR payroll with NKPD and Economic Activity classifications",
    "description": "\n"
    "    Bulgarian HR Payroll Classifications\n"
    "    ====================================\n"
    "\n"
    "    This module provides Bulgarian localization for HR and payroll management "
    "with:\n"
    "\n"
    "    Key Features:\n"
    "    -------------\n"
    "    * NCOP (National Classification of Occupations and Positions) management\n"
    "    * Economic Activities (KID) classification with MOD rates\n"
    "    * Bulgarian-specific HR menus structure\n"
    "    * Integration with standard HR modules\n"
    "\n"
    "    NCOP Classifications:\n"
    "    ---------------------\n"
    "    * Complete NCOP hierarchy management (НКПД 2011)\n"
    "    * Professional groups and categories\n"
    "    * Integration with employee positions\n"
    "\n"
    "    Economic Activities (KID):\n"
    "    --------------------------\n"
    "    * Full KID classification structure (Sections, Divisions, Groups, Classes)\n"
    "    * MOD (Minimum Insurance Income) rates by qualification groups\n"
    "    * Hierarchical structure with parent-child relationships\n"
    "\n"
    "    This module is essential for Bulgarian companies to comply with local labor "
    "regulations\n"
    "    and properly classify employees according to Bulgarian standards.\n"
    "        ",
    "author": "Rosen Vladimirov",
    "website": "https://github.com/OCA/l10n-bulgaria",
    "license": "LGPL-3",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "data/bg_hr_payroll_economic_activity/parent/bg.hr.payroll.economic.activity.csv",
        "data/bg_hr_payroll_economic_activity/div/bg.hr.payroll.economic.activity.csv",
        "data/bg_hr_payroll_economic_activity/grp/bg.hr.payroll.economic.activity.csv",
        "data/bg_hr_payroll_economic_activity/cls/bg.hr.payroll.economic.activity.csv",
        "data/bg_hr_payroll_ncop_classification/major/bg.hr.payroll.ncop.classification.csv",
        "data/bg_hr_payroll_ncop_classification/sub_major/bg.hr.payroll.ncop.classification.csv",
        "data/bg_hr_payroll_ncop_classification/minor/bg.hr.payroll.ncop.classification.csv",
        "data/bg_hr_payroll_ncop_classification/unit/bg.hr.payroll.ncop.classification.csv",
        "data/bg_hr_payroll_ncop_classification/occupation/bg.hr.payroll.ncop.classification.csv",
        "views/bg_ncop_classification.xml",
        "views/bg_mod_economic_activity.xml",
        "views/hr_job_views.xml",
        "views/hr_menus.xml",
    ],
    "images": ["static/description/banner.png"],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": False,
    "maintainers": ["rosenvladimirov"],
    "contributors": ["Rosen Vladimirov"],
    "support": "https://github.com/OCA/l10n-bulgaria/issues",
    "countries": ["BG"],
}

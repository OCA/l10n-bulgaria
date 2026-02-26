# Copyright 2023 Rosen Vladimirov
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Bulgaria - Cities and Locations",
    "summary": """
            Complete database of Bulgarian cities, municipalities,
            and administrative-territorial units with ЕКАТТЕ codes.""",
* ЕКАТТЕ code field
* Settlement type classification
* City hall code reference
* Administrative hierarchy links
* Tax office presence indicator
* Structure type identification

**Country State Enhancements**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Translatable state/region names
* Full support for Bulgarian regions (области)
* Multi-language capabilities for all geographic data

**Use Cases**
~~~~~~~~~~~~~
This module is essential for:

**Legal Compliance**
- Official document generation with correct ЕКАТТЕ codes
- Government reporting and submissions
- NRA tax declarations and registrations
- Statistical reporting to NSI (National Statistical Institute)

**Business Operations**
- Accurate address management for Bulgarian partners
- Proper geographic classification of business locations
- Tax office assignment based on location
- Regional sales and operations analysis

**Integration with Other Modules**
- Partner address completion and validation
- Intrastat reporting with correct location codes
- Tax office assignment and reporting
- Regional statistical analysis

**Geographic Analysis**
- Regional breakdown of customers/suppliers
- Sales territory management
- Logistics and delivery planning
- Market analysis by administrative region

**Data Coverage**
~~~~~~~~~~~~~~~~~
Complete Bulgarian geographic database including:
* All 265 municipalities (общини)
* Thousands of city halls (кметства)
* Over 5,000 settlements (cities, towns, villages)
* 28 regions (области)
* Monastery settlements
* Railway station settlements
* All with official ЕКАТТЕ codes

**Technical Features**
~~~~~~~~~~~~~~~~~~~~~~
* Proper model inheritance from res.city
* Smart domain functions for hierarchical filtering
* Index optimization on key fields (name, code, ЕКАТТЕ)
* Translatable content support
* Data import ready structure
* Foreign key relationships with cascading rules

**Integration Points**
~~~~~~~~~~~~~~~~~~~~~~
Works seamlessly with:
* **l10n_bg_config** - Core Bulgarian localization
* **l10n_bg_tax_offices** - NRA office assignment
* **l10n_bg_address_extended** - Enhanced address management
* **partner_multilang** - Transliteration and multi-language names
* **l10n_bg_reports_audit** - Geographic reporting requirements
* **l10n_bg_intrastat** - Location codes for intrastat declarations

**Data Import Support**
~~~~~~~~~~~~~~~~~~~~~~~
* Ready for bulk import of ЕКАТТЕ database
* Structured format for NSI official data
* Update mechanism for ЕКАТТЕ changes
* Maintains data integrity during updates

**Search and Selection**
~~~~~~~~~~~~~~~~~~~~~~~~
Enhanced search capabilities:
* Search by ЕКАТТЕ code
* Search by settlement type
* Filter by administrative hierarchy
* Quick location of tax office settlements
* Multi-language name search

**Compliance Standards**
~~~~~~~~~~~~~~~~~~~~~~~~
Meets requirements for:
* Bulgarian National Statistical Institute (НСИ) standards
* National Revenue Agency (НАП) reporting
* Ministry of Regional Development classifications
* EU geographic coding standards (NUTS)
* Official government document requirements

**Note**: This module significantly improves address management accuracy and
enables full compliance with Bulgarian administrative and statistical standards.
It's a foundational module for any serious Bulgarian localization implementation.
  """,
    "version": "18.0.1.0.0",
    "development_status": "Production/Stable",
    "category": "Localization",
    "license": "AGPL-3",
    "author": "Rosen Vladimirov,Odoo Community Association (OCA)",
    "maintainers": ["rosenvladimirov"],
    "website": "https://github.com/OCA/l10n-bulgaria",
    "depends": [
        "base_address_extended",
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/res_city_types.xml",
        "data/res_country_data.xml",
        "views/res_city_view.xml",
    ],
    "demo": [],
    "post_init_hook": "post_init_hook",
    "images": [
        "static/description/banner.png",
    ],
    "tags": ["localization", "bulgaria", "cities", "ekatte", "geographic"],
    "countries": ["BG"],
    # Version requirements
    "odoo_version": "18.0",
    "python_version": ">=3.11",
}

# -*- encoding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

{
    "name" : "Norway - Accounting",
    "version" : "1.1",
    "author" : "Rolv Råen",
    "category" : "Localization/Account Charts",
    "description": """This is the module to manage the accounting chart for Norway in eCore.

Updated for eCore 9 by Bringsvor Consulting AS <www.bringsvor.com>
""",
    "depends" : ["account", "base_iban", "base_vat"],
    "demo_xml" : [],
    "data" : ["account_chart.xml",
                    'account_tax.xml','account_chart_template.yml'],
    "active": False,
    "installable": True
}

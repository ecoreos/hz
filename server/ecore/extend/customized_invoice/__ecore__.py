# -*- coding: utf-8 -*-
{
    'name': "Customizable Invoice Templates",

    'summary': """
        Beautiful templates for invoices, customized with your corporate image.""",

    'description': """
        This module will install a customized client invoice report for accounting module.You will be able to customize the invoice colors,
        logo and the style/format of invoice to look professional and appealing to your customers. You can also create your own template 
        from scratch or edit one of the existing templates that come with this module 
    """,
    'images': ['static/description/invoice.png'],


    'author': "Optima ICT Services LTD",
    'website': "http://www.optima.co.ke",

    'category': 'Accounting & Finance',
    'version': '0.1',
    'depends': ['base', 'account', 'optima_social'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_invoice.xml',
        'views/modern_template.xml',
        'views/classic_template.xml',
        'views/retro_template.xml',
        'views/tva_template.xml',
        'views/ecore_template.xml',
        'views/account_invoice_view.xml',
        'views/res_company_view.xml',
        'reports/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
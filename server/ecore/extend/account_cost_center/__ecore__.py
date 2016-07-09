# -*- coding: utf-8 -*-

{
    'name': 'Costcenter',
    'summary': """Centro de costos para lineas de facturas""",
    'description': """
    Costcenter
================================================================

This module allow the user to link every invoice line to a costcenter
providing an extra dimension for the analysis.
    """,
    'depends': ['account','account_accountant'],
    'author': "AVALOS CORP",
    'website': 'http://ecore.net.co',
    'category': 'Accounting & Finance',
    'version': '1.0',
    'data': [
        'security/ir.model.access.csv',
        'views/costcenter_view.xml',
        'views/account_view.xml',
        'views/account_invoice_view.xml',
        'views/account_invoice_report_view.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

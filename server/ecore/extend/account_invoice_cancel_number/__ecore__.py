# -*- encoding: utf-8 -*-

{
    'name': 'Show invoice number in canceled invoices',
    'version': '0.001',
    'category': 'Account',
    'sequence': 1,
    'complexity': 'normal',
    'description': '''This module will show invoice number even if invoice is cancelled.''',
    'author': '',
    'website': 'http://ecore.net.co',
    'depends': ['base',
                'account',
                'account_cancel',
                ],
    'data': [
             'invoice_cancel_view.xml',
             ],
    'init': [],
    'demo': [],
    'update': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'certificate': '',
}

# -*- encoding: utf-8 -*-


{
    "name": "Invoice Shipping Address",
    'summary': """Direccíon de envio en facturas | Adds a shipping address field to the invoice.""",
    "version": "0.1.1",
    'category': 'Generic Modules/Accounting',
    "depends": ["account", "sale", "sale_stock"],
    "author": "AVALOS CORP",
    'website': 'http://ecore.net.co',
    'license': 'AGPL-3',
    'data': [
        'invoice_view.xml',
    ],
    'installable': True,
}

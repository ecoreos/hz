# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.


{
    'name': 'ESC/POS Hardware Driver',
    'version': '1.0',
    'category': 'Hardware Drivers',
    'sequence': 6,
    'website': 'http://www.ecore.cool/page/point-of-sale',
    'summary': 'Hardware Driver for ESC/POS Printers and Cashdrawers',
    'description': """
ESC/POS Hardware Driver
=======================

This module allows ecore to print with ESC/POS compatible printers and
to open ESC/POS controlled cashdrawers in the point of sale and other modules
that would need such functionality.

""",
    'depends': ['hw_proxy'],
    'external_dependencies': {
        'python' : ['usb.core','serial','qrcode'],
    },
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}

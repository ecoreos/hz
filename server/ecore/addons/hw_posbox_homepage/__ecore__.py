# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.


{
    'name': 'PosBox Homepage',
    'version': '1.0',
    'category': 'Hardware Drivers',
    'sequence': 6,
    'website': 'http://www.ecore.cool/page/point-of-sale',
    'summary': 'A homepage for the PosBox',
    'description': """
PosBox Homepage
===============

This module overrides ecore web interface to display a simple
Homepage that explains what's the posbox and show the status,
and where to find documentation.

If you activate this module, you won't be able to access the 
regular ecore interface anymore. 

""",
    'depends': ['hw_proxy'],
    'installable': False,
    'auto_install': False,
}

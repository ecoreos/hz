# -*- coding: utf-8 -*-

{
    "name": "Quality Management System",
    "version": "9.0.1.0.0",
    "author": "Avalos Corp",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        'base',
        'board',
        'document_page',
    ],
    "data": [
        'security/mgmtsystem_security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/mgmtsystem_system.xml',
        'views/res_config.xml'
    ],
    "demo": [],
    'installable': True,
}

# -*- coding: utf-8 -*-
{
    "name": "Date Range",
    "summary": "Manage all kind of date range",
    "version": "9.0.1.0.0",
    "category": "Tools",
    "author": "Avalos Corp",
    "application": False,
    "installable": True,
    "depends": [
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/date_range_security.xml",
        "views/assets.xml",
        "views/date_range_view.xml",
        "wizard/date_range_generator.xml",
    ],
    "qweb": [
        "static/src/xml/date_range.xml",
    ]
}

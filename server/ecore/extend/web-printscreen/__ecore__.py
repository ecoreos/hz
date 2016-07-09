# -*- encoding: utf-8 -*-

{
    'name': 'Export list to excel and pdf',
    'version': '1.0',
    'category': 'Web',
    'description': """

        Este Modulo Permite Exportar las Vistas de Arbol a Documentos PDF y Excel.

    """,
    'author': 'Avalos Corp',
    'website': 'http://ecore.cloud',
    'depends': ['web'],
    'data': ['views/web_printscreen_mw.xml'],
    'qweb': ['static/src/xml/web_printscreen_export.xml'],
    'installable': True,
    'auto_install': False,
    'web_preload': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

{
    'name': 'Web Editor',
    'category': 'Hidden',
    'description': """
eCore Web Editor widget.
==========================

""",
    'author': 'eCore S.A.',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/editor.xml',
        'views/iframe.xml',
        'views/snippets.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}

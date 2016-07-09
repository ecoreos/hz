{
    'name': 'eCommerce Optional Products',
    'category': 'Website',
    'version': '1.0',
    'website': 'http://www.ecore.cool/page/e-commerce',
    'description': """
eCore E-Commerce
==================

        """,
    'depends': ['website_sale'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
}

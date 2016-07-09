{
    'name': 'Contact Form',
    'category': 'Website',
    'website': 'http://www.ecore.cool/page/website-builder',
    'summary': 'Create Leads From Contact Form',
    'version': '2.0',
    'description': """
eCore Contact Form
====================

        """,
    'depends': ['website_form','website_partner', 'crm'],
    'data': [
        'data/website_crm_data.xml',
        'views/website_crm.xml',
    ],
    'installable': True,
    'auto_install': True,
}

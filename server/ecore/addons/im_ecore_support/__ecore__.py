{
    'name' : 'eCore Live Support',
    'version': '1.0',
    'summary': 'Chat with the eCore collaborators',
    'category': 'Tools',
    'complexity': 'medium',
    'website': 'http://www.ecore.cool/',
    'description':
        """
eCore Live Support
=================

Ask your functional question directly to the eCore Operators with the livechat support.

        """,
    'data': [
        "views/im_ecore_support.xml"
    ],
    'depends' : ["web", "mail"],
    'qweb': [
        'static/src/xml/im_ecore_support.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}

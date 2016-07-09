{

 'name' : 'eFinder - Busqueda Avanzada',
 'version' : '1.0.0',
 'author' : 'Emipro Technologies Pvt. Ltd./ Integra',
 'maintainer': 'Emipro Technologies/ Integra',
 'summary': 'Fetch your records in fraction of seconds..!!',
 'category': 'Extra Tools',
 'complexity': "normal",  # easy, normal, expert
 'depends' : ['base'],
 'description': """

INSTRUCCIONES
=============

    - Instalar el modulo.
    - Es necesario activar la importacion de CSV en la Base de Datos.
    - Cargar el csv de la carpeta data con el nombre quick.search.record.csv en el menu Configuracion --> Quick Search Record Info --> Importar.

USO
===

	- Al filtrar la busqueda de los menu, veremos en la vista de lista un icono en la parte derecha, al pulsarlo dispara la accion para entrar a los registros.

	
""",
 'website': 'http://www.emiprotechnologies.com',
 'data': [
          'view/res_users.xml',
          'view/js_view.xml',
          'view/quick_record_search_view.xml',
          'security/ir.model.access.csv',
          'data/quick.search.record.csv',
        ],
 'qweb': ['static/src/xml/job_search.xml', ],
 'js': ['static/src/js/job_search.js', ],
 'css': ['static/src/css/job_search.css', ],
 'installable': True,
 'images': ['static/description/main_screen.jpg'],
 'auto_install': False,
 'application' : True,
}

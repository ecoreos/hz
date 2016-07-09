# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to eCore, Run your business
#
#    All Rights Reserved.
#    info skype:  email: 
############################################################################

{
    'name': 'Reporte Facturacion (Cliente y Productos)',
    'version': '1',
    "author" : "",
    "category" : "Custom",
    'description': """

Reporte Facturacion
===================

Este modulo permite generar un Reporte de Facturas por Cliente y por Productos.

Los pasos para realizar el Reporte:
    1. Abrir el Asistente y Seleccionar el Cliente y el Rango de Fechas para generar el Reporte. Unicado en Contabilidad --> Reportes --> Inteligencia Empresarial --> Generar Reporte Facturacion.
    \n2. Este Formulario de puede Exportar a CSV con el boton Exportar en el mismo.

    """,
    "website" : "http://poncesoft.blogspot.com",
    "license" : "AGPL-3",
    "depends" : ["account","mail","sale"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    # 'security/ir.model.access.csv',
                    'report_customer.xml',
                    ],
    "installable" : True,
    "active" : False,
}

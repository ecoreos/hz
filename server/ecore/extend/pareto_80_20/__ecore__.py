# -*- encoding: utf-8 -*-
{
    'name': 'Analisis 80/20 Ley de Pareto',
    'version': '1',
    "author" : "Avalos Corp",
    "category" : "Analisis",
    'description': """
       La ley de pareto dice que el 20 porciento del esfuerzo genera el 80 porciento de los resultados.
       En este Analisis Enfocamos Esta Ley hacia Conceptos de eCore...
       Primero para poder Generar el Reporte, necesitamos tener permisos de Contabilidad.
       Para Generar el Analisis, tenemos un Asistente ubicado en Contabilidad --> Analisis Financieros --> Asistente 80/20 Clientes.
       En este asistente tenemos 3 formas de ver el Reporte de Pareto:
            - Excel.
            - Pdf.
            - Analisis eCore.

       Podemos Consultar el ultimo Analisis en el Menu Informes de eCore, Informes --> Ventas --> Analisis 80/20 clientes.
       
       Nota: Los Montos mostrados estan en la moneda Base MXN.
    """,
    "depends" : ["account","sale","purchase","stock","account_voucher","account_accountant",],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    'wizard/wizard_pareto_analisis_view.xml',
                    'pareto_analisis_view.xml',
                    ],
    "installable" : True,
    "active" : False,
}

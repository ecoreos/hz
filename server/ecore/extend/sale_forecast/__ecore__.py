# -*- encoding: utf-8 -*-
{
    'name': 'Sale Forecast',
    'category': 'sales',
    'summary': 'Sales Forecasting',
    'version': '1.0',
    'description': """
Provides ability to forecast the quantity for the products and based upon the calculation of action quantity, Purchase Order or Manufacture order can be created.


    """,
    'author': 'Avalos',
    'depends': ['sale', 'stock','crm','procurement_jit','purchase','mrp'],
    'data': [
        'sale_forecast_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}

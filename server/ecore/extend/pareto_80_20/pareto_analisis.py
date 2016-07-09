# -*- encoding: utf-8 -*-

from ecore import models, fields, api, _
from ecore.tools import float_compare
import ecore.addons.decimal_precision as dp
from datetime import time, datetime
from ecore import SUPERUSER_ID
from ecore import tools
from ecore.osv import osv, fields, expression
from ecore.tools.translate import _
from ecore.exceptions import except_orm, Warning, RedirectWarning
import base64

from pytz import timezone
import pytz
from datetime import timedelta

class pareto_report_customer(osv.osv):
    _name = 'pareto.report.customer'
    _description = 'Pareto Report Clientes'
    _rec_name = 'partner_id'
    _columns = {
        'partner_id':fields.many2one('res.partner', 'Cliente'),
        'sequence':fields.integer('Secuencia'),
        'percentage':fields.float('%', digits=(3,2), help="Representa el porcentaje acumulado."),
        'sales':fields.float('Ventas', digits=(22,4), help="Representa el monto de Ventas para este cliente."),
        'percentage_sales':fields.float('Ventas %', digits=(3,2), help="Representa el Porcentaje de las Ventas."),
        'cumulative_sales': fields.float('Ventas Acumuladas', digits=(22,4), help="El monto acumulado de las Ventas anteriores mas el monto de las nuevas ventas."),
        'cumulative_percentage': fields.float('Ventas Acumuladas %', digits=(22,4), help="Representa la sumatoria de los porcentajes de ventas %"),
        'utility': fields.float('Utilidad', digits=(22,4), help="Representa el Monto de Ventas - Costo de Compras"),
        'percentage_margin': fields.float('Margen %', digits=(22,4), help="Represents the profit margin is the result of the division of utility between the amount of sales"),
        'cost_purchase': fields.float('Costo de Compras', digits=(22,4), help="El costo de Compra por las ventas."),
        'cumulative_cost_purchase': fields.float('Costo de Compra acumulado', digits=(22,4), help="El monto acumulado del Costo de Compras."),
        'date': fields.date('Fecha Inicio', required=False),
        'date_end': fields.date('Fecha Fin', required=False),
        'company_id': fields.many2one('res.company','Company'),
        'shop_id': fields.related('partner_id','company_id',type='many2one',relation='res.company',string='Compañia', store=True),
        'pricelist_id': fields.related('partner_id', 'property_product_pricelist',type="many2one",relation='product.pricelist', string='Lista de Precios', store=True),

    }

    def _get_company(self, cr, uid, context=None):
        company_id = False
        for rec in self.pool.get('res.users').browse(cr, uid, [uid], context=None):
            company_id = rec.company_id.id
        return company_id

    _defaults = {
        'company_id': _get_company,
    }

    _order = 'sequence'

pareto_report_customer()

# class pareto_report(osv.osv):
#     _name = 'pareto.report'
#     _description = 'Pareto Report'
#     _rec_name = 'product_id'
#     _columns = {
#         'product_id':fields.many2one('product.product', 'Product'),
#         'sequence':fields.integer('Sequence'),
#         'description':fields.char('Description', size=128),
#         'code':fields.char('Code', size=128),
#         'percentage':fields.float('%', digits=(3,2), help="Represents the percentage of the product of the total products sold"),
#         'sales':fields.float('Sales', digits=(22,4), help="Represents the total monetary unit sales for the product described"),
#         'sale_units':fields.integer('Sale Units', help="Represents the total unit sales of the product described"),
#         'shop_id': fields.many2one('sale.shop', 'Shop'),
#         'percentage_sales':fields.float('%', digits=(3,2), help="Represents the percentage of total sales"),
#         'cumulative_sales': fields.float('Cumulative Sales', digits=(22,4), help="Represents the accumulation of sales is the total sales above + the new amount of sale"),
#         'cumulative_percentage': fields.float('%', digits=(22,4), help="Represents the cumulative percentage of sales"),
#         'utility': fields.float('Utility', digits=(22,4), help="Represents the total product sales minus the cost of buying it"),
#         'values': fields.float('Values', digits=(22,4), help="Represents national currency stocks"),
#         'units': fields.float('Units', digits=(22,4), help="Represents the units in inventory to the current date"),
#         'rsi': fields.float('RSI', digits=(22,4), help="Represents the return on investment, indicates that for every dollar invested obtains a gain of X amount"),
#         'percentage_margin': fields.float('Margin %', digits=(22,4), help="Represents the profit margin is the result of the division of utility between the amount of sales"),
#         'values_rot': fields.float('Values ROT', digits=(22,4), help="Represents the rotation of the product, this is the number of times the product came out of stock in national currency."),
#         'units_rot': fields.float('Units ROT', digits=(22,4), help="Represents the rotation of the product, this is the number of times the product came out of stock in units."),
#         'stock_to': fields.float('Stock To', digits=(10,2), help="Representa las Unidades en Stock dividido entre las Unidades Vendidas y los Dias de Inventario del Asistente"),
#         'date': fields.date('Fecha Inicio', required=False),
#         'date_end': fields.date('Fecha Fin', required=False),

#         #### Nuevas Columnas #####
#         'unit_cost_prom': fields.float('Costo Unitario P.', digits=(14,4), help='Representa el Costo Unitario Promedio' ),
#         'units_per_ordering': fields.float('Unidades P. Ordenar', digits=(14,4), help='Representa las Unidades por Ordenar' ),
#         'purchases': fields.float('Compras', digits=(14,4), help='Compras' ),
#     }

#     _defaults = {
#     }

#     _order = 'sequence'

# pareto_report()


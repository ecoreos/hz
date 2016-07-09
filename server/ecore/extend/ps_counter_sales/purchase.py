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
import time



####### HEREDA DEL MODELO BASE purchase.order ########
class purchase_order(osv.osv):
    _name = "purchase.order"
    _inherit = "purchase.order"
    _columns = {
        'product_on_id':fields.char('Producto', required=False, help="""Ingresa el Codigo del Producto Automaticamente se Agregara como linea tomando El precio del producto y su unidad de Medida
        Podemos Agregar los Siguientes Comodines:
            - Si queremos agregar el Producto y la Cantidad a la Vez ponemos el Codigo del Producto + Cantidad, es importante poner el simbolo + despues del Producto""" ),
        
        }

    _defaults = {  
        }

    def on_change_load_products(self, cr, uid, ids, partner_id, product_on_id, order_line, context=None):
        # pos_line_obj = self.pool.get('pos.order.line')
        product_obj = self.pool.get('product.product')
        salesman_obj = self.pool.get('res.users')
        partner_obj = self.pool.get('res.partner')
        partner = partner_obj.browse(cr, uid, partner_id, context=None)
        lines = order_line

        # fpos_obj = self.pool.get('account.fiscal.position')
        # fpos = partner.property_account_position.id or False
        # fpos = fpos and fpos_obj.browse(cr, uid, fpos, context=context) or False
        # tax_id = [(6, 0, [_w for _w in fpos_obj.map_tax(cr, uid, fpos, product[0].taxes_id)])],

        if not product_on_id:
            return {}
        if '+' in product_on_id:
            try:
                cod_product = product_on_id.split('+')[0]
                qty_product = product_on_id.split('+')[1]
                # print " CODIGO DEL VENDEDOR",sale_tpv_cod
                product_id = product_obj.search(cr, uid, [('default_code','=',cod_product)])
                product_br = product_obj.browse(cr, uid, product_id, context=None)[0]
                if product_br.default_code:
                    product_name = '['+product_br.default_code +']'+product_br.name
                else:
                    product_name = product_br.name

                if product_id:
                    xline = (0,0,{
                            'product_id': product_id[0],
                            'name': product_name,
                            'taxes_id': [(6, 0, [_w.id for _w in product_br.taxes_id])],
                            'product_qty': int(qty_product),
                            'price_unit': product_br.standard_price,
                            'product_uom': product_br.uom_id.id,
                            'date_planned': time.strftime('%Y-%m-%d'),

                        })
                    lines.append(xline)
                else:
                    warning = {
                                'title': 'Error Captura!',
                                'message': 'El Codigo Capturado no Encontro Ningun Producto en la Base de Datos, Codigo %s' % (cod_product,),
                            }
                    return {'value' : {'product_on_id':False,},'warning':warning}
            except:
                warning = {
                        'title':'Error !',
                        'message':'La Informacion Introducida Contiene Errores Verificar que el orden de la informacion sea de los ejemplos:\
                         \n -[CodigoProducto+Cantidad]'}
                return {'value' : {'product_on_id':False,},'warning':warning}
        else:
            try:
                cod_product = product_on_id
                qty_product = 1
                # print " CODIGO DEL VENDEDOR",sale_tpv_cod
                product_id = product_obj.search(cr, uid, [('default_code','=',cod_product)])
                product_br = product_obj.browse(cr, uid, product_id, context=None)[0]
                if product_br.default_code:
                    product_name = '['+product_br.default_code +']'+product_br.name
                else:
                    product_name = product_br.name

                if product_id:
                    xline = (0,0,{
                            'product_id': product_id[0],
                            'name': product_name,
                            'taxes_id': [(6, 0, [_w.id for _w in product_br.taxes_id])],
                            'product_qty': int(qty_product),
                            'price_unit': product_br.standard_price,
                            'product_uom': product_br.uom_id.id,
                            'date_planned': time.strftime('%Y-%m-%d'),

                        })
                    lines.append(xline)
                else:
                    warning = {
                                'title': 'Error Captura!',
                                'message': 'El Codigo Capturado no Encontro Ningun Producto en la Base de Datos, Codigo %s' % (cod_product,),
                            }
                    return {'value' : {'product_on_id':False,},'warning':warning}
            except:
                warning = {
                        'title':'Error !',
                        'message':'La Informacion Introducida Contiene Errores Verificar que el orden de la informacion sea de los ejemplos:\
                         \n -[CodigoProducto+Cantidad]'}
                return {'value' : {'product_on_id':False,},'warning':warning}

        
        return {'value' : {'product_on_id':False,'order_line':[x for x in lines]}}

purchase_order()

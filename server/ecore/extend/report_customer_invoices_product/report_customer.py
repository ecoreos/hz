# -*- encoding: utf-8 -*-

import ecore.addons.decimal_precision as dp
from ecore import tools
from ecore.osv import osv, fields, expression
from ecore.tools.translate import _
from ecore.exceptions import except_orm, Warning, RedirectWarning
from datetime import date, datetime, time, timedelta
from ecore import SUPERUSER_ID

import base64
####### TRABAJAR CON LOS EXCEL
import xlsxwriter
import tempfile
##### SOLUCIONA CUALQUIER ERROR DE ENCODING (CARACTERES ESPECIALES)
import sys
reload(sys)  
sys.setdefaultencoding('utf8')


class consult_export_csv_excel_reportcustomer (osv.osv_memory):
    _name = 'consult.export.csv.excel.reportcustomer'
    _description = 'Exportar Reporte a Excel o CSV'
    _columns = {
        'datas_fname': fields.char('File Name',size=256),
        'file': fields.binary('Layout'),
        'download_file': fields.boolean('Descargar Archivo'),
        'cadena_decoding': fields.text('Binario sin encoding'),
        'type': fields.selection([('csv','CSV')], 'Tipo Exportacion', 
                                required=False, ),
    }

    _defaults = {
        'download_file': False,
        'type': 'csv',
        }

    def export_csv_file(self, cr, uid, ids, context=None):
        document_csv = ""
        active_ids = context['active_ids']
        consult_obj = self.pool.get('stock.reportcustomer.model')
        if active_ids:
            for active in active_ids:
                da_list = []
                for rec in self.browse(cr, uid, ids, context=None):
                    consult_br = consult_obj.browse(cr, uid, active,
                                                        context=None)
                    da_list.append(consult_br.date)
                    salto_line = "\n"
                    cabeceras_p = "Cliente"+","+"Fecha Inicio"+","+"Fecha Fin"
                    document_csv = document_csv + cabeceras_p

                    linea_1 = consult_br.name.name+","+\
                    consult_br.date+","+consult_br.date_end

                    document_csv = document_csv + salto_line + linea_1 + salto_line

                    cabeceras_l = "Factura"+","+"Fecha"+","+"Monto"

                    texto_x = "Facturas del Cliente"+","+","
                    document_csv = document_csv+ salto_line+texto_x

                    document_csv = document_csv+ salto_line+cabeceras_l

                    detalle_lineas = ""
                    for linea in consult_br.reportcustomer_invoice_lines:
                        linea_str = ""
                        if linea.invoice_id:
                            linea_str = str(linea.invoice_id.number)+","+str(linea.invoice_id.date_invoice)+\
                            ","+str(linea.invoice_id.amount_total)
                       
                        detalle_lineas = detalle_lineas+salto_line+linea_str
                    document_csv = document_csv+detalle_lineas+salto_line+salto_line

                    cabeceras_l = "Producto"+","+"Cantidad"+","+\
                    "Unidad de Medida"+","+"Total Facturado"

                    texto_x = "Detalle Productos Facturados"+","+","+","
                    document_csv = document_csv+ salto_line+texto_x

                    document_csv = document_csv+ salto_line+cabeceras_l

                    detalle_lineas = ""
                    for linea in consult_br.reportcustomer_lines:
                        linea_str = ""
                        if linea.product_id:
                            linea_str = str(linea.product_id.name)+\
                            ","+str(linea.qty)+","+str(linea.uom_id.name)+","+str(linea.amount_total)
                       
                        detalle_lineas = detalle_lineas+salto_line+linea_str
                    document_csv = document_csv+detalle_lineas+salto_line+salto_line

                date = datetime.now().strftime('%d-%m-%Y')
                if len(da_list) > 1:
                    datas_fname = "Reporte Facturacion Client "+str(date)+".csv" # Nombre del Archivo
                else:
                    datas_fname = "Reporte Facturacion Client "+consult_br.date+" - "+consult_br.date_end+".csv" # Nombre del Archivo
                rec.write({'cadena_decoding':document_csv,
                    'datas_fname':datas_fname,
                    'file':base64.encodestring(document_csv),
                    'download_file': True})
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'consult.export.csv.excel.reportcustomer',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': ids[0],
            'views': [(False, 'form')],
            'target': 'new',
            }

    def process_export(self, cr, uid, ids, context=None):
        for rec in self.browse(cr, uid, ids, context=context):
            if rec.type == 'csv':
                result = self.export_csv_file(cr, uid, ids, context=context)
                return result
        return True

class stock_reportcustomer_model(osv.osv):
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _name = 'stock.reportcustomer.model'
    _description = 'Formulario de las Factuas del Cliente'
    _columns = {
        'name':fields.many2one('res.partner','Cliente'),
        'date': fields.date('Fecha Inicio', required=False),
        'date_end': fields.date('Fecha Fin', required=False),
        'reportcustomer_lines': fields.one2many('stock.reportcustomer.model.line', 'reportcustomer_id', ' Detalle de los Productos'),
        'reportcustomer_invoice_lines': fields.one2many('stock.reportcustomer.invoices.line', 'reportcustomer_id', ' Detalle de los Productos'),
        'total_invoices': fields.float('Monto Total Facturacion', digits=(14,2),)
    }
    _defaults = { 
        }
    _order = 'id desc' 

class stock_reportcustomer_model_line(osv.osv):
    _name = 'stock.reportcustomer.model.line'
    _description = 'Detalle Ventas del Producto'
    _rec_name = 'product_id' 
    _columns = {
        'product_id': fields.many2one('product.product', 'Producto', required=False),
        'qty': fields.float('Cantidad', digits=(14,4), required=False),
        'amount_total': fields.float('Total Ventas', digits=(14,4), required=False),
        'uom_id': fields.many2one('product.uom', 'Unidad de Medida', required=False),
        'reportcustomer_id': fields.many2one('stock.reportcustomer.model', 'ID Ref'),
    }

    _defaults = {
        }

class stock_reportcustomer_invoices_line(osv.osv):
    _name = 'stock.reportcustomer.invoices.line'
    _description = 'Facturas'
    _rec_name = 'invoice_id' 
    _columns = {
        'invoice_id': fields.many2one('account.invoice', 'Factura', required=False),
        'amount_total': fields.related('invoice_id', 'amount_total', string="Total", type="float", digits=(14,2)),
        'reportcustomer_id': fields.many2one('stock.reportcustomer.model', 'ID Ref'),
    }

    _defaults = {
        }

class stock_reportcustomer(osv.osv_memory):
    _name = 'stock.reportcustomer'
    _description = 'Asistente para Generacion del Reporte de Facturas'
    _columns = {
        'partner_id':fields.many2one('res.partner','Cliente', required=True),
        'date': fields.date('Fecha Inicio', required=True),
        'date_end': fields.date('Fecha Fin', required=True),

    }

    _defaults = {
        }

    def process(self, cr, uid, ids, context=None):
        picking_id = False
        inventory_lines = []
        reportcustomer = self.pool.get('stock.reportcustomer.model')
        user_br = self.pool.get('res.users').browse(cr, uid, uid, context=None)
        date = datetime.now().strftime('%Y-%m-%d')
        reportcustomer_id = False
        invoice_obj = self.pool.get('account.invoice')
        invoice_list_ids = []
        for rec in self.browse(cr, uid, ids, context=None):
            ########## INICIO DE VALIDACION DE CANTIDADDES, DESCOMENTAR CUANDO USEN SERIES ###########
            date_start = rec.date + ' 06:00:00'
            date_end = rec.date_end
            date_end_strp = datetime.strptime(date_end, '%Y-%m-%d')
            date_end = date_end_strp + timedelta(days=1)
            date_end = str(date_end).replace(' 00:00:00','')+' 05:59:59'
            cr.execute("""
                select id from account_invoice where date_invoice >= %s and date_invoice <= %s
                 and partner_id = %s and state in ('open','paid') and type = 'out_invoice';
                """,(date_start, date_end, rec.partner_id.id))
            cr_res = cr.fetchall()
            if cr_res:
                invoice_list_ids = [x[0] for x in cr_res if x]
            if not invoice_list_ids:
                raise except_orm(_('Error!'), 
                    _("No existen Facturas Relacionadas con el Rango seleccionado."))
            
            invoice_line_list = [(0,0,{'invoice_id':x}) for x in invoice_list_ids]
            product_list_ids = []
            cr.execute("""
                select product_id from account_invoice_line where invoice_id in %s group by product_id
                """ , (tuple(invoice_list_ids),))
            cr_res = cr.fetchall()
            product_list_ids = [x[0] for x in cr_res]
            if not product_list_ids:
                raise except_orm(_('Error!'), 
                    _("No existen Productos Relacionados con las Facturas de Este Cliente."))
            # product_line_list = []
            # for product in product_list_ids:
            #     print "########## PRODUCT >>> ",product
            #     cr.execute("""
            #         select uom_id from account_invoice_line where invoice_id in %s and product_id=%s group by uom_id;
            #         """, (tuple(invoice_list_ids), product))
            #     cr_res = cr.fetchall()
            #     uom_list = [x[0] for x in cr_res]
            #     for uom in uom_list:
            #         print "####### UNIDAD >>> ",uom
            #         cr.execute("""
            #             select sum(quantity), sum(price_subtotal) from account_invoice_line 
            #                 where product_id = %s and uom_id = %s and invoice_id in %s
            #             """,(product, uom, tuple(invoice_list_ids),))
            #         cr_res = cr.fetchall()
            #         print "######### CR RES >>>>> ", cr_res
            #         xline = {
            #             'product_id': product,
            #             'qty': cr_res[0][0],
            #             'amount_total':cr_res[0][1],
            #             'uom_id': uom,
            #             }
            #         product_line_list.append(xline)
            cr.execute("""
                select sum(amount_total) from account_invoice where id in %s
                """, (tuple(invoice_list_ids),))
            cr_res = cr.fetchall()
            total_invoices = cr_res[0][0] if cr_res else 0.0
            vals = {
                'name': rec.partner_id.id,
                'date': rec.date,
                'date_end': rec.date_end,
                'total_invoices': total_invoices,
                # 'reportcustomer_lines': invoice_line_list,
                # 'reportcustomer_invoice_lines': product_line_list,
            }
            reportcustomer_id = reportcustomer.create(cr, uid, vals, context=None)
            customer_invoice_obj = self.pool.get('stock.reportcustomer.invoices.line')
            product_invoice_obj = self.pool.get('stock.reportcustomer.model.line')
            for invoice_l in invoice_list_ids:
                invoice_f = {'reportcustomer_id':reportcustomer_id,'invoice_id':invoice_l}
                customer_invoice_obj.create(cr, uid, invoice_f)
            for product in product_list_ids:
                cr.execute("""
                    select uom_id from account_invoice_line where invoice_id in %s and product_id=%s group by uom_id;
                    """, (tuple(invoice_list_ids), product))
                cr_res = cr.fetchall()
                uom_list = [x[0] for x in cr_res]
                for uom in uom_list:
                    cr.execute("""
                        select sum(quantity), sum(price_subtotal) from account_invoice_line 
                            where product_id = %s and uom_id = %s and invoice_id in %s
                        """,(product, uom, tuple(invoice_list_ids),))
                    cr_res = cr.fetchall()
                    xline = {
                        'product_id': product,
                        'qty': cr_res[0][0],
                        'amount_total':cr_res[0][1],
                        'uom_id': uom,
                        'reportcustomer_id':reportcustomer_id
                        }

                    product_invoice_obj.create(cr, uid, xline)
        return {
                        'type': 'ir.actions.act_window',
                        'name': _('Reporte de Facturas por Cliente'),
                        'res_model': 'stock.reportcustomer.model',
                        'res_id': reportcustomer_id, ### Un Solo ID
                        'view_type': 'form',
                        'view_mode': 'form',
                        'view_id': False,
                        'target': 'current',
                        #'target': 'new',
                        'nodestroy': True,
                    }


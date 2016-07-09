# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to eCore,  Open Run Your Business
#
#    Copyright (c) 2015 http://www.argil.mx/
#    All Rights Reserved.
#    info skype:  email: 
############################################################################
#    Coded by:  email: 
##############################################################################

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
import time
from pytz import timezone
import pytz
from datetime import timedelta

class wizard_pareto_report_customer(osv.osv_memory):
    _name = 'wizard.pareto.report.customer'
    _description = 'Wizard Pareto Report Clientes'
    _columns = {
        'report_type':fields.selection([('analysis','Analisis eCore'),('pdf','PDF'),('xls','EXCEL')], 'Tipo', required=True),
        'date': fields.date('Fecha Inicio', required=True),
        'date_end': fields.date('Fecha Fin', required=True),
        'print_report': fields.boolean('Imprimir Reporte', help='Si esta casilla esta activa, se Imprime el Reporte PDF con los resultados del Reporte.', ),
    }

    def _get_date_start(self, cr, uid, context=None):
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        date_strp = datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        year = date_strp.year
        month = date_strp.month
        day = date_strp.day

        date_revision = date_strp - timedelta(days=30)
        return str(date_revision)

       
    _defaults = {
        'report_type': 'analysis',
        'date': _get_date_start,
        'date_end': lambda *a: datetime.now().strftime('%Y-%m-%d'),
    }


    def get_info(self, cr, uid, ids, context=None):
        pareto_report_obj = self.pool.get('pareto.report.customer')
        account_invoice_obj = self.pool.get('account.invoice')
        partner_obj = self.pool.get('res.partner')
        account_invoice_line_obj = self.pool.get('account.invoice.line')
        
        sales_global = 0.0
        product_list = []
        result = {}
        date = 0
        date_end = 0
        shop_name = ""
        type_report = ""
        date_strp_1 = False
        date_strp_2 = False

        day_minimun = 0 ### Dias Minimos Resultado de la comparacion delas Fechas del Wizard
        days_inventory = 0 ### Dias de Inventario Variable para el Calculo de las ultimas 4 columnas
        for rec in self.browse(cr, uid, ids, context=context):
            date = rec.date
            date_end = rec.date_end
            type_report = rec.report_type
            date_strp_1 = datetime.strptime(rec.date, '%Y-%m-%d')
            date_strp_2 = datetime.strptime(rec.date_end, '%Y-%m-%d')

        cr.execute("""
                   delete from pareto_report_customer;
            """)

        partner_list = []
        account_invoice_ids = account_invoice_obj.search(cr, uid, [('state','in',('paid','open')),('type','=','out_invoice'),('date_invoice','>=',date),('date_invoice','<=',date_end)])

        ######## OBTENIENDO LAS MONEDAS BASE DE VENTAS Y FACTURACION
        user_br = self.pool.get('res.users').browse(cr, uid, uid, context)
        
        currency_base_id = user_br.company_id.currency_id.id
        cr.execute("""
            select id from res_currency where UPPER(name) = 'USD';
            """)
        cr_res = cr.fetchall()
        usd_id = cr_res[0][0] if cr_res else False
        amount_sales_global = 0.0
        for ac_inv in account_invoice_obj.browse(cr, uid, account_invoice_ids, context=None):
            #### REVISION DE LA MONEDA DE FACTURA ####
            ### SI ES USD HACEMOS LA CONVERSION ###
            currency_id = ac_inv.currency_id.id
            if currency_id == currency_base_id:
                partner_list.append(ac_inv.partner_id.id)
                amount_sales_global += ac_inv.amount_untaxed
            else:
                cr.execute("""select rate from res_currency_rate 
                    where currency_id=%s and name<= %s 
                    order by name desc limit 1;
                    """, (ac_inv.currency_id.id, ac_inv.date_invoice, ))
                currency_tc = cr.fetchall()[0][0]
                mxn_convert_amount = ac_inv.amount_untaxed / currency_tc
                partner_list.append(ac_inv.partner_id.id)
                amount_sales_global += mxn_convert_amount
        partner_ids = partner_obj.search(cr, uid, [('id','in',tuple(partner_list))])

        if partner_ids:
            n = len(partner_ids)
            i=0
            while (i<n):
                amount_sales = 0.0 
                percentage_sales = 0.0
                utility = 0.0
                percentage_margin = 0.0
                cost_purchase = 0.0
                print "################# purchase price ", cost_purchase
                invoice_partner_ids = account_invoice_obj.search(cr, uid, [('partner_id','=',partner_ids[i]),('id','in',tuple(account_invoice_ids))])
                for part_inv in account_invoice_obj.browse(cr, uid, invoice_partner_ids, context=context):
                    print "################## FACTURA ", part_inv.number
                    currency_id = part_inv.currency_id.id
                    move_id = part_inv.move_id.id
                    if currency_id == currency_base_id:
                        amount_sales += part_inv.amount_untaxed
                    else:
                        cr.execute("""select rate from res_currency_rate 
                            where currency_id=%s and name<= %s 
                            order by name desc limit 1;
                            """, (ac_inv.currency_id.id, part_inv.date_invoice, ))
                        currency_tc = cr.fetchall()[0][0]
                        amount_sales += part_inv.amount_untaxed / currency_tc
                        print "################# AMOUNT SALES ", amount_sales
                    for line in part_inv.invoice_line_ids:
                        # cr.execute("""select rate from res_currency_rate 
                        #     where currency_id=%s and name<= %s 
                        #     order by name desc limit 1;
                        #     """, (ac_inv.currency_id.id, part_inv.date_invoice, ))
                        # currency_tc = cr.fetchall()[0][0]
                        if line.product_id:
                            line_cost = 0.0

                            purchase_price = line.product_id.standard_price
                            print "############ PURCHASE PRICE >>>>>>>",purchase_price
                            price_unit = line.price_unit
                            line_cost = line.quantity * purchase_price
                            print "##################### LINE COST ", line_cost

                            # if currency_id != currency_base_id:
                            #     line_cost = line_cost/currency_tc

                            # if purchase_price > price_unit:
                            #     time.sleep(10)
                            cost_purchase += line_cost
                    print "################# purchase price ", cost_purchase

                if amount_sales > 0.0:
                    percentage_sales = (amount_sales/amount_sales_global)*100
                    utility = amount_sales - cost_purchase #Representa el costo de la compra del producto - las ventas totales    
                    if utility:
                        percentage_margin = (utility/amount_sales) * 100
                vals = {
                    'partner_id': partner_ids[i],
                    'sales': amount_sales,
                    'percentage_sales': percentage_sales,
                    'utility': utility,
                    'percentage_margin': percentage_margin,
                    'cost_purchase': cost_purchase,
                    'date': date,
                    'date_end': date_end,
                }
                pareto_report_obj.create(cr, SUPERUSER_ID, vals, context)
                i+=1

            #pareto_report_ids = pareto_report_obj.search(cr, uid, [()], context)
            cr.execute("""
                   select id from pareto_report_customer order by sales desc;
            """)
            data_ids = [x[0] for x in cr.fetchall()]

            j = 0
            nl = len(data_ids)
            percentage_acum = 0.0
            percentage_val = (1/float(nl))*100
            cumulative_sales = 0.0
            cumulative_percentage = 0.0
            cumulative_cost_purchase = 0.0
            while (j<nl):
                percentage_acum += percentage_val
                
                for pr in pareto_report_obj.browse(cr, uid, [data_ids[j]], context=context):
                    cumulative_sales += pr.sales
                    cumulative_percentage += pr.percentage_sales
                    cumulative_cost_purchase += pr.cost_purchase

                    vals2 = {
                            'sequence': j+1,
                            'percentage': percentage_acum if percentage_acum < 100 else 100.00,
                            'cumulative_sales': cumulative_sales,
                            'cumulative_percentage': cumulative_percentage,
                            'cumulative_cost_purchase': cumulative_cost_purchase,
                            }
                    pr.write(vals2)
                    j += 1

        ########## Listo ##############
        values = self.pool.get('pareto.report.customer').search(cr, uid, [('id','>',0)])
        if values:
            for r in self.browse(cr, uid, ids, context=None):
                if r.report_type != 'analysis':
                    value = {
                                    'type':'ir.actions.report.xml',
                                    'report_name':'80_20_Clientes_pdf' if type_report == 'pdf' else '80_20_Clientes_xls',
                                    'datas' : {
                                        'model' : 'pareto.report.customer',
                                        'ids'   : values
                                        }
                                    }
                    return value
                else:
                    return {
                            'domain': "[('id','in', ["+','.join(map(str,values))+"])]",
                            'name': _('Informe de Pareto 80/20 Clientes'),
                            'view_type': 'form',
                            'view_mode': 'tree,form',
                            'res_model': 'pareto.report.customer',
                            'view_id': False,
                            'type': 'ir.actions.act_window'
                            }
        return True
wizard_pareto_report_customer()


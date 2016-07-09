# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to eCore, Run your business Solution
#
############################################################################

from ecore import models, fields, api, _
from ecore.tools import float_compare
import ecore.addons.decimal_precision as dp
from datetime import time, datetime, date, timedelta
from ecore import SUPERUSER_ID
from ecore import tools
from ecore.osv import osv, fields, expression
from ecore.tools.translate import _
from ecore.exceptions import except_orm, Warning, RedirectWarning

class ir_ui_menu(osv.osv):
    _name = 'ir.ui.menu'
    _inherit ='ir.ui.menu'

    def _menu_search_true(self, cr, uid, ids, field_name, args, context=None):
        if not context:
            context = {}
        res = {}
        for rec in self.browse(cr, uid, ids, context):
            if rec.action:
                if rec.action._name == 'ir.actions.act_window':
                    user_br = self.pool.get('res.users').browse(cr, uid, uid, context)
                    if user_br.lang != 'en_US':
                        trans_obj = self.pool.get('ir.translation')
                        cr.execute("""
                            select value from ir_translation
                                where lang=%s and src=%s ;
                            """, (user_br.lang, rec.name))
                        cr_res = cr.fetchall()
                        if cr_res:
                            name_f = cr_res[0][0] if cr_res[0] else ''
                            res[rec.id] = name_f
                    else:
                        res[rec.id] = rec.name
        return res


    _columns = {      
        'menu_name_search': fields.function(_menu_search_true, method=True, type='text',string='Menu de Busqueda', store=True,),
        }

    _defaults = {
        }

    def launch_action(self, cr, uid, ids, context=None):
        res = {}
        for rec in self.browse(cr, uid, ids, context):
            if rec.action:
                if rec.action._name == 'ir.actions.act_window':
                    ids_to_launch = self.pool.get(rec.action.res_model).search(cr, uid, [])
                    res = {
                    'domain': "[('id','in', ["+','.join(map(str,ids_to_launch))+"])]",
                    'name': rec.name,
                    'view_type': 'form',
                    'view_mode': 'tree,form',
                    'res_model': rec.action.res_model,
                    'view_id': False,
                    'type': 'ir.actions.act_window'
                    }
                else:
                    raise except_orm(
                        _('Error!'),
                        _('Este Menu no contiene una Accion de Ventana.')
                        )
            else:
                raise except_orm(
                    _('Error!'),
                    _('Este Menu no contiene una Accion de Ventana.')
                    )
        return res

    # def _init_(self, cr):
    #     user_br = self.pool.get('res.users').browse(cr, SUPERUSER_ID, SUPERUSER_ID, context={})
    #     cr.execute("""
    #         update ir_ui_menu set menu_name_search = ir_translation.value from ir_translation
    #             where ir_translation.src = ir_ui_menu.name and lang='%s'
    #         """ % user_br.lang)

# class creacion_registros_aut(osv.osv):
#     _name = 'creacion.registros.aut'
#     _description = 'Clase para Definir Registros desde Codigo Py'
#     _columns = {
#         'name':fields.char('Label', size=64, required=False, readonly=False), 
#     }

#     def init(self, cr):
#         quick_search = self.pool.get('quick.search.record')
#         menu_id = quick_search.search(cr, SUPERUSER_ID,
#                 [('name','=','Busqueda de Menus'),('default','=',True)])
#         if not menu_id:
#             view_obj = self.pool.get('ir.ui.view')
#             field_obj = self.pool.get('ir.model.field')
#             model_obj = self.pool.get('ir.model')
#             model_id = model_obj.search(cr, SUPERUSER_ID,
#                 [('name','=','ir.ui.menu')])
#             view_id = view_obj.search(cr, SUPERUSER_ID,
#                 [('name','=','ir.ui.menu form')])
#             tree_view_id = view_obj.search(cr, SUPERUSER_ID,
#                 [('name','=','ir.ui.menu tree')])
#             field_id = field_obj.search(cr, SUPERUSER_ID,
#                 [('name','=','menu_name_search')])
#             vals = {
#                 'name': 'Busqueda de Menus',
#                 'default': True,
#                 'search_type': 'exact',
#                 'window_type': 'new',
#                 'model_id': model_id[0],
#                 'model_model': 'ir.ui.menu',
#                 'view_id': view_id[0],
#                 'tree_view_id': tree_view_id[0],
#                 'field_id': field_id[0],
#                 }
#             quick_search.create(cr, SUPERUSER_ID,
#                 vals, {})
#         return True

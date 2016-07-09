# -*- coding: utf-8 -*-

from ecore import models, fields, api
from lxml import etree
import logging
_logger = logging.getLogger(__name__)


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    cost_center_id = fields.Many2one(
        'account.cost.center', string='Centro de costos',
        help="Centro de costos por defecto")

    @api.model
    def line_get_convert(self, line, part, date):
        res = super(account_invoice, self).line_get_convert(line, part, date)
        if line.get('cost_center_id'):
            res['cost_center_id'] = line['cost_center_id']
        return res

    def fields_view_get(self, cr, uid, view_id=None, view_type='form',
                        context=None, toolbar=False, submenu=False):
        res = super(account_invoice, self).fields_view_get(
            cr, uid, view_id=view_id, view_type=view_type,
            context=context, toolbar=toolbar, submenu=False)
        if not context:
            context = {}
        if not context.get('cost_center_default', False):
            if view_type == 'form':
                view_obj = etree.XML(res['arch'])
                invoice_line = view_obj.xpath("//field[@name='invoice_line']")
                extra_ctx = "'cost_center_default': 1, " \
                    "'cost_center_id': cost_center_id"
                for el in invoice_line:
                    ctx = el.get('context')
                    if ctx:
                        ctx_strip = ctx.rstrip("}").strip().rstrip(",")
                        ctx = ctx_strip + ", " + extra_ctx + "}"
                    else:
                        ctx = "{" + extra_ctx + "}"
                    el.set('context', str(ctx))
                    res['arch'] = etree.tostring(view_obj)
        return res


class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'

    @api.model
    def _default_cost_center(self):
        return self._context.get('cost_center_id') \
            or self.env['account.cost.center']

    cost_center_id = fields.Many2one(
        'account.cost.center', string='Centro de costo',
        default=_default_cost_center)

    @api.model
    def move_line_get_item(self, line):
        res = super(account_invoice_line, self).move_line_get_item(line)
        if line.cost_center_id:
            res['cost_center_id'] = line.cost_center_id.id
        return res

# -*- encoding: utf-8 -*-

from ecore.osv import orm
from ecore import api, fields, models,


class sale_order(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self, cr, uid, order, lines, context=None):

        res = super(sale_order, self)._prepare_invoice(
            cr, uid, order, lines, context=context
        )
        res.update({
            'address_shipping_id': order.partner_shipping_id.id, })
        return res

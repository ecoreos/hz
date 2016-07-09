# -*- coding: utf-8 -*-

from ecore.osv import orm


class StockPicking(orm.Model):
    _inherit = "stock.picking"

    def _get_invoice_vals(self, cr, uid, key, inv_type,
                          journal_id, picking, context=None):
        invoice_vals = super(StockPicking, self)._get_invoice_vals(
            cr, uid, key, inv_type, journal_id, picking, context=context)
        if picking and picking.partner_id:
            invoice_vals['address_shipping_id'] = picking.partner_id.id
        return invoice_vals

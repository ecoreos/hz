# -*- encoding: utf-8 -*-

from ecore.osv import fields, orm
from ecore import api, fields, models


class account_invoice(models.Model):
    _inherit = "account.invoice"

    _columns = {
        'address_shipping_id': fields.many2one('res.partner','Shipping Address', readonly=True,
            states={
                'draft': [('readonly', False)],
                'sent': [('readonly', False)]
            },
            help="Delivery address for current invoice."),
    }

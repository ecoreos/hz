# -*- encoding: utf-8 -*-
# Part of ecore. See LICENSE file for full copyright and licensing details.
# Integra & 

import re, time, random
from ecore import api
from ecore.osv import fields, osv
from ecore.tools.translate import _
import logging
from ecore.exceptions import UserError
_logger = logging.getLogger(__name__)


class account_invoice(osv.osv):
    _inherit = 'account.invoice'

    def create(self, cr, uid, vals, context=None):
        res = super(account_invoice, self).create(cr, uid, vals, context=context)
        for rec in self.browse(cr, uid, [res], context):
            if not rec.tax_line_ids:
                rec.compute_taxes()
                tax_grouped = rec.get_taxes_values()
        return res

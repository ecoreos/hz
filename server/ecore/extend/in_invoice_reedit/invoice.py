# -*- encoding: utf-8 -*-
###########################################################################
#  ()
##############################################################################

from ecore.tools.translate import _
from ecore.osv import fields, osv
from ecore import tools
from ecore import netsvc
from ecore import release
from ecore import workflow

import time
from xml.dom import minidom
import os
import base64
import hashlib
import tempfile
import codecs

from datetime import datetime


class account_invoice(osv.Model):
    _inherit = 'account.invoice'

    _columns = {
    'reedit_invoice': fields.boolean('Reeditando Factura'),
    'no_reedit_invoice': fields.boolean('Reeditando Factura'),
    }

    def reedit_invoice_open(self, cr, uid, ids, context=None):
        workflow.trg_validate(uid, self._name, ids[0], 'invoice_cancel', cr)
        self.action_cancel_draft(cr, uid, ids, context)
        self.write(cr, uid, ids, {'reedit_invoice':True,'no_reedit_invoice':True}, context)
        return True

    # def write(self, cr, uid, ids, vals, context=None):
    #     res = super(account_invoice, self).write(cr, uid, ids, vals, context)
    #     context = dict(context)
    #     for rec in self.browse(cr, uid, ids, context):
    #         if 'no_rewrite' in context:
    #             if context['no_rewrite'] == True:
    #                 return res
    #         if rec.state == 'open':
    #             return res
    #         if rec.no_reedit_invoice == True :
    #             rec.write({'no_reedit_invoice': False})
    #             return res
    #         if rec.reedit_invoice:
    #             context.update({'no_rewrite':True})
    #             rec.invoice_validate()
    #             rec.write({'reedit_invoice':False})
    #     return res
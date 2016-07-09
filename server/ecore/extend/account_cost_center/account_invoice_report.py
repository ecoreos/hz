# -*- coding: utf-8 -*-

from ecore.osv import fields, osv
from ecore import tools

class account_invoice_report(osv.osv):
    _inherit = "account.invoice.report"
    _columns = {
        'cost_center_id': fields.many2one('account.cost.center', string="Centro de costos", readonly=True),
        'account_analytic_id': fields.many2one('account.analytic.account', string="Cuenta analitica", readonly=True)
    }

    def _select(self):
        return  super(account_invoice_report, self)._select() + ", sub.cost_center_id as cost_center_id, sub.account_analytic_id as account_analytic_id"

    def _sub_select(self):
        return  super(account_invoice_report, self)._sub_select() + ", ail.cost_center_id as cost_center_id, ail.account_analytic_id as account_analytic_id"

    def _group_by(self):
        return super(account_invoice_report, self)._group_by() + ", ail.cost_center_id, ail.account_analytic_id"

# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore.osv import fields, osv

class hr_payroll_configuration(osv.osv_memory):
    _name = 'hr.payroll.config.settings'
    _inherit = 'res.config.settings'
    _columns = {
        'module_hr_payroll_account': fields.boolean('Link your payroll to accounting system',
            help ="""Create journal entries from payslips"""),
    }

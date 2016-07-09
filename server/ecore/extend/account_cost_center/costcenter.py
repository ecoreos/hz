# -*- coding: utf-8 -*-

from ecore import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class account_cost_center(models.Model):
    _name = 'account.cost.center'
    _description = 'Cuenta de centro de costos'

    name = fields.Char(string='Nombre', required=False, size=64)
    code = fields.Char(string='Codigo', required=True, size=16)
    company_id = fields.Many2one(comodel_name='res.company',
                                 string='Company',
                                 required=True,
                                 default=lambda self: self.env.user.company_id)

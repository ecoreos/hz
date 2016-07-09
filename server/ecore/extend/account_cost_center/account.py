# -*- coding: utf-8 -*-

from ecore import models, fields
import logging
_logger = logging.getLogger(__name__)


class account_move_line(models.Model):
    _inherit = 'account.move.line'
    cost_center_id = fields.Many2one('account.cost.center', string='Centro de costos')
# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    can_be_expensed = fields.Boolean(help="Specify whether the product can be selected in an HR expense.")

# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

import logging

import ecore

from ecore import tools
from ecore.osv import fields, osv
from ecore.tools.translate import _

class pos_config(osv.osv):
    _inherit = 'pos.config' 
    _columns = {
        'iface_discount': fields.boolean('Order Discounts', help='Allow the cashier to give discounts on the whole order.'),
        'discount_pc': fields.float('Discount Percentage', help='The default discount percentage'),
        'discount_product_id': fields.many2one('product.product','Discount Product', help='The product used to model the discount'),
    }
    _defaults = {
        'iface_discount': True,
        'discount_pc': 10,
    }

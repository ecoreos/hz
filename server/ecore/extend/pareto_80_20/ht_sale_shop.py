# -*- encoding: utf-8 -*-

from osv import osv, fields
import time
import dateutil
import dateutil.parser
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
from tools.translate import _


# Agregamos manejar una secuencia por cada tienda para controlar viajes
class sale_shop(osv.osv):
    _name = "sale.shop"
    _inherit = "sale.shop"
    _columns = {
        '80_20': fields.boolean('Disponible 80/20', help="Activar si esta tienda sera tomada en cuenta para el Analisis del 80/20"),
        }

    _defaults = {
        }

sale_shop()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
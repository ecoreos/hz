# -*- coding: utf-8 -*-
import ecore
from ecore.osv import fields
from ecore.osv.orm import Model

class test_uninstall_model(Model):
    """
    This model uses different types of columns to make it possible to test
    the uninstall feature of eCore.
    """
    _name = 'test_uninstall.model'

    _columns = {
        'name': fields.char('Name'),
        'ref': fields.many2one('res.users', string='User'),
        'rel': fields.many2many('res.users', string='Users'),
    }

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Each name must be unique.')
    ]

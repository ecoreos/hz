# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ..exceptions import except_orm
from .orm import Model, TransientModel, AbstractModel

# Deprecated, kept for backward compatibility.
# ecore.exceptions.Warning should be used instead.
except_osv = except_orm

# Deprecated, kept for backward compatibility.
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel # ;-)

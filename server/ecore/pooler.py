# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

""" Functions kept for backward compatibility.

    They are simple wrappers around a global RegistryManager methods.

"""

import logging
import ecore.conf.deprecation
from ecore.modules.registry import RegistryManager

_logger = logging.getLogger(__name__)

def get_db_and_pool(db_name, force_demo=False, status=None, update_module=False):
    """Create and return a database connection and a newly initialized registry."""
    assert ecore.conf.deprecation.ecore_pooler
    _logger.warning('ecore.pooler.get_db_and_pool() is deprecated.')
    registry = RegistryManager.get(db_name, force_demo, status, update_module)
    return registry._db, registry


def restart_pool(db_name, force_demo=False, status=None, update_module=False):
    """Delete an existing registry and return a database connection and a newly initialized registry."""
    _logger.warning('ecore.pooler.restart_pool() is deprecated.')
    assert ecore.conf.deprecation.ecore_pooler
    registry = RegistryManager.new(db_name, force_demo, status, update_module)
    return registry._db, registry

def get_db(db_name):
    """Return a database connection. The corresponding registry is initialized."""
    assert ecore.conf.deprecation.ecore_pooler
    return get_db_and_pool(db_name)[0]


def get_pool(db_name, force_demo=False, status=None, update_module=False):
    """Return a model registry."""
    assert ecore.conf.deprecation.ecore_pooler
    return get_db_and_pool(db_name, force_demo, status, update_module)[1]

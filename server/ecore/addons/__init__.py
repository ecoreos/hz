# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

""" Addons module.

This module serves to contain all eCore addons, across all configured addons
paths. For the code to manage those addons, see ecore.modules.

Addons are made available under `ecore.addons` after
ecore.tools.config.parse_config() is called (so that the addons paths are
known).

This module also conveniently reexports some symbols from ecore.modules.
Importing them from here is deprecated.

"""

# -*- encoding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

# Copyright (C) conexus.at

from ecore import tools
from ecore.osv import osv
from ecore import addons

class AccountWizard_cd(osv.osv_memory):
	_inherit='wizard.multi.charts.accounts'
	
	_defaults = {
		'code_digits' : 0,
	}

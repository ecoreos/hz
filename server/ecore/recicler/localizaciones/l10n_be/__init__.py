# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore import SUPERUSER_ID

def load_translations(cr, registry):
    chart_template = registry['ir.model.data'].xmlid_to_object(cr, SUPERUSER_ID, 'l10n_be.l10nbe_chart_template')
    chart_template.process_coa_translations()
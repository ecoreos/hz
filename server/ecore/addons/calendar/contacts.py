# -*- coding: utf-8 -*-
# Part of eCore. See LICENSE file for full copyright and licensing details.

from ecore.osv import fields, osv

class calendar_contacts(osv.osv):
    _name = 'calendar.contacts'    

    _columns = {
        'user_id': fields.many2one('res.users','Me'),
        'partner_id': fields.many2one('res.partner','Employee',required=True, domain=[]),
        'active':fields.boolean('active'),        
     }
    _defaults = {
        'user_id': lambda self, cr, uid, ctx: uid,
        'active' : True,        
    }
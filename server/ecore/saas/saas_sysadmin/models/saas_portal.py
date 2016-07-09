from ecore import models, fields, api

                   
class SaasPortalServer(models.Model):
    _inherit = 'saas_portal.server'
    
    ip_address = fields.Char('Server IP Address')
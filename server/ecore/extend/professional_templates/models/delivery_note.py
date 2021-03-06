# -*- coding: utf-8 -*-
from ecore import models, fields, api

class customized_dn_order(models.Model):
	_inherit=["stock.picking"]

	@api.model
	def _default_template(self):
	    company_obj = self.env['res.company']
	    company = self.env['res.users'].browse([self.env.user.id]).company_id
	    if not company.template_dn:
		def_tpl = self.env['ir.ui.view'].search([('key', 'like', 'professional_templates.DN_%' ), ('type', '=', 'qweb')], order='id asc', limit=1)
                company.write({'template_dn': def_tpl.id})
	    return company.template_dn or self.env.ref('stock.report_delivery_document')
	
	@api.model
	def _default_odd(self):
	    company_id = self.env['res.users'].browse([self.env.user.id]).company_id
	    return self.env['res.company'].browse([company_id.id]).odd

	@api.model
	def _default_even(self):
	    company_id = self.env['res.users'].browse([self.env.user.id]).company_id
	    return self.env['res.company'].browse([company_id.id]).even

	@api.model
	def _default_theme_color(self):
	    company_id = self.env['res.users'].browse([self.env.user.id]).company_id
	    return self.env['res.company'].browse([company_id.id]).theme_color

	@api.model
	def _default_theme_txt_color(self):
	    company_id = self.env['res.users'].browse([self.env.user.id]).company_id
	    return self.env['res.company'].browse([company_id.id]).theme_txt_color

	@api.model
	def _default_name_color(self):
	    company_id = self.env['res.users'].browse([self.env.user.id]).company_id
	    return self.env['res.company'].browse([company_id.id]).name_color

	@api.model
	def _default_cust_color(self):
	    company_id = self.env['res.users'].browse([self.env.user.id]).company_id
	    return self.env['res.company'].browse([company_id.id]).cust_color

	@api.model
	def _default_text_color(self):
	    company_id = self.env['res.users'].browse([self.env.user.id]).company_id
	    return self.env['res.company'].browse([company_id.id]).text_color

	
 	dn_logo = fields.Binary("Logo", attachment=True,
             help="This field holds the image used as logo for the delivery slip, if non is uploaded, the default logo set in the company settings will be used")
	templ_id = fields.Many2one('ir.ui.view', 'Delivery Slip Template', default=_default_template,required=True, 
		domain="[('type', '=', 'qweb'), ('key', 'like', 'professional_templates.DN\_%\_document' )]")
	odd = fields.Char('Odd parity Color', size=7, required=True, default=_default_odd, help="The background color for odd lines in the delivery slip")	
	even = fields.Char('Even parity Color', size=7, required=True, default=_default_even, help="The background color for even lines in the delivery slip" )	
	theme_color = fields.Char('Theme Color', size=7, required=True, default=_default_theme_color, help="The Main Theme color of the Delivery Slip. Normally this should be one of your official company colors")	
	theme_txt_color = fields.Char('Theme Text Color', size=7, required=True, default=_default_theme_txt_color, 
			help="The Text color of the areas with theme color. This should not be the same the theme color")	
	text_color = fields.Char('Text Color', size=7, required=True, default=_default_text_color, help="The text color of the order. Normally this\
			 should be one of your official company colors or default HTML text color")	
	name_color = fields.Char('Company Name Color', size=7, required=True, default=_default_name_color, help="The Text color of the Company Name. \
			Normally thisshould be one of your official company colors or default HTML text color")	
	cust_color = fields.Char('Customer Name Color', size=7, required=True, default=_default_name_color, help="The Text color of the Customer Name. \
			Normally this should be one of your official company colors or default HTML text color")	


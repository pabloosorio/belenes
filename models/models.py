# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

# class belenes(models.Model):
#     _name = 'belenes.belenes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class addPermission(models.Model):
	_name = 'res.users'
	_inherit = 'res.users'

	valid_purchase = fields.Boolean(string='Valida Compras')

class purchaseTypes(models.Model):
	_name = 'purchase.order.types'

	name = fields.Char(string='Tipo de compra',required=True)
	users = fields.One2many('purchase.order.types.users', 'type_id', string='Option lines')

class TrovaEmployee(models.Model):
	_name = "purchase.order.types.users"
	_description = "usuarios que autorizan la compra"

	name = fields.Many2one('res.users',string='Usuario')
	email = fields.Char(string='E-mail', related='name.login',readonly=True)
	empresa = fields.Many2one('res.partner',string='Empresa', related='name.partner_id',readonly=True)	
	type_id = fields.Many2one('purchase.order.types', string='Campo Many2one', required=True, ondelete='cascade',index=True, copy=False)

class validPurchase(models.Model):
	_name = 'purchase.order'
	_inherit = 'purchase.order'

	valid_purchase = fields.Boolean(string='Validar Compra')
	purchase_type = fields.Many2one('purchase.order.types',string='Tipo de Compra')
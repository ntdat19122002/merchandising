from odoo import models,fields

class MerchandisingReview(models.Model):
    _name = 'md.journey'

    store = fields.Many2one('md.shopify.store')
    type = fields.Char(string='Type')
